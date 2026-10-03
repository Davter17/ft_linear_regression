import json
import math
import matplotlib.pyplot as plt
from utils import load_data

def load_model():
	try:
		with open("./trained_data.json", "r") as f:
			data = json.load(f)
		return data["theta0"], data["theta1"]
	except FileNotFoundError:
		print("Warning: trained_data.json not found. Using default values (theta0=0, theta1=0).")
		print("Run training.py first to get accurate predictions.")
		return 0.0, 0.0
	except PermissionError:
		print("Error: you don't have permission to read trained_data.json")
		return None, None
	except json.JSONDecodeError as e:
		print(f"Error: trained_data.json is corrupted - {e}")
		return None, None
	except KeyError as e:
		print(f"Error: trained_data.json is missing required field - {e}")
		return None, None

def get_mileage():
	while True:
		try:
			km_input = input("Enter the car mileage: ")
			km = int(km_input)
			if km < 0:
				print("Error: mileage cannot be negative")
				continue
			return km
		except ValueError:
			print("Error: please enter a valid number")
			continue

def calculate_metrics(theta0, theta1, kms, prices):
	lenDatas = len(kms)
	squared_errors = []
	absolute_errors = []

	for i in range(lenDatas):
		prediction = theta0 + theta1 * kms[i]
		error = prediction - prices[i]
		squared_errors.append(error ** 2)
		absolute_errors.append(abs(error))

	mse = sum(squared_errors) / lenDatas
	rmse = math.sqrt(mse)
	mae = sum(absolute_errors) / lenDatas

	mean_price = sum(prices) / lenDatas
	ss_tot = sum((p - mean_price) ** 2 for p in prices)
	ss_res = sum(squared_errors)
	r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0

	return mse, rmse, mae, r2

def display_graph(kms, prices, theta0, theta1, user_km, user_price):
	predictions = [theta0 + theta1 * km for km in kms]
	combined = sorted(zip(kms, predictions))
	km_sorted, pred_sorted = zip(*combined)

	plt.scatter(kms, prices, color='blue', label='Real data')
	plt.scatter(user_km, user_price, color='red', label='Prediction', s=100)
	plt.plot(km_sorted, pred_sorted, color='green', label='Regression line')
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	plt.legend()
	plt.show()

def main():
	theta0, theta1 = load_model()
	if theta0 is None:
		return

	km = get_mileage()
	price = theta0 + theta1 * km
	print(f"The estimated price is: {price:.2f}")

	kms, prices = load_data()
	if kms is None:
		return

	if len(kms) < 2:
		print("Warning: not enough data points for metrics")
		display_graph(kms, prices, theta0, theta1, km, price)
		return

	mse, rmse, mae, r2 = calculate_metrics(theta0, theta1, kms, prices)

	print("\n=== Model accuracy metrics ===\n")
	print(f"MSE  (Mean Squared Error): {mse:.2f}")
	print(f"RMSE (Root Mean Squared Error): {rmse:.2f}")
	print(f"MAE  (Mean Absolute Error): {mae:.2f}")
	print(f"R²   (Coefficient of Determination): {r2:.4f}")
	print(f"\nInterpretation:")
	print(f"- The model is off by an average of {mae:.0f}€ per prediction")
	print(f"- R² = {r2:.2%} of the price variance is explained by the model")

	display_graph(kms, prices, theta0, theta1, km, price)

if __name__ == "__main__":
	main()
