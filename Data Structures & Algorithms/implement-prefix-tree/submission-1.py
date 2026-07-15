class Node:
    def __init__(self, value: str):
        self.value = value
        self.children = defaultdict(Node)
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = Node("")

    def insert(self, word: str):
        top = self.root
        i = 0
        while top and i < len(word):
            next = top.children
            if next and word[i] in next: 
                top = next[word[i]]
                i += 1
            else:
                break
        
        for j in range(i, len(word)):
            top.children[word[j]] = Node(word[j])
            top = top.children[word[j]]
        
        top.is_end = True
        
    def search(self, word: str) -> bool:
        top = self.root
        for i in word:
            if i in top.children:
                top = top.children[i]
            else:
                return False
        
        return top.is_end

    def startsWith(self, prefix: str) -> bool:
        top = self.root
        for i in prefix:
            if i in top.children:
                top = top.children[i]
            else:
                return False
        
        return True