from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ctr = Counter(nums)
        target = len(nums)//2
        for key, val in ctr.items():
            if val > target:
                return key
        
        return None