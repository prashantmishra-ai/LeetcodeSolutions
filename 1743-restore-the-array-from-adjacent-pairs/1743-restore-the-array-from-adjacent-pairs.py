from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
# Create a graph where each number points to its adjacent numbers

        graph = defaultdict(list)

        for u, v in adjacentPairs:

            graph[u].append(v)

            graph[v].append(u)



        # Find the start of the array (it will only have one adjacent)

        start = None

        for key, val in graph.items():

            if len(val) == 1:

                start = key

                break



        # Reconstruct the array

        nums = [start]

        while len(nums) < len(adjacentPairs) + 1:

            next_element = graph[nums[-1]][0]

            # Remove the link to avoid going back in the next iteration

            graph[nums[-1]].remove(next_element)

            graph[next_element].remove(nums[-1])

            nums.append(next_element)



        return nums


