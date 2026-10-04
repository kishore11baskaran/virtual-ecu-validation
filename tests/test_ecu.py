from ecu.ecu import VirtualECU


def test_ecu_initial_state():
    ecu = VirtualECU()

    assert ecu.state == "OFF"
    assert ecu.rpm == 0
    assert ecu.temperature == 25.0


def test_ecu_start():
    ecu = VirtualECU()

    ecu.start()

    assert ecu.state == "RUNNING"
    assert ecu.rpm == 800


def test_ecu_stop():
    ecu = VirtualECU()

    ecu.start()
    ecu.stop()

    assert ecu.state == "OFF"
    assert ecu.rpm == 0

def test_ecu_reports_high_temperature_fault():
    ecu = VirtualECU()

    sensor_data = {
        "temperature": 110.0,
        "battery_voltage": 12.6,
        "rpm": 2000,
        "vehicle_speed": 50.0,
        "throttle": 50.0,
    }

    ecu.update_sensor_data(sensor_data)

    status = ecu.get_status()

    assert len(status["faults"]) == 1
    assert status["faults"][0]["code"] == "HIGH_ENGINE_TEMPERATURE"


def test_ecu_reports_low_battery_fault():
    ecu = VirtualECU()

    sensor_data = {
        "temperature": 25.0,
        "battery_voltage": 10.5,
        "rpm": 2000,
        "vehicle_speed": 50.0,
        "throttle": 50.0,
    }

    ecu.update_sensor_data(sensor_data)

    status = ecu.get_status()

    assert len(status["faults"]) == 1
    assert status["faults"][0]["code"] == "LOW_BATTERY_VOLTAGE"