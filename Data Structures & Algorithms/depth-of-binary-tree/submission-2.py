# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        bfs = deque()
        bfs.append([root, 1])
        max_height = 1

        while bfs:
            curr = bfs.popleft()
            max_height = max(max_height, curr[1])
            if curr[0].left :
                bfs.append([curr[0].left, max_height + 1])

            if curr[0].right :
                bfs.append([curr[0].right, max_height + 1])

        return max_height