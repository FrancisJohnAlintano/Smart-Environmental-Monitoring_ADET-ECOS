# IoT Environmental Monitoring Simulation

This project simulates IoT sensor data for environmental monitoring systems. It generates realistic data for multiple sensor types to simulate a comprehensive environmental monitoring setup.

## Sensor Types

1. **Air Quality Sensors**
   - CO2 Levels (350-800 ppm)
   - PM2.5 (0-50 µg/m³)

2. **Temperature & Humidity Sensors**
   - Temperature (15-35°C)
   - Humidity (0-100%)

3. **Soil Moisture Sensors**
   - Soil Moisture Levels (0-100%)

4. **Water Quality Sensors**
   - pH Levels (0-14)
   - Turbidity (0-20 NTU)

## Data Generation

The script generates 24 hours of data at 5-minute intervals, resulting in 288 records per dataset. The data includes realistic variations and patterns:

- Daily temperature cycles
- Bounded random variations for each sensor type
- Realistic value ranges for each measurement
- Timestamps for each reading

## File Structure

- `iot_sensor_data.py` - Main script for generating sensor data
- `iot_data.csv` - Generated sensor data output

## Requirements

- Python 3.x
- pandas
- numpy

## Usage

To generate new sensor data:

```bash
python iot_sensor_data.py
```

This will create a new `iot_data.csv` file with simulated sensor readings.
