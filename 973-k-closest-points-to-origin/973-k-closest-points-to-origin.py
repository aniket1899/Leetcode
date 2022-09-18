import heapq as hq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = [(x**2 + y**2, x, y) for x,y in points]
        hq.heapify(dist)
        kNearest = [None]*k
        
        for i in range(k):
            _, *tmp = heappop(dist)
            kNearest[i] = tmp
        
        return kNearest
            