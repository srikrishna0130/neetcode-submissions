class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # do dfs on graph
        # and the returned value should be a set

        islands = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            grid[r][c] = "0"
            for d in dirs:
                x = r + d[0]
                y = c + d[1]

                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                    # mark as visited
                    # self.addToSet(x, y, islands)
                    dfs(x, y)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    # grid[r][c] = "0"
                    dfs(r, c)
                    islands += 1
        
        return islands
    
    def addToSet(self, r, c, islands):        
        notPresent = True
        for s in islands:
            if (r, c) in s:
                notPresent = False
        
        if notPresent:
            islands.append(set((r, c)))

        