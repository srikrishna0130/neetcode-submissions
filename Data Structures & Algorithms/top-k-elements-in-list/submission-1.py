class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hist = Counter(nums)

        heap = []
        for i, val in nums_hist.items():
            heapq.heappush(heap, (val, i))

            if (len(heap) > k):
                heapq.heappop(heap)

        print(heap)
        return [tup[1] for tup in heap]
        