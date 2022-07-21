from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
#         nums.sort()
#         i = 0
#         res = []
#         while i+1 < len(nums):
#             if nums[i] == nums[i+1]:
#                 i += 2
#             else:
#                 # print(i)
#                 res.append(nums[i])
#                 i += 1
                
#         if 1 == len(res):
#             res.append(nums[-1])
         
        res = []
        ctr = Counter(nums)
        for key, val in ctr.items():
            if val == 1:
                res.append(key)
                
        return res
        
        