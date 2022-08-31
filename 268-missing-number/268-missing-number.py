from heapq import heapify, heappop
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        heapify(nums)
        
        i = 0
        while nums:
            num = heappop(nums)
            if i != num:
                return i
            
            i += 1
            
        return i