# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calc_depth(self,node,depth):
        if not node:
            return depth
        return max(self.calc_depth(node.left, depth+1), self.calc_depth(node.right, depth+1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calc_depth(root, 0)
        