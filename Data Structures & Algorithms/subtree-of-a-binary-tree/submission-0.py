# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        dfs = [root]
        while dfs:
            curr = dfs.pop()
            if self.isSameTree(curr, subRoot):
              return True

            if curr.left:
                dfs.append(curr.left)
            
            if curr.right:
                dfs.append(curr.right)
        
        return False

    def isSameTree(self, s, t) -> bool:
        if s == None and t == None:
            return True
        if s == None or t == None and s != t:
            return False
        
        left = self.isSameTree(s.left, t.left)
        right = self.isSameTree(s.right, t.right)

        return left and right and s.val == t.val
            
            