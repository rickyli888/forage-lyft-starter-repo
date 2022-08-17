import unittest
from datetime import datetime

from CarFactory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tires = [0, 0, 0, 0]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(car.needs_service())

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.1, 0.8, 0.9, 0.2]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())


class TestGlissade(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tires = [0, 0, 0, 1]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tires = [0, 0, 0, 0]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tires)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.1, 0.1, 0.1, 0.1]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(car.needs_service())

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tires = [1, 1, 0.1, 1]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.9, 0.9, 0.9, 0.9]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()
