/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node prev = new Node(0);
        Node curr = prev;
        Map<Node, Node> map = new HashMap<>(); // maps orignal -> copy
        while (head!=null) {
            Node copy = map.getOrDefault(head, new Node(head.val));
            map.put(head, copy);
            curr.next = copy;
            curr = curr.next; // now at. copy
            if (head.random != null) {
                copy = map.getOrDefault(head.random, new Node(head.random.val));
                map.put(head.random, copy);
                curr.random = copy;
            }
            head = head.next;
        }
        return prev.next;
    }
}
