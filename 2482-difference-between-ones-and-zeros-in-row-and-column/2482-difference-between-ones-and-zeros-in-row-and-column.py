class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # m = len(grid)
        # n = len(grid[0])
        # onesRow =[0]*m
        # onesCol =[0]*n
        # for i in range(0,m):
        #     for j in range(0,n):
        #         onesRow[i]+=grid[i][j]
        #         onesCol[j]+=grid[i][j]
        # diff =[[0]*n]*m
        # for i in range(m):
        #     for j in range(n):
        #         diff[i][j] = 2* onesRow[i]+2*onesCol[j]-n-m
        # return diff
        m = len(grid)
        n = len(grid[0])
        ones_row = [sum(row) for row in grid]
        zeros_row = [n - ones for ones in ones_row]
        ones_col = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        zeros_col = [m - ones for ones in ones_col]

        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]
        return diff
