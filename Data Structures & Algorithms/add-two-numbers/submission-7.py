# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def convert(node):
            total = 0
            digit = 1
            while node:
                total += node.val*digit
                digit*=10
                node = node.next
            return total
        
        sum3 = convert(l1) + convert(l2)
        l3 = ListNode(0)
        if sum3 == 0:
            return l3
        node = l3
        while sum3 > 0:
            temp = ListNode(sum3%10)
            sum3 = sum3 // 10
            node.next = temp
            node = node.next
        return l3.next

        