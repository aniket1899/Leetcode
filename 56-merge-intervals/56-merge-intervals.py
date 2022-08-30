from heapq import heappush, heappop, heapify
from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # solution 1
#         heapify(intervals)
#         merged = deque([heappop(intervals)])
#         openInt = True
#         while intervals:
#             start, end = heappop(intervals)
#             if start <= merged[-1][1]:
#                 tmp = merged.pop()
#                 merged.append([tmp[0], max(tmp[1], end)])
#             else:
#                 merged.append([start, end])
                
#         return merged



        # solution 2

        intervals.sort()
        # print(intervals)
    
        merged = deque([intervals[0]])
        
        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:
                tmp = merged.pop()
                merged.append([tmp[0], max(tmp[1], interval[1])])
            else:
                merged.append(interval)
                
        return merged