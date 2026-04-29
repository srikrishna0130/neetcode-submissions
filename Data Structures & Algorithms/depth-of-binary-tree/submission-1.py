# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        dfs = [[1, root]]
        max_height = 0

        while dfs:
            curr = dfs.pop()
            height = curr[0]
            max_height = max(max_height, height)
            if curr[1].left:
                dfs.append([height + 1, curr[1].left])
            if curr[1].right:
                dfs.append([height + 1, curr[1].right])
        
        return max_height