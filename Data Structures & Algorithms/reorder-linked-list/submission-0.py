# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = head
        maps = {}
        index = 0
        while node:
            maps[index] = node
            index += 1
            node = node.next
        node = head
        l = 0
        r = index-1
        while l<r:
            right = maps[r]
            temp = node.next
            node.next = right
            right.next = temp
            node = temp
            r -=1
            l +=1
        node.next = None



        