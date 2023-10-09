class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        search = []
        for i in range(0,len(nums)):
            if target == nums[i]:
                search.append(i)
        if len(search)==0:
            search.append(-1)
            search.append(-1)
        elif len(search)==1:
            search = search*2
        return [search[0],search[-1]]