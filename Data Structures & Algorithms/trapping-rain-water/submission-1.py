class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        L = [0]*len(height)
        R = [0]*len(height)

        # left max
        prev_val = 0
        for i, val in enumerate(height):
            if (i == 0):
                L[i] = 0
                prev_val = val
                continue
            
            L[i] = max(L[i-1], prev_val)
            prev_val = val

        # right max
        prev_val = 0
        for i, val in enumerate(reversed(height)):
            if (i == 0):
                R[n - i - 1] = 0
                prev_val = val
                continue
            
            R[n - i - 1] = max(R[n - i], prev_val)
            prev_val = val

        # calculate trapped rain at each bar
        vol = 0
        for i, val in enumerate(height):
            m = min(L[i], R[i])
            if val >= m:
                continue
            vol = vol + (m - val)
        
        return vol