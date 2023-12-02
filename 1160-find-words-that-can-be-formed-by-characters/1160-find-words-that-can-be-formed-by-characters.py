class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_freq = {}
        for c in chars:
            if c in char_freq:
                char_freq[c] += 1
            else:
                char_freq[c] = 1

        total_length = 0

        for word in words:
            word_freq = {}
            for c in word:
                if c in word_freq:
                    word_freq[c] += 1
                else:
                    word_freq[c] = 1

            # Checking if the word can be formed
            can_form = True
            for c in word_freq:
                if c not in char_freq or word_freq[c] > char_freq[c]:
                    can_form = False
                    break

            # Adding the length of the word to total if it can be formed
            if can_form:
                total_length += len(word)

        return total_length