from .battery import nubbin
from .engine import capulet_engine


class CarFactory(Engine, Battery):
    def create_calliope():
        pass

calliope = [nubbin(), capulet_engine()]

for component in calliope:
    component.needs_service()