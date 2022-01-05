from uninformed_search_algorithms import *
from informed_search_algorithms import *
from street import *

from memory_profiler import memory_usage
from time import perf_counter
from random import triangular, choice
from networkx.generators.harary_graph import hnm_harary_graph

ALGORITHMS = {
    'dfs': dfs,
    'bfs': bfs,
    'iter_dfs': iter_dfs,
    'greedy': greedy,
    'a_star': a_star
}

NUMBER_OF_STREETS = 40

NUMBER_OF_CONNECTIONS = 60

NUMBER_OF_ORDERS = 10

NUMBER_OF_CIRCUITS = 1
'''
NetworkX h.hnm_harary_graph already checks this


if NUMBER_OF_CONNECTIONS < NUMBER_OF_STREETS:
    raise Exception("Number of Connections must be higher than number of Streets for good tests")

if NUMBER_OF_CONNECTIONS > ((NUMBER_OF_STREETS * (NUMBER_OF_STREETS - 1)) // 2):
    raise Exception("Number of Connections exceeds limit")
'''

g = hnm_harary_graph(NUMBER_OF_STREETS, NUMBER_OF_CONNECTIONS)

all_streets = []

for i in g.nodes:
    street = Street("Street" + str(i), Point(int(triangular(0, 2500, 5000)), int(triangular(0, 2500, 5000)))) # Make streets near the middle point as it happens in real cities
    all_streets.append(street)


station = all_streets[0]
edges = list(g.edges)

for i in range(NUMBER_OF_STREETS):
    con = edges[i]
    Street.connection("Street" + str(con[0]), "Street" + str(con[1]), both_ways=True) # both_ways is True to avoid invalid paths



tests = {algorithm_name: [0, 0] for algorithm_name in ALGORITHMS.keys()}

for i in range(NUMBER_OF_CIRCUITS):
    streets = set(choice(all_streets) for _ in range(NUMBER_OF_ORDERS))

    for (algorithm_name, algorithm) in ALGORITHMS.items():
        print(algorithm_name)

        '''
            Memory performance test
        '''
        values = memory_usage((algorithm, (station, streets.copy(), station)))
        tests[algorithm_name][0] += max(values) - min(values)

        '''
            Time performance test
        '''
        street_copy = streets.copy()
        t1 = perf_counter()
        algorithm(station, street_copy, station)
        t2 = perf_counter()
        tests[algorithm_name][1] += t2 - t1


for (algorithm_name, (sum_mem, sum_time)) in tests.items():
    mem = sum_mem / NUMBER_OF_CIRCUITS
    time = sum_time / NUMBER_OF_CIRCUITS

    print(f"{algorithm_name.capitalize()} - {{Mem: {mem} MB | Time: {time} s}}")
        

