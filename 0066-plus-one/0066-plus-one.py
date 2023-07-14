class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 1
        for i, x in enumerate(digits[::-1]):
            num += 10**i * x
        return [int(x) for x in str(num)]