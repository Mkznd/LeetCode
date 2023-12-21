class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted([i[0] for i in points])
        res = []
        for i in range(len(x)-1):
            res.append(x[i+1]-x[i])
        return max(res)