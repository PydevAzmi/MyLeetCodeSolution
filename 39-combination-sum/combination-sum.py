class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]] 
        """
        ans = []
        def backtrack(curr_comb, start):
            if sum(curr_comb) ==  target:
                ans.append(curr_comb[:])
            elif sum(curr_comb) > target:
                return
            for i in range(start,len(candidates)):
                curr_comb.append(candidates[i])
                backtrack(curr_comb, i)
                curr_comb.pop()
        
        backtrack([],0)
        return ans