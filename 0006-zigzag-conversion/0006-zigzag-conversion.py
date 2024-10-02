class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        postion = self.generator(numRows)
        output = {i:"" for i in range(numRows)}
        for char in s:
            pos = next(postion)
            output[pos] += char
        return "".join(output.values())
    
    def generator(self, r):
        while True:
            for i in range(r):
                yield i
            for j in range(r-2,0,-1):
                yield j