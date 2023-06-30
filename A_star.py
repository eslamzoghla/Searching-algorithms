graph = {
    'S': [('A', 4), ('B', 3), ('C', 2)],
    'A': [('D', 6)],
    'B': [('E', 8)],
    'C': [('G', 20)],
    'D': [('F', 2)],
    'F': [('G', 2)],
    'E': [('F', 2)],
}

H_table = {
    'S': 18,
    'A': 14,
    'B': 13,
    'C': 20,
    'D': 10,
    'E': 8,
    'F': 5,
    'G': 0
}


def path_f_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = g_cost + h_cost
    return f_cost, last_node


def A_star(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]

    while queue:
        queue.sort(key=path_f_cost)
        path = queue.pop(0)
        last_node = path[-1][0]

        if last_node is visited:
            continue
        visited.append(last_node)
        if last_node == goal:
            return path
        else:
            adjecent_nodes = graph.get(last_node, [])
            for (nodes, cost) in adjecent_nodes:
                new_path = path.copy()
                new_path.append((nodes, cost))
                queue.append(new_path)


sol = A_star(graph, 'S', 'G')
print(sol)
print(path_f_cost(sol)[0])
