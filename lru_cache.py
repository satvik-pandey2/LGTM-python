from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move key to the end to show that it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move key to the end before updating
            self.cache.move_to_end(key)
        self.cache[key] = value
        # Check if we exceed the capacity
        if len(self.cache) > self.capacity:
            # Pop the first item (least recently used)
            self.cache.popitem(last=False)

# Example usage:
lru = LRUCache(3)
lru.put(1, 100)
lru.put(2, 200)
lru.put(3, 300)
print(lru.get(2))    # Output: 200
lru.put(4, 400)      # Evicts key 1
print(lru.get(1))    # Output: -1 (not found)
print(lru.get(3))    # Output: 300
