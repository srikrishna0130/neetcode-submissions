# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        bst = root

        small = min(p.val, q.val)
        large = max(p.val, q.val)

        while bst:
            if small < bst.val and large < bst.val:
                bst = bst.left
            elif small > bst.val and large > bst.val:
                bst = bst.right
            else:
                return bst
