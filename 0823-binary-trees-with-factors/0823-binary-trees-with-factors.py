
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Convert arr into a set for O(1) lookups
        nums = set(arr)
        # A memoization table to store intermediate results
        memo = {}
        MOD = 10**9 + 7
        # Recursive helper function
        def countTrees(root):
            # If the result for this root is already computed, return it
            if root in memo:
                return memo[root]
            total = 1  # This accounts for the tree where `root` is the only node
            for num in nums:
                # Check if it's a valid left child and the division result is also in the set (right child)
                if num < root and root % num == 0 and root // num in nums:
                    total += countTrees(num) * countTrees(root // num)
                    total %= MOD  # Take modulo to avoid overflow
            memo[root] = total  # Store the result in the memoization table
            return total

        # Compute the result for each number in arr
        return sum(countTrees(num) for num in arr) % MOD
