class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_set = set(s)
        longest = s[0]
        for char in my_set:
            idxs = [idx for idx, i in enumerate(s) if i == char]
            for i in range(len(idxs)):
                for j in range(1,len(idxs)):
                    check = s[idxs[i]:idxs[j]+1]
                    if len(check) > len(longest):
                        if self.is_palindrom(check):
                            longest = s[idxs[i]:idxs[j]+1]  
        return longest

    def is_palindrom(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True