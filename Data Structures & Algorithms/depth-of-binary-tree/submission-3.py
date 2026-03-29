# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(node, count=0):
            if node:
                count +=1
                return max(depth(node.left, count), depth(node.right, count))
            else:
                return count
        return depth(root)

        