
class Node {
    int val;
    int key;
    Node next;
    Node prev;
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        next = null;
        prev = null;
    }
}
class LRUCache {
    int capacity;
    // we use a pointer for left and right, left keeps track of leftmost right for rightmost as dummies
    // have a map that gives us o(1) lookups
    Map<Integer, Node> maps;
    Node left;
    Node right;  
    public LRUCache(int capacity) {
        this.capacity = capacity;
        maps = new HashMap<>();
        left = new Node(0,0);
        right = new Node(0,0);
        left.next = right;
        right.prev = left; // create sort of sandwich l -> stuff ->
    }
    private void insert(Node node) {
        Node prev = right.prev;
        prev.next = node;
        node.prev = prev;
        node.next = right;
        right.prev = node;
    }

    private void delete(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
    }
    public int get(int key) {
        if (maps.containsKey(key)) {
            Node node = maps.get(key);
            delete(node);
            insert(node);
            return node.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        Node node = new Node(key, value);
        insert(node);
        if (maps.containsKey(key)) {
            Node dupe = maps.get(key);
            delete(dupe);
            maps.remove(dupe.key);
        }
        maps.put(key, node);
        if (maps.size() > capacity) {
            Node deletion = left.next;
            delete(deletion);
            maps.remove(deletion.key);
        }
        
    }
}
