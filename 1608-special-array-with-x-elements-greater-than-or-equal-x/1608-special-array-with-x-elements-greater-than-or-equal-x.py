class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        # nums = list(set(nums))
        nums.sort()
        
        prev = 0
        for idx, num in enumerate(nums):
            rem = len(nums)-idx
            res = num
            while res > prev:
                if res == rem:
                    print(num, res, rem)
                    return res
                res -= 1
            prev = num
            
        return -1
            