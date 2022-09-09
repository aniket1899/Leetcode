from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        
        for num, val in ctr.items():
            if val == 1:
                return num