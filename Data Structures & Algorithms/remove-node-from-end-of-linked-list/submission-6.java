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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) {
            return head;
        }
        int length = 0;
        ListNode curr = head;
        while (curr != null) {
            length += 1;
            curr = curr.next;
        }
        ListNode prev = new ListNode(0, head);
        ListNode dummy = prev;
        curr = head;
        int removal = length - n;
        for (int i = 0; i < removal; ++i) {
            prev = prev.next;
            curr = curr.next;
        }
        prev.next = curr.next;
        return dummy.next;
    }
}
