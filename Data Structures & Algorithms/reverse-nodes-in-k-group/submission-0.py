# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # divide and conquer
        prev = None
        node = head
        length = 0
        while node:
            length +=1
            node = node.next

        def reverse(node, k):
            prev = None
            count = 0
            while count < k:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                count +=1
            return prev, node

        partitions = length // k
        node = head
        splits = []
        for i in range(partitions):
            prev, node = reverse(node, k)
            splits.append(prev)
        if node:
            splits.append(node)

        print(splits)
        head = splits[0]
        prev = ListNode(0)
        for nodes in splits:
            prev.next = nodes
            while nodes:
                prev = nodes
                nodes = nodes.next
        return head
        
        

        