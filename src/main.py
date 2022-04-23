from builder import create_graph_from_csv

nodes_csv = 'data/banks.csv'
edges_csv = 'data/distances.csv'
graph = create_graph_from_csv(nodes_csv, edges_csv)

