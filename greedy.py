graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)],
}

H_table = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}


def path_h_cost(path):
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    return h_cost, last_node


def Greedy(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]

    while queue:
        queue.sort(key=path_h_cost)
        path = queue.pop(0)
        last_node = path[-1][0]

        if last_node is visited:
            continue
        visited.append(last_node)
        if last_node == goal:
            return path
        else:
            adjecent_nodes = graph.get(last_node, [])
            for (node, cost) in adjecent_nodes:
                new_path = path.copy()
                new_path.append((node, cost))
                queue.append(new_path)


sol = Greedy(graph, 'S', 'G')
print("A Solution is: ", sol)
print(path_h_cost(sol)[0])
