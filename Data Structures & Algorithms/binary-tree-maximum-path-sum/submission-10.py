# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        length = float("-inf")
        def bfs(node):
            nonlocal length
            if not node:
                return 0
            left = bfs(node.left)
            right = bfs(node.right)
            length = max(length, node.val + max(0, left+right, left, right))
            return node.val + max(0, left, right)
        
        bfs(root)
        return length

        