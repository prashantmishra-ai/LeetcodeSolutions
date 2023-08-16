class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(" ").split(" ")
        print(s)
        return len(s[-1])