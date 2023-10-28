class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0 for _ in range(5)] for _ in range(n)]
        for v in range(5):
            dp[0][v] = 1  # Base case: For length 1, there's one string for each vowel

        # Updating the DP table
        for i in range(1, n):
            dp[i][0] = dp[i - 1][1]  # a -> e
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD  # e -> a or i
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % MOD  # i -> a, e, o, u
            dp[i][3] = (dp[i - 1][2] + dp[i - 1][4]) % MOD  # o -> i or u
            dp[i][4] = dp[i - 1][0]  # u -> a

        # Summing up all possibilities for strings of length n
        return sum(dp[n - 1]) % MOD