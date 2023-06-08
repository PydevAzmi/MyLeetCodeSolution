class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count_1 = 0        
        count_n = 0

        if nums[0] == 1 and nums[-1] == n:
            return 0
        else :
            for i, num in enumerate(nums):
                if num == 1 :
                    if nums.index(n) < i :
                        count_1 += i
                    else:
                        count_1 = i
                elif num == n:
                     if i < nums.index(1) :
                        count_n += (n-1)-i
                        count_1 -= 1
                     else:
                        count_n = (n-1)-i
            return count_n + count_1
        