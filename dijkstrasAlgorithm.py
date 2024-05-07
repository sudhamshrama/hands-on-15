import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to store nodes with their current distances
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Pop node with smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Check if the current distance is already greater than known shortest distance
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
print("Shortest distances from node", start_node, ":", dijkstra(graph, start_node))
