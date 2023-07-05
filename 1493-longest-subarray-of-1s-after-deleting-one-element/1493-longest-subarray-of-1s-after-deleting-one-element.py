class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flag = 0
        for i in nums:
            if i==0:
                flag = 1
        if flag == 0:
            return len(nums)-1
        maxlen = 0
        currlen = 0
        prevlen = 0
        for num in nums:
            if num==1:
                currlen+=1
            else:
                maxlen = max(maxlen,currlen+prevlen,prevlen)
                prevlen = currlen
                currlen = 0
        maxlen = max(maxlen,currlen+prevlen,prevlen)
        return maxlen