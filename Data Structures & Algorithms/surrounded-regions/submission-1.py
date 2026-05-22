class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        q = deque()
        ROWS, COLS = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]      

        def bfs():
            while q:
                r, c = q.popleft()

                for dx, dy in dirs:
                    x = dx + r
                    y = dy + c

                    if (0 <= x < ROWS and 0 <= y < COLS) and (x, y) not in visited and board[x][y] == 'O':
                        q.append((x, y))
                        visited.add((x, y))
        
        for r in range(ROWS):
            if board[r][0] == 'O':
                visited.add((r, 0))
            if board[r][COLS-1] == 'O':
                visited.add((r, COLS-1))

        for c in range(COLS):
            if board[0][c] == 'O':
                visited.add((0, c))
            if board[ROWS-1][c] == 'O':
                visited.add((ROWS-1, c))
        
        q = deque(visited)
        bfs()

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    board[r][c] = 'X'


        
