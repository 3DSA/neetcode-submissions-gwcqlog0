# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        p_path = []
        q_path = []
        def traverse(node, val, path):
            if not node:
                return 
            path.append(node)
            if node.val == val:
                return path
            if node.val < val:
                return traverse(node.right, val, path)
            else:
                return traverse(node.left, val, path)
        p_path = traverse(root, p.val, p_path)
        q_path = traverse(root, q.val, q_path)

        lca = None
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                lca = p_path[i]
        return lca
            
        