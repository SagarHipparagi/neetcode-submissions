class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # maps key to Node
        
        # Dummy nodes to prevent boundary edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove an existing node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node: Node) -> None:
        """Insert a new node right before the tail (Most Recently Used)."""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)  # Move to the tail (MRU)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        # Create and insert the new/updated node
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)
        
        # Check capacity constraints
        if len(self.cache) > self.cap:
            # Remove from head (Least Recently Used)
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]

        
