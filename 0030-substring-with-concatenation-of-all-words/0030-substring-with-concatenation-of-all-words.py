class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter

        wordBag = Counter(words)  # Counter for the words array
        wordLen, numWord = len(words[0]), len(words)
        totalLen = wordLen * numWord  # total length of all words
        res = []

        for i in range(wordLen):  # i is the offset
            left = i
            right = i
            currCounter = Counter()

            while right + wordLen <= len(s):
                w = s[right:right + wordLen]
                right += wordLen
                currCounter[w] += 1

                while currCounter[w] > wordBag[w]:
                    left_w = s[left:left+wordLen]
                    left += wordLen
                    currCounter[left_w] -= 1

                if right - left == totalLen:
                    res.append(left)
                    
        return res
