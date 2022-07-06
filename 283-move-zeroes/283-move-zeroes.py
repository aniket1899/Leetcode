class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countZeros = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                countZeros += 1
                
            else: 
                i+=1
        
        nums += [0]*countZeros
        return nums