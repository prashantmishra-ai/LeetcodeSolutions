class Solution:
    def knightDialer(self, n: int) -> int:
    # Modulo constant
        knight_moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],  # 5 cannot be reached by a knight's move
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        MOD = 10**9 + 7

        # If n is 1, the knight can be placed on any of the 10 digits
        if n == 1:
            return 10

        # Initialize the previous count for each digit as 1 (for n = 1)
        previous_count = [1] * 10

        # Iterate from 2 to n
        for _ in range(2, n + 1):
            current_count = [0] * 10
            # Calculate the number of ways to reach each digit
            for digit in range(10):
                for move in knight_moves[digit]:
                    current_count[digit] = (current_count[digit] + previous_count[move]) % MOD
            previous_count = current_count

        # Sum the ways to reach each digit for length n
        return sum(previous_count) % MOD