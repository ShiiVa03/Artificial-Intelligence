from sys import version_info


if (version_info.major < 3 or (version_info.major == 3 and version_info.minor < 10)):
    raise Exception("This script requires Python 3.10+") # bisect.insort_right requires 3.10+



from itertools import permutations
from exceptions import *
from circuit import *
from courier import *
from order import *
from street import *
from transport import *
from typing import Tuple, List

import random













        










        


Courier("João")
Courier("Manuel")
Courier("Carlos")

green_station = Street("Rua dos Pergaminhos", Point(0,0))
Street("Rua dos Amendoins", Point(2500, 0))
Street("Rua das Cores", Point(0,10))

Street.connection("Rua dos Pergaminhos", "Rua dos Amendoins", both_ways=True)
Street.connection("Rua dos Amendoins", "Rua das Cores", both_ways=True)
Street.connection("Rua das Cores", "Rua dos Pergaminhos")

Bike()
Bike()
Bike()
Motorcycle()
Motorcycle()
Car()
Car()

        
print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)



c1 = OrdersCircuit(green_station,
[
    Order("Rua dos Pergaminhos", 20, "00:20"),
    Order("Rua das Cores", 20, "00:30")
])

c2 = OrdersCircuit(green_station,
[
    Order("Rua dos Amendoins", 0, "00:05")
])

print("C1 DFS - ", c1.generate_circuit_dfs(), "Transport:", c1.can_transport(Car()))
print("C1 BFS - ", c1.generate_circuit_bfs(), "Transport:", c1.can_transport(Car()))
print("C1 Iter-DFS - ", c1.generate_circuit_iter_dfs(), "Transport:", c1.can_transport(Car()))
print("C1 Greedy - ", c1.generate_circuit_greedy(), "Transport:", c1.can_transport(Car()))
print("C1 A* - ", c1.generate_circuit_a_star(), "Transport:", c1.can_transport(Car()))

print("C2 DFS - ", c2.generate_circuit_dfs(), "Transport:", c2.can_transport(Car()))
print("C2 BFS - ", c2.generate_circuit_bfs(), "Transport:", c2.can_transport(Car()))
print("C2 Iter-DFS - ", c2.generate_circuit_iter_dfs(), "Transport:", c2.can_transport(Car()))
print("C2 Greedy - ", c2.generate_circuit_greedy(), "Transport:", c2.can_transport(Car()))
print("C2 A* - ", c2.generate_circuit_a_star(), "Transport:", c2.can_transport(Car()))

'''
def dfs(orders: list[Order]):
    for (idx in range(len(orders))):
        orders_copy = orders.copy()
        order = orders_copy.pop(idx)

        dfs(orders_copy)
'''



        

        
