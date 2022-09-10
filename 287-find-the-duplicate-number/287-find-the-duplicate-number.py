class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        low = 1
        high = len(nums) - 1
        dup = (low+ high) // 2
        while low <= high:
            
            arb = (low+ high) // 2
            count = 0
            count = sum([x <= arb for x in nums])
            if count > arb:
                dup = arb
                high = arb - 1
            else:
                low = arb + 1
        return dup