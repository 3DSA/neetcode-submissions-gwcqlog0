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
            return
        maps = {}
        visited = set()
        head = node
        def dfs(node):
            if not node or node in visited:
                return
            copy = maps.setdefault(node, Node(node.val))
            visited.add(node)
            for neighbor in node.neighbors:
                neighbor_copy = maps.setdefault(neighbor, Node(neighbor.val))
                copy.neighbors.append(neighbor_copy)
                dfs(neighbor)
        dfs(node)
        return maps[head]
        