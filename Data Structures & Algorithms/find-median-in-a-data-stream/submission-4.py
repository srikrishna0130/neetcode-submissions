class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)

        if self.minheap and (-self.maxheap[0] > self.minheap[0]):
            ele = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -ele)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            ele = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -ele)
        elif len(self.minheap) > len(self.maxheap):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)
        
    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (self.minheap[0] + -self.maxheap[0])/2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return -self.maxheap[0]
        
        