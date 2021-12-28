from itertools import permutations
from exceptions import *
from circuit import *
from courier import *
from order import *
from street import *
from transport import *
from typing import Tuple, List

import random













        










        

    

green_station = "Rua dos Pergaminhos"

Courier("João")
Courier("Manuel")
Courier("Carlos")

Street("Rua dos Pergaminhos")
Street("Rua dos Amendoins")
Street("Rua das Cores")

Street.connection("Rua dos Pergaminhos", "Rua dos Amendoins", 2500, True)
Street.connection("Rua dos Amendoins", "Rua das Cores", 50, True)
Street.connection("Rua das Cores", "Rua dos Pergaminhos", 10)

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
    Order("Rua dos Amendoins", 0, "00:06")
])

print("C1 DFS - ", c1.generate_circuit_dfs(), "Transport:", c1.can_transport(Car()))
print("C1 BFS - ", c1.generate_circuit_bfs(), "Transport:", c1.can_transport(Car()))
print("C1 Iter-DFS - ", c1.generate_circuit_iter_dfs(), "Transport:", c1.can_transport(Car()))

print("C2 DFS - ", c2.generate_circuit_dfs(), "Transport:", c2.can_transport(Car()))
print("C2 BFS - ", c2.generate_circuit_bfs(), "Transport:", c2.can_transport(Car()))
print("C2 Iter-DFS - ", c2.generate_circuit_iter_dfs(), "Transport:", c2.can_transport(Car()))

'''
def dfs(orders: list[Order]):
    for (idx in range(len(orders))):
        orders_copy = orders.copy()
        order = orders_copy.pop(idx)

        dfs(orders_copy)
'''



        

        
