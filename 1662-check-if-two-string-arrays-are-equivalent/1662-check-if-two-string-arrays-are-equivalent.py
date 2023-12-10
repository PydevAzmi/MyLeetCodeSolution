class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ex1, ex2 = "".join(word1), "".join(word2)
        return ex1 == ex2        
        