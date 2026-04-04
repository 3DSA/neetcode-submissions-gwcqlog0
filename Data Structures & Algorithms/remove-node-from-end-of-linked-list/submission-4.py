# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        count = 0
        while node:
            count +=1
            node = node.next
        
        node = head
        prev = None
        removal = count-n
        if removal == 0:
            return head.next
        for i in range(removal):
            prev = node
            node = node.next
        temp = node.next
        prev.next = temp
        return head
        