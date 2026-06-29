# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left, right):
            dummy = ListNode(0)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            while left:
                curr.next = left
                left = left.next
                curr = curr.next
            while right:
                curr.next = right
                right = right.next
                curr = curr.next
            return dummy.next
        
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return
        left = self.mergeKLists(lists[:len(lists) // 2])
        right = self.mergeKLists(lists[len(lists) // 2:])
        return merge(left, right)
        