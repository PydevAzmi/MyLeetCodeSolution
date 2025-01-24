/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    const { length } = nums;
    for (let i=0; i< length; i++){
        for (let j=0; j< length -i-1; j++){
            if(nums[j] > nums[j+1]){
            const temp = nums[j];
            nums[j] = nums[j+1];
            nums[j+1] = temp;
            }
        }
    }
};