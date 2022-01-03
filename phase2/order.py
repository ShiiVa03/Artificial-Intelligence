from street import Street
from exceptions import *

class Order:
    def __init__(self, street_name: str, weight: int, volume:int, time: str):

        self.street = Street.get_street_by_name(street_name)
        self.weight = weight
        self.volume = volume

        hours, minutes = map(int, time.split(':'))
        if (hours < 0 or minutes < 0 or minutes > 60):
            raise TimeFormatError

        self.time = hours * 60 + minutes

    
    def get_weight(self) -> int:
        return self.weight
    
    def get_volume(self) -> int:
        return self.volume
    
    def get_street(self) -> Street:
        return self.street
    
    def get_time(self) -> int:
        return self.time






    