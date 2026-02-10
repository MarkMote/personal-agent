Got it—let’s turn the “in-memory file system” prompt into a Leetcode-style spec and then chip away at it together.

-------------------------------------------------
Problem 1. Design In-Memory File System
-------------------------------------------------
Design a simple in-memory file system that supports the following operations:

1. `ls(path: str) -> List[str]`  
   Return the names of files and immediate sub-directories contained in the directory at the given path.  
   - The contents must be returned in **lexicographic order**.  
   - If `path` is a file path, return a list containing only the file name.

2. `mkdir(path: str) -> None`  
   Create a directory (and any missing parent directories) for the given path.  
   - Leading `/` is optional; treat `/a/b` and `a/b` as the same path.  
   - Do nothing if the directory already exists.

3. `add_content(path: str, content: str) -> None`  
   Create the file (and any missing parent directories) if it does not exist, then append the given content to the file.  
   - If the file already exists, the new content is appended.

4. `read_content(path: str) -> str`  
   Return the full content of the file at the given path.

Constraints
-----------
- All paths are non-empty strings.  
- Path components are separated by `/`.  
- File and directory names are alphanumeric.  
- All operations must be O(d) where d is the depth of the path.  
- You may assume no concurrent calls.

You must implement the class:

```python
class FileSystem:
    def __init__(self): ...
    def ls(self, path: str) -> List[str]: ...
    def mkdir(self, path: str) -> None: ...
    def add_content(self, path: str, content: str) -> None: ...
    def read_content(self, path: str) -> str: ...
```



-------------------------------------------------
Problem 2. Design Transactional Key-Value Store
-------------------------------------------------
Implement an in-memory key-value store that supports **nested transactions** with *set/get/delete* and *begin/commit/rollback*.

You must implement the class:

```python
class TxnKVStore:
    def __init__(self): ...
    def get(self, key: str) -> Optional[str]: ...
    def set(self, key: str, value: str) -> None: ...
    def delete(self, key: str) -> None: ...
    def begin(self) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
```

Operations
----------
1. `get(key: str) -> Optional[str]`  
   Return the most-recently-set value for `key` in the current transactional context.  
   - If the key was deleted in this context, return `None`.  
   - If no transactional context exists, fall back to the global store.

2. `set(key: str, value: str) -> None`  
   Upsert the key in the **current** transactional context.  
   - Does **not** affect outer contexts until `commit`.

3. `delete(key: str) -> None`  
   Mark the key as deleted in the current transactional context.  
   - Subsequent `get` in the same context returns `None`.  
   - Does **not** delete from outer contexts until `commit`.

4. `begin() -> None`  
   Start a new transaction.  
   - Transactions may be nested arbitrarily deep.  
   - Each `begin` increments an internal *transaction level* by 1.

5. `commit() -> bool`  
   Persist the innermost transaction to its parent.  
   - On success, merge the current delta into the parent context and decrement the transaction level.  
   - Return `True` on success.  
   - If no open transaction, raise `RuntimeError`.

6. `rollback() -> bool`  
   Discard the innermost transaction.  
   - On success, discard the current delta and decrement the transaction level.  
   - Return `True` on success.  
   - If no open transaction, raise `RuntimeError`.

Constraints
-----------
- All keys and values are non-empty strings.  
- Maximum number of nested transactions ≤ 100 (you may assume this limit is never exceeded).  
- All operations must be O(1) time (excluding built-in dict operations).  
- Memory usage must be proportional to the number of keys touched in the uncommitted transactions.  
- You may assume no concurrent calls.

Examples
--------
```
store = TxnKVStore()
store.set("a", "1")
store.begin()
store.set("a", "2")
print(store.get("a"))      # "2"
store.rollback()
print(store.get("a"))      # "1"

store.begin()
store.delete("a")
print(store.get("a"))      # None
store.commit()
print(store.get("a"))      # None
```



-------------------------------------------------
Problem 3. Design Sliding-Window Rate Limiter / Hit Counter
-------------------------------------------------
Implement an in-memory hit counter that enforces a **sliding-window** rate limit and cleans up stale timestamps on the fly.

You must implement the class:

