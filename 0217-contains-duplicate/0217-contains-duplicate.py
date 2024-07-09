class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        repeted =set()
        for num in nums:
            if num not in repeted:
                repeted.add(num)
            else: 
                return True
            
        return False