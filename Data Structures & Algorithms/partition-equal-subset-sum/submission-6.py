class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        t = sum(nums) // 2

        dp = [[False]*(t+1) for _ in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(0, t+1):
                if i == len(nums) - 1:
                    dp[i][j] = nums[i] == j
                    continue
                
                if j == 0:
                    dp[i][j] = True
                    continue

                if nums[i] <= j:
                    dp[i][j] = dp[i+1][j] or dp[i+1][j-nums[i]]
                else:
                    dp[i][j] = dp[i+1][j]
                
        return dp[0][t]

