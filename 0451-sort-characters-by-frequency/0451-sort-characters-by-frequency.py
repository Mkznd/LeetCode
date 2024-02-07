from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        a = dict(Counter(s))
        return ''.join([i*a[i] for i in sorted(a.keys(), key=lambda x: a[x], reverse=True)])
            