from __future__ import annotations
from exceptions import *
from math import sqrt, ceil

class Point:
    def __init__(self, x: int, y: int):
      self.x = x
      self.y = y

    def get_x(self) -> int:
      return self.x

    def get_y(self) -> int:
      return self.y
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"



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

    all_streets = {}
    
    def __init__(self, name: str, location: Point):
        '''
            Just to garantee that this street exists in order to avoid future misspellings
        '''

        if name in self.__class__.all_streets:
            raise StreetAlreadyExistsException

        self.name = name
        self.location = location

        add_vertex(self)


        self.__class__.all_streets[name] = self


    def get_name(self) -> str:
        return self.name
    
    def get_location(self) -> Point:
        return self.location
    
    def euclidian_dist(self, other_street: Street) -> int:
        street_location = self.location
        other_location = other_street.get_location()

        return ceil(sqrt((other_location.get_x() - street_location.get_x()) ** 2 + (other_location.get_y() - street_location.get_y()) ** 2))

    @classmethod
    def get_street_by_name(cls, name: str) -> Street:
        try:
            return cls.all_streets[name]
        except KeyError:
            raise StreetDoesntExistException


    @staticmethod
    def connection(street1_name: str, street2_name: str, distance: int=None, both_ways: bool=False):
        street1 = Street.get_street_by_name(street1_name)
        street2 = Street.get_street_by_name(street2_name)

        dist = street1.euclidian_dist(street2)

        if (distance is not None):
            if (distance < dist):
                raise ConnectionDistHigherThanEuclidian
            
            dist = distance


        add_edge(street1, street2, dist)
        if (both_ways):
            add_edge(street2, street1, dist)
    

    def __repr__(self) -> str:
        return self.name