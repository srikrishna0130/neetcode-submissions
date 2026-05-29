class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        # Unused variable removed for memory optimization
        # numToLetter = defaultdict() ...

        dp = [0] * len(s)
        
        for i in range(len(s)):
            if i == 0:
                dp[i] = 1
                continue
            
            # 1. Single digit evaluation
            if s[i] != '0':
                dp[i] = dp[i-1]
            
            # 2. Two-digit merge evaluation
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                if i == 1:
                    # If we are at index 1, the "previous state" before the merge is simply 1
                    dp[i] += 1
                else:
                    # Add the total number of paths that existed before this 2-digit merge
                    dp[i] += dp[i-2]

            # 3. Dead end trap
            if dp[i] == 0:
                return 0
            
        return dp[-1]