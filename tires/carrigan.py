from tires.tire import Tire


class Carrigan(Tire):
    def __init__(self, pressure: []):
        self.pressure = pressure

    def needs_service(self) -> bool:
        for x in self.pressure:
            if x >= 0.9:
                return True
        return False
