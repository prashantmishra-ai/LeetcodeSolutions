class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0

        # Iterate through the string to split into two parts
        for i in range(1, len(s)):
            # Split the string into left and right parts
            left, right = s[:i], s[i:]

            # Calculate the score for the current split
            score = left.count('0') + right.count('1')

            # Update the maximum score if necessary
            max_score = max(max_score, score)

        return max_score