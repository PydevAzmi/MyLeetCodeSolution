class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result = [None] * len(s)
        for i, letter in enumerate(s):
            result[indices[i]] =  letter
        return "".join(result)