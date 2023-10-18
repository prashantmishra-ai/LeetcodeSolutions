class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Create an adjacency list for the directed graph
        adj_list = [[] for _ in range(n)]
        in_degree = [0] * n
        start_time = [0] * n

        # Create the graph and calculate in-degrees
        for u, v in relations:
            adj_list[u-1].append(v-1)
            in_degree[v-1] += 1

        # Add nodes with in-degree 0 to the queue
        queue = [i for i in range(n) if in_degree[i] == 0]

        while queue:
            course = queue.pop(0)
            end_time = start_time[course] + time[course]

            for next_course in adj_list[course]:
                in_degree[next_course] -= 1
                start_time[next_course] = max(start_time[next_course], end_time)
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # Calculate ending times of all courses and return the maximum value
        ending_times = [start_time[i] + time[i] for i in range(n)]
        return max(ending_times)