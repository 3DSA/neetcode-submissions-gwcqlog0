# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        place = 1
        while l1 or l2:
            if l1:
                num1 += l1.val * place
                l1 = l1.next
            if l2:
                num2 += l2.val * place
                l2 = l2.next
            place *= 10

        num3 = num1+num2
        print(num3)
        prev = ListNode(0)
        l3 = prev
        while num3 >=0:
            node = ListNode(num3 % 10)
            l3.next = node
            l3 = l3.next
            num3 = num3 // 10
            if num3 == 0:
                break
        return prev.next


        