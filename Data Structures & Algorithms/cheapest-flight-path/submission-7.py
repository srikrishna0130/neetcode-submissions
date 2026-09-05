"""
will try the bellmand ford algo with a queue over here 

we're maintaining an array which maintains the shortest distance to reach each node at each iteration from the src node
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, cost in flights:
            adj[s].append([d, cost])
        
        min_distances = [10**6+1]*n
        min_distances[src] = 0
        bfs = deque([(src, 0, 0)])

        while bfs:
            city, cost, stops = bfs.popleft()
            if stops > k:
                break
            
            for nei, nei_cost in adj[city]:
                if min_distances[nei] > cost + nei_cost:
                    min_distances[nei] = cost + nei_cost
                    bfs.append((nei, cost + nei_cost, stops + 1))
            
        return -1 if min_distances[dst] == 1000001 else min_distances[dst]
       