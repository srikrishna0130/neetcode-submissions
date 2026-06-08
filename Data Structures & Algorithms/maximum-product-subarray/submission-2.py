class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], nums[0]]
        res = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i], dp[i-1][1]*nums[i], dp[i-1][0]*nums[i])
            dp[i][1] = min(nums[i], dp[i-1][1]*nums[i], dp[i-1][0]*nums[i])
            res = max(res, dp[i][0])
        
        return res