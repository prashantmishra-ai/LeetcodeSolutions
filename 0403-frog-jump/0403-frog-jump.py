class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        n = len(stones)
        dp = [set() for _ in range(n)]
        dp[1].add(1)

        for i in range(2, n):
            for j in range(1, i):
                diff = stones[i] - stones[j]
                if diff in dp[j] or diff-1 in dp[j] or diff+1 in dp[j]:
                    dp[i].add(diff)

        return len(dp[-1]) > 0