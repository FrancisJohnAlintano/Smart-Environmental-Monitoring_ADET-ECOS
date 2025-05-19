from web3 import Web3

# Connect to local Ganache blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if web3.is_connected():
    print("✅ Connected to Ganache successfully!")
else:
    print("❌ Connection failed. Ensure Ganache is running.")

# Replace with your deployed contract address from Remix
contract_address = "0x76CcB060Fc3037a4b3Ea0fcA6aB5fA75B53f03BA"

# Replace with the address that deployed the contract (the owner)
owner_address = "0xF7bCCC490DfeAEDAF10b6b12A9aE05eD9B05e77c"

# Contract ABI - Replace this with your actual ABI from Remix after deploying
contract_abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"},{"indexed":false,"internalType":"string","name":"sensorId","type":"string"},{"indexed":false,"internalType":"string","name":"parameterType","type":"string"},{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":false,"internalType":"string","name":"unit","type":"string"}],"name":"DataStored","type":"event"},{"inputs":[{"internalType":"string","name":"_sensorId","type":"string"},{"internalType":"string","name":"_parameterType","type":"string"},{"internalType":"string","name":"_value","type":"string"}],"name":"storeData","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"dataRecords","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"string","name":"sensorId","type":"string"},{"internalType":"string","name":"parameterType","type":"string"},{"internalType":"string","name":"value","type":"string"},{"internalType":"string","name":"unit","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_parameterType","type":"string"}],"name":"getLatestRecord","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"string","name":"sensorId","type":"string"},{"internalType":"string","name":"value","type":"string"},{"internalType":"string","name":"unit","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRecord","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"string","name":"sensorId","type":"string"},{"internalType":"string","name":"parameterType","type":"string"},{"internalType":"string","name":"value","type":"string"},{"internalType":"string","name":"unit","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalRecords","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_ENTRIES","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"validParameters","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]

try:
    # Load the smart contract
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Set the owner address as the default account
    web3.eth.default_account = owner_address

    print(f"✅ Connected to Smart Contract at {contract_address}")
    print(f"✅ Using owner address: {owner_address}")

    # Verify we're using the correct account
    contract_owner = contract.functions.owner().call()
    if contract_owner.lower() != owner_address.lower():
        print("❌ Error: The provided address is not the contract owner!")
        print(f"Contract owner is: {contract_owner}")
        exit(1)

    # Test contract interaction
    def test_contract_interaction():
        try:
            # Store dummy data
            txn = contract.functions.storeData("TEST001", "Temperature", "22.5").transact({
                'from': owner_address,
                'gas': 1000000
            })
            web3.eth.wait_for_transaction_receipt(txn)
            print("✅ Dummy data stored on blockchain!")

            # Get total records
            total_records = contract.functions.getTotalRecords().call()
            print(f"Total Records: {total_records}")

            # Get the first record
            if total_records > 0:
                record = contract.functions.getRecord(0).call()
                print("First Stored Record:")
                print(f"  Timestamp: {record[0]}")
                print(f"  Sensor ID: {record[1]}")
                print(f"  Parameter Type: {record[2]}")
                print(f"  Value: {record[3]}")
                print(f"  Unit: {record[4]}")

        except Exception as e:
            print(f"❌ Error during contract interaction: {str(e)}")

    # Run the test
    test_contract_interaction()

except Exception as e:
    print(f"❌ Error loading contract: {str(e)}")
