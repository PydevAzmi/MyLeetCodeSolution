class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        max_equal = 0    
        for row in matrix:
            flipped = [1 - x for x in row]
            count = sum(
                1
                for xrow in matrix
                if xrow == row or xrow == flipped)
            max_equal = max(count, max_equal)
            
        return max_equal
                    
        
        