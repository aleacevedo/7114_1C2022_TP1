import matplotlib.pyplot as plt
import networkx as nx

def init_graph(edges):
  graph = nx.Graph()
  for edge in edges:
    graph.add_edge(edge[0], edge[1], weight=edge[2])
  return graph

def load_nodes_from_csv(file_name): 
  nodes = []
  with open(file_name, 'r') as file:
    next(file)
    for line in file:
      nodes.append(line.strip())
  return nodes

def load_edges_from_csv(file_name):
  edges = []
  with open(file_name, 'r') as file:
    next(file)
    for line in file:
      edge = line.strip().split(',')
      edges.append((int(edge[0]), int(edge[1]), float(edge[2])))
  return edges

def create_graph_from_csv(nodes_file, edges_file):
  _nodes = load_nodes_from_csv(nodes_file)
  edges = load_edges_from_csv(edges_file)
  return init_graph(edges)

