class Node:

    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRU_Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.ckeys = {}
        self.top = Node(None, -1)
        self.tail = Node(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key):
        if self.capacity <= 0:
            return "Cannot perform operations on 0 capacity cache"
        if key in self.ckeys.keys():
            current = self.ckeys[key]
            current.next.prev = current.prev
            current.prev.next = current.next
            top_node = self.top.next
            self.top.next = current
            current.prev = self.top
            top_node.prev = current
            return self.ckeys[key].value
        return -1

    def set(self, key, value):
        if self.capacity <= 0:
            print("Cannot perform operations on 0 capacity cache")
            return
        if key in self.ckeys.keys():
            current = self.ckeys[key]
            current.value = value
            current.prev.next = current.next
            current.next.prev = current.prev
            top_node = self.top.next
            self.top.next = current
            current.prev = self.top
            top_node.prev = current
        else:
            current = Node(key, value)
            self.ckeys[key] = current
            top_node = self.top.next
            self.top.next = current
            current.prev = self.top
            current.next = top_node
            top_node.prev = current
            if len(self.ckeys.keys()) > self.capacity:
                self.ckeys.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        values = []
        p = self.top.next
        while p.next:
            values.append(str(p.value))
            p = p.next
        return '->'.join(values)

    __str__ = __repr__


if __name__ == "__main__":
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))      # returns 2
    # returns -1 because 9 is not present in the cache
    print(our_cache.get(9))

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(our_cache.get(3))

    our_cache = LRU_Cache(2)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(1, 3)
    print(our_cache.get(1))  # should return 3
    print(our_cache.get(2))  # should return 2

    our_cache = LRU_Cache(0)
    our_cache.set(1, 1)
    # should print some message like "Can't perform operations on 0 capacity cache"
    print(our_cache.get(1))
    # should print some message like "Can't perform operations on 0 capacity cache"
