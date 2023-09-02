class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for word in dictionary:
                l = len(word)
                if i >= l and s[i - l:i] == word:
                    dp[i] = min(dp[i], dp[i - l])
                dp[i] = min(dp[i], dp[i - 1] + 1)
        return dp[n]