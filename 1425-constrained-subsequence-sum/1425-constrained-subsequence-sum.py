class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # Initialize a deque and a variable to store the result
        dq = deque()
        res = float('-inf')

        # Traverse the nums array
        for i, num in enumerate(nums):
            # If the deque is not empty, add the front number to the current number
            if dq:
                nums[i] += nums[dq[0]]

            # Update the result with the maximum value
            res = max(res, nums[i])

            # Maintain the deque to ensure numbers within are in decreasing order
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            # If the current number is non-negative, add its index to the deque
            if nums[i] > 0:
                dq.append(i)

            # Remove indices that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

        return res