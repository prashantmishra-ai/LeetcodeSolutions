class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0.0] * k for k in range(1, 101)]
        glasses[0][0] = poured
        for r in range(min(99, query_row + 1)):
            for c in range(r + 1):
                q = (glasses[r][c] - 1.0) / 2.0
                if q > 0:
                    glasses[r + 1][c] += q
                    glasses[r + 1][c + 1] += q
        return min(1, glasses[query_row][query_glass])