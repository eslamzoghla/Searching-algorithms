graph = {
    'S': ['A', 'B', 'D'],
    'A': ['C'],
    'B': ['D'],
    'C': ['D', 'G'],
    'D': ['G'],
}


def BFS(graph, start, goal):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)  # SA
        last_node = path[-1]  # A

        if last_node in visited:  # NO
            continue
        visited.append(last_node)  # Add node A to visited
        if last_node == goal:  # NO
            return path
        else:
            adjecent_nodes = graph.get(last_node, [])  # C
            for node2 in adjecent_nodes:  # node2 = C
                new_path = path.copy()   # S,A
                new_path.append(node2)   # S,A,C
                queue.append(new_path)


output = BFS(graph, 'S', 'D')
print(output)
