import json
from utils import load_data

def main():
	kms, prices = load_data()
	if kms is None:
		return

	lenDatas = len(kms)
	if lenDatas < 2:
		print("Error: need at least 2 data points for linear regression")
		return

	km_min = min(kms)
	km_max = max(kms)
	price_min = min(prices)
	price_max = max(prices)

	if km_max == km_min:
		print("Error: all mileage values are identical")
		return
	if price_max == price_min:
		print("Error: all price values are identical")
		return

	kms_norm = [(k_act - km_min) / (km_max - km_min) for k_act in kms]
	prices_norm = [(p_act - price_min) / (price_max - price_min) for p_act in prices]

	theta0 = 0.0
	theta1 = 0.0
	lr = 0.1
	iterations = 1000

	for i in range(iterations):
		sumError0 = 0.0
		sumError1 = 0.0
		for j in range(lenDatas):
			estimate = theta0 + theta1 * kms_norm[j]
			errorPrice = estimate - prices_norm[j]
			sumError0 += errorPrice
			sumError1 += errorPrice * kms_norm[j]
		theta0 -= lr * (1 / lenDatas) * sumError0
		theta1 -= lr * (1 / lenDatas) * sumError1

	theta0_orig = theta0 * (price_max - price_min) + price_min - theta1 * (km_min / (km_max - km_min)) * (price_max - price_min)
	theta1_orig = theta1 * (price_max - price_min) / (km_max - km_min)

	mse = 0.0
	for j in range(lenDatas):
		estimate = theta0_orig + theta1_orig * kms[j]
		mse += (estimate - prices[j]) ** 2
	mse /= lenDatas

	print(f"theta0: {theta0_orig}")
	print(f"theta1: {theta1_orig}")
	print(f"MSE: {mse}")

	data = {"theta0": theta0_orig, "theta1": theta1_orig}
	try:
		with open("./trained_data.json", "w") as f:
			json.dump(data, f)
	except PermissionError:
		print("Error: you don't have permission to write trained_data.json")
		return
	except Exception as e:
		print(f"Error writing trained_data.json: {e}")
		return

if __name__ == "__main__":
	main()
