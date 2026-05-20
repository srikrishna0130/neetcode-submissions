class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                # start bfs from rotten fruits
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
        
        def bfs():
            curr_step = 0
            while queue:
                r, c, step = queue.popleft()
                for dx, dy in dirs:
                    x = dx + r
                    y = dy + c
                    
                    if (0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 1):
                        grid[x][y] = -1
                        queue.append((x, y, step + 1))
                        curr_step = step + 1

            return curr_step
        
        steps = bfs()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return steps