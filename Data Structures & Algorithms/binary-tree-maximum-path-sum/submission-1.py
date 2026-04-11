# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        res = root.val
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, node.val, left+node.val, right+node.val, node.val+left+right)
            return max(node.val, left+node.val, right+node.val)
        val = dfs(root)
        return res