import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate timestamps for 24 hours of data at 5-minute intervals
timestamps = [datetime.now() - timedelta(minutes=i*5) for i in range(288)]
timestamps.reverse()  # Make timestamps go forward in time

# Initialize data dictionary
data = {
    'timestamp': timestamps,
    
    # Air Quality Sensors
    'co2_ppm': np.random.normal(400, 50, len(timestamps)),  # CO2 in parts per million
    'pm25_ugm3': np.random.normal(15, 5, len(timestamps)),  # PM2.5 in µg/m³
    
    # Temperature & Humidity Sensors
    'temperature_c': np.random.normal(25, 3, len(timestamps)),  # Temperature in Celsius
    'humidity_pct': np.random.normal(60, 10, len(timestamps)),  # Humidity percentage
    
    # Soil Moisture Sensors
    'soil_moisture_pct': np.random.normal(35, 5, len(timestamps)),  # Soil moisture percentage
    
    # Water Quality Sensors
    'water_ph': np.random.normal(7, 0.5, len(timestamps)),  # pH level
    'water_turbidity_ntu': np.random.normal(5, 1, len(timestamps)),  # Turbidity in NTU
}

# Create DataFrame
df = pd.DataFrame(data)

# Apply constraints to make data more realistic
df['co2_ppm'] = df['co2_ppm'].clip(350, 800)  # Typical outdoor CO2 range
df['pm25_ugm3'] = df['pm25_ugm3'].clip(0, 50)  # Realistic PM2.5 range
df['humidity_pct'] = df['humidity_pct'].clip(0, 100)  # Valid humidity range
df['soil_moisture_pct'] = df['soil_moisture_pct'].clip(0, 100)  # Valid moisture range
df['water_ph'] = df['water_ph'].clip(0, 14)  # Valid pH range
df['water_turbidity_ntu'] = df['water_turbidity_ntu'].clip(0, 20)  # Typical turbidity range

# Add some daily patterns to temperature
time_of_day = np.array([(t.hour + t.minute/60) for t in df['timestamp']])
temperature_variation = 2 * np.sin(2 * np.pi * (time_of_day - 14) / 24)  # Peak at 2 PM
df['temperature_c'] += temperature_variation

# Save to CSV
df.to_csv('environmental_monitoring/iot_data.csv', index=False)

print("Dataset preview:")
print(df.head())

print("\nDataset summary statistics:")
print(df.describe())
