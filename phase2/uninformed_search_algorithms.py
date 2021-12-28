from street import *
from order import *
from typing import Set, List
from queue import Queue

def dfs(initial, streets_names: Set[Order], end) -> List[str]:
    (path, _) = dfs_aux(initial, streets_names, end, set())

    if path is not None:
        path.insert(0, (initial, 0))

    return path

def dfs_aux(initial, streets_names: Set[Order], end, history: Set[str], max_depth: int=None, depth: int=0) -> List[str]:

    if initial in history:
        return (None, 1)

    streets_names_copy = streets_names
    
    history.add(initial)

    if streets_names:
        if initial in streets_names:
            streets_names_copy = streets_names.copy()
            streets_names_copy.remove(initial)
            history = {initial}
    
    elif initial == end:
        return ([], 1)


    max_depth_reached = 0

    
    if max_depth is None or depth < max_depth:
        for adj in graph[initial]:

            (path, depth_reached) = dfs_aux(adj[0], streets_names_copy, end, history, max_depth, depth + 1)

            if depth_reached > max_depth_reached:
                max_depth_reached = depth_reached

            if path is not None:
                path.insert(0, adj)
                return (path, max_depth_reached + 1)

    history.discard(initial)
    return (None, max_depth_reached + 1)




def bfs(initial, streets_names: Set[Order], end) -> List[str]:

    queue = Queue()
    
    if not streets_names:
        return []
    
    queue.put([(initial, 0)])
    
    while not queue.empty():
        path = queue.get()
        last_street = path[-1][0]

        if last_street == end: # Check if circuit covers all orders
            missing_streets = streets_names.difference(map(lambda x: x[0], path))

            if not missing_streets:
                return path

        rev_streets_gen = map(lambda x: x[0], reversed(path))

        for adj in graph[last_street]:

            in_cycle = False 

            for street in rev_streets_gen:
                if street in streets_names:
                    break
                if street == adj[0]:
                    in_cycle = True
                    return None

            queue.put(path + [adj])

    return None



def iter_dfs(initial, streets_names: Set[Order], end) -> List[str]:
    max_depth = max_depth_reached = 1
    path = None

    while (path is None and max_depth == max_depth_reached):
        (path, max_depth_reached) = dfs_aux(initial, streets_names, end, set(), max_depth)
        max_depth += 1
    
    
    if path is not None:
        path.insert(0, (initial, 0))

    return path
