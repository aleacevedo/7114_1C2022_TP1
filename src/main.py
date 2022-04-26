from builder import create_graph_from_csv
import matplotlib.pyplot as plt
import networkx as nx

nodes_csv = 'data/banks.csv'
edges_csv = 'data/distances.csv'
graph = create_graph_from_csv(nodes_csv, edges_csv)

x = nx.shortest_path(graph, 1, 2)
print(x)

