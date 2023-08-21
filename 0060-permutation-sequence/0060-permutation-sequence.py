class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        factorial = 1
        for i in range(1, n):
            factorial *= i
        k -= 1  # Convert k from 1-based to 0-based index
        res = []

        while n > 0:
            idx = k // factorial
            res.append(nums[idx])
            nums.pop(idx)

            k %= factorial
            if n > 1:
                factorial //= (n-1)
            n -= 1

        return ''.join(res)