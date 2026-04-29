# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        def dfs(node, l , r) -> bool:
            if node == None:
                return True
            
            if l < node.val < r:
                return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)
            else:
                return False

        
        return dfs(root, float('-inf'), float('inf'))
            
            
        
        
        