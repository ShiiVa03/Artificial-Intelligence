from order import Order
from math import ceil
from typing import Set
from exceptions import *

class Transport:

    _all_transports = set() # type: Set[Transport]

    def __init__(self):

        if type(self) == Transport:
            raise Exception("Transport must be subclassed.")

        self.weight = 0
        self.travelled_distance = 0
        self.time = 0

        self.__class__._all_transports.add(self)

    
    @property
    def velocity(self):
        return self.MAX_VELOCITY - self.weight * self.RATIO_WEIGHT_VELOCITY # type: ignore
    
    def get_ecologic_level(self):
        return self.ECOLOGIC_LEVEL
    

    def travel(self, distance: int):
        self.time += ceil((60/1000) * (distance/self.velocity)) # In minutes
        self.travelled_distance += distance
    

    def get_time(self) -> int:
        return self.time
    
    def get_travelled_distance(self) -> int:
        return self.travelled_distance

    
    def add_order(self, order: Order) -> bool:
        weight = order.get_weight()

        MAX_WEIGHT = self.MAX_WEIGHT # type: ignore

        if (self.weight + weight > MAX_WEIGHT):
            return False

        self.weight += weight
        return True


    def drop_order(self, order: Order):
        weight = self.weight - order.get_weight()
        
        if (weight < 0):
            raise TransportWeightException

        self.weight = weight
    

    @classmethod
    def get_all_new_transports(cls):
        return [transport.clean_new() for transport in cls._all_transports]

    

    @classmethod
    def clean_new(cls):
        return cls()


    def __hash__(self):
        return id(self.__class__)

    def __eq__(self, other):
        return self.__class__ == other.__class__
    
    def __repr__(self):
        return self.__class__.__name__
        

class Bike(Transport):
    ECOLOGIC_LEVEL = 3
    MAX_WEIGHT = 5
    MAX_VELOCITY = 10
    RATIO_WEIGHT_VELOCITY = 0.7


class Motorcycle(Transport):
    ECOLOGIC_LEVEL = 2
    MAX_WEIGHT = 20
    MAX_VELOCITY = 35
    RATIO_WEIGHT_VELOCITY = 0.5

class Car(Transport):
    ECOLOGIC_LEVEL = 1
    MAX_WEIGHT = 100
    MAX_VELOCITY = 25
    RATIO_WEIGHT_VELOCITY = 0.1