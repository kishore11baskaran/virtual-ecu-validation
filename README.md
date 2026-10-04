# Virtual ECU Validation

A Python-based virtual ECU validation project that simulates vehicle behavior, engine behavior, sensors, ECU data handling, and diagnostic fault detection.

## Project Overview

This project provides a simple virtual vehicle environment for validating ECU functionality without physical hardware.

The system includes:

- Virtual ECU
- Vehicle simulation
- Engine model
- Sensor models
- Diagnostic fault monitoring
- Integration between vehicle and ECU
- Automated tests using pytest

## Project Structure

```text
virtual-ecu-validation/
│
├── config/
│
├── ecu/
│   ├── ecu.py
│   └── diagnostics.py
│
├── simulation/
│   ├── engine.py
│   ├── sensors.py
│   └── vehicle.py
│
├── tests/
│   ├── test_diagnostics.py
│   ├── test_ecu.py
│   ├── test_engine.py
│   ├── test_integration.py
│   ├── test_sensors.py
│   └── test_vehicle.py
│
├── pytest.ini
├── requirements.txt
└── README.md
## Features

- Virtual ECU state management
- Vehicle simulation
- Engine behavior simulation

- Temperature, battery voltage, vehicle speed, and throttle sensors
- Diagnostic fault monitoring
- High engine temperature detection
- Low battery voltage detection
- Engine overspeed detection
- Invalid throttle detection
- ECU and vehicle integration
- Automated pytest test suite

## Testing

The project uses `pytest` for automated validation.

Run all tests:

```bash
pytest


Then add:

```markdown
## Test Coverage

The test suite validates:

- ECU initialization, start, and stop
- Engine behavior and throttle response
- Vehicle simulation
- Temperature, battery voltage, vehicle speed, and throttle sensors
- ECU and vehicle integration
- High engine temperature detection
- Low battery voltage detection
- Engine overspeed detection
- Invalid throttle detection
- Automated diagnostic fault monitoring

Current test status: **26 tests passed**

## Usage

The project simulates a vehicle, engine, sensors, and ECU working together.

Run the complete test suite:

```bash
pytest

The tests validate the simulated vehicle behavior, ECU data handling, sensor updates, and diagnostic fault detection.


## Project Status

The Virtual ECU Validation project is complete and all automated tests are passing.

**Test result: 26 passed**
```bash
git clone https://github.com/kishore11baskaran/virtual-ecu-validation.git
cd virtual-ecu-validation