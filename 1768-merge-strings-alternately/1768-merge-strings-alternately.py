class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res+=word1[i]+word2[i]
            
        res+=word1[len(word2):] if len(word2)<len(word1) else word2[len(word1):]
        return res