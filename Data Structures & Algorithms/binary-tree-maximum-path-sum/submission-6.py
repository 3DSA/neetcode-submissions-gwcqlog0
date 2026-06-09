# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total_max = float('-inf')
        def calc(node):
            nonlocal total_max
            if not node:
                return 0
            
            left = calc(node.left)
            right = calc(node.right)
            total_max = max(total_max, node.val + max(0, left, right, left+right))
            return node.val + max(0, left, right)
        calc(root)
        return total_max
            
            
        