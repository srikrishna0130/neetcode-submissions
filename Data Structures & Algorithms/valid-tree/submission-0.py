class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        visited = set()
        adj = {}

        # create adj list
        for e1, e2 in edges:
            if adj.get(e1, False):
                adj[e1].append(e2)
            else:
                adj[e1] = [e2]

            if adj.get(e2, False):
                adj[e2].append(e1)
            else:
                adj[e2] = [e1]

        print("adj", adj)
        def dfs(edge):
            print(edge, visited)
            if edge in visited:
                return
            
            visited.add(edge)
            neighbours = adj.get(edge, [])

            for e in neighbours:
                dfs(e)
        
        dfs(0)

        return len(visited) == n
