"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        maps = {} # this will hold the node mapping of real to copy
        visited = set() # if node has been traversed with neighbors

        def copy(node):
            if node in visited:
                return
            visited.add(node)
            
            curr = maps.setdefault(node, Node(node.val))

            for neighbors in node.neighbors:
                curr.neighbors.append(maps.setdefault(neighbors, Node(neighbors.val)))
                copy(neighbors)
        
        if not node:
            return
        head = node
        copy(node)
        return maps[head]

        
        