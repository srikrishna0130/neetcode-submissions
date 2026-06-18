class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            dist = - (x**2 + y**2)
            heapq.heappush(maxheap, [dist, [x, y]])

            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        res = []
        while maxheap:
            res.append(heapq.heappop(maxheap)[1])
        
        return res
        
        