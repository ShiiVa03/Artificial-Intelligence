from street import *
from order import *
from typing import Set, List
from collections import deque

def dfs(initial: Street, streets: Set[Street], end) -> List[Street]:
    (path, _) = dfs_aux(initial, streets, end, set())

    if path is not None:
        path.insert(0, (initial, 0))

    return path

def dfs_aux(initial: Street, streets: Set[Order], end: Street, history: Set[Street], max_depth: int=None, depth: int=0) -> List[Street]:

    if initial in history:
        return (None, 1)

    streets_copy = streets
    
    history.add(initial)

    if streets:
        if initial in streets:
            streets_copy = streets.copy()
            streets_copy.remove(initial)
            history = {initial}
    
    elif initial == end:
        return ([], 1)


    max_depth_reached = 0

    
    if max_depth is None or depth < max_depth:
        for adj in graph[initial]:

            (path, depth_reached) = dfs_aux(adj[0], streets_copy, end, history, max_depth, depth + 1)

            if depth_reached > max_depth_reached:
                max_depth_reached = depth_reached

            if path is not None:
                path.insert(0, adj)
                return (path, max_depth_reached + 1)

    history.discard(initial)
    return (None, max_depth_reached + 1)




def bfs(initial: Street, streets: Set[Street], end: Street) -> List[Street]:
    
    if not streets:
        return []
    
    queue = deque([[(initial, 0)]]) # queue is a List[Path] where Path is [(Street, distance)]
    
    while len(queue) > 0:
        path = queue.popleft()
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
                queue.append(path + [adj])

    return None



def iter_dfs(initial: Street, streets: Set[Street], end: Street) -> List[Street]:
    max_depth = max_depth_reached = 1
    path = None

    while (path is None and max_depth == max_depth_reached):
        (path, max_depth_reached) = dfs_aux(initial, streets, end, set(), max_depth)
        max_depth += 1
    
    
    if path is not None:
        path.insert(0, (initial, 0))

    return path
