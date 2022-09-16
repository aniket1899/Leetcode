class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return nums.index(max(nums))
        def isPeak(idx):
            return idx if nums[idx]>nums[idx-1] and nums[idx]>nums[idx+1] else False
                
        def findThePeak(l, h):
            if l==h:
                return isPeak(l)
            
            
            mid = (l + h)//2
            # if isPeak(nums, mid):
            #     return mid
            
            return findThePeak(l, mid) or findThePeak(mid+1, h)
        
        peak =  findThePeak(1, len(nums)-2)
        if peak: return peak
        # else:
        if nums[0]>=nums[-1]:
            return 0
        else:
            return len(nums)-1
                
            
        
        
        