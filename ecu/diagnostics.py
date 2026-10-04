class DiagnosticMonitor:
    TEMPERATURE_WARNING = 100.0
    BATTERY_LOW_WARNING = 11.5
    RPM_WARNING = 6000

    def check(self, sensor_data):
        faults = []

        temperature = sensor_data["temperature"]
        battery_voltage = sensor_data["battery_voltage"]
        rpm = sensor_data["rpm"]
        throttle = sensor_data["throttle"]

        if temperature > self.TEMPERATURE_WARNING:
            faults.append({
                "code": "HIGH_ENGINE_TEMPERATURE",
                "severity": "WARNING",
                "value": temperature,
            })

        if battery_voltage < self.BATTERY_LOW_WARNING:
            faults.append({
                "code": "LOW_BATTERY_VOLTAGE",
                "severity": "WARNING",
                "value": battery_voltage,
            })

        if rpm > self.RPM_WARNING:
            faults.append({
                "code": "ENGINE_OVERSPEED",
                "severity": "CRITICAL",
                "value": rpm,
            })

        if not 0.0 <= throttle <= 100.0:
            faults.append({
                "code": "INVALID_THROTTLE",
                "severity": "CRITICAL",
                "value": throttle,
            })

        return faults