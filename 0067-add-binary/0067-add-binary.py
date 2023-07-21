class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        re = bin(int(a,2) + int(b,2))
        return re[re.index('b')+1:]