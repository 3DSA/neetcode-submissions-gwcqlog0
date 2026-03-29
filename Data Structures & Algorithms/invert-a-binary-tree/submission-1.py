# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap(self, root):
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.right:
            self.swap(root.right)
        if root.left:
            self.swap(root.left)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        node = root
        self.swap(node)
        return root