# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def swap(node):
            left = node.left
            node.left = node.right
            node.right = left
            if node.left:
                swap(node.left)
            if node.right:
                swap(node.right)
            return node
        node = swap(root)
        return node