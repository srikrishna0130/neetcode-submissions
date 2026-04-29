# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int: 
        goodNodes = 0
        if root == None:
            return 0

        def dfs(node, currMax):
            nonlocal goodNodes
            if node == None:
                return
            
            if node.val >= currMax:
                currMax = node.val
                goodNodes = goodNodes + 1

            dfs(node.left, currMax)
            dfs(node.right, currMax)
        
        dfs(root, root.val)
        return goodNodes