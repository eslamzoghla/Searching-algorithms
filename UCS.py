graph = {
    'S': [('A', 4), ('B', 3), ('C', 2)],
    'A': [('D', 6)],
    'B': [('E', 8)],
    'C': [('G', 20)],
    'D': [('F', 2)],
    'F': [('G', 2)],
    'E': [('F', 2)],
}


def path_cost(path):
    total = 0
    for (node, cost) in path:
        total += cost
    return total, path[-1][0]


def UCS(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]

    while queue:
        queue.sort(key=path_cost)
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


sol = UCS(graph, 'S', 'G')
print(sol)
print(path_cost(sol)[0])
