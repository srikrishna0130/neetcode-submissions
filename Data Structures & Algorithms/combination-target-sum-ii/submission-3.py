class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(index, subset, curr_sum):
            if curr_sum > target:
                return
            
            if curr_sum == target:
                result.append(subset)
                return
            
            if index > len(candidates) - 1:
                return
            
            # select curr index
            dfs(index+1, subset + [candidates[index]], curr_sum + candidates[index])
            
            # don't select curr index by ignoring duplicates
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index+1, subset, curr_sum)

        
        dfs(0, [], 0)
        return result