class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def evict(self):
        lru = self.head.next
        self.remove(lru)
        return lru.key


class LRUCache:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self._map = {}
        self._cache = DoublyLinkedList()

    def get(self, key):
        if key not in self._map:
            return -1
        node = self._map[key]
        self._cache.remove(node)
        self._cache.add(node)
        return node.val

    def put(self, key, val):
        if key in self._map:
            self._cache.remove(self._map[key])
        node = Node(key, val)
        self._cache.add(node)
        self._map[key] = node
        if self._cache.size > self.capacity:
            evicted = self._cache.evict()
            del self._map[evicted]
