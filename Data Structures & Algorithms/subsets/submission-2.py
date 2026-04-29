class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        dfs = [[]]

        for i in nums:
            for subset in dfs:
                s = subset.copy()
                s.append(i)
                dfs = dfs + [s]        
        return dfs