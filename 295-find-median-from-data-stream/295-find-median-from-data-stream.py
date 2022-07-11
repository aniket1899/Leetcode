from heapq import heappop, heappush
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        
        if len(self.maxHeap) == len(self.minHeap):
            heappush(self.minHeap, -num)
            heappush(self.maxHeap, -heappop(self.minHeap) )
        else:
            heappush(self.maxHeap, num)
            heappush(self.minHeap, -heappop(self.maxHeap))
        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.maxHeap[0] - self.minHeap[0])/2
        else:
            return float(self.maxHeap[0])
        
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()