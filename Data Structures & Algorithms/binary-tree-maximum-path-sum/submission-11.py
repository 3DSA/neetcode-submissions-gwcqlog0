# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        path = float("-inf") # this holds our max path sum
        def dfs(node):
            nonlocal path
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            path = max(path, node.val + max(0, left+right, left, right))
            return node.val + max(0, left, right)
        
        dfs(root)
        return path