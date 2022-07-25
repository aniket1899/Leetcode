class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # prev = nums[0]
        ranges = []
        
        i = 0
        
        while i < len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i+=1
            if start == nums[i]:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + '->' + str(nums[i]))
            i+=1
        
        return ranges