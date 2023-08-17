class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        dist = [[float('inf')] * n for _ in range(m)]
        queue = []

        # Initialize with all 0 cells
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.pop(0)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check bounds and if the new distance is shorter
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        return dist