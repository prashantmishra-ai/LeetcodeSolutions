class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        # Initialize the DP array. dp[i][j] will store the number of ways to achieve a sum of j with i dice.
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Base case: There is 1 way to achieve a sum of 0 with 0 dice.
        dp[0][0] = 1

        # Fill the DP array.
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for face in range(1, k + 1):
                    if j - face >= 0:
                        dp[i][j] += dp[i - 1][j - face]
                        dp[i][j] %= MOD

        return dp[n][target]
