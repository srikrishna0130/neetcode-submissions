class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        unvisited = set(wordList)
        if beginWord in unvisited:
            unvisited.remove(beginWord)
        queue = deque()
        def bfs():
            while queue:
                start, count = queue.popleft()
                # print("start, count", start, count)
                if count > len(wordList):
                    return 0

                if start == endWord:
                    return count
                
                for word in list(unvisited):
                    # print("start", word, unvisited, self.editDistance(start, word))
                    if self.editDistance(start, word) == 1:
                        queue.append((word, count + 1))
                        unvisited.remove(word)
            return 0
        
        queue.append((beginWord, 1))
        return bfs()
    
    def editDistance(self, start, word):
        if start == word:
            return 0
        
        dist = 0
        for i in range(len(start)):
            if start[i] == word[i]:
                dist += 1
        
        return len(start) - dist 
            
            
