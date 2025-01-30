function sortArray(nums: number[]): number[] {
    const maxDigit = mostDigits(nums);
    for (let i=0 ; i < maxDigit; i++){
        const bucket= Array.from({length: 10}, () => [] as number[]);
        for(let j=0; j< nums.length; j++){
            const digit = getDigit(nums[j], i)
            bucket[digit].push(nums[j])
        }   
        nums = ([] as number[]).concat(...bucket)
    }
    return Signed(nums)
};

function getDigitCount(num:number): number{
    if (num === 0) {
        return 1
    }
    return Math.floor(Math.log10(Math.abs(num)))+1 
}


function getDigit(num:number, i:number): number{
    return Math.floor(Math.abs(num)/ Math.pow(10, i)) % 10;
}

function mostDigits(nums: number[]):number {
    let max = 0;
    for (let num of nums){
        let count = getDigitCount(num)
        if (count > max){
            max = count;
        }
    }
    return max;
}

function Signed(nums: number[]): number[]{
    let signed = nums.filter(num => num < 0);
    signed.sort((a,b) => a-b);
    let unsigned = nums.filter(num => num >= 0);
    return signed.concat(unsigned);
}