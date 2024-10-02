class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x) < 2 ** 31 - 1:
            if x>=0:
                result = int("".join([s for s in str(x)[::-1]]))
            else:
                result = int("".join([s for s in str(x)[:0:-1]]))*-1
            return result if abs(result) <= 2 ** 31 - 1 else 0
        return 0