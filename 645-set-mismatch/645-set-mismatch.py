from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # apsum = N*(N-1)//2
        diffsum = N*(N+1)//2 - sum(nums)
        
        ctr = Counter(nums)
        for key, val in ctr.items():
            if val == 2:
                return [key, key + diffsum]
        
        # nums.sort()
        # prev = num
        # for num