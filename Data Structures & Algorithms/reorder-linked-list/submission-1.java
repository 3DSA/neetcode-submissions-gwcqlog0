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
    public void reorderList(ListNode head) {
        ListNode node = head;
        Map<Integer, ListNode> maps = new HashMap<>();
        int index = 0;
        while (node!=null) {
            maps.put(index, node);
            index += 1;
            node = node.next;
        }
        int left = 0;
        int right = index-1;
        ListNode curr = head;
        while (left < right) {
            ListNode temp = curr.next;
            curr.next = maps.get(right);
            curr = curr.next;
            curr.next = temp;
            curr = curr.next;
            left+= 1;
            right -= 1;
        }
        curr.next = null;

    }
}
