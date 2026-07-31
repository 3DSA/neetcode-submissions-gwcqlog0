"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # have a way to track nodes already created, have a way to track nodes visited
        # easiest way is dfs, utilize the map ds to check if node is already made
        if not node:
            return
        maps = {}
        def dfs(node):
            if node in maps:
                return
            maps.setdefault(node, Node(node.val))
            for neighbor in node.neighbors:
                dfs(neighbor)
                maps[node].neighbors.append(maps[neighbor])

        head = node
        dfs(node)
        return maps[head]
        