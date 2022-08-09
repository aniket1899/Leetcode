class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        length = len(nums)
        i=0
        while i < length:
            while nums[i] == val and i < length:
                nums[i], nums[length-1] = nums[length-1], nums[i]
                length -= 1
                
            i += 1
        
        return length