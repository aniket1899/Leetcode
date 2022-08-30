from collections import defaultdict

class Solution:
    def solution_1(self, nums: List[int]) -> bool:
        
        ctr = defaultdict(int)
        for num in nums:
            if ctr[num] == 1:
                return True
            ctr[num] += 1
            
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        return self.solution_1(nums)