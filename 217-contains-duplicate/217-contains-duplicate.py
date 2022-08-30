from collections import defaultdict

class Solution:
    def solution_1(self, nums: List[int]) -> bool:
        
        ctr = defaultdict(int)
        for num in nums:
            if ctr[num] == 1:
                return True
            ctr[num] += 1
            
        return False
    def solution_2(self, nums: List[int]) -> bool:
        nums.sort()
        prev = nums[0]
        for num in nums[1:]:
            if num == prev:
                return True
            prev = num
        
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        return self.solution_2(nums)