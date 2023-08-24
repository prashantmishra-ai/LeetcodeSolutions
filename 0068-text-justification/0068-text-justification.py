class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        for word in words:
            # Check if adding the next word exceeds the width limit
            if num_of_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [word]
            num_of_letters += len(word)
        # For the last line, left-justify and add spaces to the right
        return res + [' '.join(cur).ljust(maxWidth, ' ')]
