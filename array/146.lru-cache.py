# doublely linked list node class
class DLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        # left points to the least recently used, and right points to the most recently used
        # In the beginning, left points to right, and right points to left (both are dummy nodes)
        self.left, self.right = DLNode(0, 0), DLNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            # if key already in cache remove key from list and move it to the right most of the DL list
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # if key already in cache, remove from DL list
            self.remove(self.cache[key])
        # add the node to cache
        self.cache[key] = DLNode(key, value)
        # insert key to the right most of the DL list
        self.insert(self.cache[key])
        # if cache size > capacity remove LRU from list and cache
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    # helper func1: remove node from the doublely linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # helper func2: insert node to the right most of the DL list
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)