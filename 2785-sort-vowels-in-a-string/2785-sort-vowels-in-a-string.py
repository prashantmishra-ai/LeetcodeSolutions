class Solution:
    def sortVowels(self, s: str) -> str:
        # Define vowels
        vowels = 'aeiouAEIOU'
        # Create a list of vowels in the string sorted by their ASCII values
        sorted_vowels = sorted([c for c in s if c in vowels])
        # Rebuild the string with sorted vowels
        result = []
        vowel_index = 0
        for c in s:
            if c in vowels:
                result.append(sorted_vowels[vowel_index])
                vowel_index += 1
            else:
                result.append(c)
        return ''.join(result)
