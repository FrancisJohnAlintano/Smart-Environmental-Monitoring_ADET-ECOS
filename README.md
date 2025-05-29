# 🌍 Environmental IoT Data Storage on Blockchain

A comprehensive solution for secure and transparent environmental monitoring using blockchain technology. This project demonstrates how IoT sensor data can be stored immutably on the Ethereum blockchain using smart contracts and Python integration.

## 🎯 Project Overview

This system bridges the gap between IoT environmental sensors and blockchain technology, ensuring data integrity, transparency, and immutability for environmental monitoring applications.

### Key Features

- 🔒 **Secure**: Immutable blockchain storage prevents data tampering
- 👁️ **Transparent**: All transactions are publicly verifiable
- 🌐 **Decentralized**: No single point of failure
- 📝 **Auditable**: Complete transaction history
- ⚡ **Scalable**: Support for 1000+ environmental readings
- 🐍 **Python Integration**: Seamless blockchain interaction via Web3

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   IoT Sensors   │ ──▶│  Python Scripts  │ ──▶│  Smart Contract │
│                 │    │                  │    │                 │
│ • Temperature   │    │ • Data Processing│    │ • Data Storage  │
│ • Humidity      │    │ • Web3 Interface │    │ • Verification  │
│ • CO2 Levels    │    │ • Blockchain TX  │    │ • Retrieval     │
│ • Air Quality   │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                ↓
                       ┌──────────────────┐
                       │ Ganache Network  │
                       │                  │
                       │ • Local Testing  │
                       │ • Transaction    │
                       │   Management     │
                       └──────────────────┘
```

## 📁 Project Structure

```
environmental_monitoring/
├── 📊 data_simulation/
│   └── generate_iot_data.py          # IoT sensor data generation
├── ⛓️ smart_contract/
│   ├── IoTDataStorage.sol            # Smart contract for data storage
│   └── store_simple_data.py          # Python-blockchain integration
├── 📈 environmental_data.csv         # Generated sensor data
├── 📈 environmental_data.json        # Alternative data format
├── 🎨 presentation.html              # Project presentation
├── 📝 presentation_script.md         # Presentation script
├── ⚙️ .gitignore                     # Git ignore file
└── 📚 README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js (for Ganache)
- Ganache CLI or Ganache GUI
- Web browser (for presentation)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd environmental_monitoring
   ```

2. **Install Python dependencies**
   ```bash
   pip install web3 pandas numpy
   ```

3. **Install and setup Ganache**
   ```bash
   npm install -g ganache-cli
   # OR download Ganache GUI from https://trufflesuite.com/ganache/
   ```

4. **Start Ganache**
   ```bash
   ganache-cli --port 7545 --networkId 5777
   # OR start Ganache GUI on http://127.0.0.1:7545
   ```

### Usage

1. **Generate Environmental Data**
   ```bash
   cd data_simulation
   python generate_iot_data.py
   ```

2. **Deploy Smart Contract**
   - Open Remix IDE (https://remix.ethereum.org)
   - Load `smart_contract/IoTDataStorage.sol`
   - Connect to Ganache network
   - Deploy the contract
   - Copy the contract address

3. **Store Data on Blockchain**
   ```bash
   cd smart_contract
   # Update contract_address and owner_address in store_simple_data.py
   python store_simple_data.py
   ```

4. **View Presentation**
   ```bash
   # Open presentation.html in your browser
   start presentation.html  # Windows
   open presentation.html   # macOS
   ```

## 🔧 Configuration

### Smart Contract Settings

```solidity
// Storage capacity (adjustable)
uint256 public constant MAX_ENTRIES = 1000;

// Data structure
struct IoTData {
    uint256 timestamp;
    string deviceId;
    string dataType;
    string dataValue;
}
```

### Python Configuration

```python
# Ganache connection
ganache_url = "http://127.0.0.1:7545"

# Contract details (update these after deployment)
contract_address = "0x450394A99fbe8270Bfb8D9027d0d5172A755Df16"
owner_address = "0x33BBdA64f76eE0c52752bEf6Fe462B157161BC01"

