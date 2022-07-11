from heapq import heappop, heappush
class MedianFinder:

    def __init__(self):
        # self.nums = []
        # self.minheap =  [] # negative values
        # self.maxheap = []
        
        self.upperHeap = [float('inf')]
        self.lowerHeap = [float('inf')]
        

    def addNum(self, num: int) -> None:
        
        upperMin = + self.upperHeap[0]
        lowerMax = - self.lowerHeap[0]

        if num > upperMin or (lowerMax<=num<=upperMin and len(self.upperHeap)==len(self.lowerHeap)):
            heappush(self.upperHeap, num)
        else:
            heappush(self.lowerHeap, -num)

        # maintain the invariant that their lens are equal, or upper has 1 more than lower
        if len(self.upperHeap)-len(self.lowerHeap) > 1:
            heappush( self.lowerHeap, -heappop( self.upperHeap ) )
        elif len(self.lowerHeap) > len(self.upperHeap):
            heappush( self.upperHeap, -heappop( self.lowerHeap ) )
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
        if len(self.upperHeap) == len(self.lowerHeap):
            upperMin = + self.upperHeap[0]
            lowerMax = - self.lowerHeap[0]
            return ( float(upperMin) + float(lowerMax) ) / 2.0
        else:
            assert len(self.upperHeap) == len(self.lowerHeap) + 1
            return float(self.upperHeap[0])
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