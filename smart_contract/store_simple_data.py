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
contract_address = Web3.to_checksum_address("0xB2F15D4a01F8977C369fcfC300bd1F1e46686b2C")
# Replace with the address that deployed the contract (the owner)
owner_address = Web3.to_checksum_address("0x7794122Ec9c2a50FE00E05a3090755a4AD5A992b")

print(f"Using contract address: {contract_address}")
print(f"Using owner address: {owner_address}")

# Contract ABI
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
    
    # Load the environmental data CSV
    df = pd.read_csv("environmental_data.csv")
    print(f"\nLoaded CSV with {len(df)} rows")
    print("\nData structure:")
    print(df.head())

    def send_environmental_data(device_id, data_type, value):
        """Sends environmental data to the deployed smart contract"""
        try:
            txn = contract.functions.storeData(device_id, data_type, str(value)).transact({
                'from': owner_address,
                'gas': 500000
            })
            receipt = web3.eth.wait_for_transaction_receipt(txn)
            print(f"✅ Data Stored: {data_type} = {value}, Txn Hash: {receipt.transactionHash.hex()}")
            return True
        except Exception as e:
            print(f"❌ Error storing data: {str(e)}")
            return False
    
    # Process each row and send data to blockchain
    print("\nStoring environmental data on blockchain...")
    stored_count = 0
    
    # Process each environmental parameter separately
    for index, row in df.iterrows():
        # Temperature
        success = send_environmental_data(
            row["device_id"],
            "Temperature",
            f"{row['temperature']}°C"
        )
        if success:
            stored_count += 1
        else:
            print(f"Failed to store temperature data for row {index}. Stopping...")
            exit(1)
        
        # Humidity
        success = send_environmental_data(
            row["device_id"],
            "Humidity",
            f"{row['humidity']}%"
        )
        if success:
            stored_count += 1
        else:
            print(f"Failed to store humidity data for row {index}. Stopping...")
            exit(1)
        
        # CO2 Level
        success = send_environmental_data(
            row["device_id"],
            "CO2",
            f"{row['co2_level']}ppm"
        )
        if success:
            stored_count += 1
        else:
            print(f"Failed to store CO2 data for row {index}. Stopping...")
            exit(1)
        
        # Air Quality
        success = send_environmental_data(
            row["device_id"],
            "AirQuality",
            str(row['air_quality'])
        )
        if success:
            stored_count += 1
        else:
            print(f"Failed to store air quality data for row {index}. Stopping...")
            exit(1)
        
        print(f"Progress: {(index + 1)}/{len(df)} records processed")
        time.sleep(1)  # Delay to prevent flooding transactions
    
    # Verify storage
    total_records = contract.functions.getTotalRecords().call()
    print(f"\nTotal records stored: {total_records}")
    
    if total_records > 0:
        # Get the first record
        print("\nFirst record:")
        try:
            record = contract.functions.getRecord(0).call()
            print(f"  Timestamp: {record[0]}")
            print(f"  Device ID: {record[1]}")
            print(f"  Data Type: {record[2]}")
            print(f"  Value: {record[3]}")
        except Exception as e:
            print(f"Could not retrieve record: {str(e)}")

except Exception as e:
    print(f"❌ Error: {str(e)}")
