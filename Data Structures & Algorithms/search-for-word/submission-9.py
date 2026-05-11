class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # check from all positions in the board
        # start dfs with the matching position
        # build word sequentially, iterate over the word length
            # dfs(i+1, curr_word)
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(a, b, curr_word):
            if board[a][b] == "":
                return False
            if curr_word == word:
                return True
            if len(curr_word) == len(word):
                return False
            
            for d in dirs:
                i = a + d[0]
                j = b + d[1]
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    # print("next word", board[i][j], i, j, "curr word", curr_word)
                    if board[i][j] == word[len(curr_word)]:
                        temp = board[a][b]
                        board[a][b] = ""
                        res = dfs(i, j, curr_word + board[i][j])
                        board[a][b] = temp
                        if res:
                            return True

        # iterate over all positions in the board

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    # temp = 
                    result = dfs(i, j, word[0])
                    if result:
                        return True

        return False       