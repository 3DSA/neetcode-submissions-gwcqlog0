# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        if not root:
            return []
        queue = [root]
        def bfs(queue):
            if not queue:
                return
            traverse = []
            vals = []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    traverse.append(node.left)
                if node.right:
                    traverse.append(node.right)
            arr.append(vals)
            bfs(traverse)
        bfs(queue)
        return arr

        