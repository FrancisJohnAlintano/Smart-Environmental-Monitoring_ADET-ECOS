import pandas as pd
from web3 import Web3
import time

# Connect to local Ganache blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if web3.is_connected():
    print("✅ Connected to Ganache successfully!")
else:
    print("❌ Connection failed. Ensure Ganache is running.")

# Replace with your deployed contract address from Remix
contract_address = Web3.to_checksum_address("0x555BbC6AD8185B306E12051D49bdBFa5F0cEBD18")
# Replace with the address that deployed the contract (the owner)
owner_address = Web3.to_checksum_address("0x1CB8a815F37D32b97E30CbdaECeba3C8fC1f891B")

print(f"Using contract address: {contract_address}")
print(f"Using owner address: {owner_address}")

# Simplified Contract ABI with single data parameter
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
				"name": "sensorId",
				"type": "string"
			}
		],
		"name": "BatchedDataStored",
		"type": "event"
	},
	{
		"inputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "sensorId",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "dataType",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "value",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "unit",
						"type": "string"
					}
				],
				"internalType": "struct EnvironmentalMonitoring.SensorDataInput",
				"name": "_data",
				"type": "tuple"
			}
		],
		"name": "storeBatchedData",
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
		"name": "batchedRecords",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "sensorId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "dataType",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "value",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "unit",
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
		"name": "getBatchedRecord",
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
		"name": "getLatestBatchedRecord",
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
		"name": "getTotalBatchedRecords",
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
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "validParameters",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

try:
    # Load the smart contract
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    
    # Set the owner address as the default account
    web3.eth.default_account = owner_address
    
    print(f"✅ Connected to Smart Contract at {contract_address}")
    
    # Verify owner
    contract_owner = contract.functions.owner().call()
    print(f"Contract owner address: {contract_owner}")
    print(f"Your address: {owner_address}")
    
    if contract_owner.lower() != owner_address.lower():
        print(f"❌ Error: The provided address is not the contract owner!")
        print(f"Please use the owner address: {contract_owner}")
        exit(1)
    else:
        print(f"✅ Owner verification successful")
    
    # Verify storage space
    max_entries = contract.functions.MAX_ENTRIES().call()
    print(f"Maximum storage capacity: {max_entries} records")
    
    # Load the new simplified CSV data
    df = pd.read_csv("simple_iot_data.csv")
    print(f"\nLoaded simplified CSV with {len(df)} rows")
    print("\nSimplified CSV structure:")
    print(df.head())

    def send_sensor_data(sensor_data):
        """Sends simplified IoT data to the deployed smart contract"""
        try:
            # Create the struct tuple for the transaction
            data_tuple = (
                sensor_data["sensorId"],
                sensor_data["dataType"],
                sensor_data["value"],
                sensor_data["unit"]
            )
            
            txn = contract.functions.storeBatchedData(data_tuple).transact({
                'from': owner_address,
                'gas': 500000  # Reduced gas for simplified data
            })
            receipt = web3.eth.wait_for_transaction_receipt(txn)
            print(f"✅ Data Stored: {sensor_data['dataType']} = {sensor_data['value']} {sensor_data['unit']}, Txn Hash: {receipt.transactionHash.hex()}")
            return True
        except Exception as e:
            print(f"❌ Error storing data: {str(e)}")
            return False
    
    # Process each row and send simplified data to blockchain
    print("\nStoring simplified sensor data on blockchain...")
    stored_count = 0
    
    # Store data from the simplified CSV
    for index, row in df.iterrows():
        # Prepare sensor data from CSV
        sensor_data = {
            "sensorId": row["sensor_id"],
            "dataType": row["data_type"],
            "value": str(row["value"]),
            "unit": row["unit"]
        }
        
        success = send_sensor_data(sensor_data)
        if success:
            stored_count += 1
            print(f"Progress: {stored_count}/{len(df)} records stored ({(stored_count/len(df))*100:.1f}%)")
        else:
            print(f"Failed to store data for row {index}. Stopping...")
            exit(1)
        
        time.sleep(1)  # Delay to prevent flooding transactions
    
    # Verify storage
    total_records = contract.functions.getTotalBatchedRecords().call()
    print(f"\nTotal records stored: {total_records}")
    
    if total_records > 0:
        # Get the latest record
        print("\nLatest record:")
        try:
            record = contract.functions.getLatestBatchedRecord().call()
            print(f"  Timestamp: {record[0]}")
            print(f"  Sensor ID: {record[1]}")
            print(f"  Data Type: {record[2]}")
            print(f"  Value: {record[3]}")
            print(f"  Unit: {record[4]}")
        except Exception as e:
            print(f"Could not retrieve latest record: {str(e)}")

except Exception as e:
    print(f"❌ Error: {str(e)}")