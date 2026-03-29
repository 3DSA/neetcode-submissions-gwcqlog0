# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        while node:
            temp = node.next # 1 2
            node.next = prev # 0 -> none
            prev = node # 0
            node = temp # 1
        return prev



        