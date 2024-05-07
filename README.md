# hands-on-15

### Python Graph Algorithms

This repository contains implementations in Python of three fundamental graph algorithms: Floyd-Warshall, Bellman-Ford, and Dijkstra's algorithms. These techniques are widely utilized in many domains, including computer science, operations research, and network analysis, for determining the shortest paths in graphs.

1. **Dijkstra's Algorithm**

   In a graph with non-negative edge weights, the shortest path between nodes is found using Dijkstra's algorithm. It begins with a single source node and moves through the graph, repeatedly choosing the node that is closest to the source.

2. **Bellman-Ford Algorithm**

   In a weighted network, the shortest paths between a single source vertex and every other vertex are found using the Bellman-Ford technique. It can handle graphs with negative edge weights, in contrast to Dijkstra's method, but it also recognizes and reports negative weight cycles.

3. **Floyd-Warshall Algorithm**

   In a weighted network, the shortest paths between each pair of vertices are found using the Floyd-Warshall algorithm. It takes into account every possible path between two pairs of vertices in order to calculate the shortest distances.
