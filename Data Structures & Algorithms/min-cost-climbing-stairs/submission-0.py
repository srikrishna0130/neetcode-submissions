class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [-1]*(len(cost)+1)

        for i in range(len(cost)+1):
            if i <= 1:
                mincost[i] = 0
                continue
            
            mincost[i] = min(cost[i-1] + mincost[i-1], cost[i-2] + mincost[i-2])
        
        # print(cost, mincost)
        return mincost[-1]