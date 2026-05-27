class Solution:
    def rob(self, nums: List[int]) -> int:
        maxcost = [0]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                maxcost[i] = nums[i]
                continue
            
            if i == 1:
                maxcost[i] = max(nums[i], nums[i-1])
                continue
            
            maxcost[i] = max(maxcost[i-1], maxcost[i-2] + nums[i])
        
        return maxcost[-1]
        