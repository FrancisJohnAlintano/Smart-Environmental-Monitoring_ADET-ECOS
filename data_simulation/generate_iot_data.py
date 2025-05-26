import csv
from datetime import datetime, timedelta
import random

def generate_temperature_data(start_time, num_records=100):
    data = []
    current_time = start_time
    
    for _ in range(num_records):
        # Generate temperature between 12°C and 34°C with 2 decimal precision
        temperature = round(random.uniform(12.0, 34.0), 2)
        
        # Create record
        record = {
            'timestamp': current_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
            'sensor_id': 'TEMP_001',
            'data_type': 'Temperature',
            'value': temperature,
            'unit': 'C'
        }
        data.append(record)
        
        # Increment time by 15 minutes
        current_time += timedelta(minutes=15)
    
    return data

def save_to_csv(data, filename):
    fieldnames = ['timestamp', 'sensor_id', 'data_type', 'value', 'unit']
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # Start time (24 hours ago from current time)
    start_time = datetime.now() - timedelta(days=1)
    
    # Generate data
    iot_data = generate_temperature_data(start_time, num_records=96)  # 96 records = 24 hours of 15-min intervals
    
    # Save to CSV using absolute path
    csv_path = 'simple_iot_data.csv'
    save_to_csv(iot_data, csv_path)
    print(f"IoT data has been generated and saved to {csv_path}")
