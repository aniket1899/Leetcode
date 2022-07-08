from collections import defaultdict
# import numpy as np
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counts = defaultdict(int)
        res = set([])
        n3 = len(nums)//3
        
        for num in nums:
            # if counts[num] <= n3:
            counts[num] += 1
            if counts[num] > n3:
                res.add(num)
                
        return list(res)
                
        
        # unique, counts = np.unique(x, return_counts=True)
        