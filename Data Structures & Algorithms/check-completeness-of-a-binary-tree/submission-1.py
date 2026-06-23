# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = deque()
        bfs.append(root)
        
        while bfs:
            node = bfs.popleft()
            if node:
                bfs.append(node.left)
                bfs.append(node.right)
            else:
                while bfs:
                    if bfs.popleft():
                        return False
        
        return True
        