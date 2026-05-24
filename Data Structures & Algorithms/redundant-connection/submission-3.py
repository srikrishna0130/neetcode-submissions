from collections import defaultdict
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        path_list = []
        path_set = set()
        cycle_nodes = set()
        
        def dfs(curr, parent):
            if curr in path_set:
                # Cycle detected. Extract only the nodes within the cycle loop.
                idx = path_list.index(curr)
                for node in path_list[idx:]:
                    cycle_nodes.add(node)
                return True
                
            path_list.append(curr)
            path_set.add(curr)
            
            for neighbor in adj[curr]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, curr):
                    return True
                    
            # Backtrack
            path_list.pop()
            path_set.remove(curr)
            return False
            
        # The graph is connected; a single DFS execution will locate the cycle.
        dfs(1, -1)
        
        # Scan in reverse to return the last edge forming the cycle
        for u, v in reversed(edges):
            if u in cycle_nodes and v in cycle_nodes:
                return [u, v]
        
        return []