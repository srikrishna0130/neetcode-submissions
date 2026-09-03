class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i][j] = min(dp[i-1][j-k] + 1 (k is value of each coin, and j is the target, i is array till ith coin))

        dp = [[amount+1]*(amount+1) for _ in range(len(coins)+1)]

        # target 0 always requires 0 coins
        for i in range(len(coins) + 1):
            dp[i][0] = 0

        # dp[0][x] is always zero
        # dp[x][0] is also always zero
        # fill the dp state here
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                # not take ith coin case
                dp[i][j] = dp[i-1][j]

                # take the ith coin case if applicable
                if j >= coins[i-1]:
                    dp[i][j] = min(dp[i][j], dp[i][j-coins[i-1]] + 1)
        
        return -1 if dp[len(coins)][amount] == amount + 1 else dp[len(coins)][amount]
        