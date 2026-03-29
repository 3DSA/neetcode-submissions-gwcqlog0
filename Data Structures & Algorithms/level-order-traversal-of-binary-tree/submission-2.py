# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        def bfs(queue, order=[]):
            if not queue:
                return order
            # order.append(queue)
            traversal = []
            vals = []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    traversal.append(node.left)
                if node.right:
                    traversal.append(node.right)
            order.append(vals)
            return bfs(traversal, order)
        return bfs(queue)
        