import random

class Courier:

    available_couriers = {}
    busy_couriers = {}

    def __init__(self, name: str):
        if (self.__class__.exists(name)):
            raise CourierAlreadyExistsException
        
        self.name = name
        self.penalties = 0

        self.__class__.available_couriers[name] = self
    
    def get_name(self) -> str:
        return self.name
    

    @classmethod
    def exists(cls, name : str):
        return name in cls.available_couriers or name in cls.busy_couriers
    
    
    @classmethod
    def book_courier(cls):
        if not cls.available_couriers:
            return None

        couriers = list(cls.available_couriers.values())

        def probability(courier: Courier) -> float:
            try:
                return 1/courier.penalties
            except ZeroDivisionError:
                return 1

        courier = random.choices(couriers, weights=map(probability, couriers))[0]

        courier_name = courier.get_name()

        cls.available_couriers.pop(courier_name)
        cls.busy_couriers[courier_name] = courier

        return courier_name