class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_steps = m+n-2
        down_steps = m-1
        unique = math.comb(total_steps,down_steps)
        return unique