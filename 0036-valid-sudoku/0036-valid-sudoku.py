class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(nums):
            nums = [n for n in nums if n != '.']
            return len(nums) == len(set(nums))
        # check rows
        for row in board:
            if not is_valid(row):
                return False
        # check columns
        for j in range(9):
            if not is_valid([board[i][j] for i in range(9)]):
                return False
        # check 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_valid([board[x][y] for x in range(i, i+3) for y in range(j, j+3)]):
                    return False
        return True