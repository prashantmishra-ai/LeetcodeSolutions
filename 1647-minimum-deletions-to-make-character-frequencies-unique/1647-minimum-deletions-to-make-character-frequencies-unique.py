class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter

        char_freq = Counter(s)  # Count frequency of each character

        freqs = list(char_freq.values())  # List of frequencies
        freqs.sort(reverse=True)

        deletions = 0  # Number of deletions required to make the string good

        # To keep track of what frequencies we have already seen
        seen_freqs = set()

        for freq in freqs:
            while freq in seen_freqs and freq > 0:  # If frequency is not unique, decrement it
                freq -= 1
                deletions += 1
            seen_freqs.add(freq)

        return deletions