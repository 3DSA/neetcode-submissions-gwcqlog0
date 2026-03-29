# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        def bfs(queue, side=[]):
            if not queue:
                return side
            
            side.append(queue[-1].val)
            traversal = []
            for node in queue:
                if node.left:
                    traversal.append(node.left)
                if node.right:
                    traversal.append(node.right)

            return bfs(traversal, side)
        return bfs(queue)

        