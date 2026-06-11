# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        def calc(p, q):
            nonlocal same
            if not p and not q:
                return
            if not p or not q or  p.val != q.val:
                same = False
                return
            calc(p.left, q.left)
            calc(p.right, q.right)
        calc(p, q)
        return same
            
        