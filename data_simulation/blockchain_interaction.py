from web3 import Web3
import json

# Connect to local Ganache blockchain using custom HTTP provider
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url, request_kwargs={'timeout': 30}))

# Check connection
if web3.is_connected():
    print("✅ Connected to Ganache successfully!")
else:
    print("❌ Connection failed. Ensure Ganache is running.")

# Contract details
contract_address = "0x4D0680Daf1edd5128C3e34C6Db43659410Fb71Df"

# Contract ABI
abi = [
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
                "internalType": "uint256",
                "name": "co2_ppm",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "pm25_ugm3",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "temperature_c",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "humidity_pct",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "soil_moisture_pct",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "water_ph",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "water_turbidity_ntu",
                "type": "uint256"
            }
        ],
        "name": "DataStored",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_co2_ppm",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_pm25_ugm3",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_temperature_c",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_humidity_pct",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_soil_moisture_pct",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_water_ph",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_water_turbidity_ntu",
                "type": "uint256"
            }
        ],
        "name": "storeData",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getTotalRecords",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}],
        "name": "getRecord",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Load the smart contract
contract = web3.eth.contract(address=contract_address, abi=abi)

# Set the default sender address (first account from Ganache)
web3.eth.default_account = web3.eth.accounts[0]

print(f"✅ Connected to Smart Contract at {contract_address}")

# Test storing dummy data
try:
    # Store dummy environmental data
    txn = contract.functions.storeData(
        400,      # CO2 PPM
        25,       # PM2.5 (µg/m³)
        22,       # Temperature (°C)
        65,       # Humidity (%)
        35,       # Soil Moisture (%)
        7,        # Water pH
        5         # Water Turbidity (NTU)
    ).transact({
        'from': web3.eth.default_account,
        'gas': 1000000
    })
    
    # Wait for transaction to be mined
    web3.eth.wait_for_transaction_receipt(txn)
    print("✅ Dummy data stored on blockchain!")

    # Get total records
    total_records = contract.functions.getTotalRecords().call()
    print(f"Total Records: {total_records}")

    # Retrieve and display the first record
    if total_records > 0:
        record = contract.functions.getRecord(0).call()
        print("\nFirst Stored Record:")
        print(f"Timestamp: {record[0]}")
        print(f"CO2: {record[1]} PPM")
        print(f"PM2.5: {record[2]} µg/m³")
        print(f"Temperature: {record[3]} °C")
        print(f"Humidity: {record[4]} %")
        print(f"Soil Moisture: {record[5]} %")
        print(f"Water pH: {record[6]}")
        print(f"Water Turbidity: {record[7]} NTU")

except Exception as e:
    print(f"❌ Error: {str(e)}")
