# from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # solution 1
        # ctr = Counter(nums)
        
        # for num, val in ctr.items():
            # if val == 1:
                # return num
        # solution 2
        
        return sum(set(nums))*2 - sum(nums)
        