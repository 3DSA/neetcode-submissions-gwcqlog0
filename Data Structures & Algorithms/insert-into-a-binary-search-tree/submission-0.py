# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert(prev, node, val):
            if not node:
                temp = TreeNode(val)
                if prev.val < val:
                    prev.right = temp
                else:
                    prev.left = temp
                return
            prev = node
            if node.val < val:
                node = node.right
                
            else:
                prev = node
                node = node.left
            insert(prev, node, val)
                
            
        
        if not root:
            return TreeNode(val)

        insert(None, root, val)
        return root 

        