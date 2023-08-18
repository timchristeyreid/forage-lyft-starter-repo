from car import Car
from engine import Engine
from battery import Battery

class Serviceable(Car):
    def needs_service(engine:Engine, battery:Battery):
        pass
    