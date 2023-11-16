class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Convert each binary string to an integer
        nums_as_int = set(int(num, 2) for num in nums)

        # Iterate through all possible binary numbers of length n
        n = len(nums[0])
        for i in range(2 ** n):
            if i not in nums_as_int:
                # Convert the number back to a binary string and return
                return format(i, '0' + str(n) + 'b')
