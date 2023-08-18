import unittest

from tyre.carrigan_tyre import CarriganTyre

class TestCarriganTyres(unittest.TestCase):
    def test_tyres_need_service_true(self):
        tyre_wear_array = [0.1, 0.3, 0.2, 0.9]
        tyres = CarriganTyre(tyre_wear_array)
        self.assertTrue(tyres.needs_service())

    def test_tyres_need_service_false(self):
        tyre_wear_array = [0.1, 0.3, 0.2, 0.8]
        tyres = CarriganTyre(tyre_wear_array)
        self.assertFalse(tyres.needs_service())   