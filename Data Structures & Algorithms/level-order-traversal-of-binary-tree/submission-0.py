# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, arr, queue):
        if not queue:
            return arr
        level = []
        next_q = []
        for i in queue:
            level.append(i.val)
            if i.left:
                next_q.append(i.left)
            if i.right:
                next_q.append(i.right)
        arr.append(level)
        return self.helper(arr, next_q)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        return self.helper([],[root])



        