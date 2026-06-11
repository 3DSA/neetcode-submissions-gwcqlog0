# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        def calc(node):
            nonlocal max_length
            if not node:
                return 0
            left = calc(node.left)
            right = calc(node.right)
            max_length = max(max_length, left + right)
            return 1 + max(left, right)
        calc(root)
        return max_length
        