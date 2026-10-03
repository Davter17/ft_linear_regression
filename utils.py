import csv

def load_data(filename="./data.csv"):
	kms = []
	prices = []
	try:
		with open(filename, "r") as f:
			reader = csv.DictReader(f)
			for i, row in enumerate(reader, 1):
				try:
					km_raw = row.get("km")
					price_raw = row.get("price")
					if km_raw is None or price_raw is None:
						print(f"Error: row {i} is incomplete")
						return None, None
					km_raw = km_raw.strip()
					price_raw = price_raw.strip()
					if km_raw == "" or price_raw == "":
						print(f"Error: row {i} has empty values")
						return None, None
					km = int(km_raw)
					price = int(price_raw)
					if km < 0 or price < 0:
						print(f"Error: row {i} has negative values (km={km}, price={price})")
						return None, None
					kms.append(km)
					prices.append(price)
				except ValueError as e:
					print(f"Error: row {i} has invalid data - {e}")
					return None, None
	except FileNotFoundError:
		print(f"Error: {filename} not found")
		return None, None
	except PermissionError:
		print(f"Error: you don't have permission to read {filename}")
		return None, None
	except Exception as e:
		print(f"Error reading {filename}: {e}")
		return None, None
	return kms, prices
