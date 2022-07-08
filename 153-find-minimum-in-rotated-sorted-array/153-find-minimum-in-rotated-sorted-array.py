class Solution:
    def findMin(self, nums: List[int]) -> int:
#         [ - - - - | - - - -]
#         [ 0 | 1 | 2 3 4 ]        
        
        if nums[0] <= nums[-1]:
            return nums[0]
        l , h = 0, len(nums)-1
        while l < h:
            if h-l <= 1:
                return min(nums[l:h+1])
            mid = (l + h)//2
            
            if nums[l] > nums[mid-1]:
                h = mid -1 
            elif nums[mid] > nums[h]:
                l = mid
            else:
                return nums[mid]
            
        return None