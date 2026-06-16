class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        t = sum(nums) // 2
        
        memo = [[-1]*(t+1) for _ in range(len(nums))]
        
        def dp(i, target):
            if i >= len(nums):
                return target == 0

            if target < 0:
                return False
            
            if memo[i][target] != -1:
                return memo[i][target]
            
            memo[i][target] = dp(i+1, target - nums[i]) or dp(i+1, target)

            return memo[i][target]

        return dp(0, t)
        