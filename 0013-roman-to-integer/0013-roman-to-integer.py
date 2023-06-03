class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        sum = 0
        for i in range(len(s)):
            value = roman_numerals[s[i]]
            if i+1 < len(s) and roman_numerals[s[i+1]] > value:
                sum -= value
            else: sum += value
        return sum