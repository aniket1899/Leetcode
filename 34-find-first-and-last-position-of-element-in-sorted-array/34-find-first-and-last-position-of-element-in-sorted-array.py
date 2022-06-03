class Solution:
    def binarySearch(self, A, target):
        l, h = 0, len(A)-1
        
        while l<=h:
            mid = (l+h)//2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                l = mid+1
            else:
                h = mid-1
                
        return -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        idx = self.binarySearch(nums, target)
        
        
        res = [idx, idx]
        if idx == -1:
            return res
        
        flag = [False, False]
        N = len(nums)
        
        while True:
            if res[0]-1>= 0 and not flag[0] and nums[res[0]-1] == target:
                res[0] -= 1
            else: 
                flag[0] = True
            if res[1]+1 < N and not flag[1] and nums[res[1]+1] == target:
                res[1] += 1
            else: 
                flag[1] = True
                
            if flag[0] and flag[1]:
                break
        return res
        
        