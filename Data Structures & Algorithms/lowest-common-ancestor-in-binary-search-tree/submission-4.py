# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node,search,arr):
            arr.append(node)
            if node == search:
                return arr
            elif search.val < node.val:
                return dfs(node.left, search, arr)
            else:
                return dfs(node.right,search, arr)
        p_arr = dfs(root,p,[])
        q_arr = dfs(root,q,[])
        curr = None
        for i in range(min(len(p_arr),len(q_arr))):
            if p_arr[i] == q_arr[i]:
                curr = p_arr[i]
        return curr
        