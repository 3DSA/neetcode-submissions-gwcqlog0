# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def calc(node):
            total = 0
            digit = 1
            while node:
                total += node.val * digit
                digit *= 10
                node = node.next
            return total
        
        total = calc(l1) + calc(l2)
        dummy = ListNode(0)
        if total == 0:
            return dummy
        prev = dummy
        while total > 0:
            node = ListNode(total % 10)
            prev.next = node
            prev = node
            total = total // 10
        return dummy.next