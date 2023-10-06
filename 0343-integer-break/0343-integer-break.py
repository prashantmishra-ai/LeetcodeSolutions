class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 2:

            # This case should not happen based on the problem statement

            return 0



        # Handling the special cases

        if n == 2:

            return 1  # Since 2 can only be broken into 1 + 1

        elif n == 3:

            return 2  # Since 3 can only be broken into 1 + 2

        elif n % 3 == 0:

            return int(3 ** (n // 3))

        elif n % 3 == 1:

            return int(4 * (3 ** ((n - 4) // 3)))

        else:  # n % 3 == 2

            return int(2 * (3 ** (n // 3)))
