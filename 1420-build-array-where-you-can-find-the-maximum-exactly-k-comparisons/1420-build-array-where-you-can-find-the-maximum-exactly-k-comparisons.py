class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
        for j in range(1, m+1):
            dp[1][j][1] = 1
        for i in range(2, n+1):
            for j in range(1, m+1):
                for kk in range(1, k+1):
                    dp[i][j][kk] = (dp[i][j][kk] + dp[i-1][j][kk]*j) % mod
                    for p in range(1, j):
                        dp[i][j][kk] = (dp[i][j][kk] + dp[i-1][p][kk-1]) % mod
        return sum(dp[n][j][k] for j in range(1, m+1)) % mod
