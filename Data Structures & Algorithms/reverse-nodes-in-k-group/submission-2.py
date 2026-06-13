# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        maps = {}
        node = head
        index = 0
        while node:
            maps[index] = node
            index +=1
            node = node.next
        partitions = (index) // k

        def reverse(node):
            prev = None
            count = 0
            while count < k:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                count +=1
            return prev, node
        
        heads = []
        node = head
        for r in range(partitions):
            prev, node = reverse(node)
            heads.append(prev)
        if node:
            heads.append(node)

        prev = None
        for node in heads:
            if prev:
                prev.next = node
            while node:
                prev = node
                node = node.next
        return heads[0]
        