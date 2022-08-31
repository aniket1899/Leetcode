# from heapq import heapify, heappop
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # solution 2
        N = len(nums)
        total = N*(N+1)//2
        
        return total - sum(nums)
        
        
        # solution 1
#         heapify(nums)
        
#         i = 0
#         while nums:
#             num = heappop(nums)
#             if i != num:
#                 return i
            
#             i += 1
            
#         return i