from helpers.graph_builder import create_graph_from_csv
import matplotlib.pyplot as plt
from helpers.parser import parse_file
import networkx as nx

nodes_csv = 'data/banks.csv'
edges_csv = 'data/distances.csv'
data = 'data/data_mod.txt'

model = parse_file(data)
graph = model.init_graph()

nx.draw(graph)  # networkx draw()
plt.draw()  # pyplot draw()
plt.show()

