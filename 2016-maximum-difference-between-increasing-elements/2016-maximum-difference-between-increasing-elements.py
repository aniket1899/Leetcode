class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        low = nums[0]
        maxdiff = -1
        for i in nums[1:]:
            if i < low:
                low = i
            elif  i - low > maxdiff:
                maxdiff = i - low
                
        return -1 if not maxdiff else maxdiff
               