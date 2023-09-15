class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        # Create a list of edges with their weights
        for i in range(n):
            for j in range(i+1, n):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((weight, i, j))

        # Sort the edges by weight
        edges.sort()

        uf = UnionFind(n)
        res = 0
        count = 0

        # Add edges to the MST
        for edge in edges:
            weight, u, v = edge
            if not uf.isConnected(u, v):
                uf.union(u, v)
                res += weight
                count += 1
                if count == n - 1:
                    break

        return res
