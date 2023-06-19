class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)

        if k == 0 or (k == 1 and nums[0] == val):
            return 0
        indx = [x for x in range(len(nums)) if nums[x] == val]
        
        for i, x in enumerate(indx):
            nums.append(nums.pop(x - i))
        return k-len(indx)
                
        
                
                
            