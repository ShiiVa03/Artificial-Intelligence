from exceptions import *

vertices_no = 0

def has_vertex(v):
    global graph
    return v in graph

# Add a vertex to the dictionary
def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
  global graph
  # Check if vertex v1 is a valid vertex
  if v1 not in graph:
    raise StreetDoesntExistException
  # Check if vertex v2 is a valid vertex
  elif v2 not in graph:
    raise StreetDoesntExistException
  else:
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    temp = (v2, e)
    graph[v1].append(temp)

# Print the graph
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

graph = {}

class Street:
    
    def __new__(cls, street):
        '''
            Just to garantee that this street exists in order to avoid future misspellings
        '''

        add_vertex(street)


    @classmethod
    def connection(cls, street1, street2, distance, both_ways=False):
        add_edge(street1, street2, distance)
        if (both_ways):
            add_edge(street2, street1, distance)