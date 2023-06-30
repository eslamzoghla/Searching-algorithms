graph = {
    'S': ['A', 'B', 'D'],
    'A': ['C'],
    'B': ['D'],
    'C': ['D', 'G'],
    'D': ['G'],
}


def DFS(graph, start, goal):
    visited = []
    stack = [[start]]

    while stack:
        path = stack.pop()
        last_node = path[-1]

        if last_node is visited:
            continue
        visited.append(last_node)

        if last_node == goal:
            return path
        else:
            adjecent_nodes = graph.get(last_node, [])
            for nodes in adjecent_nodes:
                new_path = path.copy()
                new_path.append(nodes)
                stack.append(new_path)


print(DFS(graph, 'S', 'D'))
