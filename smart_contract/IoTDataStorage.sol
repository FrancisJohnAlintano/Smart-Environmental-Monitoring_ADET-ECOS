// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EnvironmentalMonitoring {
    struct BatchedSensorData {
        uint256 timestamp;
        string sensorId;
        string dataType;
        string value;
        string unit;
    }

    struct SensorDataInput {
        string sensorId;
        string dataType;
        string value;
        string unit;
    }

    uint256 public constant MAX_ENTRIES = 1000;
    BatchedSensorData[] public batchedRecords;
    address public owner;
    mapping(string => string) public validParameters;

    event BatchedDataStored(
        uint256 timestamp,
        string sensorId
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

    // Simple helper function
    function addDecimals(string calldata _value) internal pure returns (string memory) {
        return string(abi.encodePacked(_value, ".00"));
    }

    function storeBatchedData(SensorDataInput calldata _data) external onlyOwner {
        require(batchedRecords.length < MAX_ENTRIES, "Storage limit reached");
        
        // Create the record with simplified data structure
        batchedRecords.push(BatchedSensorData({
            timestamp: block.timestamp,
            sensorId: _data.sensorId,
            dataType: _data.dataType,
            value: _data.value,
            unit: _data.unit
        }));
        
        emit BatchedDataStored(block.timestamp, _data.sensorId);
    }

    function getTotalBatchedRecords() external view returns (uint256) {
        return batchedRecords.length;
    }

    function getBatchedRecord(uint256 index) external view returns (
        uint256,
        string memory,
        string memory,
        string memory,
        string memory
    ) {
        require(index < batchedRecords.length, "Index out of bounds");
        return (
            batchedRecords[index].timestamp,
            batchedRecords[index].sensorId,
            batchedRecords[index].dataType,
            batchedRecords[index].value,
            batchedRecords[index].unit
        );
    }

    function getLatestBatchedRecord() external view returns (
        uint256,
        string memory,
        string memory,
        string memory,
        string memory
    ) {
        require(batchedRecords.length > 0, "No records found");
        uint256 lastIndex = batchedRecords.length - 1;
        return (
            batchedRecords[lastIndex].timestamp,
            batchedRecords[lastIndex].sensorId,
            batchedRecords[lastIndex].dataType,
            batchedRecords[lastIndex].value,
            batchedRecords[lastIndex].unit
        );
    }
}
