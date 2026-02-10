# Saturday 2/14 — Games + Graphs

---

## Core 1: Tetris-Lite

Build a simplified Tetris engine. Progressive stages — stop wherever time runs out.

```python
class Tetris:
    def __init__(self, rows: int = 20, cols: int = 10): ...
    def drop_block(self, col: int) -> int: ...          # Stage 1
    def clear_rows(self) -> int: ...                     # Stage 2
    def drop_piece(self, piece: str, col: int) -> int: ...  # Stage 3
    def __str__(self) -> str: ...
```

**Stage 1 — Basic grid + 1x1 blocks (~15 min):**
- Initialize a `rows x cols` grid filled with 0.
- `drop_block(col)` — Drop a 1x1 block into the given column. It falls to the lowest empty row. Return the row it lands on. Return -1 if column is full.
- `__str__()` — Print the board. Use `.` for empty and `#` for filled.

**Stage 2 — Row clearing + gravity (~15 min):**
- `clear_rows()` — Check all rows. Any row that is completely filled gets removed. All rows above shift down. Return the number of rows cleared.
- Call this after every drop.

**Stage 3 — Standard pieces (~20 min):**
Define pieces as lists of (row_offset, col_offset) relative to an anchor point:
```python
PIECES = {
    "I": [(0,0), (0,1), (0,2), (0,3)],   # horizontal line
    "O": [(0,0), (0,1), (1,0), (1,1)],    # 2x2 square
    "T": [(0,0), (0,1), (0,2), (1,1)],    # T-shape
    "L": [(0,0), (1,0), (2,0), (2,1)],    # L-shape
}
```
- `drop_piece(piece_name, col)` — Drop the piece anchored at `col`. All cells of the piece fall together until any cell would collide. Return the row of the anchor, or -1 if can't place.

**Stage 4 — Collision detection (~10 min):**
- Before placing, check that all cells of the piece are within bounds and unoccupied.
- The piece "falls" row by row. At each row, check if the next row down would collide. If yes, lock in place at current row.

**Key practice:** This is exactly the "build a thing progressively" pattern JS uses. Narrate each stage transition: "Now that basic drops work, the natural next concern is row clearing..."

---

## Core 2: Least-Loaded Load Balancer

Implement a load balancer that assigns tasks to the least-loaded server.

```python
import heapq
from typing import Optional

class LoadBalancer:
    def __init__(self):
        self.heap = []
        self.entry_map = {}
        self.removed = set()

    def add_server(self, server_id: int) -> None: ...
    def remove_server(self, server_id: int) -> bool: ...
    def assign_task(self) -> Optional[int]: ...
    def update_load(self, server_id: int, delta: int) -> bool: ...
```

**Operations:**
1. `add_server(server_id)` — Register with zero load. Ignore duplicates.
2. `remove_server(server_id)` — Remove server and its load. Return True/False.
3. `assign_task()` — Return server_id with smallest load (ties broken by smallest server_id). Increment that server's load by 1. Return None if no servers.
4. `update_load(server_id, delta)` — Adjust load by delta (may be negative). Clamp to 0. Return True/False.

**Implementation — Heap with lazy deletion:**
- Push `(load, server_id)` tuples onto a min-heap.
- When removing or updating, mark old entries as stale (add to `removed` set or increment a version counter). Push new entry.
- When popping from heap, skip stale entries.
- This gives O(log S) amortized for all operations.

**Constraints:**
- server_id is 32-bit signed int.
- At most 10^5 total calls.
- All operations O(log S) where S = number of servers.

**Example:**
```
lb = LoadBalancer()
lb.add_server(1)
lb.add_server(2)
lb.update_load(1, 3)    # server 1 load = 3
lb.assign_task()         # returns 2 (load 0 → 1)
lb.remove_server(1)      # True
lb.assign_task()         # returns 2 (load 1 → 2)
```

---

## Core 3: Course Schedule I + II (LC 207 + 210)

**Part A — Course Schedule (LC 207):**

There are `numCourses` courses (0 to numCourses-1). `prerequisites[i] = [a, b]` means you must take b before a. Return True if you can finish all courses.

```python
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool: ...
```

This is cycle detection in a directed graph. If there's a cycle, you can't finish.

