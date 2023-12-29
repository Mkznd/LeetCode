class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n ==1:
            return [[1]]
        if n==2:
            return [[1], [1,1]]
        
        
        dp = [[0]*i for i in range(0, n+1)]
        dp[1] = [1]
        dp[2] = [1,1]
        
        for i in range(3, n+1):
            print(i)
            dp[i][0] = 1
            for j in range(1, i-1):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            dp[i][-1] = 1
        return dp[1:]