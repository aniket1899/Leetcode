class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n)
        dp[0] = 1
        dp[1] = 1
        i=0
        while i < n-1:
            if i+2 < n:
                dp[i+2] = dp[i] 
            if i+1 < n:
                dp[i+1] += dp[i]           
            i += 1
            
        # print(dp)
        return dp[-1]