from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        a = defaultdict(lambda: 0)
        for i in s:
            a[i]+=1
        return ''.join([i*a[i] for i in sorted(a.keys(), key=lambda x: a[x], reverse=True)])
            