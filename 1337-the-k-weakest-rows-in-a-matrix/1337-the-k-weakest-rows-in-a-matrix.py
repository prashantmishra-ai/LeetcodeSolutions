class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [(sum(row), i) for i, row in enumerate(mat)]

        # Sort the rows based on the number of soldiers and then by the row index
        sorted_rows = sorted(soldiers)

        # Return the first k row indices
        return [row[1] for row in sorted_rows[:k]]