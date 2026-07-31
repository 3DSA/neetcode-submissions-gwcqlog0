# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1, l2):
            dummy = ListNode(0)
            node = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            
            while l1:
                node.next = l1
                l1 = l1.next
                node = node.next
            while l2:
                node.next = l2
                l2 = l2.next
                node = node.next

            return dummy.next
    
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return
        mid = len(lists)//2
        left = self.mergeKLists(lists[mid:])
        right = self.mergeKLists(lists[:mid])
        return merge(left,right)

        