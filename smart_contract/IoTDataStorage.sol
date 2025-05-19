// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EnvironmentalMonitoring {
    struct SensorData {
        uint256 timestamp;
        string sensorId;
        string parameterType;  // e.g., "CO2", "PM2.5", "Temperature"
        string value;         // Store as string to handle different units
        string unit;          // e.g., "ppm", "µg/m³", "°C"
    }

    uint256 public constant MAX_ENTRIES = 1000; // Increased to handle more data points
    SensorData[] public dataRecords;
    address public owner;

    // Valid parameter types and their units
    mapping(string => string) public validParameters;

    event DataStored(
        uint256 timestamp,
        string sensorId,
        string parameterType,
        string value,
        string unit
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

    function storeData(
        string memory _sensorId,
        string memory _parameterType,
        string memory _value
    ) public onlyOwner {
        require(dataRecords.length < MAX_ENTRIES, "Storage limit reached");
        require(bytes(validParameters[_parameterType]).length > 0, "Invalid parameter type");

        string memory unit = validParameters[_parameterType];
        dataRecords.push(SensorData(block.timestamp, _sensorId, _parameterType, _value, unit));
        
        emit DataStored(block.timestamp, _sensorId, _parameterType, _value, unit);
    }

    function getTotalRecords() public view returns (uint256) {
        return dataRecords.length;
    }

    function getRecord(uint256 index) public view returns (
        uint256 timestamp,
        string memory sensorId,
        string memory parameterType,
        string memory value,
        string memory unit
    ) {
        require(index < dataRecords.length, "Index out of bounds");
        SensorData memory record = dataRecords[index];
        return (
            record.timestamp,
            record.sensorId,
            record.parameterType,
            record.value,
            record.unit
        );
    }

    function getLatestRecord(string memory _parameterType) public view returns (
        uint256 timestamp,
        string memory sensorId,
        string memory value,
        string memory unit
    ) {
        require(bytes(validParameters[_parameterType]).length > 0, "Invalid parameter type");
        
        for (uint256 i = dataRecords.length; i > 0; i--) {
            SensorData memory record = dataRecords[i-1];
            if (keccak256(bytes(record.parameterType)) == keccak256(bytes(_parameterType))) {
                return (
                    record.timestamp,
                    record.sensorId,
                    record.value,
                    record.unit
                );
            }
        }
        revert("No records found for this parameter type");
    }
}
