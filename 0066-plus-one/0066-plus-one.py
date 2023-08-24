class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total_sum = 0
        for i in range(len(digits)):
            total_sum+=digits[i]*(10**(len(digits)-i))
        total_sum//=10
        total_sum+=1
        output = []
        while total_sum>0:
            output.append(total_sum%10)
            total_sum//=10
        output.reverse()
        return output