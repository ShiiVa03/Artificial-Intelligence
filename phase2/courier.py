import random

from typing import Dict
from exceptions import *

class Courier:

    _available_couriers = {} # type: Dict[str, Courier]
    _busy_couriers = {} # type: Dict[str, Courier]

    def __init__(self, name: str):
        if (self.__class__.exists(name)):
            raise CourierAlreadyExistsException
        
        self.name = name
        self.penalties = 0

        self.__class__._available_couriers[name] = self
    
    def get_name(self) -> str:
        return self.name
    

    @classmethod
    def exists(cls, name : str):
        return name in cls._available_couriers or name in cls._busy_couriers
    
    
    @classmethod
    def book_courier(cls):
        if not cls._available_couriers:
            raise NoAvailableCouriers

        couriers = list(cls._available_couriers.values())

        def probability(courier: Courier) -> float:
            try:
                return 1/courier.penalties
            except ZeroDivisionError:
                return 1

        courier = random.choices(couriers, weights=map(probability, couriers))[0]

        courier_name = courier.get_name()

        cls._available_couriers.pop(courier_name)
        cls._busy_couriers[courier_name] = courier

        return courier
    

    def finish(self):
        courier_name = self.name

        if courier_name not in self.__class__._busy_couriers:
            raise CourierNotBusy

        self.__class__._busy_couriers.pop(courier_name)
        self.__class__._available_couriers[courier_name] = self

    def add_penalty(self):
        self.penalties += 1
    
    def __repr__(self) -> str:
        return self.name