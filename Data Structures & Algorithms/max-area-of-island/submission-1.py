class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        curr_len = 0
        max_len = -1
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            nonlocal curr_len
            if not (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1):
                return
            
            grid[r][c] = 0
            curr_len = curr_len + 1
            for d in dirs:
                x = r + d[0]
                y = c + d[1]
                dfs(x, y)
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
                # reset curr len after dfs
                max_len = max(max_len, curr_len)
                curr_len = 0
            
        return max_len