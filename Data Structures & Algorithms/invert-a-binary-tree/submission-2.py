# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap(self, node):
        left = node.left
        right = node.right
        node.right = left
        node.left = right
        if node.right:
            self.swap(node.right)
        if node.left:
            self.swap(node.left)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        curr = root
        self.swap(curr)
        return root

        