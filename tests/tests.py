import unittest

from datetime import datetime
from engine.capulet_engine import CapuletEngine
from battery.nubbin import NubbinBattery
from carfactory import CarFactory


class TestNeedsService(unittest.TestCase):

    def test_engine(self):
        last_service_mileage = 0
        current_mileage = 30001
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())


    def test_battery(self):
        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year-4)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())


    def test_car(self):
        last_service_mileage = 0
        current_mileage = 30001
        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year-4)
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

if __name__ == '__main__':
    unittest.main()