```python
class RateLimiter:
    def __init__(self, max_hits: int, window_sec: int): ...
    def hit(self, timestamp: int) -> bool: ...
    def get_hits(self, timestamp: int) -> int: ...
```

Operations
----------
1. `hit(timestamp: int) -> bool`  
   Record one hit at the given Unix-second timestamp and return `True` if the hit is **allowed**, else `False`.  
   - Allowed ⇒ total hits in the sliding window ending at `timestamp` ≤ `max_hits`.  
   - Rejected hits are **not** stored.

2. `get_hits(timestamp: int) -> int`  
   Return the number of hits in the sliding window ending at `timestamp` **without** recording a new hit.  
   - Must exclude any hits older than `timestamp - window_sec + 1`.

Constraints
-----------
- `timestamp` is a non-negative integer (Unix seconds).  
- `1 ≤ max_hits ≤ 10^9`, `1 ≤ window_sec ≤ 10^9`.  
- All operations must be amortized **O(1)** time and **O(window_sec)** memory in the worst case.  
- You may assume monotonically non-decreasing timestamps (no time travel).  
- Handle **bursty input** gracefully: sudden spikes of thousands of calls within the same second must not degrade performance.  
- No external libraries.

Edge-Case Examples
------------------
```python
rl = RateLimiter(max_hits=3, window_sec=5)
rl.hit(1)   # True
rl.hit(1)   # True
rl.hit(1)   # True
rl.hit(1)   # False  (limit reached)
rl.get_hits(6)  # 0  (all old hits expired)
rl.hit(6)   # True
```

Skeleton
--------
```python
from collections import deque

class RateLimiter:
    def __init__(self, max_hits: int, window_sec: int):
        self.max = max_hits
        self.win = window_sec
        self.q = deque()  # store only relevant timestamps

    def hit(self, timestamp: int) -> bool: ...
    def get_hits(self, timestamp: int) -> int: ...
```


-------------------------------------------------
Problem 4. Design Log Parser & Aggregator
-------------------------------------------------
Build an in-memory component that ingests structured log strings, filters by a time window, then groups and sorts the results.

You must implement the class:

```python
class LogAggregator:
    def __init__(self): ...
    def ingest(self, log: str) -> None: ...
    def query(self, start: int, end: int, group_by: str) -> List[str]: ...
```

Operations
----------
1. `ingest(log: str) -> None`  
   Accept a log string formatted exactly as:  
   `<timestamp> "<level>" <component> "<message>"`  
   - `timestamp` is a Unix-second integer.  
   - `level` is one of `DEBUG`, `INFO`, `WARN`, `ERROR`.  
   - `component` and `message` are alphanumeric-plus-hyphen strings (no spaces or quotes inside).  
   - Store the parsed entry in memory.  
   - If the format is invalid, silently ignore the log (do not raise).

2. `query(start: int, end: int, group_by: str) -> List[str]`  
   Return a list of strings summarizing logs in the **inclusive** time window `[start, end]`.  
   - `group_by` is one of:  
     - `"level"` – aggregate counts per level.  
     - `"component"` – aggregate counts per component.  
   - Output format:  
     `<group>:<count>` sorted first by descending `count`, then alphabetically by `group` when counts tie.  
   - If no logs match, return an empty list.  
   - Must run in **O(k + g log g)** time where `k = #logs in window` and `g = #groups`.

Constraints
-----------
- `1 ≤ total ingest calls ≤ 10^5`.  
- `0 ≤ timestamp ≤ 10^9`.  
- `0 ≤ start ≤ end ≤ 10^9`.  
- Memory must be **O(n)** where `n = #stored logs`.  
- You may assume no concurrent calls.

Example
-------
```
agg = LogAggregator()
agg.ingest('1620001010 "INFO" auth "login-ok"')
agg.ingest('1620001011 "ERROR" db "conn-fail"')
agg.ingest('1620001012 "INFO" auth "logout"')
agg.query(1620001010, 1620001012, "level")
→ ['INFO:2', 'ERROR:1']
```

