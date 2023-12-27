class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0

        i = 0
        while i < len(colors):
            if i + 1 < len(colors) and colors[i] == colors[i + 1]:
                max_time = neededTime[i]
                sum_time = neededTime[i]
                i += 1

                while i < len(colors) and colors[i] == colors[i - 1]:
                    sum_time += neededTime[i]
                    max_time = max(max_time, neededTime[i])
                    i += 1

                total_time += sum_time - max_time
            else:
                i += 1

        return total_time