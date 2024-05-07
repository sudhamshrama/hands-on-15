def floyd_warshall(graph):
    distances = {node: {neighbor: float('inf') for neighbor in graph} for node in graph}

    # Initialize distances with edge weights
    for node in graph:
        for neighbor, weight in graph[node].items():
            distances[node][neighbor] = weight

    # Update distances by considering all possible paths
    for node in graph:
        distances[node][node] = 0
        for start in graph:
            for end in graph:
                distances[start][end] = min(distances[start][end], distances[start][node] + distances[node][end])

    return distances

# Example graph
graph = {
    'A': {'B': 3, 'C': 8, 'E': -4},
    'B': {'D': 1, 'C': 4},
    'C': {'B': -5},
    'D': {'A': 2, 'C': 2},
    'E': {'D': 7}
}

print("Shortest distances between all pairs of vertices:")
for node, distances in floyd_warshall(graph).items():
    print(node, ":", distances)
