from igraph import Graph, plot
import matplotlib.pyplot as plt

def init_graph(nodes, edges):
  graph = Graph(directed=False)
  graph.add_vertices(len(nodes)+1)
  graph.add_edges(edges)
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
      edges.append((int(edge[0]), int(edge[1])))
  return edges

def create_graph_from_csv(nodes_file, edges_file):
  nodes = load_nodes_from_csv(nodes_file)
  edges = load_edges_from_csv(edges_file)
  return init_graph(nodes, edges)

nodes_csv = 'data/banks.csv'
edges_csv = 'data/distances.csv'
graph = init_graph(load_nodes_from_csv(nodes_csv), load_edges_from_csv(edges_csv))
fig, ax = plt.subplots()
plot(graph, target=ax)