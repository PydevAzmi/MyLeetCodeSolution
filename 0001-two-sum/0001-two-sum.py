class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            for x, num2 in enumerate(nums):
                if i != x and num1 + num2 == target:
                    return [i, x]
        