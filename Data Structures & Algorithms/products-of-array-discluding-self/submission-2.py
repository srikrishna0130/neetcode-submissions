class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [None]*(len(nums))
        prev_prod = 1
        for i, val in enumerate(nums):
            prefix_prod[i] = prev_prod
            prev_prod = val * prev_prod
        
        sufix_prod = [None]*(len(nums))
        result = [None]*(len(nums))
        prev_prod = 1
        n = len(nums) - 1 
        for i, val in enumerate(reversed(nums)):
            sufix_prod[n - i] = prev_prod
            prev_prod = val * prev_prod
            result[n - i] = prefix_prod[n - i] * sufix_prod[n - i]
        
        print("prefix prod", prefix_prod)
        print("sufix prod", sufix_prod)
        return result