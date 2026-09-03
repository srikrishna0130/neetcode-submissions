"""
making use of 1d dp here instead of 2d dp to define take and not take states

dp[target] -> what is the minimum no of coins required to reach target.
    this works because we can definitely define current state as a function of the previous state in the dp[i][target] method

dp[t] = min dp[t - c] where t >= c; this works because we can reach t from only these 
    particular states
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        
        return -1 if dp[amount] == amount + 1 else dp[amount]