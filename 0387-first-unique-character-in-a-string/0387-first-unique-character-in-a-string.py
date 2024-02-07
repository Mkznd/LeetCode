from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = dict(Counter(s))
        a = {i: s.index(i) for i in counts.keys() if counts[i] == 1}
        return min([i for i in a.values()], default=-1)
