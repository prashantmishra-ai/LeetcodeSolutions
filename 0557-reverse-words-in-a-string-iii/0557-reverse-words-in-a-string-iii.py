class Solution:
    def reverseWords(self, s: str) -> str:
        length = s.split(" ")
        for i in range(len(length)):
            length[i] = length[i][::-1]
        return " ".join(length)