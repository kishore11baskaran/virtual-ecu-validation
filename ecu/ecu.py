from ecu.diagnostics import DiagnosticMonitor

class VirtualECU:
    def __init__(self):
        self.state = "OFF"

        self.rpm = 0
        self.temperature = 25.0
        self.battery_voltage = 12.6
        self.vehicle_speed = 0.0
        self.throttle = 0.0

        self.diagnostic_monitor = DiagnosticMonitor()
        self.faults = []

    def start(self):
        self.state = "RUNNING"
        self.rpm = 800

    def stop(self):
        self.state = "OFF"
        self.rpm = 0

    def update_sensor_data(self, sensor_data):
        """
        Receive sensor data from the vehicle simulation.
        """

        self.rpm = sensor_data["rpm"]
        self.temperature = sensor_data["temperature"]
        self.battery_voltage = sensor_data["battery_voltage"]
        self.vehicle_speed = sensor_data["vehicle_speed"]
        self.throttle = sensor_data["throttle"]

        self.faults = self.diagnostic_monitor.check(sensor_data)

    def get_status(self):
        return {
            "state": self.state,
            "rpm": self.rpm,
            "temperature": self.temperature,
            "battery_voltage": self.battery_voltage,
            "vehicle_speed": self.vehicle_speed,
            "throttle": self.throttle,
            "faults": self.faults
        }