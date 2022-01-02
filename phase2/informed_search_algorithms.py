from street import *
from order import *
from typing import Set, List, Tuple, Callable
from bisect import insort_right
from collections import deque

'''
def greedy(initial: Street, streets: Set[Street], end: Street):
    path = greedy_aux(initial, streets, end, set())

    if path is not None:
        path.insert(0, (initial, 0))
    
    return path


def greedy_aux(initial: Street, streets: Set[Street], end: Street, history: Set[Street]) -> List[Street]:
    if initial in history:
        return None

    streets_copy = streets

    history.add(initial)

    if streets:
        if initial in streets:
            streets_copy = streets.copy()
            streets_copy.remove(initial)
            history = {initial}
    
    elif initial == end:
        return []

    adjs_dist = sorted(((adj, adj[0].euclidian_dist(initial)) for adj in graph[initial]), key=lambda x: x[1])
    
    for (adj, _) in adjs_dist:

        path = greedy_aux(adj[0], streets_copy, end, history)

        if path is not None:
            path.insert(0, adj)
            return path

    history.discard(initial)
    return None

'''

def greedy(initial: Street, streets: Set[Street], end: Street) -> List[Street]:

    def heuristic(node: Tuple[List[Tuple[Street, int]], int], adj: Tuple[Street, int]) -> int:
        path = node[0]
        adj_street = adj[0]

        missing_streets = streets.difference(map(lambda x: x[0], path))

        if missing_streets:
            return min(adj_street.euclidian_dist(street) for street in missing_streets)
        else:
            return adj_street.euclidian_dist(end)
    
    return algorithm(initial, streets, end, heuristic)


def a_star(initial: Street, streets: Set[Street], end: Street) -> List[Street]:

    def heuristic(node: Tuple[List[Tuple[Street, int]], int], adj: Tuple[Street, int]) -> int:
        path = node[0]
        adj_street = adj[0]

        missing_streets = streets.difference(map(lambda x: x[0], path))
        path_cost = sum(cost for (_, cost) in path) + adj[1]

        if missing_streets:
            return min(path_cost + adj_street.euclidian_dist(street) for street in missing_streets)
        else:
            return path_cost + adj_street.euclidian_dist(end)
    
    return algorithm(initial, streets, end, heuristic)
    


def algorithm(initial: Street, streets: Set[Street], end: Street, heuristic: Callable[[Tuple[List[Tuple[Street, int]], int], Tuple[Street, int]], int]) -> List[Street]:

    if not streets:
        return []
    
    queue = deque([([(initial, 0)], 0)]) # queue is a List[(Path, heuristic_result)] where Path is [(Street, cost)]
                                         # First node there is no need to execute heuristic
    
    while len(queue) > 0:
        node = queue.popleft()
        path = node[0]
        last_street = path[-1][0]

        if last_street == end: # Check if circuit covers all orders
            missing_streets = streets.difference(map(lambda x: x[0], path))

            if not missing_streets:
                return path

        rev_streets_gen = map(lambda x: x[0], reversed(path))

        for adj in graph[last_street]:

            in_cycle = False
            adj_street = adj[0]

            for street in rev_streets_gen:
                if street in streets:
                    break
                if street == adj_street:
                    in_cycle = True
                    break

            if not in_cycle:
                heuristic_result = heuristic(node, adj)
                insort_right(queue, (path + [adj], heuristic_result), key=lambda x: x[1])

    return None


        