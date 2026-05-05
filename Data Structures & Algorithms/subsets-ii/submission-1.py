class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def subsets(i, curr):
            if i > len(nums) - 1:
                result.append(curr.copy())
                return
            
            curr.append(nums[i])
            subsets(i+1, curr)
            curr.pop()

            # skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            subsets(i+1, curr)
        
        subsets(0, [])

        return result