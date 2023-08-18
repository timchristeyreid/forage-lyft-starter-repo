from tyre.tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, tyre_wear_array):
        self.tyre_wear_array = tyre_wear_array
    
    def needs_service(self):
        if sum(self.tyre_wear_array) >= 3:
                return True
        else:
            return False