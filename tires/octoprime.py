from tires.tire import Tire


class Octoprime(Tire):
    def __init__(self, pressure: []):
        self.pressure = pressure

    def needs_service(self) -> bool:
        wear = sum(self.pressure)
        if wear >= 3:
            return True
        return False
