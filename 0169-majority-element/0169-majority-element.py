class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        empty_dic = {}
        for i in nums:
            if i in empty_dic:
                empty_dic[i]+=1
            else:
                empty_dic[i]=1
        return max(zip(empty_dic.values(),empty_dic.keys()))[1]
            