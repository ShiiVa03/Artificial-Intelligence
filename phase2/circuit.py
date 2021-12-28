from order import Order
from transport import *
from courier import *
from algorithms import *
from typing import List, Tuple, Set, Callable
from queue import Queue
from collections import defaultdict

class OrdersCircuit:
    def __init__(self, initial, orders: List[Order]):
        self.initial = initial
        self.orders = defaultdict(list)
        self.path = None

        for order in orders:
            self.orders[order.get_street()].append(order)

    def generate_circuit(self, algorithm: Callable[[str, Set[str], str], List[Tuple[str, int]]]) -> List[Tuple[str, int]]:
        courier_name = Courier.book_courier()
        print(courier_name)

        streets_names = set(self.orders.keys())

        self.path = algorithm(self.initial, streets_names, self.initial)

        return self.path

    def generate_circuit_dfs(self) -> List[Tuple[str, int]]:
        return self.generate_circuit(dfs)
    
    def generate_circuit_bfs(self) -> List[Tuple[str, int]]:
        return self.generate_circuit(bfs)
    
    def generate_circuit_iter_dfs(self) -> List[Tuple[str, int]]:
        return self.generate_circuit(iter_dfs)

    
    def can_transport(self, transport: Transport) -> bool:
        if (self.path is None):
            return False
        
        transport = transport.clone_class()
        orders = self.orders.copy() # Caution: Shallow Clone
        time = 0


        for street_orders in orders.values():
            for order in street_orders:
                transport.add_order(order)

        for (street, dist) in self.path:

            time += (6/100) * (dist/transport.velocity) # In minutes

            try:
                street_orders = orders.pop(street)
            except KeyError:
                pass
            else:
                for order in street_orders:
                    if order.get_time() < time:
                        return False
                    
                    transport.drop_order(order)

        return True

        

