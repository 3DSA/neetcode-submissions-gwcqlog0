# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def traverse(node, find, arr):
            arr.append(node)
            if node.val == find.val:
                return arr
            if node.val > find.val:
                return traverse(node.left, find, arr)
            else:
                return traverse(node.right, find, arr)
        
        p_arr = traverse(root, p, [])
        q_arr = traverse(root, q, [])
        res = None
        for i in range(min(len(p_arr), len(q_arr))):
            if p_arr[i] == q_arr[i]:
                res = p_arr[i]
            
        return res



        