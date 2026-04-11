# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(node, length):
            if not node:
                return length
            length +=1
            return max(depth(node.left,length), depth(node.right,length))
        return depth(root, 0)
        