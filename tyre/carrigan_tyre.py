from tyre.tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, tyre_wear_array):
        self.tyre_wear_array = tyre_wear_array
    
    def needs_service(self):
        for number in self.tyre_wear_array:
            if number >= 0.9:
                return True
        else:
            return False
