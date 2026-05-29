class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0, 0]
        dp = [ [0]*len(s) for _ in range(len(s)) ]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if (s[i] == s[j]) and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    a, b = res
                    if (b - a) < (j - i):
                        res = [i, j]
        i, j = res
        return s[i:j+1]