# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []

        dfs = [(root, float('-inf'))]
        good_nodes = 0

        while dfs:
            node, max_val = dfs.pop()

            if node.val >= max_val:
                good_nodes += 1
                max_val = node.val
            
            if node and node.left:
                dfs.append((node.left, max_val))
            if node and node.right:
                dfs.append((node.right, max_val))
        
        return good_nodes


        