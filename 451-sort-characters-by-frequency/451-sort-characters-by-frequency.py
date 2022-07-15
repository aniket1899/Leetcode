
from collections import Counter, defaultdict
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        # ctr = OrderedDict(ctr)
        sortq = [(-v, k) for k, v in ctr.items()]
        heapq.heapify(sortq)
        res = ''
        print(sortq)
        while sortq:
            f, ch = heapq.heappop(sortq)
            # print(f, ch)
            res =  res + ch*(-f) 
        
        return res