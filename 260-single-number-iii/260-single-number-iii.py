class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        i = 0
        res = []
        while i+1 < len(nums):
            if nums[i] == nums[i+1]:
                i += 2
            else:
                # print(i)
                res.append(nums[i])
                i += 1
                
        if 1 == len(res):
            res.append(nums[-1])
            
        return res
        
        