# Transaction settings
gas_limit = 500000
```

## 📊 Environmental Data Types

The system monitors four critical environmental parameters:

| Parameter | Range | Unit | Description |
|-----------|-------|------|-------------|
| 🌡️ Temperature | 15-35 | °C | Ambient temperature |
| 💧 Humidity | 30-90 | % | Relative humidity |
| 🌬️ CO2 Levels | 350-500 | ppm | Carbon dioxide concentration |
| 🌍 Air Quality | 1-5 | Index | Air quality rating |

## ⛓️ Smart Contract Features

### Core Functions

- **`storeData()`**: Store environmental readings on blockchain
- **`getTotalRecords()`**: Get total number of stored records
- **`getRecord()`**: Retrieve specific record by index
- **`owner()`**: Get contract owner address

### Security Features

- Owner-only data storage
- Input validation
- Storage limit enforcement
- Event emission for transparency

### Events

```solidity
event DataStored(
    uint256 timestamp,
    string deviceId,
    string dataType,
    string dataValue
);
```

## 📈 Performance Metrics

### Current Statistics

- ✅ **100 CSV records** processed successfully
- ✅ **400 blockchain transactions** completed
- ✅ **4 data types** per device reading
- ✅ **1000 max storage capacity** (10x improvement)
- ✅ **~2 seconds** per transaction
- ✅ **100% success rate** achieved

### Transaction Details

- **Gas Limit**: 500,000 per transaction
- **Average Gas Used**: ~89,432
- **Transaction Cost**: ~0.01 ETH (on testnet)
- **Block Confirmation**: ~2 seconds

## 🛠️ Development

### Adding New Sensor Types

1. **Update data generation** in `generate_iot_data.py`
2. **Modify contract** if new data structures needed
3. **Update Python integration** in `store_simple_data.py`

### Extending Storage Capacity

```solidity
// Increase MAX_ENTRIES in IoTDataStorage.sol
uint256 public constant MAX_ENTRIES = 5000; // New limit
```

### Custom Data Processing

```python
# Add custom processing in store_simple_data.py
def process_custom_data(value):
    # Your custom logic here
    return processed_value
```

## 🎨 Presentation

The project includes a comprehensive presentation showcasing:

- 📋 Project overview and team introduction
- 🔗 Smart contract connection setup
- 📊 Data transactions and retrieval
- 🏆 Results and achievements

**To view**: Open `presentation.html` in any modern web browser

**Presentation script**: See `presentation_script.md` for detailed talking points

## 🔮 Future Enhancements

### Network Integration
- [ ] Deploy to Ethereum testnet (Ropsten/Goerli)
- [ ] IPFS integration for large data storage
- [ ] Real-time IoT sensor integration
- [ ] Multi-network support

### User Interface
- [ ] Web dashboard for data visualization
- [ ] Mobile app for remote monitoring
- [ ] Alert system for environmental anomalies
- [ ] Historical data analytics

### Advanced Features
- [ ] Data encryption for sensitive readings
- [ ] Multi-signature contract upgrades
- [ ] Automated data validation
- [ ] Integration with existing IoT platforms

## 🐛 Troubleshooting

### Common Issues

**Connection Failed**
```bash
❌ Connection failed. Ensure Ganache is running.
```
*Solution*: Start Ganache on port 7545

**Storage Limit Reached**
```bash
❌ Error: Storage limit reached
```
*Solution*: Increase MAX_ENTRIES in contract and redeploy

**Owner Verification Failed**
```bash
❌ Error: The provided address is not the contract owner!
```
*Solution*: Use the correct owner address from contract deployment

### Debug Mode

Enable detailed logging in `store_simple_data.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 👥 Team

- **Honey Grace Denolan** - Blockchain Developer
- **Adam Raymond Belda** - IoT Specialist  
- **Francis John Alintano** - Python Developer

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For questions and support:
- 📧 Email: [your-email@domain.com]
- 💬 Issues: Use GitHub Issues
- 📋 Documentation: See project wiki

---

**Made with ❤️ for environmental monitoring and blockchain innovation**
