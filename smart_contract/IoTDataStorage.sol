// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EnvironmentalMonitoring {
    struct BatchedSensorData {
        uint256 timestamp;
        string sensorId;
        string co2;
        string pm25;
        string temperature;
        string humidity;
        string soilMoisture;
        string waterPh;
        string waterTurbidity;
    }

    uint256 public constant MAX_ENTRIES = 1000;
    BatchedSensorData[] public batchedRecords;
    address public owner;
    mapping(string => string) public validParameters;

    event BatchedDataStored(
        uint256 timestamp,
        string sensorId,
        string co2,
        string pm25,
        string temperature,
        string humidity,
        string soilMoisture,
        string waterPh,
        string waterTurbidity
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor() {
        owner = msg.sender;
        
        // Initialize valid parameters and their units
        validParameters["CO2"] = "ppm";
        validParameters["PM2.5"] = "ugm3";
        validParameters["Temperature"] = "C";
        validParameters["Humidity"] = "pct";
        validParameters["SoilMoisture"] = "pct";
        validParameters["WaterPH"] = "pH";
        validParameters["WaterTurbidity"] = "NTU";
    }

    // Helper function to format number to 2 decimal places
    function formatDecimals(string memory _value) internal pure returns (string memory) {
        // Convert string to bytes for manipulation
        bytes memory value = bytes(_value);
        
        // Find decimal point position
        uint dotPos = 0;
        bool hasDot = false;
        
        for(uint i = 0; i < value.length; i++) {
            if(value[i] == '.') {
                dotPos = i;
                hasDot = true;
                break;
            }
        }
        
        // If no decimal point, add .00
        if(!hasDot) {
            return string(abi.encodePacked(_value, ".00"));
        }
        
        // Count digits after decimal
        uint decimals = value.length - dotPos - 1;
        
        if(decimals == 0) {
            // If ends with dot, add 00
            return string(abi.encodePacked(_value, "00"));
        } else if(decimals == 1) {
            // If one decimal, add 0
            return string(abi.encodePacked(_value, "0"));
        } else if(decimals == 2) {
            // If two decimals, return as is
            return _value;
        } else {
            // If more than two decimals, truncate to two
            bytes memory result = new bytes(dotPos + 3);
            for(uint i = 0; i < dotPos + 3; i++) {
                result[i] = value[i];
            }
            return string(result);
        }
    }

    function storeBatchedData(
        string memory _sensorId,
        string memory _co2,
        string memory _pm25,
        string memory _temperature,
        string memory _humidity,
        string memory _soilMoisture,
        string memory _waterPh,
        string memory _waterTurbidity
    ) public onlyOwner {
        require(batchedRecords.length < MAX_ENTRIES, "Storage limit reached");
        
        // Format all values to 2 decimal places
        string memory co2 = formatDecimals(_co2);
        string memory pm25 = formatDecimals(_pm25);
        string memory temperature = formatDecimals(_temperature);
        string memory humidity = formatDecimals(_humidity);
        string memory soilMoisture = formatDecimals(_soilMoisture);
        string memory waterPh = formatDecimals(_waterPh);
        string memory waterTurbidity = formatDecimals(_waterTurbidity);
        
        batchedRecords.push(
            BatchedSensorData(
                block.timestamp,
                _sensorId,
                co2,
                pm25,
                temperature,
                humidity,
                soilMoisture,
                waterPh,
                waterTurbidity
            )
        );
        
        emit BatchedDataStored(
            block.timestamp,
            _sensorId,
            co2,
            pm25,
            temperature,
            humidity,
            soilMoisture,
            waterPh,
            waterTurbidity
        );
    }

    function getTotalBatchedRecords() public view returns (uint256) {
        return batchedRecords.length;
    }

    function getBatchedRecord(uint256 index) public view returns (
        uint256 timestamp,
        string memory sensorId,
        string memory co2,
        string memory pm25,
        string memory temperature,
        string memory humidity,
        string memory soilMoisture,
        string memory waterPh,
        string memory waterTurbidity
    ) {
        require(index < batchedRecords.length, "Index out of bounds");
        BatchedSensorData memory record = batchedRecords[index];
        return (
            record.timestamp,
            record.sensorId,
            record.co2,
            record.pm25,
            record.temperature,
            record.humidity,
            record.soilMoisture,
            record.waterPh,
            record.waterTurbidity
        );
    }

    function getLatestBatchedRecord() public view returns (
        uint256 timestamp,
        string memory sensorId,
        string memory co2,
        string memory pm25,
        string memory temperature,
        string memory humidity,
        string memory soilMoisture,
        string memory waterPh,
        string memory waterTurbidity
    ) {
        require(batchedRecords.length > 0, "No records found");
        BatchedSensorData memory record = batchedRecords[batchedRecords.length - 1];
        return (
            record.timestamp,
            record.sensorId,
            record.co2,
            record.pm25,
            record.temperature,
            record.humidity,
            record.soilMoisture,
            record.waterPh,
            record.waterTurbidity
        );
    }
}
