class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            vol = self.calculate_vol(heights, l, r)
            max_vol = max(vol, max_vol)

            if (heights[l] <= heights[r]):
                l += 1
            elif (heights[l] > heights[r]):
                r -= 1
        
        return max_vol


    
    def calculate_vol(self, heights, l, r):
        return min(heights[l], heights[r]) * (r - l)
        