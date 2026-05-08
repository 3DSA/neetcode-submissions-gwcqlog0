class Node {
    int key;
    int val;
    Node next;
    Node prev;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    Map<Integer, Node> maps;
    int capacity;
    Node left;
    Node right;

    public LRUCache(int capacity) {
        maps = new HashMap<>();
        this.capacity = capacity;
        left = new Node(0,0);
        right = new Node(0,0);
        left.next = right;
        right.prev = left;  // left -> actually whats here - > right
        // when something is added, we use right prev
        // when something is removed we use left next
        
    }

    private void insert(Node node) {
        Node temp = right.prev;
        temp.next = node;
        right.prev = node;
        node.next = right;
        node.prev = temp;
    }

    private void delete(Node node) {
        Node temp = node.prev;
        Node next = node.next;
        temp.next = next;
        next.prev = temp;
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
        Node temp;
        if (maps.containsKey(key)) {
            temp = maps.get(key);
            delete(temp);
        }
        insert(node);
        maps.put(key, node);
        if (maps.size() > capacity) {
            temp = left.next;
            delete(temp);
            maps.remove(temp.key);
        }
    }
}
