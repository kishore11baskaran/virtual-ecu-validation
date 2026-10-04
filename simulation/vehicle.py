from simulation.engine import EngineModel
from simulation.sensors import (
    TemperatureSensor,
    BatteryVoltageSensor,
    VehicleSpeedSensor,
    ThrottleSensor,
)


class VehicleSimulation:
    def __init__(self):
        self.engine = EngineModel()

        self.temperature_sensor = TemperatureSensor()
        self.battery_sensor = BatteryVoltageSensor()
        self.speed_sensor = VehicleSpeedSensor()
        self.throttle_sensor = ThrottleSensor()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def update(self, throttle):
        # Update throttle sensor
        self.throttle_sensor.update(throttle * 100)

        # Update engine using normalized throttle
        self.engine.update(throttle)

        # Update temperature sensor
        self.temperature_sensor.update(
            self.engine.temperature
        )

        # Calculate simplified vehicle speed
        speed = self.engine.rpm * 0.02

        # Update speed sensor
        self.speed_sensor.update(speed)

    def get_sensor_data(self):
        return {
            "rpm": self.engine.rpm,
            "temperature": self.temperature_sensor.read(),
            "battery_voltage": self.battery_sensor.read(),
            "vehicle_speed": self.speed_sensor.read(),
            "throttle": self.throttle_sensor.read(),
        }