class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
         # result = int("".join([s for s in str(x)[:0:-1]]))*-1
        """
        if abs(x) <= 2 ** 31 - 1:
            i = 1
            result = 0
            if x < 0:
                i = -1
            x = abs(x)
            while x > 0: 
                result = result * 10 + x % 10 
                x //= 10
            return result*i if abs(result) <= 2 ** 31 - 1 else 0
        return 0