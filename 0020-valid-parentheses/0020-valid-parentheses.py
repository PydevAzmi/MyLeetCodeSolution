class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = ["(", "{", "["]
        close = [")", "}", "]"]
        valid_li = []
        for sympol in s:
            if sympol in open:
                valid_li.append(sympol)
            else:
                if valid_li:
                    idx = close.index(sympol)
                    if open[idx] == valid_li[-1]:
                        valid_li.pop()
                    else:
                        return False
                else:
                        return False
        if len(valid_li) != 0:
            return False
        else:
            return True
