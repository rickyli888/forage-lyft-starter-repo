from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from car import Car

from datetime import datetime


class CarFactory:
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int) -> Car:
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int) -> Car:
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
