from helpers.graph_builder import create_graph_from_csv
import matplotlib.pyplot as plt
from helpers.parser import parse_file
import networkx as nx
import algorithms.greedy as gr
import algorithms.backtracking as bt

nodes_csv = 'data/banks.csv'
edges_csv = 'data/distances.csv'
data = 'data/data_2.txt'

print('//////// PARSING FILE... ////////')
model = parse_file(data)
print('//////// INIT GRAPH... ////////')
graph = model.init_graph()

print('//////// GOING TO BACKTRACK... ////////')

# greedy_solution = gr.solultion(model)
# print(len(greedy_solution))
# with open('solutions/greedy_solution_2.txt', 'w') as f:
#     f.write(' '.join(greedy_solution))

bt_solution = [str(s) for s in bt.solution(model)]
with open('solutions/entrega_2.txt', 'w') as f:
    f.write(' '.join(bt_solution))
