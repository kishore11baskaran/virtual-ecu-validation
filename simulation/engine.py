class EngineModel:
    def __init__(self):
        self.rpm = 0
        self.temperature = 25.0
        self.load = 0.0

    def start(self):
        self.rpm = 800
        self.load = 10.0

    def stop(self):
        self.rpm = 0
        self.load = 0.0

    def update(self, throttle):
        """
        Update engine behavior based on throttle input.

        throttle: value from 0.0 to 1.0
        """

        if not 0.0 <= throttle <= 1.0:
          raise ValueError("Throttle must be between 0.0 and 1.0")
        
        if self.rpm == 0:
            return

        # Calculate target RPM
        target_rpm = 800 + (throttle * 5200)

        # Move RPM gradually toward target
        self.rpm += (target_rpm - self.rpm) * 0.2

        # Calculate engine load
        self.load = throttle * 100

        # Temperature increases with load
        self.temperature += self.load * 0.01

    def get_state(self):
        return {
            "rpm": round(self.rpm, 1),
            "temperature": round(self.temperature, 2),
            "load": round(self.load, 1),
        }