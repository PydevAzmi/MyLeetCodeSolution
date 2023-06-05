class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        longest_common = ""
        if len(strs) == 0:
            return longest_common
        min_len = len(min(strs))
        for st_idx in range(min_len):
            for s in strs:
                if strs[0][st_idx] != s[st_idx]:
                    return longest_common
            longest_common += strs[0][st_idx]

        return longest_common



            