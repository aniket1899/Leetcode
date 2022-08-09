class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [1, 1]+ [0] * (n-2)
        
        for i in range(n):
            if i+1 < n:
                dp[i+1] += dp[i]
            if i+2 < n:
                dp[i+2] += dp[i]
            
            # print(dp)
        
        return dp[-1]