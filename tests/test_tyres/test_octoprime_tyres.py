import unittest

from tyre.octoprime_tyre import OctoprimeTyre

class TestOctoprimeTyre(unittest.TestCase):
    def test_tyres_need_service_true(self):
        tyre_wear_array = [0.8, 0.7, 0.9, 0.9]
        tyres = OctoprimeTyre(tyre_wear_array)
        self.assertTrue(tyres.needs_service())

    def test_tyres_need_service_false(self):
        tyre_wear_array = [0.8, 0.7, 0.9, 0.4]
        tyres = OctoprimeTyre(tyre_wear_array)
        self.assertFalse(tyres.needs_service())