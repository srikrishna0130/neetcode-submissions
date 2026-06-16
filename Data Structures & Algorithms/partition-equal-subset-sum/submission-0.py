class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        def dp(i, target):
            if i >= len(nums):
                return target == 0

            if target < 0:
                return False
            
            res = dp(i+1, target - nums[i]) or dp(i+1, target)
            return res
        
        return dp(0, sum(nums)//2)
        