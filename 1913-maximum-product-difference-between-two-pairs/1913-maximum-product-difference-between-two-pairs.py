class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        # The maximum product difference is obtained by subtracting the product of the two smallest numbers from the product of the two largest numbers
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])