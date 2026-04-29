# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = []

        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
            print(sorted_list, node.val)
            sorted_list.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return sorted_list[k-1]
