from street import has_vertex

class Order:
    def __init__(self, street: str, weight: int, time: str):

        if not has_vertex(street):
            raise StreetDoesntExistException

        self.street = street
        self.weight = weight

        hours, minutes = map(int, time.split(':'))
        if (hours < 0 or minutes < 0 or minutes > 60):
            raise TimeFormatError

        self.time = hours * 60 + minutes

    
    def get_weight(self) -> int:
        return self.weight
    
    def get_street(self) -> str:
        return self.street
    
    def get_time(self) -> int:
        return self.time






    