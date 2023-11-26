class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        height = [[0] * n for _ in range(m)]

        # Building the height matrix
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == 0:
                    height[i][j] = 0
                else:
                    height[i][j] = height[i - 1][j] + 1 if i > 0 else 1

        max_area = 0

        # Finding the largest submatrix for each row
        for i in range(m):
            # Sorting the row in non-increasing order
            sorted_height = sorted(height[i], reverse=True)
            for j in range(n):
                # Calculating the area of submatrix with height sorted_height[j]
                max_area = max(max_area, sorted_height[j] * (j + 1))

        return max_area
