class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lengths = {}
        for num in arr:
            prev_num = num-difference
            if prev_num in lengths:
                lengths[num] = lengths[prev_num]+1
            else:
                lengths[num] = 1
        return max(lengths.values())