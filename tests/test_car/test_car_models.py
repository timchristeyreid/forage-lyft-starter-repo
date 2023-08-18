import unittest

from datetime import datetime
from battery.nubbin import NubbinBattery
from carfactory import CarFactory


class TestNeedsService(unittest.TestCase):

    def test_car(self):
        last_service_mileage = 0
        current_mileage = 30001
        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year-4)
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

if __name__ == '__main__':
    unittest.main()