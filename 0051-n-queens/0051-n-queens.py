class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row,col):
            for prev_row in range(row):
                if board[prev_row]==col or board[prev_row]-prev_row==col-row or board[prev_row]+prev_row == col+row:
                    return False
            return True
        def place_queen(n,row):
            if row==n:
                result.append(board[:])
                return
            for col in range(n):
                if is_not_under_attack(row,col):
                    board[row]=col
                    place_queen(n,row+1)
                    board[row]=0
        def board_to_result(board):
            res = []
            for row in board:
                res.append("."*row+'Q'+'.'*(n-row-1))
            return res
        result = []
        board = [0]*n
        place_queen(n,0)
        return [board_to_result(b) for b in result]