// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Smart contract for storing IoT sensor data
contract IoTDataStorage {
    // Scaling factors for decimal values
    uint256 public constant SCALE_FACTOR = 1e6; // 6 decimal places

    // Helper functions for scaling
    function scaleValue(uint256 value) internal pure returns (uint256) {
        return value * SCALE_FACTOR;
    }

    function unscaleValue(uint256 value) internal pure returns (uint256) {
        return value / SCALE_FACTOR;
    }

    // Structure to store environmental sensor data
    struct SensorData {
        uint256 timestamp;
        uint256 co2_ppm;
        uint256 pm25_ugm3;
        uint256 temperature_c;
        uint256 humidity_pct;
        uint256 soil_moisture_pct;
        uint256 water_ph;
        uint256 water_turbidity_ntu;
    }

    // Constants and state variables
    uint256 public constant MAX_ENTRIES = 1000;
    SensorData[] public dataRecords;
    address public owner;

    // Event for data storage
    event DataStored(
        uint256 timestamp,
        uint256 co2_ppm,
        uint256 pm25_ugm3,
        uint256 temperature_c,
        uint256 humidity_pct,
        uint256 soil_moisture_pct,
        uint256 water_ph,
        uint256 water_turbidity_ntu
    );

    // Modifier for owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set owner
    constructor() {
        owner = msg.sender;
    }

    // Function to store environmental sensor data
    function storeData(
        uint256 _co2_ppm,
        uint256 _pm25_ugm3,
        uint256 _temperature_c,
        uint256 _humidity_pct,
        uint256 _soil_moisture_pct,
        uint256 _water_ph,
        uint256 _water_turbidity_ntu
    ) public onlyOwner {
        require(dataRecords.length < MAX_ENTRIES, "Storage limit reached");
        
        // Scale and validate percentage values
        uint256 scaledHumidity = scaleValue(_humidity_pct);
        uint256 scaledMoisture = scaleValue(_soil_moisture_pct);
        require(scaledHumidity <= scaleValue(100), "Humidity cannot exceed 100%");
        require(scaledMoisture <= scaleValue(100), "Soil moisture cannot exceed 100%");
        
        uint256 timestamp = block.timestamp;
        
        // Scale all decimal values before storing
        dataRecords.push(SensorData(
            timestamp,
            scaleValue(_co2_ppm),
            scaleValue(_pm25_ugm3),
            scaleValue(_temperature_c),
            scaledHumidity,
            scaledMoisture,
            scaleValue(_water_ph),
            scaleValue(_water_turbidity_ntu)
        ));
        
        emit DataStored(
            timestamp,
            _co2_ppm,
            _pm25_ugm3,
            _temperature_c,
            _humidity_pct,
            _soil_moisture_pct,
            _water_ph,
            _water_turbidity_ntu
        );
    }

    // Function to get total number of records
    function getTotalRecords() public view returns (uint256) {
        return dataRecords.length;
    }

    // Function to get a specific record
    function getRecord(uint256 index) public view returns (
        uint256,
        uint256,
        uint256,
        uint256,
        uint256,
        uint256,
        uint256,
        uint256
    ) {
        require(index < dataRecords.length, "Index out of bounds");
        SensorData memory record = dataRecords[index];
        return (
            record.timestamp,
            unscaleValue(record.co2_ppm),
            unscaleValue(record.pm25_ugm3),
            unscaleValue(record.temperature_c),
            unscaleValue(record.humidity_pct),
            unscaleValue(record.soil_moisture_pct),
            unscaleValue(record.water_ph),
            unscaleValue(record.water_turbidity_ntu)
        );
    }
}
