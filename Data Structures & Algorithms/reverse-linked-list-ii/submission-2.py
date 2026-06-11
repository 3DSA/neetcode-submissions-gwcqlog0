# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 0
        dummy = ListNode(0, head)
        maps = {index: dummy}
        node = head
        while node:
            index += 1
            maps[index] = node
            node = node.next
        maps[index+1] = node
        if index == 1:
            return head
        prev = None
        node = maps[left]
        while node != maps[right+1]:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        maps[left-1].next = maps[right]
        maps[left].next = maps[right+1]
        return dummy.next

        