from battery.battery import Battery
from engine.engine import Engine
from serviceable import Serviceable


class Car(Serviceable, Engine, Battery):
    def __init__(self, engine: Engine, battery: Battery):
        super().__init__()
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
