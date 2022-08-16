import unittest
from datetime import datetime
from CarFactory import CarFactory


class TestcfCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime(2020, 1, 1)
        last_service_date = datetime(2019, 1, 1)
        current_mileage = 0
        last_service_mileage = 0
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
