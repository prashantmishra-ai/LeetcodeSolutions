class Solution:
    def isNumber(self, s: str) -> bool:
            # Check if the string s is a valid integer.
        def isInteger(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()

        # Check if the string s is a valid decimal number.
        def isDecimal(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            if s.count('.') > 1:
                return False
            # Split string by the dot and validate both parts.
            parts = s.split('.')
            if len(parts) == 1:
                return parts[0].isdigit()
            if not parts[0] and not parts[1]:
                return False
            if parts[0] and not parts[0].isdigit():
                return False
            if parts[1] and not parts[1].isdigit():
                return False
            return True

        # Split the string by 'e' or 'E' and validate each part.
        if 'e' in s or 'E' in s:
            parts = s.split('e') if 'e' in s else s.split('E')
            if len(parts) != 2:
                return False
            return (isDecimal(parts[0]) or isInteger(parts[0])) and isInteger(parts[1])
        return isDecimal(s) or isInteger(s)
