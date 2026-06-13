# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            res = ListNode(0)
            head = res
            while l1 and l2:
                if l1.val < l2.val:
                    res.next = l1
                    l1 = l1.next
                else:
                    res.next = l2
                    l2 = l2.next
                res = res.next
            
            while l1:
                res.next = l1
                l1 = l1.next
                res = res.next
            while l2:
                res.next = l2
                l2 = l2.next
                res = res.next
            return head.next
        
        def mergeLists(lists):
            if len(lists) == 1:
                return lists[0]
            if len(lists) == 0:
                return
            mid = len(lists) // 2
            left = mergeLists(lists[:mid])
            right = mergeLists(lists[mid:])
            return merge(left,right)
        
        return mergeLists(lists)
                
        