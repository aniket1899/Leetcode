from heapq import heappush, heappop, heapify
from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapify(intervals)
        merged = deque([heappop(intervals)])
        openInt = True
        while intervals:
            start, end = heappop(intervals)
            if start <= merged[-1][1]:
                tmp = merged.pop()
                merged.append([tmp[0], max(tmp[1], end)])
            else:
                merged.append([start, end])
                
        return merged
                