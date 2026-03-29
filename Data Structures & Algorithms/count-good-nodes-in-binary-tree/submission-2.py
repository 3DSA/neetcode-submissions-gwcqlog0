# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node , top):
        additive = 0
        if not node:
            return 0
        if node.val >= top:
            top = node.val
            additive = 1
        return additive + self.dfs(node.right, top) + self.dfs(node.left, top)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, root.val)
