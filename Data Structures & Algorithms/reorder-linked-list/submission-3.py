# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        maps = {} # key: index, val: node
        node = head
        i = 0
        while node:
            maps[i] = node
            node = node.next
            i+=1
        #
        l = 0
        r = len(maps)-1
        prev = ListNode(0)
        node = prev
        while l<r:
            node.next = maps[l]
            maps[l].next = maps[r]
            node = maps[r]
            l += 1
            r -=1
        if l == r:
            node.next = maps[l]
            node = node.next
        node.next = None
