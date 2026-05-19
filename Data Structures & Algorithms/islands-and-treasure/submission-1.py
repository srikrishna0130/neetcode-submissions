class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        INF = 2147483647

        def bfs():
            if not queue:
                return

            r, c, step = queue.popleft()            
            for dx, dy in dirs:
                x = dx + r
                y = dy + c
                #  if it's INF then it's not visited
                if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == INF:
                    grid[x][y] = 1 + grid[r][c]
                    queue.append((x, y, step + 1))
            bfs()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    # start bfs from all chests
                    queue.append((r, c, 0))
        
        bfs()

        return