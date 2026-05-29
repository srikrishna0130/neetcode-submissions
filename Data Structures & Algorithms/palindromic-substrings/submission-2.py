class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        res = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if (s[i] == s[j]) and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    res=res + 1
        return res