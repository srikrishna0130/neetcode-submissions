from heapq import *

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > self.k:
            heappop(self.heap)
    
    def add(self, n: int):
        heappush(self.heap, n)
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]