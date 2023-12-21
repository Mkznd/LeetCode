from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(lambda: 0)
        res = []
        for i in nums:
            a[i]+=1
        return sorted(a, key=lambda x: a[x], reverse=True)[:k]
        
