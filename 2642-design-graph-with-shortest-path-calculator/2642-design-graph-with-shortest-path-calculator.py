import heapq

class Graph:
    def __init__(self, n, edges):
        self.n = n
        # Using a dictionary to represent the adjacency list for the graph
        self.graph = {i: [] for i in range(n)}
        for from_node, to_node, cost in edges:
            self.graph[from_node].append((to_node, cost))

    def addEdge(self, edge):
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1, node2):
        # Dijkstra's algorithm to find the shortest path from node1 to node2
        # Priority queue to keep track of nodes to visit, format: (cost, node)
        pq = [(0, node1)]
        visited = set()

        while pq:
            cost, node = heapq.heappop(pq)
            if node == node2:
                return cost
            if node not in visited:
                visited.add(node)
                for neighbour, edge_cost in self.graph[node]:
                    if neighbour not in visited:
                        heapq.heappush(pq, (cost + edge_cost, neighbour))

        # If node2 is not reachable from node1
        return -1