# Blockchain Interaction with Environmental Monitoring Smart Contract

This document provides instructions for interacting with the IoTDataStorage smart contract deployed on Ganache.

## Prerequisites

- Python 3.8+
- web3.py library (`pip install web3`)
- Running Ganache instance on port 7545
- Deployed IoTDataStorage smart contract

## Files

- `blockchain_interaction.py` - Python script version
- `blockchain_interaction.ipynb` - Jupyter Notebook version

## Smart Contract Details

- Contract Address: `0x4D0680Daf1edd5128C3e34C6Db43659410Fb71Df`
- Network: Ganache (http://127.0.0.1:7545)

## Usage

### Python Script

```bash
python blockchain_interaction.py
```

### Jupyter Notebook

1. Start Jupyter Notebook
2. Open `blockchain_interaction.ipynb`
3. Run each cell sequentially

## Features

- Connects to Ganache using custom HTTP provider
- Loads the IoTDataStorage smart contract
- Stores environmental monitoring data:
  - CO2 levels (PPM)
  - PM2.5 (µg/m³)
  - Temperature (°C)
  - Humidity (%)
  - Soil Moisture (%)
  - Water pH
  - Water Turbidity (NTU)
- Retrieves and displays stored records

## Example Output

```
✅ Connected to Ganache successfully!
✅ Connected to Smart Contract at 0x4D0680Daf1edd5128C3e34C6Db43659410Fb71Df
✅ Dummy data stored on blockchain!
Total Records: 1

First Stored Record:
Timestamp: 1746606346
CO2: 400 PPM
PM2.5: 25 µg/m³
Temperature: 22 °C
Humidity: 65 %
Soil Moisture: 35 %
Water pH: 7
Water Turbidity: 5 NTU
```

## Error Handling

The scripts include error handling for common scenarios:
- Ganache connection failures
- Smart contract interaction errors
- Transaction failures

## Notes

- Ensure Ganache is running before executing the scripts
- The contract address must match your deployed contract
- Gas limit is set to 1,000,000 for transactions
- Uses the first account in Ganache as the default sender
