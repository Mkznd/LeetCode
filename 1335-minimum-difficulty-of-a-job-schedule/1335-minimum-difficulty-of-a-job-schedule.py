class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        if sum(jobDifficulty) == 0:
            return 0
        
        @functools.cache
        def dfs(i, d, day_max):
            if i==len(jobDifficulty):
                return 0 if d==0 else inf
            if d==0:
                return inf
            
            day_max = max(day_max, jobDifficulty[i])
            
            res = min(
                dfs(i+1, d, day_max),
                day_max + dfs(i+1, d-1, -1)
            )
            
            return res
        
        return dfs(0, d, -1)
        
        