class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)

        # Target subarray sum
        target = total - x
        if target < 0:
            return -1

        # If the total sum is equal to x, then return n (all elements are used)
        if total == x:
            return n

        left_ptr = 0
        curr_sum = 0
        max_len_subarray = -1

        for right_ptr in range(n):
            curr_sum += nums[right_ptr]

            while curr_sum > target and left_ptr <= right_ptr:
                curr_sum -= nums[left_ptr]
                left_ptr += 1

            if curr_sum == target:
                max_len_subarray = max(max_len_subarray, right_ptr - left_ptr + 1)

        # If no subarray is found, return -1
        if max_len_subarray == -1:
            return -1

        return n - max_len_subarray