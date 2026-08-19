import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prims algorithm
        # start with node 0; and add all it's edges to min-heap
        # select the min edge which is not in MST and continue till
        # all nodes are added
        visited = set()
        total_cost = 0
        min_heap = [[0, 0]]

        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            total_cost += cost
            
            if len(visited) == len(points):
                return total_cost
            
            # add edges of that node
            for p in range(len(points)):
                if p not in visited:
                    x1, y1 = points[node][0], points[node][1] 
                    x2, y2 = points[p][0], points[p][1] 
                    cost = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, [cost, p])
        
        return total_cost

