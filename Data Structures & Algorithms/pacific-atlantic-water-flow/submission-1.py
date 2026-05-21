class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pqueue = deque()
        p = set()
        aqueue = deque()
        a = set()

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # ROWS
        for c in range(COLS):
            if (0, c) not in p:
                pqueue.append((0, c))
                p.add((0, c))
            
            if (ROWS - 1, c) not in a:
                aqueue.append((ROWS - 1, c))
                a.add((ROWS - 1, c))

        # COLS
        for r in range(ROWS):
            if (r, 0) not in p:
                pqueue.append((r, 0))
                p.add((r, 0))

            if (r, COLS - 1) not in a:
                aqueue.append((r, COLS - 1))
                a.add((r, COLS - 1))
        
        def bfs(q, visit):
            while q:
                r, c = q.popleft()

                for dx, dy in dirs:
                    x = r + dx
                    y = c + dy
                    if ((x, y) not in visit) and (0 <= x < ROWS and 0 <= y < COLS) and heights[x][y] >= heights[r][c]:
                        q.append((x, y))
                        visit.add((x, y))

        bfs(pqueue, p)
        bfs(aqueue, a)
        common = p.intersection(a)
        return list(common)
        













