from web3 import Web3
import pandas as pd
import numpy as np

# Connect to Ethereum node (user should replace with their provider URL)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))  # Default Ganache URL

# Load contract ABI and address (user should replace with actual values)
contract_address = '0xB2F15D4a01F8977C369fcfC300bd1F1e46686b2C'
contract_abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "deviceId",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "dataType",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "dataValue",
				"type": "string"
			}
		],
		"name": "DataStored",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_deviceId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_dataType",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_dataValue",
				"type": "string"
			}
		],
		"name": "storeData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "dataRecords",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "deviceId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "dataType",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "dataValue",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getRecord",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTotalRecords",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "MAX_ENTRIES",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

# Create contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def retrieve_and_process_data():
    # Get total records
    total_records = contract.functions.getTotalRecords().call()
    print(f"Total IoT records stored: {total_records}")

    # Retrieve all IoT records
    data = []
    for i in range(total_records):
        record = contract.functions.getRecord(i).call()
        data.append({
            "timestamp": record[0],
            "device_id": record[1],
            "data_type": record[2],
            "data_value": record[3]
        })

    # Convert to DataFrame
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    # Extract numeric values
    df["numeric_value"] = df["data_value"].str.extract(r'(\d+\.?\d*)').astype(float)

    # Handle missing values
    if df.isnull().sum().sum() < len(df) * 0.1:  # If less than 10% missing
        df.fillna(0, inplace=True)
    else:
        # Use mean/median based on data type
        for col in df.select_dtypes(include=['float64']):
            df[col].fillna(df[col].median(), inplace=True)

    # Save to CSV
    df.to_csv("cleaned_iot_data.csv", index=False)
    print("✅ Cleaned IoT data saved successfully as cleaned_iot_data.csv")

    return df

if __name__ == "__main__":
    df = retrieve_and_process_data()
    print(df.head())
