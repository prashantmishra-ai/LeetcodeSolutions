class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        This function takes an array of numbers, nums, and two arrays of range queries, l and r. It returns a list of
        booleans indicating whether each subarray can be rearranged to form an arithmetic sequence.
        """
        def isArithmetic(arr):
            """
            Helper function to check if a given array can be rearranged into an arithmetic sequence.
            """
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True

        result = []
        for i in range(len(l)):
            # Extract the subarray based on the current range query
            subarray = nums[l[i]:r[i] + 1]
            # Check if this subarray can be rearranged into an arithmetic sequence
            result.append(isArithmetic(subarray))

        return result