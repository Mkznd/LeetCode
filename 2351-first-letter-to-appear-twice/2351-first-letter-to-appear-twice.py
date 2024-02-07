from collections import defaultdict
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a = set()
        for i in s:
            if i in a:
                return i
            else:
                a.add(i)