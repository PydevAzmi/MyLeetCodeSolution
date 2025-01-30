function maximumGap(nums: number[]): number {
    if (nums.length < 2){return 0};
    const maxDigit = mostDigits(nums);
    for (let i=0 ; i < maxDigit; i++){
        const bucket= Array.from({length: 10}, () => [] as number[]);
        for(let j=0; j< nums.length; j++){
            const digit = getDigit(nums[j], i)
            bucket[digit].push(nums[j])
        }   
        nums = ([] as number[]).concat(...bucket)
    }
    return SignedDiffrence(nums);
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

function SignedDiffrence(nums: number[]): number{
    let max = 0;
    let signed = nums.filter(num => num < 0);
    let unsigned = nums.filter(num => num >= 0);
    const all = signed.concat(unsigned);
    for (let i=0; i< all.length ;i++){
        let diff = all[i+1]-all[i]
        if (diff > max){
            max = diff
        }
    }
    return max
}
