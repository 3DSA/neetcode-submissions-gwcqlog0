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
        side = []
        def bfs(queue):
            if not queue:
                return
            
            side.append(queue[-1].val)
            traverse = []
            for node in queue:
                if node.left:
                    traverse.append(node.left)
                if node.right:
                    traverse.append(node.right)
            bfs(traverse)
        bfs([root])
        return side