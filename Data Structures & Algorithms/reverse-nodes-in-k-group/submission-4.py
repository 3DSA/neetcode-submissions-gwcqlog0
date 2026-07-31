# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(node, k):
            prev = None
            for i in range(k):
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev, node
        
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        
        heads = []
        node = head
        for i in range(count // k):
            prev, node = reverse(node,k)
            heads.append(prev)
        if node:
            heads.append(node)
        
        prev = ListNode(0)
        for node in heads:
            while node:
                prev.next = node
                prev = node
                node = node.next
            
        return heads[0]
        
        