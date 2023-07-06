class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        running_sum = 0
        minLen = float('inf')
        for right in range(n):
            running_sum += nums[right]
            while running_sum >= target:
                minLen = min(minLen,right-left+1)
                running_sum -= nums[left]
                left+=1
        return minLen if minLen != float('inf') else 0