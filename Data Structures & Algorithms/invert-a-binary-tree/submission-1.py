# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dfs = []
        dfs.append(root)

        if root == None:
            return root

        while dfs:
            node = dfs.pop()
            if node.left:
                dfs.append(node.left)
            
            if node.right:
                dfs.append(node.right)
            
            node.left, node.right = node.right, node.left

        return root
        