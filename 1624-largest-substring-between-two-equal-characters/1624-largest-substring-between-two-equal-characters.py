class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}
        max_length = -1

        for i, char in enumerate(s):
            # If the character is seen for the first time, store its index
            if char not in first_occurrence:
                first_occurrence[char] = i
            else:
                # Calculate the length of substring excluding the two characters
                length = i - first_occurrence[char] - 1
                # Update the max_length if the current length is greater
                max_length = max(max_length, length)

        return max_length
