class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
            # Step 1: Initialize the count list
        count = [0] * n

        # Step 2: Update the count list
        for road in roads:
            count[road[0]] += 1
            count[road[1]] += 1

        # Step 3: Initialize max_rank to 0
        max_rank = 0

        # Step 4: Iterate over all pairs of cities
        for i in range(n):
            for j in range(i+1, n):
                # Compute the network rank for cities i and j
                rank = count[i] + count[j]
                if [i, j] in roads or [j, i] in roads:
                    rank -= 1
                # Update max_rank
                max_rank = max(max_rank, rank)

        # Step 5: Return max_rank
        return max_rank