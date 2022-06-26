from helpers.distances import coor_to_km


def can_go(model, charge, actual_charge):
    if(0 < actual_charge + charge and actual_charge + charge <= model.capacity):
        return True
    return False


def solution(model):
    requests = model.get_requests()
    nodes = model.get_nodes()
    visited = [False] * len(nodes)
    matrix = []
    actual_charge = 0
    path = [0]
    visited[0] = True
    current_node = 0
    next_node = 0
    total_distance = 0

    print(' Creating matrix...')
    for i in range(len(nodes)):
        matrix.append([coor_to_km(nodes[i], node) for node in nodes])

    print(' Solving...')

    while(len(path) < model.get_dimension()+1):
        next_distance = float("inf")
        for neighbour in range(len(matrix[current_node])):
            if(not visited[neighbour]):
                if(matrix[current_node][neighbour] < next_distance):
                    next_distance = matrix[current_node][neighbour]
                    next_node = neighbour
        path.append(next_node)
        actual_charge += requests[next_node]
        total_distance += next_distance
        current_node = next_node
        visited[next_node] = True

    print(' Total distance: ', total_distance)
    return [str(x) for x in path[1:]]
