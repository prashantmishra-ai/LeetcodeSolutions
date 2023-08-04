class Solution(object):
    def findSubstring(self, s, words):
        from collections import Counter
        wordBag = Counter(words)
        wordLen, numWord = len(words[0]), len(words)
        totalLen = wordLen * numWord 
        res = []
        for i in range(len(s) - totalLen + 1):
            wordSeen = [s[i+j*wordLen:i+j*wordLen+wordLen] for j in range(numWord)]
            if Counter(wordSeen) == wordBag:
                res.append(i)
        return res
