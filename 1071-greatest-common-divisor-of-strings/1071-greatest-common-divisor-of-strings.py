class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        max_s = ""
        for i in range(1,len(str1)+1):
            if len(str1)%i!=0 or len(str2)%i!=0:
                continue
            
            s = str1[:i]
            print(s)
            if s*(len(str1)//i) != str1 or s*(len(str2)//i) != str2: continue
            
            if len(max_s) < len(s):
                max_s = s
        return max_s