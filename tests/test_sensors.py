from simulation.sensors import (
    TemperatureSensor,
    BatteryVoltageSensor,
    VehicleSpeedSensor,
    ThrottleSensor,
)


def test_temperature_sensor_initial_value():
    sensor = TemperatureSensor()

    assert sensor.read() == 25.0


def test_temperature_sensor_updates():
    sensor = TemperatureSensor()

    sensor.update(75.5)

    assert sensor.read() == 75.5


def test_battery_voltage_sensor():
    sensor = BatteryVoltageSensor()

    assert sensor.read() == 12.6

    sensor.update(13.8)

    assert sensor.read() == 13.8


def test_vehicle_speed_sensor():
    sensor = VehicleSpeedSensor()
    assert sensor.read() == 0.0

    sensor.update(60.5)

    assert sensor.read() == 60.5


def test_throttle_sensor():
    sensor = ThrottleSensor()

    assert sensor.read() == 0.0

    sensor.update(75.0)

    assert sensor.read() == 75.0


def test_throttle_sensor_rejects_invalid_value():
    sensor = ThrottleSensor()

    try:
        sensor.update(120.0)
        assert False
    except ValueError:
        assert True