# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def LWA(self, root, p, q):
        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root
        if p.val < root.val:
            return self.LWA(root.left, p, q)
        else:
            return self.LWA(root.right, p, q)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p or not q:
            return False
        if p.val == q.val:
            return p
        return self.LWA(root, p, q)

