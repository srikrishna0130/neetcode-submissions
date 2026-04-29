class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for i in nums:
            subset = []
            for res in result:
                subset.append(res + [i])
            result = result + subset
        
        return result