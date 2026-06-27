# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.preorder_idx = 0
        def dfs(l, r):
            nonlocal indices
            if l > r:
                return None
            
            mid = indices[preorder[self.preorder_idx]]
            curr = TreeNode(preorder[self.preorder_idx])
            self.preorder_idx = self.preorder_idx + 1

            curr.left = dfs(l, mid-1)
            curr.right = dfs(mid+1, r)

            return curr

        return dfs(0, len(inorder) - 1)