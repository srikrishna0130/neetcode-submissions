class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            
            nei = adj[node]
            for nn in nei:
                dfs(nn)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count