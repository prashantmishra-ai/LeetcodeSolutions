class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        i = 0
        curr = 1
        while (curr * 2) <= n:
            curr *= 2
            i += 1

        return 2**(i+1)-1-self.minimumOneBitOperations(n ^ curr)