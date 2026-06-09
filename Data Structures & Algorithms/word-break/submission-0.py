class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = defaultdict(bool)

        def dfs(i):
            if i in visited:
                return visited[i]
            
            if i == len(s):
                return True
    
            
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    visited[j+1] = dfs(j+1)
                    if visited[j+1]:
                        return True
            
            return False
        
        return dfs(0)