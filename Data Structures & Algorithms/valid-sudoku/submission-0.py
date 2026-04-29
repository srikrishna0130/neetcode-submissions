class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows valid

        rows = board
        columns = [list(column) for column in zip(*board)]

        grids3x3 = []
        for i in range(0,9,3):
            grids = [list(i) for i in zip(*board[i:i+3])]

            for j in range(0,9,3):
                grids3x3.append(grids[j:j+3])
    
        for row in rows:
            if (not self.isInputValid(row)):
                return False
        
        for column in columns:
            if(not self.isInputValid(column)):
                return False
    
        # flatten grids
        for grid in grids3x3:
            flattened = sum(grid, [])
            if (not self.isInputValid(flattened)):
                return False
        
        print('asdf')
        return True


    def isInputValid(self, inp: List[str]) -> bool:
        counts = [0]*10

        for i in inp:
            if i == '.':
                continue
            
            if (counts[int(i)] != 0):
                return False
            else:
                counts[int(i)] = 1
        return True
        