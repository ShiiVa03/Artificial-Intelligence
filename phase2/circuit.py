from order import Order
from transport import *
from courier import *
from uninformed_search_algorithms import *
from informed_search_algorithms import *
from typing import List, Tuple, Set, Callable
from queue import Queue
from collections import defaultdict

class OrdersCircuit:
    def __init__(self, initial: Street, orders: List[Order]):
        self.initial = initial
        self.orders = defaultdict(list)
        self.path = None

        for order in orders:
            self.orders[order.get_street()].append(order)

    def generate_circuit(self, algorithm: Callable[[Street, Set[Street], Street], List[Tuple[Street, int]]]) -> List[Tuple[Street, int]]:
        courier_name = Courier.book_courier()
        print(courier_name)

        streets_names = set(self.orders.keys())

        self.path = algorithm(self.initial, streets_names, self.initial)

        return self.path

    def generate_circuit_dfs(self) -> List[Tuple[Street, int]]:
        return self.generate_circuit(dfs)
    
    def generate_circuit_bfs(self) -> List[Tuple[Street, int]]:
        return self.generate_circuit(bfs)
    
    def generate_circuit_iter_dfs(self) -> List[Tuple[Street, int]]:
        return self.generate_circuit(iter_dfs)
    
    def generate_circuit_greedy(self) -> List[Tuple[Street, int]]:
        return self.generate_circuit(greedy)
    
    def generate_circuit_a_star(self) -> List[Tuple[Street, int]]:
        return self.generate_circuit(a_star)

    
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

        

