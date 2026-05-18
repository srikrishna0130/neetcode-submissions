"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        # clone graph by dfs
        oldToNew = {}

        def dfs(start):
            # return reference of the already visited node
            if start in oldToNew:
                return oldToNew[start]
            
            copy = Node(start.val)
            oldToNew[start] = copy
            
            for n in start.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node)

            
                            

            


                