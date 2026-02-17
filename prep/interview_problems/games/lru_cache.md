# LRU Cache

Jane Street's canonical blog example. The "Memo" problem. Practice until this is muscle memory.

**Task:** Build a memoization wrapper for functions that caches results. Add a capacity limit — when the cache is full, evict the **least recently used** entry. Both `get` and `put` must be O(1).

```python
class LRUCache:
    def __init__(self, capacity: int): ...
    def get(self, key: str) -> any: ...
    def put(self, key: str, value: any) -> None: ...
```

## Stage 1 — Basic memoization wrapper (~10 min)
- `memoize(fn)` — Return a wrapped version that caches results.
- Use a plain `dict` mapping args → return value.
- If args seen before, return cached. Otherwise compute, store, return.

```python
def memoize(fn):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrapper
```

- Test with an expensive function. Verify second call is instant.
- **Problem to identify:** Cache grows without bound. Memory leak.

## Stage 2 — FIFO eviction with O(1) operations (~15 min)
- Add capacity limit. When full, evict the **oldest** entry.
- Naive: use a list. But removing from a list is O(n).
- Better: `collections.OrderedDict` gives O(1) FIFO. Or use a `deque` + dict.

```python
from collections import OrderedDict

class FIFOCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        return self.cache.get(key)  # don't move to end

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            return
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # pop oldest
        self.cache[key] = value
```

- **Problem to identify:** FIFO evicts oldest inserted, not least recently **used**. Frequently accessed items get evicted unfairly.

## Stage 3 — LRU eviction with O(1) operations (~15 min)
- On every `get`, move item to "most recently used" position.
- `OrderedDict.move_to_end(key)` does this in O(1).

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)  # mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict LRU
```

- **Know this cold.** 15 lines, all O(1).

## Stage 4 — Implement WITHOUT OrderedDict (~15 min)
- Build it from scratch: hash map + doubly-linked list.
- Hash map: `key → node`. Linked list: order of access (head = LRU, tail = MRU).
- `get`: look up in map, move node to tail, return value.
- `put`: if exists, update + move to tail. If new + at capacity, remove head node + its map entry. Add new node at tail.

```python
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCacheManual:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.head = Node(0, 0)  # dummy
        self.tail = Node(0, 0)  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add_to_tail(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
```

## Talking points
- Why dummy head/tail nodes? Eliminates null checks at boundaries.
- OrderedDict vs manual: OrderedDict is fine for interviews. Manual shows deep understanding.
- Thread safety: wrap operations in a lock. Or use `threading.Lock` with context manager.
- What about TTL (time-to-live)? Store timestamp with each entry, check on get, lazy cleanup.
