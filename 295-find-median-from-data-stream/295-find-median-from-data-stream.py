from heapq import heappop, heappush
class MedianFinder:

    def __init__(self):
        # self.nums = []
        # self.minheap =  [] # negative values
        # self.maxheap = []
        
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        
        if len(self.maxHeap) == len(self.minHeap):
            heappush(self.minHeap, -num)
            heappush(self.maxHeap, -heappop(self.minHeap) )
        else:
            heappush(self.maxHeap, num)
            heappush(self.minHeap, -heappop(self.maxHeap))
#         if len(self.minheap) == len(self.maxheap):
#             if not self.maxheap or self.maxheap[0] <= num:
#                 heappush(self.maxheap, num)
#             else:
#                 heappush(self.maxheap, -heappop(self.minheap))
#                 heappush(self.minheap, -num)
                
#         else:
#             if self.maxheap[0] <= num:
#                 heappush(self.minheap, -heappop(self.maxheap))
#                 heappush(self.maxheap, num)
#             else:
#                 heappush(self.minheap, -num)
        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.maxHeap[0] - self.minHeap[0])/2
        else:
            return float(self.maxHeap[0])
        
        
        # if len(self.upperHeap) == len(self.lowerHeap):
        #     upperMin = + self.upperHeap[0]
        #     lowerMax = - self.lowerHeap[0]
        #     return ( float(upperMin) + float(lowerMax) ) / 2.0
        # else:
        #     return float(self.upperHeap[0])
        # print(self.minheap ,self.maxheap)
        # if len(self.maxheap) == len(self.minheap) + 1:
        #     return float(self.maxheap[0])
        # # elif len(self.maxheap) == len(self.minheap):
        # else:
        #     return (self.maxheap[0]-self.minheap[-1]) / 2
            
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()