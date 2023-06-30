class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        sign = 1
        i =0
        if s[0] in ['-','+']:
            if s[0] == '-':
                sign = -1
            i+=1
        result = 0
        while i<len(s) and s[i].isdigit():
            digit = int(s[i])
            result = result*10 + digit
            if sign == 1 and result >= 2**31 - 1:
                return 2**31 - 1
            elif sign == -1 and result >=2**31:
                return -2**31
            i+=1
        return sign*result
        
        