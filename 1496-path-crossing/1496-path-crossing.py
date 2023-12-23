class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0

        # Set to store visited points
        visited = set()
        visited.add((x, y))

        # Mapping the directions to their respective coordinate changes
        move = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        for direction in path:
            dx, dy = move[direction]
            x, y = x + dx, y + dy
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False