class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
                # Phase 1: Detecting the cycle using Floyd's Tortoise and Hare
        tortoise, hare = nums[0], nums[nums[0]]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

        # Phase 2: Find the start of the cycle (duplicate number)
        hare = 0
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]

        return hare
