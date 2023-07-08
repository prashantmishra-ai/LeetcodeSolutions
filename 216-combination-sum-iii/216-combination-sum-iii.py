class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start,curr_sum,curr_combination):
            if curr_sum == n and len(curr_combination)==k:
                result.append(curr_combination[:])
                return
            if curr_sum>n or len(curr_combination)>k:
                return
            for i in range(start,10):
                curr_combination.append(i)
                backtrack(i+1,curr_sum+i,curr_combination)
                curr_combination.pop()
        result = []
        backtrack(1,0,[])
        return result