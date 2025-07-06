import pandas as pd
import numpy as np

# Simulate data
data = {
    'Time': np.random.randint(0, 24, 100),
    'Humidity': np.random.randint(40, 101, 100),
    'Altitude': np.random.randint(0, 3001, 100)
}
df = pd.DataFrame(data)

# Apply the temperature function
T = (
    31.285 + 0.7046 * df['Time'] - 0.0122 * df['Humidity'] - 0.0161 * df['Altitude']
    - 0.0228 * df['Time']**2 - 0.0003 * df['Time'] * df['Humidity']
    + 0.0003 * df['Time'] * df['Altitude'] + 0.0200 * df['Humidity']**2
    - 0.0001 * df['Humidity'] * df['Altitude'] - 0.0007 * df['Altitude']**2
)
df['Temperature'] = T

df.to_csv("simulated_climate_data.csv", index=False)