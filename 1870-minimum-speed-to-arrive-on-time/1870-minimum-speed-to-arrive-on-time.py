from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], t: float) -> int:
        n = len(dist)
        if n - 1 > t:
            return -1  # Impossible to reach in time

        left, right = 1, int(1e9) + 1  # Adjust the right boundary based on the problem constraints
        min_speed = -1

        while left < right:
            speed = (left + right) // 2
            time_taken = 0

            for i in range(n - 1):
                time_taken += (dist[i] + speed - 1) // speed

            time_taken += dist[-1] / speed

            if time_taken <= t:
                min_speed = speed
                right = speed
            else:
                left = speed + 1

        return min_speed
