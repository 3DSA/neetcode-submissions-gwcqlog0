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
        node = head
        maps = {}
        head2 = Node(0)
        prev = head2
        while node:
            if node in maps:
                curr = maps[node]
            else:
                curr = Node(node.val)
                maps[node] = curr


            random = node.random
            if random:
                if random in maps:
                    curr.random = maps[random]
                else:
                    curr.random = Node(random.val)
                    maps[random] = curr.random
            prev.next = curr
            prev = curr
            node = node.next
            
        return head2.next
        