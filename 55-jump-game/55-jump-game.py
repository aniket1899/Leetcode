class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        target = len(nums)-1
        valid = [0] * (len(nums))
        
        # for i, n in enumerate(nums):
        #     if valid[i] == len(nums)-1 or n + i == len(nums)-1 :
        #         return True
        #     for nxt in range(1, n):
        #         if nxt+i >= len(nums):
        #             continue
        #         valid[nxt+i] = nums[nxt+i] + nxt+i
        
        valid[0] = 1
        for i, n in enumerate(nums):
            # print(valid)
            if (valid[i] and i + n == target) or valid[-1]:
                return True
            if valid[i] == 0: 
                continue
            
            valid[i+1:min(target+1, i+n+1)] = [1]*(min(target+1, i+n+1) - (i+1))
        return valid[-1] == 1
        
        
            
            