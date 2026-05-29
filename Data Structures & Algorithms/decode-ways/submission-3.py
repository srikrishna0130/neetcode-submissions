class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        numToLetter = defaultdict()

        for i in range(ord("A"), ord("Z")+1):
            numToLetter[str(i-ord("A")+1)] = chr(i)
        
        dp = [0]*len(s)
        for i in range(len(s)):
            if i == 0:
                dp[i] = 1
                continue
            
            if s[i-1] == s[i] == '0':
                return 0

            # previous set with the current letter
            if s[i] != '0':
                dp[i] = dp[i-1]
            # condition to check if there can be a merge possible
            if '10' <= s[i-1]+s[i] <= '26':
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]

            if dp[i] == 0:
                return 0
                
        return dp[-1]
            
            

