class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
                
        last_idx = {}
        for idx, num in enumerate(nums):
            if num in last_idx and abs(idx-last_idx[num]) <= k:
                return True
            last_idx[num] = idx
        return False