class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        two = 0
        for num in nums:
            ones = (ones^num)& ~two
            two = (two^num)& ~ones
        return ones