from __future__ import annotations
from order import Order
from transport import *
from courier import *
from uninformed_search_algorithms import *
from informed_search_algorithms import *
from typing import List, Tuple, Set, Callable, Optional
from collections import defaultdict

class OrdersCircuit:

    _all_circuits = [] # type: List[OrdersCircuit]

    def __init__(self, name: str, initial: Street, orders: List[Order]):

        self.path_transports_per_algorithm = {
            'dfs': (None, None),
            'bfs': (None, None),
            'iter_dfs': (None, None),
            'greedy': (None, None),
            'a_star': (None, None)
        }

        self.name = name
        self.initial = initial
        self.orders = orders
        self.orders_streets = defaultdict(list)
        self.courier = None

        for order in orders:
            self.orders_streets[order.get_street()].append(order)
        
        self.generate_circuit()

        self.__class__._all_circuits.append(self)
        
    
    def get_number_of_orders(self) -> int:
        return len(self.orders)

    def get_total_volume(self) -> int:
        return sum(order.get_volume() for order in self.orders)
    
    def get_total_weight(self) -> int:
        return sum(order.get_weight() for order in self.orders)

    def _generate_circuit_algorithm(self, algorithm: Callable[[Street, Set[Street], Street], Optional[List[Tuple[Street, int]]]]) -> Optional[List[Tuple[Street, int]]]:

        streets = set(self.orders_streets.keys())

        return algorithm(self.initial, streets, self.initial)

    def generate_circuit_dfs(self) -> Optional[List[Tuple[Street, int]]]:
        return self._generate_circuit_algorithm(dfs)
    
    def generate_circuit_bfs(self) -> Optional[List[Tuple[Street, int]]]:
        return self._generate_circuit_algorithm(bfs)
    
    def generate_circuit_iter_dfs(self) -> Optional[List[Tuple[Street, int]]]:
        return self._generate_circuit_algorithm(iter_dfs)
    
    def generate_circuit_greedy(self) -> Optional[List[Tuple[Street, int]]]:
        return self._generate_circuit_algorithm(greedy)
    
    def generate_circuit_a_star(self) -> Optional[List[Tuple[Street, int]]]:
        return self._generate_circuit_algorithm(a_star)


    
    def possible_transports(self, path: Optional[List[Tuple[Street, int]]]) -> List[Transport]:
        if (path is None):
            raise NoPathForCircuitTransport
        
        transports = Transport.get_all_new_transports()

        if not transports:
            return []

        orders = self.orders_streets.copy() # Caution: Shallow Clone
        time = 0


        for street_orders in orders.values():
            for order in street_orders:
                transports[:] = [transport for transport in transports if transport.add_order(order)]

        for (street, dist) in path:

            for transport in transports:
                transport.travel(dist)

            try:
                street_orders = orders.pop(street)
            except KeyError:
                pass
            else:
                for order in street_orders:
                    order_time_limit = order.get_time()

                    transports[:] = [transport for transport in transports if order_time_limit >= transport.get_time()]

                    if not transports:
                        return []

                    for transport in transports:
                        transport.drop_order(order)           

        return transports
    

    def generate_circuit(self):
        one_possible_circuit = False

        for algorithm in self.path_transports_per_algorithm.keys():
            path = getattr(self, 'generate_circuit_' + algorithm)()

            if (path is None):
                self.path_transports_per_algorithm[algorithm] = (None, None)
            else:
                transports = self.possible_transports(path)

                if transports:
                    one_possible_circuit = True

                self.path_transports_per_algorithm[algorithm] = (path, transports)
            
        if not one_possible_circuit:
            raise NoPossibleCircuit


    def run_fastest(self) -> Optional[Tuple[List[Tuple[Street, int]], Transport, Courier]]:
        if self.courier is not None:
            raise CircuitAlreadyInProgress
        
        best_path_transport = None
                    
        for (path, transports) in self.path_transports_per_algorithm.values():
            if path and transports:

                for transport in transports:
                    if best_path_transport is None:
                        best_path_transport = (path, transport)
                    else:
                        best_transport = best_path_transport[1]
                        best_transport_time = best_transport.get_time()
                        transport_time= transport.get_time()

                        if transport_time < best_transport_time or \
                        (transport_time == best_transport_time and transport.get_travelled_distance() < best_transport.get_travelled_distance()):
                            best_path_transport = (path, transport)
        
        if best_path_transport is None:
            return None
        
        self.courier = courier = Courier.book_courier()
        
        (path,transport) = best_path_transport
        return (next(zip(*path)), transport, courier)


    
    def run_ecologic(self) -> Optional[Tuple[List[Tuple[Street, int]], Transport, Courier]]:
        if self.courier is not None:
            raise CircuitAlreadyInProgress
        
        best_path_transport = None
                    
        for (path, transports) in self.path_transports_per_algorithm.values():
            if path and transports:

                for transport in transports:
                    if best_path_transport is None:
                        best_path_transport = (path, transport)
                    else:
                        best_transport = best_path_transport[1]
                        best_transport_eco_lvl = best_transport.get_ecologic_level()
                        transport_eco_lvl = transport.get_ecologic_level()

                        if transport_eco_lvl > best_transport_eco_lvl or \
                        (transport_eco_lvl == best_transport_eco_lvl and transport.get_time() < best_transport.get_time()):
                            best_path_transport = (path, transport)

        if best_path_transport is None:
            return None
        
        self.courier = courier = Courier.book_courier()
        
        (path,transport) = best_path_transport
        return (next(zip(*path)), transport, courier)


    def finish(self, on_time: bool=True):
        if self.courier is None:
            raise CircuitIsNotInProgress

        if on_time:
            self.courier.add_penalty()

        self.courier.finish()
        self.courier = None
    

    @classmethod
    def _circuits_with_most_orders(cls) -> List[OrdersCircuit]:
        best_circuits = [] # type: List[OrdersCircuit]
        number_of_orders = 0
    
        for circuit in cls._all_circuits:

            if not best_circuits:
                number_of_orders = circuit.get_number_of_orders()
                best_circuits.append(circuit)
                
            else:
                circuit_total_orders = circuit.get_number_of_orders()

                if circuit_total_orders == number_of_orders:
                    best_circuits.append(circuit)

                elif circuit_total_orders > number_of_orders:
                    number_of_orders = circuit_total_orders
                    best_circuits = [circuit]
        
        return best_circuits

    @classmethod
    def circuits_with_most_orders_per_volume(cls):   
        return sorted(cls._circuits_with_most_orders(), reverse=True, key=lambda x:x.get_total_volume())


    
    @classmethod
    def circuits_with_most_orders_per_weight(cls):
        return sorted(cls._circuits_with_most_orders(), reverse=True, key=lambda x:x.get_total_weight())


    
    
    
    def get_info(self) -> str:
        result = [f"\n\n\n\n<-- {self.name} -->\n"]

        for (algorithm, path_transports) in self.path_transports_per_algorithm.items():
            result.append("\nAlgorithm: " + algorithm.capitalize())
            result.append("\nPath: ")

            (path, transports) = path_transports

            if path is None:
                result.append("Not found\n\n")
            else:        
                result.append(str(next(zip(*path))))

                if not transports:
                    result.append(f"\nDistance: {sum(x[1] for x in path)} m")
                    result.append("\nTransports: Not found or time exceeds fastest possible transport\n\n")
                else:
                    result.append(f"\nDistance: {transports[0].get_travelled_distance()} m") # No need to calculate distance
                    result.append("\nTransports:\n")
                    for transport in transports:
                        result.append(f"\t-{transport}\t{{Time: {transport.get_time()} min}}\n")
                    result.append("\n")

        return "".join(result)
    

    def __repr__(self) -> str:
        return f"{{\nName: {self.name}\nStation: {self.initial}\nOrders: {self.orders}\n}}"
