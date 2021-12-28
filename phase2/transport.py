from order import Order

class Transport:
    all_transports = []

    def __init__(self, weight: int=0, new_transport: bool=True):

        if (weight < 0 or weight > self.MAX_WEIGHT):
            raise TransportWeightException

        self.weight = weight

        if new_transport:
            self.__class__.all_transports.append(self)
    
    @property
    def velocity(self):
        return self.MAX_VELOCITY - self.weight * self.RATIO_WEIGHT_VELOCITY

    
    def add_order(self, order: Order):
        self.weight += order.get_weight()


    def drop_order(self, order: Order):
        weight = self.weight - order.get_weight()
        
        if (weight < 0):
            raise TransportWeightException

        self.weight = weight

    

    @classmethod
    def clone_class(cls):
        return(cls(new_transport=False))
        

class Bike(Transport):
    MAX_WEIGHT = 5
    MAX_VELOCITY = 10
    RATIO_WEIGHT_VELOCITY = 0.7


class Motorcycle(Transport):
    MAX_WEIGHT = 20
    MAX_VELOCITY = 35
    RATIO_WEIGHT_VELOCITY = 0.5

class Car(Transport):
    MAX_WEIGHT = 100
    MAX_VELOCITY = 25
    RATIO_WEIGHT_VELOCITY = 0.1