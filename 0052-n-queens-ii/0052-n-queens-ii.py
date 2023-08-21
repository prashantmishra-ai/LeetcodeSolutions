class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def is_valid(row, col):
        # Check current column, diagonal, and anti-diagonal
            return col not in columns and row - col not in diagonals and row + col not in anti_diagonals

        def backtrack(row):
            # If we reach the last row, we found a valid placement
            if row == n:
                return 1
            total_solutions = 0
            for col in range(n):
                if is_valid(row, col):
                    # Place queen and mark the attacked paths
                    columns.add(col)
                    diagonals.add(row - col)
                    anti_diagonals.add(row + col)
                    # Move on to the next row
                    total_solutions += backtrack(row + 1)
                    # Remove queen and unmark the attacked paths (backtrack)
                    columns.remove(col)
                    diagonals.remove(row - col)
                    anti_diagonals.remove(row + col)
            return total_solutions

        columns = set()
        diagonals = set()
        anti_diagonals = set()

        return backtrack(0)