Skeleton
--------
```python
from collections import defaultdict
from typing import List

class LogAggregator:
    def __init__(self):
        self.logs = []  # list of dicts or objects

    def ingest(self, log: str) -> None: ...
    def query(self, start: int, end: int, group_by: str) -> List[str]: ...
```



-------------------------------------------------
Problem 5. Design Least-Loaded Load Balancer
-------------------------------------------------
Implement an in-memory load balancer that always assigns a task to the **currently least-loaded** server, supports dynamic server removals, and updates server loads efficiently.

You must implement the class:

```python
class LoadBalancer:
    def __init__(self): ...
    def add_server(self, server_id: int) -> None: ...
    def remove_server(self, server_id: int) -> bool: ...
    def assign_task(self) -> Optional[int]: ...
    def update_load(self, server_id: int, delta: int) -> bool: ...
```

Operations
----------
1. `add_server(server_id: int) -> None`  
   Register a new server with zero load.  
   - Duplicate adds are ignored.

2. `remove_server(server_id: int) -> bool`  
   Remove the server and its load.  
   - Return `True` if the server existed and was removed, else `False`.

3. `assign_task() -> Optional[int]`  
   Return the `server_id` with the **smallest current load**.  
   - Ties broken by **smallest server_id** first.  
   - Increment that server’s load by 1.  
   - Return `None` if no servers are registered.

4. `update_load(server_id: int, delta: int) -> bool`  
   Atomically adjust the load of an existing server by `delta` (may be negative).  
   - Return `True` if the server existed and was updated, else `False`.  
   - Server load must never drop below 0; clamp to 0 if necessary.

Constraints
-----------
- `server_id` is a 32-bit signed integer.  
- At most `10^5` total calls across all methods.  
- All operations must be **O(log S)** time where `S = #servers`.  
- Memory must be **O(S)**.  
- You may assume no concurrent calls.

Edge-Case Examples
------------------
```python
lb = LoadBalancer()
lb.add_server(1)
lb.add_server(2)
lb.update_load(1, 3)   # server 1 now has load 3
lb.assign_task()        # returns 2 (load 0), server 2 load → 1
lb.remove_server(1)     # True
lb.assign_task()        # returns 2 again
```

Skeleton
--------
```python
import heapq
from typing import Optional

class LoadBalancer:
    def __init__(self):
        self.heap = []          # (load, server_id)
        self.entry_map = {}     # server_id -> heap entry
        self.removed = set()    # servers that are deleted or outdated

    def add_server(self, server_id: int) -> None: ...
    def remove_server(self, server_id: int) -> bool: ...
    def assign_task(self) -> Optional[int]: ...
    def update_load(self, server_id: int, delta: int) -> bool: ...
```



-------------------------------------------------
Problem 6. Design LRU Cache with Optional TTL
-------------------------------------------------
Implement an in-memory key-value cache that evicts the **least-recently-used** item when capacity is exceeded and supports per-key TTL (time-to-live) in seconds.

You must implement the class:

```python
class LRUCache:
    def __init__(self, capacity: int): ...
    def get(self, key: str) -> Optional[str]: ...
    def put(self, key: str, value: str, ttl: Optional[int] = None) -> None: ...
    def size(self) -> int: ...
```

Operations
----------
1. `get(key: str) -> Optional[str]`  
   Return the value for `key` and mark it as **most-recently-used**.  
   - If the key does not exist or has **expired**, return `None` and remove the expired entry.

2. `put(key: str, value: str, ttl: Optional[int] = None) -> None`  
   Insert or update the value for `key`.  
   - `ttl` is an optional positive integer in **seconds**; if omitted, the key never expires.  
   - If the cache exceeds `capacity` after insertion, evict the **LRU** non-expired item.  
   - Expired items are **ignored** during eviction (they are silently removed on access or when encountered).

3. `size(self) -> int`  
   Return the number of **non-expired** keys currently stored.

Constraints
-----------
- `1 ≤ capacity ≤ 10^4`.  
- `0 ≤ ttl ≤ 10^9` when provided.  
- All keys and values are non-empty strings.  
- Total number of calls ≤ `10^5`.  
- All operations must be **O(1)** amortized time.  
- Memory must be **O(capacity)**.  
- You may assume monotonically non-decreasing integer timestamps supplied via a global `now()` function (you do **not** need to implement the clock).

