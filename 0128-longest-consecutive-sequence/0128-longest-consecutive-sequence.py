class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        best = 1
        if not nums:
            return 0
        for i in a:
            if i-1 in a:
                continue
            t = i+1
            c = 1
            while t in a:
                c+=1
                t+=1
            if best < c:
                best = c
        return best