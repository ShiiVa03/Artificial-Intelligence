from street import *
from order import *
from typing import Set, List, Tuple, Callable, Optional
from bisect import insort_right
from collections import deque



def greedy(initial: Street, streets: Set[Street], end: Street) -> Optional[List[Tuple[Street, int]]]:

    def function(node: Tuple[List[Tuple[Street, int]], int], adj: Tuple[Street, int]) -> int:
        path = node[0]
        adj_street = adj[0]

        missing_streets = streets.difference(map(lambda x: x[0], path))

        if missing_streets:
            return min(adj_street.euclidian_dist(street) for street in missing_streets)
        else:
            return adj_street.euclidian_dist(end)
    
    return informed_search_algorithm(initial, streets, end, function)


def a_star(initial: Street, streets: Set[Street], end: Street) -> Optional[List[Tuple[Street, int]]]:

    def function(node: Tuple[List[Tuple[Street, int]], int], adj: Tuple[Street, int]) -> int:
        path = node[0]
        adj_street = adj[0]

        missing_streets = streets.difference(map(lambda x: x[0], path))
        path_cost = sum(cost for (_, cost) in path) + adj[1]

        if missing_streets:
            return min(path_cost + adj_street.euclidian_dist(street) for street in missing_streets)
        else:
            return path_cost + adj_street.euclidian_dist(end)
    
    return informed_search_algorithm(initial, streets, end, function)
    


def informed_search_algorithm(initial: Street, streets: Set[Street], end: Street, function: Callable[[Tuple[List[Tuple[Street, int]], int], Tuple[Street, int]], int]) -> Optional[List[Tuple[Street, int]]]:

    queue = deque([([(initial, 0)], 0)]) # queue is a List[(Path, function_result)] where Path is [(Street, cost)]
                                         # First node there is no need to execute function
    
    while len(queue) > 0:
        node = queue.popleft()
        path = node[0]
        last_street = path[-1][0]

        if last_street == end: # Check if circuit covers all orders
            missing_streets = streets.difference(map(lambda x: x[0], path))

            if not missing_streets:
                return path

        streets_copy = streets.copy()
        last_order_idx = -1
        for (idx, (street, _)) in enumerate(path):
            try:
                streets_copy.remove(street)
            except KeyError:
                if not streets_copy:
                    break
            else:
                last_order_idx = idx

        visited_streets_after_last_order = set(x[0] for x in path[last_order_idx:])

        for adj in graph[last_street]:

            in_cycle = adj[0] in visited_streets_after_last_order

            if not in_cycle:
                function_result = function(node, adj)
                insort_right(queue, (path + [adj], function_result), key=lambda x: x[1])

    return None


        