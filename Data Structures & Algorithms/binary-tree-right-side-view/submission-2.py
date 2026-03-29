# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, root):
        queue = [[root, 1]]
        right_edge = []
        max_height = 0
        while queue:
            edge, height = queue.pop()
            print(edge.val)
            if height > max_height:
                max_height = height
                right_edge.append(edge.val)
            if edge.left:
                queue.append([edge.left, height+1])
            if edge.right:
                queue.append([edge.right, height+1])
        return right_edge



    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.bfs(root)

        