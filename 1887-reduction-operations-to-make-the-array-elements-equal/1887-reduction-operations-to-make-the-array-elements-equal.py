class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Sort the unique numbers in descending order
        unique_nums = sorted(frequency.keys(), reverse=True)

        operations = 0
        cumulative_frequency = 0

        # Iterate over the unique numbers
        for i in range(len(unique_nums) - 1):
            # Add the frequency of the current number to the cumulative frequency
            cumulative_frequency += frequency[unique_nums[i]]
            # Increase the operations by the cumulative frequency
            operations += cumulative_frequency

        return operations