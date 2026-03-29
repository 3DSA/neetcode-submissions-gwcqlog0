# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return count
        def traverse(node, val = None):
            nonlocal count
            if not val or node.val >= val:
                val = node.val
                count +=1
            if node.left:
                traverse(node.left, val)
            if node.right:
                traverse(node.right, val)
        traverse(root)
        return count 