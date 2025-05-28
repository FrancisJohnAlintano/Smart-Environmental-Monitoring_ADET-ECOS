import pandas as pd
import numpy as np
from datetime import datetime, timedelta

num_records = 100  # Adjust this number as needed

# Example for Environmental Monitoring
data = []

for _ in range(num_records):
    record = {
        "timestamp": datetime.now() - timedelta(minutes=np.random.randint(0, 1440)),  # Random timestamp in the last 24 hours
        "device_id": f"ENV{np.random.randint(100, 999)}",  # Random device ID
        "temperature": round(np.random.uniform(20.0, 35.0), 1),  # Temperature in Celsius
        "humidity": round(np.random.uniform(30.0, 80.0), 1),  # Humidity percentage
        "co2_level": np.random.randint(300, 1500),  # CO2 levels in ppm
        "air_quality": round(np.random.uniform(0, 500), 1)  # Air quality index
    }
    data.append(record)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("environmental_data.csv", index=False)
df.to_json("environmental_data.json", orient="records")

# Display first few rows
print("Generated Environmental Monitoring Data:")
print(df.head())
