class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        crr = 0
        MOD = 10**9 + 7
        for i in range(len(s)):
            if i==0 or s[i]==s[i-1]:
                crr+=1
            else:
                crr = 1
            res = (res+crr)%MOD
        return res