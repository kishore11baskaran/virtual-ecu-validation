from ecu.ecu import VirtualECU
from simulation.vehicle import VehicleSimulation


def test_vehicle_data_reaches_ecu():
    vehicle = VehicleSimulation()
    ecu = VirtualECU()

    vehicle.start()
    vehicle.update(0.5)

    sensor_data = vehicle.get_sensor_data()

    ecu.start()
    ecu.update_sensor_data(sensor_data)

    status = ecu.get_status()

    assert status["rpm"] == sensor_data["rpm"]
    assert status["temperature"] == sensor_data["temperature"]
    assert status["battery_voltage"] == sensor_data["battery_voltage"]
    assert status["vehicle_speed"] == sensor_data["vehicle_speed"]
    assert status["throttle"] == sensor_data["throttle"]


def test_ecu_receives_throttle_data():
    vehicle = VehicleSimulation()
    ecu = VirtualECU()

    vehicle.start()
    vehicle.update(0.75)

    ecu.update_sensor_data(vehicle.get_sensor_data())

    assert ecu.throttle == 75.0