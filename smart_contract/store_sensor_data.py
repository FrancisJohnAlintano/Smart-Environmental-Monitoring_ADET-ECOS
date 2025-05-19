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
contract_address = Web3.to_checksum_address("0x6Ff48a55dfad5ab57134940Db605E20b52e7CA78")
# Replace with the address that deployed the contract (the owner)
owner_address = Web3.to_checksum_address("0x01EfCCF4f049c32E5b09D48B22238BA17094324e")

print(f"Using contract address: {contract_address}")
print(f"Using owner address: {owner_address}")

# Contract ABI from the updated smart contract
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
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "parameterType",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "value",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "unit",
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
				"name": "_sensorId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_parameterType",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_value",
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
				"name": "sensorId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "parameterType",
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
				"internalType": "string",
				"name": "_parameterType",
				"type": "string"
			}
		],
		"name": "getLatestRecord",
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
		"name": "getRecord",
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
				"name": "parameterType",
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
    
    # Load IoT sensor data from CSV with reduced sampling
    df = pd.read_csv("data_simulation/iot_data.csv")
    # Take every 3rd row to reduce data volume
    df = df.iloc[::3, :]  
    print(f"\nLoaded {len(df)} data points from CSV (sampling every 3rd row)")
    print("\nFirst few rows of the data:")
    print(df.head())

    def format_value(value):
        """Format numeric value to string with 2 decimal places"""
        return f"{float(value):.2f}"
    
    def send_iot_data(device_id, data_type, data_value):
        """Sends IoT data to the deployed smart contract"""
        try:
            # Format the value to 2 decimal places
            formatted_value = format_value(data_value)
            
            txn = contract.functions.storeData(device_id, data_type, formatted_value).transact({
                'from': owner_address,
                'gas': 3000000
            })
            receipt = web3.eth.wait_for_transaction_receipt(txn)
            print(f"✅ Data Stored: {data_type} - {formatted_value}, Txn Hash: {receipt.transactionHash.hex()}")
            return True
        except Exception as e:
            print(f"❌ Error storing data: {str(e)}")
            return False
    
    # Process each row and send data to blockchain
    print("\nStoring data on blockchain...")
    sensor_id = "ENV_MONITOR_01"
    total_parameters = len(df) * 7  # 7 parameters per row
    stored_count = 0
    
    for index, row in df.iterrows():
        # Store each parameter
        parameters = {
            "CO2": row["co2_ppm"],
            "PM2.5": row["pm25_ugm3"],
            "Temperature": row["temperature_c"],
            "Humidity": row["humidity_pct"],
            "SoilMoisture": row["soil_moisture_pct"],
            "WaterPH": row["water_ph"],
            "WaterTurbidity": row["water_turbidity_ntu"]
        }
        
        for param_type, value in parameters.items():
            success = send_iot_data(sensor_id, param_type, value)
            stored_count += 1 if success else 0
            print(f"Progress: {stored_count}/{total_parameters} records stored ({(stored_count/total_parameters)*100:.1f}%)")
            
            if not success:
                print(f"Failed to store {param_type} data. Stopping...")
                exit(1)
            time.sleep(1)  # Delay to prevent flooding transactions
    
    # Verify storage
    total_records = contract.functions.getTotalRecords().call()
    print(f"\nTotal records stored: {total_records}")
    
    if total_records > 0:
        # Get the latest records for each parameter type
        print("\nLatest readings for each parameter:")
        parameters = ["CO2", "PM2.5", "Temperature", "Humidity", "SoilMoisture", "WaterPH", "WaterTurbidity"]
        
        for param in parameters:
            try:
                record = contract.functions.getLatestRecord(param).call()
                print(f"\n{param}:")
                print(f"  Timestamp: {record[0]}")
                print(f"  Sensor ID: {record[1]}")
                print(f"  Value: {record[2]}")
                print(f"  Unit: {record[3]}")
            except Exception as e:
                print(f"Could not retrieve latest {param} reading: {str(e)}")

except Exception as e:
    print(f"❌ Error: {str(e)}")
