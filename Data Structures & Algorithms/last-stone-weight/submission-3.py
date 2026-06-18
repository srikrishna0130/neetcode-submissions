class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = len(stones)
        if l == 1:
            return stones[0]
            
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            first = heapq.heappop(maxheap)
            second = heapq.heappop(maxheap)
            heapq.heappush(maxheap, -abs(first - second))
        
        return -maxheap[0]


    