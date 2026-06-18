class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.heap = nums
    
    def add(self, num: int):
        heapq.heappush(self.heap, num)
        return heapq.nlargest(self.k, self.heap)[-1]