class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L = 0
        R = 0
        res = 0
        
        for i in s:
            if i =="L":
                L+=1
            else:
                R+=1
            res+=L == R
        return res