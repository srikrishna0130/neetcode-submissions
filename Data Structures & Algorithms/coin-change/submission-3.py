class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque() 
        visited = set()

        def bfs():
            while q:
                target, num = q.popleft()
                if target == amount:
                    return num

                for c in coins:
                    if target + c <= amount and (target+c, num+1) not in visited:
                        q.append((target+c, num+1))
                        visited.add((target+c, num+1))
            
            return -1
        
        q.append((0, 0))
        visited.add((0, 0))
        return bfs()

