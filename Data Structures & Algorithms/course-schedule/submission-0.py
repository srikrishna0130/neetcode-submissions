class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        current_path = set()
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[b].append(a)
        
        def dfs(current):
            next_courses = adj[current]

            for nc in next_courses:
                if nc in current_path:
                    return False
                current_path.add(nc)
                if not dfs(nc):
                    return False
                current_path.remove(nc)
            
            return True


        for i in range(numCourses):
            while i not in visited:
                current_path.add(i)
                visited.add(i)
                if not dfs(i):
                    return False
                current_path.remove(i)
        
        return True