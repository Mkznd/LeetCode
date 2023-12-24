class Solution:
    def minOperations(self, s: str) -> int:
        a = 0
        b = 0
        for i in range(len(s)):
            if i%2 == 0:
                if s[i]=="0":
                    a += 1
                else:
                    b+=1
            else:
                if s[i] == "0":
                    b += 1
                else:
                    a+=1
        return min(a,b)