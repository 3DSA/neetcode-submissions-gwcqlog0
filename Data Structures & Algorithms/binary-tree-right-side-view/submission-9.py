# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def bfs(queue):
            if not queue:
                return
            res.append(queue[-1].val)
            traverse = []
            for node in queue:
                if node.left:
                    traverse.append(node.left)
                if node.right:
                    traverse.append(node.right)
            bfs(traverse)
        
        if not root:
            return res
        
        bfs([root])
        return res

            