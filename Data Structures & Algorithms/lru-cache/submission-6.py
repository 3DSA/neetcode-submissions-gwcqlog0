class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.maps = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        node.prev = prev
        self.right.prev = node
    
    def delete(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.maps:
            self.delete(self.maps[key])
            self.insert(self.maps[key])
            return self.maps[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            self.delete(self.maps[key])
            del self.maps[key]
        self.maps[key] = Node(key, value)
        self.insert(self.maps[key])
        if len(self.maps) > self.capacity:
            temp = self.left.next
            self.delete(temp)
            del self.maps[temp.key]




