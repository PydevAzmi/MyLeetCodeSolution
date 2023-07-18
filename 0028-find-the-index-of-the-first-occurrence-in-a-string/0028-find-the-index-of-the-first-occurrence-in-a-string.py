class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        scope = []
        lenth = len(needle)
        for start in range(len(haystack)-lenth+1):
            scope.append(haystack[start:lenth])
            lenth += 1
        index = [i for i, x in enumerate(scope) if x == needle]
        if index :
            return index[0]
        else :
            return -1