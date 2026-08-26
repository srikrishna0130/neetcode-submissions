class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # try the binary search variant with dfs for this one

        # get the max value in the grid
        LEN = len(grid)
        max_val = 0
        for i in range(LEN):
            for j in range(LEN):
                max_val = max(grid[i][j], max_val)

        l, r = 0, max_val
        print(l, r)

        while l < r:
            m = (l + r)//2
            is_reachable = self.isReachable(grid, m)
            print(l, r, m, is_reachable)
            if is_reachable:
                r = m
            else:
                l = m + 1
        
        return l

    def isReachable(self, grid: List[List[int]], time: int) -> bool:
        if grid[0][0] > time:
            return False

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        LEN = len(grid)

        dfs = [[0, 0]]
        visited = set()

        while dfs:
            r, c = dfs.pop()
            if r == c and r == LEN - 1:
                return True

            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            for dx, dy in dirs:
                x = r + dx
                y = c + dy
                if x >= 0 and x < LEN and y >= 0 and y < LEN and grid[x][y] <= time:
                    dfs.append([x, y])

        return False