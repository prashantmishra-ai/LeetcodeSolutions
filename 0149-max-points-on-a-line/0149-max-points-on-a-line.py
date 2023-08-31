class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        maxPoints = 2
        for i in range(n - 1):
            slopeCount = {}
            for j in range(n):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                slope = math.atan2(y2 - y1, x2 - x1)
                slopeCount[slope] = slopeCount.get(slope, 0) + 1
                maxPoints = max(maxPoints, slopeCount[slope] + 1)
        return maxPoints
