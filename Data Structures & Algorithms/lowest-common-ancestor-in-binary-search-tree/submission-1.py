# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, node, p, sets):
        if not node:
            return sets
        sets.add(node)
        if node.val == p.val:
            return sets
        elif node.val > p.val:
            return self.bfs(node.left, p, sets)
        else:
            return self.bfs(node.right, p, sets)  
    
    def LCA(self, node, q, sets, LC):
        if not node:
            return LC
        if node in sets:
            LC = node
        if node.val == q.val:
            return LC
        elif node.val > q.val:
            return self.LCA(node.left, q, sets, LC)
        else:
            return self.LCA(node.right, q, sets, LC)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        sets = self.bfs(root,p, set([]))
        return self.LCA(root, q, sets, None)
        