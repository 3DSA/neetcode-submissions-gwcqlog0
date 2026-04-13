# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        node = head
        count = 0
        while node:
            count +=1
            node = node.next
        
        node = dummy
        curr = 0
        removal = count - n+1
        prev = None
        while node:
            prev = node
            node = node.next
            curr += 1
            if curr == removal:
                temp = node.next
                prev.next = temp
        return dummy.next


        