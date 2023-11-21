class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        MOD = 10**9 + 7
        # We can transform the condition nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        # to nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        # This way we can use a hash map to count occurrences
        count = {}
        for num in nums:
            diff = num - rev(num)
            count[diff] = count.get(diff, 0) + 1

        # Count pairs
        result = 0
        for k in count:
            result += count[k] * (count[k] - 1) // 2
            result %= MOD

        return result