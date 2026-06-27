# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # have a check for the leaf node, check if leaf node
        # dfs, since we can traverse to leaf, delete, and recursively delete

        def dfs(prev, node, direction): # true is left, false is right
            if not node:
                return
            dfs(node, node.left, True)
            dfs(node, node.right, False)
            if not node.left and not node.right and node.val == target:
                if direction:
                    prev.left = None
                else:
                    prev.right = None
                return
        dummy = TreeNode(0, root)
        dfs(dummy, root, True)
        return dummy.left