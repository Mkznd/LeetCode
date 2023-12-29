class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<2:
            return 1
        
        pre,cur = 0,1
        for i in range(n):
            pre,cur = cur, pre+cur
        return cur
        
#         @functools.cache
#         def dfs(n):
#             if n == 0:
#                 return 1
#             if n < 0:
#                 return 0
            
#             return dfs(n-1) + dfs(n-2)
        
#         return dfs(n)
