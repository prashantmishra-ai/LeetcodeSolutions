class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(num, row, col):
            # Check row
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check column
            for i in range(9):
                if board[row][i] == num:
                    return False

            # Check 3x3 box
            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[i + startRow][j + startCol] == num:
                        return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(num, i, j):
                                board[i][j] = num
                                if solve():
                                    return True  # If next recursive call returns True, puzzle is solved
                                board[i][j] = "."
                        return False
            return True
        solve()