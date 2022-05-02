import networkx as nx


def sort_by_distance(neighbors):
    return sorted(neighbors, key=lambda x: x[1]['weight'])


def filter_visited(neighbors, visited):
    res = []
    for node in neighbors:
        if node[0][0] not in visited:
            res.append(node)
    return res


def solution_recursive(model, graph, next_stop_id, path, actual_charge, solutions, total_distance):
    if len(path) == 151:
        solutions.append((path, {"weight": total_distance}))
        return path
    neighbors = [(list(graph.nodes(data=True))[nei], graph.get_edge_data(
        next_stop_id, nei)) for nei in list(nx.all_neighbors(graph, next_stop_id))]
    neighbors = sort_by_distance(neighbors)
    posibles_stops = filter_visited(neighbors, path)
    for neighbor in posibles_stops:
        neighbor_id = neighbor[0][0]
        if actual_charge + model.requests[neighbor_id] <= model.capacity and actual_charge + model.requests[neighbor_id] >= 0:
            actual_charge += model.requests[neighbor_id]
            total_distance += neighbor[1]['weight']
            path.append(neighbor_id)
            temp_sol = solution_recursive(
                model, graph, neighbor_id, path, actual_charge, solutions, total_distance)
            if temp_sol == None:
                path.pop()

    return None


def solution(model):
    graph = model.init_graph()
    path = [0]
    actual_charge = 0
    first_stop_id = 0
    solutions = []
    sol = solution_recursive(
        model, graph, first_stop_id, path, actual_charge, solutions, 0)
    # print(sol, len(sol))
    sorted_solutions = sort_by_distance(solutions)
    print(sorted_solutions[0])
    return sorted_solutions[0][0]
