class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        n = len(nums)
        min_values = [0] * n
        min_values[0] = nums[0]
        # Step 1: Compute the min_values array
        for i in range(1, n):
            min_values[i] = min(min_values[i - 1], nums[i])
        # Step 2: Initialize a stack
        stack = []
        # Step 3: Iterate from right to left
        for j in range(n - 1, -1, -1):
            if nums[j] > min_values[j]:
                # Step 4: Pop elements from stack that are not candidates for nums[k]
                while stack and stack[-1] <= min_values[j]:
                    stack.pop()
                # Step 5: Check if we found a 132 pattern
                if stack and stack[-1] < nums[j]:
                    return True
                # Step 6: Push current element into stack
                stack.append(nums[j])
        # If loop ends, no 132 pattern found
        return False