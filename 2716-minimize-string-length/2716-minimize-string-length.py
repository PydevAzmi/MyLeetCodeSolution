import string
class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        lower = []
        for letter in s:
            if letter not in lower:
                lower.append(letter)
        return len(lower)
        