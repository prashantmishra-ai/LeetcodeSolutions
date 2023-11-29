class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # Loop through all 32 bits of the integer
        for i in range(32):
            # Check if the ith bit is 1
            if n & (1 << i):
                count += 1

        return count