class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L_min = prices[0]
        curr_max = 0

        for i in prices:
            if i < L_min:
                L_min = i
            
            curr = 0
            if (i > L_min):
                curr = i - L_min
                curr_max = max(curr, curr_max)
        
        return curr_max
        