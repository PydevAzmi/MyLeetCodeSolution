class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = ""
        for e in s:
            if e == " " and len(out) == 0:
                continue
            elif (e == "-" or e == "+") and len(out) == 0:
                out = e
                continue
            elif not e.isdigit():
                break
            elif e.isdigit():
                out += e
            else:
                break
        try:
            return max(-(1 << 31), min(int(out), (1 << 31) - 1))
        except :
            return 0