Edge-Case Examples
------------------
```python
cache = LRUCache(2)
cache.put("a", "1", ttl=5)  # expires at now()+5
cache.put("b", "2")         # never expires
cache.get("a")              # "1"
cache.put("c", "3")         # evicts "b" (LRU), not "a"
cache.size()                # 2
```

Skeleton
--------
```python
from collections import OrderedDict
from typing import Optional

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = OrderedDict()  # key -> (expiry, value)

    def _now(self) -> int: ...

    def get(self, key: str) -> Optional[str]: ...
    def put(self, key: str, value: str, ttl: Optional[int] = None) -> None: ...
    def size(self) -> int: ...
```


-------------------------------------------------
Problem 7. Design Spreadsheet with Dependency Graph
-------------------------------------------------
Implement an in-memory spreadsheet that supports **cell references**, **on-demand recomputation**, and **cycle detection** during updates.

You must implement the class:

```python
class Spreadsheet:
    def __init__(self): ...
    def set(self, cell: str, value: str) -> None: ...
    def get(self, cell: str) -> int: ...
```

Operations
----------
1. `set(cell: str, value: str) -> None`  
   Store a value or formula for `cell`.  
   - `value` is either:  
     - an integer literal (e.g., `"42"`), or  
     - a formula starting with `"="` followed by an **integer** or a **sum expression**  
       `=SUM(C1,C2,…)` where each `Ci` is a cell identifier (A1-style).  
   - Whitespace is ignored.  
   - If the formula introduces a **cyclic dependency**, raise `ValueError("cycle")` and leave the spreadsheet unchanged.  
   - Overwriting a cell removes its old dependencies and installs new ones.

2. `get(cell: str) -> int`  
   Return the **current evaluated value** of `cell`.  
   - If the cell is empty, return 0.  
   - If any referenced cell is part of a cycle or contains an invalid formula, raise `ValueError("bad ref")`.

Constraints
-----------
- Cell identifiers are Excel-style (letter+number, e.g., A1, B3).  
- Total number of cells ≤ 1000.  
- Total number of dependencies per cell ≤ 10.  
- All operations must be **O(V+E)** in the size of the dependency graph.  
- You may assume no concurrent calls.

Edge-Case Examples
----------------
```
sheet = Spreadsheet()
sheet.set("A1", "=SUM(B1,B2)")
sheet.set("B1", "10")
sheet.set("B2", "20")
sheet.get("A1")  # 30

sheet.set("B2", "=A1")  # cycle → ValueError
```

Skeleton
--------
```python
class Spreadsheet:
    def __init__(self):
        self.graph = {}  # cell -> set of cells it directly depends on
        self.val = {}    # cell -> current integer value
        self.formula = {} # cell -> raw string formula

    def set(self, cell: str, value: str) -> None: ...
    def get(self, cell: str) -> int: ...
```



-------------------------------------------------
Problem 7. Design Spreadsheet with Dependency Graph
-------------------------------------------------
Implement an in-memory spreadsheet that supports **cell references**, **on-demand recomputation**, and **cycle detection** during updates.

You must implement the class:

```python
class Spreadsheet:
    def __init__(self): ...
    def set(self, cell: str, value: str) -> None: ...
    def get(self, cell: str) -> int: ...
```

Operations
----------
1. `set(cell: str, value: str) -> None`  
   Store a value or formula for `cell`.  
   - `value` is either:  
     - an integer literal (e.g., `"42"`), or  
     - a formula starting with `"="` followed by an **integer** or a **sum expression**  
       `=SUM(C1,C2,…)` where each `Ci` is a cell identifier (A1-style).  
   - Whitespace is ignored.  
   - If the formula introduces a **cyclic dependency**, raise `ValueError("cycle")` and leave the spreadsheet unchanged.  
   - Overwriting a cell removes its old dependencies and installs new ones.

2. `get(cell: str) -> int`  
   Return the **current evaluated value** of `cell`.  
   - If the cell is empty, return 0.  
   - If any referenced cell is part of a cycle or contains an invalid formula, raise `ValueError("bad ref")`.

