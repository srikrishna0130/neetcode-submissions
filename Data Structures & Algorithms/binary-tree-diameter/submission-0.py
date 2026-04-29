# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameterOfBinaryTreeVal = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        self.diameterOfBinaryTreeVal = 0
        self.maxDepth(root)
        return self.diameterOfBinaryTreeVal

    def maxDepth(self, root) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        depth = 1 + max(right, left)
        self.diameterOfBinaryTreeVal = max(self.diameterOfBinaryTreeVal, left+right)
        
        return depth
        
            
