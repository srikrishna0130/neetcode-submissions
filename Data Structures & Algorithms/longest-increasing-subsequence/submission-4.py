class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        visited = {}
        if len(nums) == 1:
            return 1
        
        def dfs(i):
            if i in visited:
                return visited[i]
            
            if i == (len(nums)-1):
                return 1
            
            m = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    m = max(m, 1 + dfs(j))
            
            visited[i] = m
            return m
    
        return max(dfs(i) for i in range(len(nums)))

            

        