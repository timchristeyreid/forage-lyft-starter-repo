import unittest
from datetime import datetime

from battery.nubbin import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(today.year - 5)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(today.year - 3)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())