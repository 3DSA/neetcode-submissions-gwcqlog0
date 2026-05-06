/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        int count = 0;
        ListNode curr = head;
        while (curr!=null) {
            count += 1;
            curr = curr.next;
        }
        if (count == 0 || count < k) { // edge case if head is empty or less nodes than k
            return head;
        }
        //we can sort of slice the linked list into partitions, and keep track of the partitions
        // have a for loop while count // k, iterate through node
        Deque<ListNode> queue = new ArrayDeque<>();
        curr = head;
        ListNode prev = null;
        ListNode temp;
        int j = 0;
        for (int i = 0; i < count / k; ++i) {
            for ( j = 0; j < k; ++j) {
                temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            } // curr equal next head, prev will be new head, 1<-2<-3(prev) 4(curr) 5 6
            queue.offer(prev);
            prev = null;
        }
        if (curr!=null) {
            queue.offer(curr);
        }
        ListNode dummy = new ListNode(0);
        prev = dummy;
        while(!queue.isEmpty()) {
            curr = queue.pop();
            while (curr!= null) {
                prev.next = curr;
                prev = curr;
                curr = curr.next;
            }
        }
        return dummy.next;
    }
}
