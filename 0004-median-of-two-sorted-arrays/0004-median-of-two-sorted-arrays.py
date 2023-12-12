class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        lenth = 0
        for i, x in enumerate(nums1):
            if x == nums1[-1]:
                lenth = i 
        if lenth % 2 != 0:
            return (nums1[int(lenth/2)] + nums1[int((lenth+1)/2)] )/2
        else: 
            return nums1[int((lenth+1)/2)]