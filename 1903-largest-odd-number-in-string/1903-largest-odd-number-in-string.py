class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        Function to find the largest-valued odd integer that is a non-empty substring of num.
        """
        # Iterate over the string in reverse order
        for i in range(len(num) - 1, -1, -1):
            # Check if the current digit is odd
            if int(num[i]) % 2 != 0:
                # Return the substring from the beginning to the current index (inclusive)
                return num[:i + 1]
        # Return an empty string if no odd number is found
        return ""
