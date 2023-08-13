class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start,target,comb,res):
            if target == 0:
                res.append(list(comb))
                return
            if target<0:
                return
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                backtrack(i,target-candidates[i],comb,res)
                comb.pop()
        res = []
        backtrack(0,target,[],res)
        return res