# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length +=1
            node = node.next

        index = length - n
        node = head
        prev = None
        count = 0
        if index == 0:
                return head.next
        while node:
            if index == count:
                temp = node.next
                prev.next = temp
                break
            prev = node
            node = node.next
            count +=1
        return head
            

        