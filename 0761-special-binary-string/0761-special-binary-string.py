class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        specials = []
        ones,zeros = 0,0
        start = 0
        for i,c in enumerate(s):
            if c=='1':
                ones+=1
            else:
                zeros+=1
            if ones==zeros:
                specials.append("1"+ self.makeLargestSpecial(s[start+1:i])+"0")
                start = i+1
        return "".join(sorted(specials,reverse=True))