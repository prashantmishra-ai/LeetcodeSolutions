class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        maxRequests = 0
        def backtrack(start,currRequests):
            nonlocal maxRequests
            if start == len(requests):
                buildingEmployees = [0]*n
                for i, (fromBuilding,toBuilding) in enumerate(requests):
                    if currRequests[i] == '1':
                        buildingEmployees[fromBuilding]-=1
                        buildingEmployees[toBuilding]+=1
                if all(employees == 0 for employees in buildingEmployees):
                    maxRequests = max(maxRequests,currRequests.count('1'))
                return
            currRequests += '1'
            backtrack(start+1,currRequests)
            currRequests = currRequests[:-1]
            currRequests += '0'
            backtrack(start+1,currRequests)
            currRequests = currRequests[:-1]
        backtrack(0,'')
        return maxRequests