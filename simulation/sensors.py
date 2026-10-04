class TemperatureSensor:
    def __init__(self, initial_temperature=25.0):
        self.temperature = initial_temperature

    def update(self, engine_temperature):
        self.temperature = engine_temperature

    def read(self):
        return round(self.temperature, 2)


class BatteryVoltageSensor:
    def __init__(self, initial_voltage=12.6):
        self.voltage = initial_voltage

    def update(self, voltage):
        self.voltage = voltage

    def read(self):
        return round(self.voltage, 2)


class VehicleSpeedSensor:
    def __init__(self, initial_speed=0.0):
        self.speed = initial_speed

    def update(self, speed):
        self.speed = speed

    def read(self):
        return round(self.speed, 2)


class ThrottleSensor:
    def __init__(self, initial_position=0.0):
        self.position = initial_position

    def update(self, position):
        if not 0.0 <= position <= 100.0:
            raise ValueError("Throttle position must be between 0 and 100")

        self.position = position

    def read(self):
        return round(self.position, 2)