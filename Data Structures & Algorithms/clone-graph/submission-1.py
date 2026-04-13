"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        maps = {}
        head = node
        visited = set()
        def dfs(node):
            if not node or node in visited:
                return
            copy = maps.setdefault(node, Node(node.val))
            visited.add(node)
            for neighbors in node.neighbors:
                neighbor_copy = maps.setdefault(neighbors, Node(neighbors.val))
                copy.neighbors.append(neighbor_copy)
                dfs(neighbors)
        dfs(node)
        return maps[head]
        