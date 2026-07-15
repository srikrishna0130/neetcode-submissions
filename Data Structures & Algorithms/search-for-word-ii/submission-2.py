from collections import defaultdict

class TrieNode:
    def __init__(self, val) -> None:
        self.val = val
        self.children = defaultdict(TrieNode)
        self.end_of_word = False
        pass

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")
        pass
    
    def insert(self, word: str) -> None:
        top = self.root
        for w in word:
            if w not in top.children:
                top.children[w] = TrieNode(w)
            
            top = top.children[w]
        
        top.end_of_word = True
    
    def search(self, word: str) -> bool:
        top = self.root
        for w in word:
            if w not in top.children:
                return [False, False]
            top = top.children[w]

        # we also return prefix matches here
        return [top.end_of_word, True]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)
            print(word, trie.search(word))
        
        ROWS = len(board)
        COLS = len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visited = set()
        current_word = ""
        current_visited = set()
        found_words = set()

        def dfs(row, col):
            nonlocal current_word

            if not (0 <= row < ROWS and 0 <= col < COLS):
                return
            
            if (row, col) in current_visited:
                return
            
            current_word += board[row][col]
            current_visited.add((row, col))
            is_end, is_prefix = trie.search(current_word)
            # print(current_word, is_end, is_prefix)
            if is_end:
                # dont return here 2 words can be substrings of each other
                # example back and backend
                found_words.add(current_word)
            if not is_prefix:
                current_visited.remove((row, col))
                current_word = current_word[:-1]
                return
            
            for dx, dy in dirs:
                x = row + dx
                y = col + dy
                dfs(x, y)
            
            # backtrack here
            current_visited.remove((row, col))
            current_word = current_word[:-1]

        for row in range(ROWS):
            for col in range(COLS):
                current_visited = set()
                current_word = ""
                dfs(row, col)
        
        return list(found_words)
                



