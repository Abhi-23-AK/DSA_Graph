def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=' ')      # Process the node
        visited.add(node)         # Mark as visited

        for neighbor in graph[node]:     # Explore each neighbor deeply
            dfs(graph, neighbor, visited)
'''graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

dfs(graph, 0)
'''