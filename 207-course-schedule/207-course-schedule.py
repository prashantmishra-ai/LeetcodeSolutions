class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0]* numCourses
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            degree[prerequisite[0]]+=1
        queue = deque()
        for i in range(numCourses):
            if degree[i]==0:
                queue.append(i)
        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1
            for neighbor in adj[node]:
                degree[neighbor]-=1
                if degree[neighbor]==0:
                    queue.append(neighbor)
        return nodesVisited == numCourses