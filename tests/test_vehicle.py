from simulation.vehicle import VehicleSimulation


def test_vehicle_initialization():
    vehicle = VehicleSimulation()

    data = vehicle.get_sensor_data()

    assert data["rpm"] == 0
    assert data["temperature"] == 25.0
    assert data["battery_voltage"] == 12.6
    assert data["vehicle_speed"] == 0.0
    assert data["throttle"] == 0.0


def test_vehicle_start():
    vehicle = VehicleSimulation()

    vehicle.start()

    data = vehicle.get_sensor_data()

    assert data["rpm"] == 800


def test_vehicle_responds_to_throttle():
    vehicle = VehicleSimulation()

    vehicle.start()

    vehicle.update(1.0)

    data = vehicle.get_sensor_data()

    assert data["rpm"] > 800
    assert data["throttle"] == 100.0
    assert data["vehicle_speed"] > 0


def test_vehicle_stop():
    vehicle = VehicleSimulation()

    vehicle.start()
    vehicle.update(0.5)
    vehicle.stop()

    data = vehicle.get_sensor_data()

    assert data["rpm"] == 0

    