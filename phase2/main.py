from sys import version_info


if (version_info.major < 3 or (version_info.major == 3 and version_info.minor < 10)):
    raise Exception("This script requires Python 3.10+") # bisect.insort_right requires 3.10+


from exceptions import *
from circuit import *
from courier import *
from order import *
from street import *
from transport import *

Courier("João")
Courier("Manuel")
Courier("Carlos")

green_station = Street("Rua dos Pergaminhos", Point(0,0))
Street("Rua dos Amendoins", Point(2500, 0))
Street("Rua das Cores", Point(0,10))
Street("Rua Augusta", Point(3000,50))
Street("Rua Santa Catarina", Point(500,1000))
Street("Rua Gil Vicente", Point(2100,2000))
Street("Rua da Junqueira", Point(1940,1320))

Street.connection("Rua dos Pergaminhos", "Rua dos Amendoins", both_ways=True)
Street.connection("Rua dos Amendoins", "Rua das Cores", distance=3000, both_ways=True)
Street.connection("Rua das Cores", "Rua dos Pergaminhos")
Street.connection("Rua dos Amendoins", "Rua Augusta", both_ways=True)
Street.connection("Rua Gil Vicente", "Rua Augusta", both_ways=True)
Street.connection("Rua da Junqueira", "Rua Santa Catarina", both_ways=True)
Street.connection("Rua Gil Vicente", "Rua da Junqueira", both_ways=True)
Street.connection("Rua das Cores", "Rua Santa Catarina", both_ways=True)
Street.connection("Rua Santa Catarina", "Rua dos Pergaminhos")
Street.connection("Rua dos Pergaminhos", "Rua Gil Vicente", distance=3300)

Bike()
Motorcycle()
Car()

        
print_graph()
print("\n\n")



c1 = OrdersCircuit("C1", green_station,
[
    Order("Rua dos Pergaminhos", 20, 12, "00:20"),
    Order("Rua das Cores", 15, 10, "00:30"),
    Order("Rua Gil Vicente", 7, 7, "00:40"),

])

print(c1.get_info())

c2 = OrdersCircuit("C2", green_station,
[
    Order("Rua dos Amendoins", 1, 2, "00:06")
])

print(c2.get_info())

c3 = OrdersCircuit("C3", green_station,
[
    Order("Rua dos Amendoins", 2, 10, "10:00"),
    Order("Rua Augusta", 2, 10, "10:00"),
    Order("Rua Gil Vicente", 1, 5, "8:00")
])

print(c3.get_info())

c4 = OrdersCircuit("C4", green_station,
[
    Order("Rua dos Pergaminhos", 8, 12, "5:00"),
    Order("Rua Gil Vicente", 4, 9, "10:00"),
    Order("Rua da Junqueira", 2, 3, "12:00")
])

print(c4.get_info())

        

        
