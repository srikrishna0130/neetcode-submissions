class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        visited = set()

        def dfs(subset):
            if tuple(subset) in visited:
                return
            else:
                visited.add(tuple(subset))

            if sum(subset) > target:
                return
            
            if sum(subset) == target:
                result.add(tuple(subset))
                return

            for num in nums:
                dfs(sorted(subset + [num]))

        dfs([])

        return [list(l) for l in result]   
