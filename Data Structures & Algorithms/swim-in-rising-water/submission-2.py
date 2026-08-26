class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        LEN = len(grid)

        heap = [[grid[0][0], 0, 0]]
        heapq.heapify(heap)
        visited = set()

        while heap:
            cost, x, y = heapq.heappop(heap)
            if x == LEN - 1 and y == LEN - 1:
                return cost
            
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            
            for dx, dy in dirs:
                r = x + dx
                c = y + dy

                if r >= 0 and r < LEN and c >= 0 and c < LEN:
                    next_cost = max(grid[r][c], cost)
                    heapq.heappush(heap, [next_cost, r, c])