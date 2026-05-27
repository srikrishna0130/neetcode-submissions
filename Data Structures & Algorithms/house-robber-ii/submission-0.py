class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # include 0
        cost = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                cost[i] = nums[i]
                continue
            if i == 1:
                cost[i] = max(nums[0], nums[1])
                continue
            
            # don't include n
            if i == len(nums) - 1:
                cost[i] = cost[i-1]
                continue

            cost[i] = max(cost[i-1], cost[i-2] + nums[i])
        
        # dont' include 0
        cost_n = [0]*len(nums)
        for i in range(1, len(nums)):
            if i == 1:
                cost_n[i] = nums[i]
                continue
            
            cost_n[i] = max(cost_n[i-1], cost_n[i-2] + nums[i])
        
        print(cost, cost_n)
        
        return max(cost[-1], cost_n[-1])


