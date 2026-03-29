# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, node, count):
        if node is None:
            return count
        count+=1
        return max(self.depth(node.left, count), self.depth(node.right, count))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        curr = root
        return self.depth(curr, 0)



        