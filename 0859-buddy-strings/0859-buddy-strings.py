class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            return len(set(s))<len(s)
        mismatches = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatches.append((s[i],goal[i]))
        if len(mismatches)==2:
            return mismatches[0] == mismatches[1][::-1]
        return False