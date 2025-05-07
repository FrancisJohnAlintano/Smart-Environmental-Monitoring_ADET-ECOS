# IoT Environmental Monitoring System

This project consists of two main components:
1. A data simulation system that generates realistic IoT sensor data for environmental monitoring
2. A smart contract for storing and managing the sensor data on a blockchain

## Project Structure

```
.
├── data_simulation/          # IoT data generation components
│   ├── IoT_Data_Generation.ipynb
│   └── iot_data.csv
├── smart_contract/          # Blockchain storage components
│   └── IoTDataStorage.sol
└── README.md
```

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

## Data Simulation Component

The data simulation is implemented in a Jupyter Notebook that generates realistic IoT sensor data.

### Requirements

- Python 3.x
- Jupyter Notebook
- pandas
- numpy

### Sensor Types Simulated

### Usage

1. Open `data_simulation/IoT_Data_Generation.ipynb` in Jupyter Notebook
2. Run the notebook cells to generate new sensor data
3. The data will be saved to `data_simulation/iot_data.csv`

## Smart Contract Component

The `IoTDataStorage.sol` contract provides blockchain storage for the IoT sensor data. It is designed to be used with:
- Remix IDE for contract development and testing
- Ganache for local blockchain deployment

### Contract Features
- Store sensor readings with timestamp
- Retrieve latest reading for any sensor
- Track reading history per sensor
- Event emission for data storage operations