Constraints
-----------
- Cell identifiers are Excel-style (letter+number, e.g., A1, B3).  
- Total number of cells ≤ 1000.  
- Total number of dependencies per cell ≤ 10.  
- All operations must be **O(V+E)** in the size of the dependency graph.  
- You may assume no concurrent calls.

Edge-Case Examples
----------------
```
sheet = Spreadsheet()
sheet.set("A1", "=SUM(B1,B2)")
sheet.set("B1", "10")
sheet.set("B2", "20")
sheet.get("A1")  # 30

sheet.set("B2", "=A1")  # cycle → ValueError
```

Skeleton
--------
```python
class Spreadsheet:
    def __init__(self):
        self.graph = {}  # cell -> set of cells it directly depends on
        self.val = {}    # cell -> current integer value
        self.formula = {} # cell -> raw string formula

    def set(self, cell: str, value: str) -> None: ...
    def get(self, cell: str) -> int: ...
```



-------------------------------------------------
Problem 8. Design Task Queue / Job Runner with Retry & Delay
-------------------------------------------------
Build an in-memory task queue that supports **enqueue**, **in-order processing**, and **configurable retry / delay semantics**.

You must implement the class:

```python
class TaskQueue:
    def __init__(self): ...
    def enqueue(self, task_id: str, delay_ms: int = 0) -> None: ...
    def poll(self) -> Optional[str]: ...
    def fail(self, task_id: str, retry_delay_ms: int) -> None: ...
    def succeed(self, task_id: str) -> None: ...
```

Operations
----------
1. `enqueue(task_id: str, delay_ms: int = 0) -> None`  
   Insert a new task.  
   - `delay_ms` ≥ 0: the task becomes eligible for polling only after **delay_ms** milliseconds counted from **enqueue time**.  
   - Duplicate `task_id` is ignored if the task is still pending (not yet succeeded).

2. `poll() -> Optional[str]`  
   Return the **next eligible** task in **enqueue order** (FIFO among eligible tasks).  
   - Return `None` if no eligible task exists.  
   - A task is eligible when its delay has expired and it is not currently **in-flight**.  
   - Once returned, the task is considered **in-flight** until `succeed` or `fail` is called.

3. `fail(task_id: str, retry_delay_ms: int) -> None`  
   Mark an in-flight task as failed and re-schedule it after **retry_delay_ms**.  
   - If `task_id` is not currently in-flight, do nothing.  
   - The retry keeps the original enqueue time, so order among eligible tasks is preserved.

4. `succeed(task_id: str) -> None`  
   Permanently remove the task.  
   - If `task_id` is not in-flight, do nothing.

Constraints
-----------
- All `task_id` strings are non-empty and ≤ 100 characters.  
- Total number of calls ≤ 10⁵.  
- All operations must be **O(log n)** time where `n = #pending tasks`.  
- Memory must be **O(n)**.  
- You may assume a monotonic millisecond timer via `now_ms()` (you do **not** need to implement the clock).

Edge-Case Examples
------------------
```
q = TaskQueue()
q.enqueue("t1", delay_ms=50)
q.enqueue("t2", delay_ms=0)
q.poll()        # "t2"  (t1 still delayed)
q.succeed("t2")
q.poll()        # None  (t1 not yet eligible)
# after 50 ms
q.poll()        # "t1"
q.fail("t1", 10)  # retry in 10 ms
# after 10 ms
q.poll()        # "t1" again
q.succeed("t1")
q.poll()        # None
```

Skeleton
--------
```python
import heapq
from typing import Optional

class TaskQueue:
    def __init__(self):
        self.ready = []               # min-heap of (enqueue_time, task_id)
        self.delayed = []             # min-heap of (eligible_time, task_id)
        self.inflight = set()         # tasks currently out for processing
        self.task_info = {}           # task_id -> metadata

    def now_ms(self) -> int: ...

    def enqueue(self, task_id: str, delay_ms: int = 0) -> None: ...
    def poll(self) -> Optional[str]: ...
    def fail(self, task_id: str, retry_delay_ms: int) -> None: ...
    def succeed(self, task_id: str) -> None: ...
```