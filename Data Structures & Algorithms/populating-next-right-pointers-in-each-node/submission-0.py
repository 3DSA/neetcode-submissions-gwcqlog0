"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def bfs(queue):
            if not queue:
                return
            traverse = deque()
            while queue:
                node = queue.popleft()
                if queue:
                    node.next = queue[0]
                if node.left:
                    traverse.append(node.left)
                if node.right:
                    traverse.append(node.right)
            bfs(traverse)

        if not root:
            return

        queue = deque()
        queue.append(root)
        bfs(queue)
        return root

        
        