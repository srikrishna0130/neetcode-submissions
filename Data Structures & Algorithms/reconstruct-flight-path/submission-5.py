class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s, d in tickets:
            adj[s].append(d)
        
        for src in adj:
            adj[src].sort()

        visited_paths = set()
        curr_path = ["JFK"]

        def dfs(node):
            if len(curr_path) == len(tickets) + 1:
                return True

            neis = adj[node]
            if not neis:
                return False
                
            for i, nei in enumerate(neis):
                curr_path.append(nei)
                adj[node].pop(i)
                if dfs(nei):
                    return True
                else:
                    adj[node].insert(i, nei)
                    curr_path.pop()

        dfs("JFK")
        return curr_path