
class DisjointUnion:
    parents = [] 

    def __init__(self, n) -> None:
        # keep parents assigned to self
        self.parents = [i for i in range(n)]
    
    # finds the topmoost parent of this node,
    # and then updates it's parent with this topmost parent as well
    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        
        return self.parents[node]

    
    def union(self, a, b):
        # we'll always merge a to b here
        # we're pointing root of set b to point to a
        self.parents[self.parents[b]] = self.find(a)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskals
        # start with the edges array from least weights
        # keep adding it and if there is any cycle, discard that edge
        # keep doing it till all distinct points are covered.
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([weight, i, j])

        edges.sort()

        disj = DisjointUnion(len(points))
        min_weight = 0

        for w, p1, p2 in edges:
            if disj.find(p1) != disj.find(p2):
                min_weight += w
                disj.union(p1, p2)

        return min_weight