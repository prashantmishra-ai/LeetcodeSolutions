from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights or not heights[0]:
            return 0

        # Check if it's possible to reach the destination with the given effort.
        def canReachDest(effort):
            rows, cols = len(heights), len(heights[0])
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            queue = deque([(0, 0)])
            visited[0][0] = True

            # Define directions for up, down, left, and right movements.
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        if abs(heights[r][c] - heights[nr][nc]) <= effort:
                            visited[nr][nc] = True
                            queue.append((nr, nc))

            return False

        # Binary search on the effort values.
        low, high = 0, max(max(row) for row in heights) - min(min(row) for row in heights)
        while low <= high:
            mid = (low + high) // 2
            if canReachDest(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low