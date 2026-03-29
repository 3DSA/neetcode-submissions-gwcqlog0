# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        queue = []
        def dfs(node, val):
            nonlocal queue
            if not node:
                return

            if node.val == val:
                queue.append(node)

            dfs(node.left,val)
            dfs(node.right,val)

        dfs(root, subRoot.val)

        #now queue is populated for equivalent values
        def check(p,q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q) or p.val != q.val:
                return False
            return check(p.left, q.left) and check(p.right, q.right)
        
        for node in queue:
            if check(node,subRoot):
                return True
        return False

        