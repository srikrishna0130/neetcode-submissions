from _heapq import heapify
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        
        curr_path = []
        # adj is guareenteed to follow atleast one valid flight path
        def dfs(node):
            while adj[node]:
                dst = adj[node].pop()
                dfs(dst)
            
            curr_path.append(node)
        
        dfs("JFK")
        
        return curr_path[::-1]

        


