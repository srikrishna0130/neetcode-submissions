class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        indeg = [0]*numCourses
        q = deque()

        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        
        finish = 0
        def bfs():
            nonlocal finish
            while q:
                curr = q.popleft()
                next_courses = adj[curr]
                
                finish += 1
                for nc in next_courses:
                    indeg[nc] -= 1
                    if indeg[nc] == 0:
                        q.append(nc)

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
                visited.add(i)
        
        bfs()
        return finish == numCourses