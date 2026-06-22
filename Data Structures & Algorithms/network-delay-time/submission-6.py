class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        visited = set()

        for t in times:
            adj[t[0]].append([t[2], t[1]])
        
        minheap = []
        heapq.heappush(minheap, [0, k])

        weight = 0
        while minheap:
            w1, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            weight = w1

            for w2, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minheap, [w1+w2, nei])
        
        if len(visited) != n:
            return -1

        return weight