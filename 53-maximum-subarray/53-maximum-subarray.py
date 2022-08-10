class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = nums
        ATMax = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            ATMax = max(ATMax, dp[i])
        
        return ATMax