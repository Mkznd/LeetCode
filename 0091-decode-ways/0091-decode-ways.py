class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [0 for _ in range(n+1)]
        nums = {i for i in range(10, 27)}
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            one_digit = int(s[i-1])
            two_digit = int(s[i-2:i])
            
            if one_digit >= 1:
                dp[i] = dp[i-1]
            if two_digit in nums:
                dp[i] += dp[i-2]
                
        return dp[n]
            
            