
from helpers.distances import coor_to_km
import networkx as nx

class Node:
    def __init__(self, request):
        self.request = request

class Model:
    capacity = 0
    dimension = 0
    requests = [0]
    nodes = [(0, 0)]
    distance_type = ''
    graph = nx.Graph()

    def __init__(self):
        pass

    def init_graph(self):
        if(len(self.nodes) == 0):
            raise Exception('No nodes found')
        if(len(self.nodes) != self.dimension+1):
            raise Exception('Invalid dimension')
        if(self.distance_type == 'EUC_2D'):
            for i in range(self.dimension+1):
                self.graph.add_node(i, request = self.requests[i])
            for i in range(self.dimension+1):
                for j in range(self.dimension+1):
                    if(i != j):
                        self.graph.add_edge(i, j, weight=self.euclidean_distance(self.nodes[i], self.nodes[j]))
        print('Inited Graph ', self.distance_type)
        print('Size: ', len(self.nodes), self.dimension)
        return self.graph

    def euclidean_distance(self, node1, node2):
        return coor_to_km(node1, node2)

    def get_graph(self):
        return self.graph
