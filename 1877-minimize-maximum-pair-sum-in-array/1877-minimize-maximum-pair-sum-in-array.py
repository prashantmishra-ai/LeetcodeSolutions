class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        # Initialize the maximum pair sum
        max_pair_sum = 0
        # Iterate over the pairs
        for i in range(len(nums) // 2):
            # Calculate the pair sum
            pair_sum = nums[i] + nums[len(nums) - 1 - i]
            # Update the maximum pair sum if necessary
            max_pair_sum = max(max_pair_sum, pair_sum)
        return max_pair_sum