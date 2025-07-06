# Temperature Modeling Project

This project uses a multivariable regression model to simulate and analyze temperature changes based on:
- Time of day (t)
- Humidity (h)
- Altitude (a)

## Features
- Simulates temperature using a non-linear polynomial function
- Calculates gradients and steepest descent
- Compares climate data for three cities
- Computes triple integral to estimate total temperature load over a region

## Tools Used
- Python (NumPy, pandas, SciPy)
- Math concepts: Gradient, Integrals

## Model Function
```
T(t, h, a) = 31.285 + 0.7046t − 0.0122h − 0.0161a − 0.0228t² − 0.0003th + 0.0003ta + 0.0200h² − 0.0001ha − 0.0007a²
```

## Project Structure
- `01_data_preprocessing.py`: Generates sample dataset
- `02_temperature_modeling.py`: Defines and tests T(t,h,a)
- `03_gradient_analysis.py`: Computes gradients and steepest descent
- `04_city_comparison.py`: Compares temperature across 3 cities
- `05_triple_integral_estimate.py`: Estimates accumulated temperature over a range

## Example Output
```
City B: 106.86°C (hottest)
City C: 0.45°C (coldest)
Triple Integral: 26652.29°C
```