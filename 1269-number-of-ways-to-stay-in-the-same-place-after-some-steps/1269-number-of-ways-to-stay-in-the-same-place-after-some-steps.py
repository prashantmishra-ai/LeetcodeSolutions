class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        maxLen = min(arrLen,steps//2+1)
        dp = [[0]* maxLen for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(1,steps+1):
            for j in range(maxLen):
                dp[i][j] = dp[i-1][j]
                if j>0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD
                if j<maxLen-1:
                    dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % MOD
        return dp[steps][0]