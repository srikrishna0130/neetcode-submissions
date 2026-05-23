class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        queue = deque()
        adj = defaultdict(list)
        indeg = [0]*numCourses

        for a, b in prerequisites: 
            adj[b].append(a)
            indeg[a] += 1

        total = 0
        def bfs():
            nonlocal total
            while queue:
                curr = queue.popleft()
                total += 1
                next_courses = adj[curr]
                order.append(curr)

                for nc in next_courses:
                    indeg[nc] = indeg[nc] - 1
                    if indeg[nc] == 0:
                        queue.append(nc)


        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
        
        bfs()

        if total == numCourses:
            return order
        else:
            return []