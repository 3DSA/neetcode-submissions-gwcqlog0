# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit = 1
        num1 = 0
        while l1:
            num1 += l1.val*digit
            digit *= 10
            l1 = l1.next
        digit = 1
        num2 = 0
        while l2:
            num2 += l2.val*digit
            digit *= 10
            l2 = l2.next
        num = num1+num2
        head = ListNode(0)
        curr = head
        it = 0
        while num >= 0:
            value = num % 10
            num = num // 10
            curr.next = ListNode(value)
            curr = curr.next
            if num == 0:
                break
        return head.next

        