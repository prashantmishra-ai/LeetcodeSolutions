class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = {}

        # Iterate over the matrix to populate the dictionary.
        # The key is the sum of the indices (i+j) which represents each diagonal.
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(nums[i][j])

        # Output array
        result = []

        # Iterate over the diagonals in order and append them to the result.
        # Each diagonal's elements are added in reverse order because they're read bottom-up.
        for key in sorted(diagonals.keys()):
            result.extend(diagonals[key][::-1])

        return result