# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSameTree = True

        def dfs(p, q):
            nonlocal isSameTree
            if (p == None or q == None):
                if p != q:
                    isSameTree = False
                return

            if p.val != q.val:
                isSameTree = False
                return
            
            dfs(p.left, q.left)
            dfs(p.right, q.right)

            return

        dfs(p, q)
        return isSameTree        