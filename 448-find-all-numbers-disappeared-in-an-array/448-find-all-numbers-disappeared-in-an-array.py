class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # sol 1
        # max_num = len(nums)
        # res = list(set(range(1, max_num+1)) - set(nums))
        # return res 
        
        max_num = len(nums)
        nums = set(nums)
        noShow = []
        for i in range(1, max_num+1):
            if i not in nums:
                noShow.append(i)
                
        return noShow
        
        