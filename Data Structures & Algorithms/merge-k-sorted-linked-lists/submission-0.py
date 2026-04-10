# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left, right):
            res = ListNode(0)
            temp = res
            while left and right:
                if left.val < right.val:
                    res.next = left
                    left = left.next
                else:
                    res.next = right
                    right = right.next
                res = res.next

            while left:
                res.next = left
                res = res.next
                left = left.next
            while right:
                res.next = right
                res = res.next
                right = right.next
            return temp.next
        if len(lists) <=1:
            if lists:
                return lists[0]
            return None
        mid = len(lists) //2
        left = self.mergeKLists(lists[mid:])
        right = self.mergeKLists(lists[:mid])

        return merge(left,right)
        
     


        