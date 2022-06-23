class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return 2*sum(set(nums)) - sum(nums)
        