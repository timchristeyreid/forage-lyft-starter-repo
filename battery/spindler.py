from utils import add_years_to_date
from battery.battery import Battery

class SpindlerBattery(Battery):
    def needs_service(self, current_date, last_service_date):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 3)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False