class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        # Iterate over the points
        for i in range(len(points) - 1):
            # Current point
            x1, y1 = points[i]
            # Next point
            x2, y2 = points[i + 1]

            # Calculate the difference in x and y coordinates
            delta_x = abs(x2 - x1)
            delta_y = abs(y2 - y1)

            # The time to move diagonally is the max of delta_x and delta_y
            # as moving diagonally covers both x and y distances simultaneously
            total_time += max(delta_x, delta_y)

        return total_time