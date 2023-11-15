class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort the array
        arr.sort()

        # Initialize the first element to be 1
        arr[0] = 1

        # Iterate through the array from the second element
        for i in range(1, len(arr)):
            # If the current element is greater than the previous element + 1, reduce it
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1

        # The maximum value will be the last element in the array
        return arr[-1]
