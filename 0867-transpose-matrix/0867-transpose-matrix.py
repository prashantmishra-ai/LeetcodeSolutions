class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = list(zip(*matrix))
        # Converting tuples to lists
        return [list(row) for row in transposed]