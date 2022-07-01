class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums = sorted(list(set(nums)))
        # print(nums)
        prev = nums[0]
        local = 1
        max_series = 1
        for num in nums[1:]:
            if num - prev == 1:
                local += 1
                max_series = max(max_series, local)
            else:
                local = 1
                
            prev = num
        
        return max_series