/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  const nums = nums1.slice(0, m).concat(nums2.slice(0, n));
  for (let i = 0; i < m+n; i++) {
    for (let j = 0; j < m+n - i - 1; j++) {
      if (nums[j] > nums[j + 1]) {
        const temp = nums[j];
        nums[j] = nums[j + 1];
        nums[j + 1] = temp;
      }
    }
  }
 nums1.splice(0, m+n, ...nums);
};