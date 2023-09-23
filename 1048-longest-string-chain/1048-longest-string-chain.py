class Solution(object):
    def longestStrChain(self, words):
        # Sort words based on their length
        words.sort(key=len)

        # Dictionary to keep track of the longest word chain for each word
        dp = {}

        longest_chain = 0

        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                # Try removing each character to get a possible predecessor
                prev_word = word[:i] + word[i+1:]
                if prev_word in dp:
                    # Update the word chain length for the current word
                    dp[word] = max(dp[word], dp[prev_word] + 1)
            # Update the longest word chain found so far
            longest_chain = max(longest_chain, dp[word])

        return longest_chain