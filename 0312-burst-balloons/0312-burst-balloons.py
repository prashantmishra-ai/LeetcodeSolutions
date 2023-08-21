class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add border balloons
        nums = [1] + nums + [1]
        n = len(nums)
        # Create a 2D dp table
        dp = [[0]*n for _ in range(n)]

        # Iterate over all subarrays
        for len_sub in range(2, n):
            for i in range(0, n - len_sub):
                j = i + len_sub
                for k in range(i+1, j):
                    # Update dp table
                    dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])

        return dp[0][n-1]