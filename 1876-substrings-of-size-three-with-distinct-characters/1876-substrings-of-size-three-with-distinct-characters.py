class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)-2):
            t = s[i:i+3]
            res+=len(t) == len(set(t))
        return res