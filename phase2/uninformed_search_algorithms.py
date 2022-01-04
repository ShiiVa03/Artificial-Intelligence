from street import *
from order import *
from typing import Set, List, Optional, Tuple
from collections import deque

def dfs(initial: Street, streets: Set[Street], end) -> Optional[List[Tuple[Street, int]]]:
    (path, _) = dfs_aux(initial, streets, end, set())

    if path is not None:
        path.insert(0, (initial, 0))

    return path

def dfs_aux(initial: Street, streets: Set[Street], end: Street, history: Set[Street], max_depth: int=None, depth: int=0) -> Tuple[Optional[List[Tuple[Street, int]]], int]:

    if initial in history:
        return (None, 1)

    streets_copy = streets
    
    history.add(initial)
    new_history = None

    if streets:
        if initial in streets:
            streets_copy = streets.copy()
            streets_copy.remove(initial)
            new_history = {initial}
    
    elif initial == end:
        return ([], 1)


    max_depth_reached = 0

    
    if max_depth is None or depth < max_depth:
        for adj in graph[initial]:

            (path, depth_reached) = dfs_aux(adj[0], streets_copy, end, new_history or history, max_depth, depth + 1)

            if depth_reached > max_depth_reached:
                max_depth_reached = depth_reached

            if path is not None:
                path.insert(0, adj)
                return (path, max_depth_reached + 1)


    history.discard(initial)
    return (None, max_depth_reached + 1)




def bfs(initial: Street, streets: Set[Street], end: Street) -> Optional[List[Tuple[Street, int]]]:
    
    queue = deque([[(initial, 0)]]) # queue is a List[Path] where Path is [(Street, distance)]
    
    while len(queue) > 0:
        path = queue.popleft()
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

        visited_streets_after_last_order = set(x[0] for x in path[last_order_idx + 1:])

        for adj in graph[last_street]:

            in_cycle = adj[0] in visited_streets_after_last_order

            if not in_cycle:
                queue.append(path + [adj])

    return None



def iter_dfs(initial: Street, streets: Set[Street], end: Street) -> Optional[List[Tuple[Street, int]]]:
    max_depth = max_depth_reached = 1
    path = None

    while (path is None and max_depth == max_depth_reached):
        (path, max_depth_reached) = dfs_aux(initial, streets, end, set(), max_depth)
        max_depth += 1
        
    
    
    if path is not None:
        path.insert(0, (initial, 0))

    return path
