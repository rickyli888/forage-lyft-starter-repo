from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from car import Car


class CarFactory:
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage,
                        last_service_mileage) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage,
                        last_service_mileage) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage,
                         last_service_mileage) -> Car:
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage,
                      last_service_mileage) -> Car:
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
