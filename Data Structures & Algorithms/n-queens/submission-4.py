class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]

        if n == 2:
            return []
        
        if n == 3:
            return []
        
        # curr_board = [['.']*n]*n
        curr_board = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        def dfs(row):
            if row == n:
                # print("result", curr_board)
                copy = ["".join(row) for row in curr_board]
                result.append(copy)
                return
            
            for col in range(n):
                # print("each iter", row, col, curr_board)
                if self.isValidPosition(row, col, curr_board):
                    curr_board[row][col] = 'Q'
                    dfs(row+1)
                    curr_board[row][col] = '.'
        
        dfs(0)
        # print(result)
        return result

    
    def isValidPosition(self, i, j, board):
        # check if the current piece colludes with a Q?
        n = len(board)

        for a in range(n):
            # straight
            if board[a][j] == 'Q' or board[i][a] == 'Q':
                return False
        
        # check across 4 diagonals
        dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        for d in dirs:
            x, y = i + d[0], j + d[1]
            while 0 <= x < n and 0 <= y < n:
                if board[x][y] == 'Q':
                    return False
                x = x + d[0]
                y = y + d[1]

        return True
