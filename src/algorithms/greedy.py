from random import random
import networkx as nx

def sort_by_distance(neighbors):
    return sorted(neighbors, key=lambda x: x[1]['weight'])

def can_go(model, node, actual_charge):
    if(0 < actual_charge + node[1]['request'] and actual_charge + node[1]['request'] <= model.capacity):
        return True
    return False

def filter_visited(neighbors, visited):
    return [node for node in neighbors if node[0] not in visited]


def solultion(model):
    graph = model.init_graph()
    actual_charge = 0
    total_distance = 0
    visiting_order = []
    init = list(graph.nodes(data=True))[0]
    visiting_order.append(init)
    while (len(visiting_order) < 11):
        # Tomo vecinos del ultimo nodo visitado y los ordeno por distancia
        neighbors = [(list(graph.nodes(data=True))[nei], graph.get_edge_data(visiting_order[-1][0], nei)) for nei in list(nx.all_neighbors(graph, visiting_order[-1][0]))]
        neighbors = sort_by_distance(neighbors)
        # Filtro los vecinos que ya fueron visitados
        for node in filter_visited(neighbors, visiting_order):
            if(can_go(model, node[0], actual_charge)):
                visiting_order.append(node[0])
                actual_charge += node[0][1]['request']
                total_distance += node[1]['weight']
                break
    # Descarto punto de inicio
    path = [str(node[0]) for node in visiting_order[1:]]
    return path
            


