import numpy as np
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a = []
        for i in range(1, len(str(high))+1):
            for j in range(1,10):
                s = ""
                for k in range(i):
                    s+=str(j+k) if j+k < 10 else ''
                if int(s) in range(low, high+1):
                    a.append(int(s))
        return sorted(set(a))