class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = set(zip(set(s), [s.count(i) for i in set(s)]))
        b = set(zip(set(t), [t.count(i) for i in set(t)]))
        return a == b