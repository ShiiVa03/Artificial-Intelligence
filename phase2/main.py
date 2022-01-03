from sys import version_info


if (version_info.major < 3 or (version_info.major == 3 and version_info.minor < 10)):
    raise Exception("This script requires Python 3.10+") # bisect.insort_right requires 3.10+

import random

from itertools import permutations
from exceptions import *
from circuit import *
from courier import *
from order import *
from street import *
from transport import *
from typing import Tuple, List
from pprint import PrettyPrinter



pprint = PrettyPrinter(indent=4).pprint













        










        


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
Motorcycle()
Car()

        
print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)



c1 = OrdersCircuit(green_station,
[
    Order("Rua dos Pergaminhos", 20, 10, "00:20"),
    Order("Rua das Cores", 20, 10, "00:30")
])

c2 = OrdersCircuit(green_station,
[
    Order("Rua dos Amendoins", 0, 10, "00:06")
])

print("{C1}")
pprint(c1.run_fastest())
c1.finish()
print("{C2}")
pprint(c2.run_ecologic())
c2.finish(on_time=False)

print(c2)

        

        
