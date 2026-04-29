class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        
        if curr == None:
            return False

        for char in word:
            if char not in curr.children:
                return False
                
            curr = curr.children[char]
        
        if curr.endOfWord:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        if curr == None:
            return False


        for char in prefix:
            if not curr.children.get(char, False):
                return False
                
            curr = curr.children.get(char)
        
        return True
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
