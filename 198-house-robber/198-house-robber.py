import heapq as hq
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] + nums
        print(dp)
        print('--')
        for i in range(3, len(dp)):
            dp[i] = dp[i] + max(dp[i-2], dp[i-3])
            print(dp)
            print('--')
            
        return max(dp[-1], dp[-2])
        