class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [start for start, end, value in events]
        dp = [[-1] * n for _ in range(k + 1)]
        def dfs(cur_idx, count):
            if count == 0 or cur_idx == n:
                return 0
            if dp[count][cur_idx] != -1:
                return dp[count][cur_idx]
            next_idx = bisect_right(starts, events[cur_idx][1])
            dp[count][cur_idx] = max(dfs(cur_idx + 1, count), events[cur_idx][2] + dfs(next_idx, count - 1))
            return dp[count][cur_idx]
        return dfs(0, k)        