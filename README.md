# ft_linear_regression - 42 School Project

Implementation of a simple linear regression algorithm from scratch using gradient descent to predict car prices based on mileage.

## Overview

This project predicts car prices using the linear hypothesis:

```
price = theta0 + theta1 * mileage
```

The model is trained using gradient descent with min-max normalization for better convergence. Parameters are saved to `trained_data.json` for later predictions.

## Features

### Training
- Gradient descent optimization
- Min-max normalization for better convergence
- Configurable learning rate and iterations
- Saves trained parameters to JSON
- Handles edge cases (empty data, single point, identical values)

### Prediction & Evaluation
- Real-time price estimation from mileage input
- Visual graph with regression line and data points
- Model accuracy metrics (MSE, RMSE, MAE, R²)
- Input validation for negative/invalid values

## Project Structure

```
linearRegression/
├── data.csv              # Dataset with 24 cars (mileage and price)
├── training.py           # Train the model and save parameters
├── predict.py            # Predict price, show metrics and visualize results
├── utils.py              # Shared data loading utilities
├── trained_data.json     # Trained parameters (generated)
└── .gitignore
```

## Dependencies

- Python 3
- matplotlib (for visualization)

## Installation

### Option 1: Virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate
pip install matplotlib
```

### Option 2: System package
```bash
sudo apt install python3-matplotlib
```

## Usage

### Train the model
```bash
python training.py
```

Output:
```
theta0: 8481.17
theta1: -0.0213
MSE: 445727.42
```

### Make predictions and evaluate
```bash
python predict.py
```

Enter mileage when prompted:
```
Enter the car mileage: 100000
The estimated price is: 6353.80

=== Model accuracy metrics ===

MSE  (Mean Squared Error): 445727.42
RMSE (Root Mean Squared Error): 667.63
MAE  (Mean Absolute Error): 556.50
R²   (Coefficient of Determination): 0.7329

Interpretation:
- The model is off by an average of 557€ per prediction
- R² = 73.29% of the price variance is explained by the model
```

A graph displays:
- Blue dots: real data
- Green line: regression line
- Red dot: your prediction

## Error Handling

The programs handle all edge cases gracefully:

- **Empty CSV**: "Error: need at least 2 data points for linear regression"
- **Single data point**: "Error: need at least 2 data points for linear regression"
- **Incomplete rows**: "Error: row X is incomplete"
- **Invalid data**: "Error: row X has invalid data"
- **Negative values**: "Error: row X has negative values"
- **Identical values**: "Error: all mileage/price values are identical"
- **Missing JSON**: Uses default values with warning
- **Corrupted JSON**: "Error: trained_data.json is corrupted"
- **Invalid user input**: Re-prompts until valid number entered

## Algorithm

### Gradient Descent

The algorithm iteratively adjusts theta0 and theta1 to minimize prediction error:

```
theta0 = theta0 - alpha * (1/m) * sum(y_hat - y)
theta1 = theta1 - alpha * (1/m) * sum(y_hat - y) * x
```

Where:
- `alpha` = learning rate (0.1)
- `m` = number of samples
- `y_hat` = predicted value
- `y` = actual value

### Normalization

Data is normalized using min-max scaling:

```
x_norm = (x - x_min) / (x_max - x_min)
```

After training, parameters are denormalized to work with original values.

## Configuration

In `training.py`, you can adjust:
- **lr** (learning rate): 0.1
- **iterations**: 1000

A learning rate too high may cause divergence, too low will converge slowly.

## Code Quality

- Comprehensive error handling for all edge cases
- Data validation with row numbers for CSV errors
- Input validation for negative/invalid values
- JSON validation for corrupted files
- Clean separation of concerns with shared utilities

## Requirements

- Python 3
- matplotlib
- Unix-like environment (Linux, macOS, or WSL)

## Author

- **Mario Pico** (@Davter17)

## License

This project is part of the 42 school curriculum and follows its academic guidelines.
