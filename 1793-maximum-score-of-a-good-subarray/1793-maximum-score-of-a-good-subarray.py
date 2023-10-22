class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Initialize the left and right boundary arrays
        left = [-1] * n
        right = [n] * n

        # Determine the left boundaries
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        # Clear the stack and determine the right boundaries
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        # Compute the max score
        maxScore = 0
        for i in range(n):
            if left[i] < k < right[i]:
                maxScore = max(maxScore, nums[i] * (right[i] - left[i] - 1))
        return maxScore