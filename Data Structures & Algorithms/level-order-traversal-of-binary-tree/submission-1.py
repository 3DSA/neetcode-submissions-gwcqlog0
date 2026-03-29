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
        level = []
        length = len(queue)
        for i in range(length):
            node = queue.pop(0)
            level.append(node.val)
            print(level)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        arr.append(level)
        return self.bfs(queue,arr)
        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        return self.bfs([root], [])

        