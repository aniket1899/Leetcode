class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        max_num = len(nums)
        
        res = list(set(range(1, max_num+1)) - set(nums))
        return res 
        