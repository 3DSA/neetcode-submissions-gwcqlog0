# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, top):
        if not node:
            return 0
        if node.val >= top:
            top = node.val
            return 1 + self.dfs(node.left, top) + self.dfs(node.right, top)
        else:
            return self.dfs(node.left, top) + self.dfs(node.right, top)


    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, root.val)
        