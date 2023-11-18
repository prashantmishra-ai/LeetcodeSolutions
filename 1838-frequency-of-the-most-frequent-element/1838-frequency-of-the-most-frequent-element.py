class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, total, max_freq = 0, 0, 0

        for r in range(len(nums)):
            total += nums[r]

            # If the total sum + k is less than the current number * length of the window
            # it means we cannot make all elements in the window equal to nums[r]
            # so we shrink the window from left
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1

            # update max_freq with the size of the current window
            max_freq = max(max_freq, r - l + 1)

        return max_freq