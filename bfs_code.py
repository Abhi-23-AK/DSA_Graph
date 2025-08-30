from collections import deque

def bfs(graph, start):
    visited = set()              # To track visited nodes
    queue = deque([start])       # Initialize queue with the starting node

    while queue:
        node = queue.popleft()   # Remove from front (FIFO)

        if node not in visited:
            print(node, end=' ')      # Process the node
            visited.add(node)         # Mark as visited

            for neighbor in graph[node]:  # Add all unvisited neighbors
                if neighbor not in visited:
                    queue.append(neighbor)
'''graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

bfs(graph, 0)
'''