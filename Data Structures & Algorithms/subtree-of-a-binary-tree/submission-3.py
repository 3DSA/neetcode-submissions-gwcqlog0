# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q) or p.val != q.val:
                return False
            return check(p.left,q.left) and check(p.right, q.right)
        
        start = []
        def dfs(node, subRoot):
            if not node:
                return
            if node.val == subRoot.val:
                start.append(node)
            dfs(node.left,subRoot)
            dfs(node.right,subRoot)

        dfs(root,subRoot)
        for node in start:
            if check(node, subRoot):
                return True
        return False
        