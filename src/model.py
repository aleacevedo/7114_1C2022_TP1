from helpers.distances import coor_to_km
import networkx as nx


class Model:
    capacity = 0
    dimension = 0
    request = []
    nodes = []
    distance_type = ''
    graph = nx.Graph()

    def __init__(self):
        pass

    def init_graph(self):
        if(len(self.nodes) == 0):
            raise Exception('No nodes found')
        if(len(self.nodes) != self.dimension):
            raise Exception('Invalid dimension')
        if(self.distance_type == 'EUC_2D'):
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if(i != j):
                        self.graph.add_edge(i, j, weight=self.euclidean_distance(self.nodes[i], self.nodes[j]))
        return self.graph

    def euclidean_distance(self, node1, node2):
        return coor_to_km(node1, node2)