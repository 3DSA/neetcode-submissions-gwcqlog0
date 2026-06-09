class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.maps = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
       prev = self.right.prev
       prev.next = node
       node.prev = prev
       node.next = self.right
       self.right.prev = node
    
    def delete(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key in self.maps:
            node = self.maps[key]
            self.delete(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            self.delete(self.maps[key])
        node = Node(key, value)
        self.insert(node)
        self.maps[key] = node
        if len(self.maps) > self.capacity:
            temp = self.left.next
            self.delete(temp)
            self.maps.pop(temp.key)
        