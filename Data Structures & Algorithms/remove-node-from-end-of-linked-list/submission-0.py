# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length+=1
        remove = length - n
        prev = None
        curr = head
        if remove == 0:
            return head.next
        for i in range(remove+1):
            if i == remove:
                temp = curr.next
                prev.next = temp
            else:
                prev = curr
                curr = curr.next
        return head
        

        

        

        