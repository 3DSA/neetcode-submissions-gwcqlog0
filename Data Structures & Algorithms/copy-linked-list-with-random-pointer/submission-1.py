"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        node = head

        maps = {} # node to deep copy node
        dummy = Node(0)
        prev = dummy
        while node:
            copy = maps.setdefault(node, Node(node.val))
            if node.random:
                random = maps.setdefault(node.random, Node(node.random.val))
                copy.random = random
            prev.next = copy
            prev = copy
            node = node.next

        return dummy.next
        