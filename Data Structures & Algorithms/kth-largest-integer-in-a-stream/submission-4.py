from heapq import *

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapify(nums)
        self.heap = nums
        while len(self.heap) > self.k:
            heappop(self.heap)
    
    def add(self, n: int):
        heappush(self.heap, n)
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]

    
    def rebalance(self):
        while len(self.heap) > self.k:
            heappop(self.heap)
