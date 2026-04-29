class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [1]*len(nums)
        bwd = [1]*len(nums)
        res = [1]*len(nums)

        # define fwd sequence
        for i in range(0, len(nums)):
            if (i == 0):
                fwd[i] = 1
                continue

            fwd[i] = fwd[i-1]*nums[i-1]

        # define bwd sequence
        for i in range(len(nums) - 1, -1, -1):
            if (i == len(nums) - 1):
                bwd[i] = 1
                continue 

            bwd[i] = bwd[i+1]*nums[i+1]
        
        # res
        for i in range(0, len(nums)):
            res[i] = fwd[i]*bwd[i]
        
        return res
            
        