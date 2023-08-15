class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path,remaining_nums):
            if not remaining_nums:
                res.append(path[:])
                return
            seen = set()
            for i,num in enumerate(remaining_nums):
                if num in seen:
                    continue
                seen.add(num)
                backtrack(path+[num],remaining_nums[:i]+remaining_nums[i+1:])
        res = []
        backtrack([],nums)
        return res
    