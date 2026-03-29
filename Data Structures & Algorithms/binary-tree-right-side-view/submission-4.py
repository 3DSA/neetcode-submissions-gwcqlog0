# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, queue, arr):
        if not queue:
            return arr
        length = len(queue)
        for i in range(length):
            node = queue.pop(0)
            if i == length-1:
                arr.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return self.bfs(queue,arr)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.bfs([root], [])
        