class Solution:
    def largestGoodInteger(self, num: str) -> str:
        similar = ['999','888','777','666','555','444','333','222','111','000']
        myarr = []
        for i in similar:
            if i in num:
                myarr.append(i)
        if len(myarr)==0:
            return ""
        else:
            return str(max(myarr))