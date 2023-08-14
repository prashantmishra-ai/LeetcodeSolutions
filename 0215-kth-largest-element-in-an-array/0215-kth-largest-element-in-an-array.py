class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot_index = random.randint(0,len(nums)-1)
        low,equal,high = [],[],[]
        pivot = nums[pivot_index]
        for num in nums:
            if num<pivot:
                low.append(num)
            elif num==pivot:
                equal.append(num)
            else:
                high.append(num)
        if k<=len(high):
            return self.findKthLargest(high,k)
        elif k<=len(high)+len(equal):
            return equal[0]
        else:
            return self.findKthLargest(low,k-len(high)-len(equal))