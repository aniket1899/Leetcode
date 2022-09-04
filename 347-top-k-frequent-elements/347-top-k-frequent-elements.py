from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        kfreq = []
        ctrhq = [(-val, key) for key, val in ctr.items()]
        heapify(ctrhq)
        
        for _ in range(k):
            _, key = heappop(ctrhq)
            kfreq.append(key)
            
        return kfreq