**Approach — Kahn's BFS:**
1. Build adjacency list and in-degree count.
2. Start BFS from all nodes with in-degree 0.
3. For each node processed, decrement in-degree of its neighbors. If any neighbor reaches 0, add to queue.
4. If total processed == numCourses, no cycle.

**Part B — Course Schedule II (LC 210):**

Return an ordering of courses that satisfies all prerequisites. If impossible, return empty list.

```python
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]: ...
```

Same as Part A, but collect the order as you process.

**Alternative — DFS approach:**
- Three states: WHITE (unvisited), GRAY (in current path), BLACK (done).
- Visit a GRAY node = cycle.
- Topological order = reverse of DFS finish order.

**Know both approaches.** Kahn's is more intuitive for "course schedule" type problems. DFS is more natural for "can I reach X from Y" problems.

**Example:**
```
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

canFinish → True
findOrder → [0, 1, 2, 3] or [0, 2, 1, 3]  (multiple valid orderings)
```

---

## Non-Core 1: Async Tool-Calling Agent

Like the ReAct agent from Thursday, but async with proper error handling.

```python
from typing import Callable, Awaitable
from pydantic import BaseModel
import asyncio, json, re

class ToolCall(BaseModel):
    tool: str
    input: dict

class ToolAgent:
    def __init__(self, llm: Callable[[str], Awaitable[str]],
                       tools: dict[str, Callable],
                       timeout: float = 5.0):
        self.llm = llm
        self.tools = tools
        self.timeout = timeout

    async def run(self, prompt: str, max_steps: int = 10) -> str: ...
```

**Requirements:**
1. Extract first JSON object from LLM response using regex.
2. Validate against `ToolCall` Pydantic model.
3. Error handling:
   - Invalid JSON → append "Observation: Invalid JSON" and continue.
   - Missing tool → append "Observation: Tool not found".
   - Tool raises or times out → append "Observation: Tool error: <msg>".
4. Stop on line starting with `Answer:` (case-insensitive).
5. Raise `RuntimeError("max steps")` if loop exceeds max_steps.
6. Tool calls have timeout via `asyncio.wait_for`.

**Keep code ≤ 120 lines.** Focus on error handling — that's what makes this production-grade.

---

## Non-Core 2: Dirty Data Stream Processor

Process out-of-order log lines with time-windowed queries.

```python
class LogProcessor:
    def __init__(self): ...
    def ingest(self, log_line: str) -> None: ...
    def get_top_users(self, k: int, window_minutes: int) -> List[str]: ...
    def detect_anomaly(self, threshold: int) -> Optional[tuple]: ...
```

**Operations:**
1. `ingest(log_line)` — Parse: `"2026-02-01 10:00:01 | USER_123 | LOGIN | SUCCESS"`. Fields: timestamp, user_id, action, status.
2. `get_top_users(k, window_minutes)` — Return top k users with most "SUCCESS" events in the last `window_minutes` minutes. Must be faster than O(n) where n is total logs.
3. `detect_anomaly(threshold)` — If any user has more than `threshold` "FAIL" events within any 60-second window, return (user_id, last_failure_timestamp).

**Constraints:**
- Logs may arrive out of order.
- Memory must be managed (can't store everything indefinitely).
- `get_top_users` must use a heap for efficiency.

**Implementation hints:**
- Store logs in a sorted structure (SortedList or list + bisect).
- For top-k: maintain per-user success counts, use heapq.nlargest.
- For anomaly: per-user deque of failure timestamps, sliding window.

---

## Wildcard: System Design — Model Evaluation Pipeline

*(Talk-through exercise, no coding. ~1hr.)*

You're building an internal platform for evaluating LLM quality. Hundreds of eval jobs per week across different models, prompts, and datasets.

**Talk through:**
- Data model: eval job → dataset → examples → predictions → scores.
- Eval types: exact match, LLM-as-judge, human review, custom metrics.
- Regression detection: model A was better last week, now worse — how do you alert?
- Storage and comparison: versioning, dashboards, diffs across runs.
- Scale: thousands of examples. Parallel execution, batching, cost management.
- Interface: CLI? Web UI? API that plugs into CI/CD?
