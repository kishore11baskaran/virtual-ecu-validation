from ecu.diagnostics import DiagnosticMonitor


def test_no_faults_for_normal_data():
    monitor = DiagnosticMonitor()

    sensor_data = {
        "temperature": 75.0,
        "battery_voltage": 13.8,
        "rpm": 2500,
        "throttle": 50.0,
    }

    faults = monitor.check(sensor_data)

    assert faults == []


def test_high_temperature_fault():
    monitor = DiagnosticMonitor()

    sensor_data = {
        "temperature": 105.0,
        "battery_voltage": 13.8,
        "rpm": 2500,
        "throttle": 50.0,
    }

    faults = monitor.check(sensor_data)

    assert len(faults) == 1
    assert faults[0]["code"] == "HIGH_ENGINE_TEMPERATURE"
    assert faults[0]["severity"] == "WARNING"


def test_low_battery_fault():
    monitor = DiagnosticMonitor()

    sensor_data = {
        "temperature": 75.0,
        "battery_voltage": 10.8,
        "rpm": 2500,
        "throttle": 50.0,
    }

    faults = monitor.check(sensor_data)

    assert len(faults) == 1
    assert faults[0]["code"] == "LOW_BATTERY_VOLTAGE"


def test_engine_overspeed_fault():
    monitor = DiagnosticMonitor()

    sensor_data = {
        "temperature": 75.0,
        "battery_voltage": 13.8,
        "rpm": 6500,
        "throttle": 80.0,
    }

    faults = monitor.check(sensor_data)

    assert len(faults) == 1
    assert faults[0]["code"] == "ENGINE_OVERSPEED"
    assert faults[0]["severity"] == "CRITICAL"


def test_multiple_faults():
    monitor = DiagnosticMonitor()

    sensor_data = {
        "temperature": 110.0,
        "battery_voltage": 10.5,
        "rpm": 7000,
        "throttle": 50.0,
    }

    faults = monitor.check(sensor_data)

    assert len(faults) == 3

    def test_high_rpm_fault():
     
     monitor = DiagnosticMonitor()

    sensor_data = {
        "temperature": 25.0,
        "battery_voltage": 12.6,
        "rpm": 7000,
        "throttle": 50.0,
    }

    faults = monitor.check(sensor_data)

    assert len(faults) == 1
    assert faults[0]["code"] == "ENGINE_OVERSPEED"
    assert faults[0]["severity"] == "CRITICAL"