# Friday 2/13 — System Building II (D.E. Shaw at 2pm)

---

## Core 1: Sliding-Window Rate Limiter

Implement a sliding-window hit counter with rate limiting.

```python
from collections import deque

class RateLimiter:
    def __init__(self, max_hits: int, window_sec: int):
        self.max = max_hits
        self.win = window_sec
        self.q = deque()

    def hit(self, timestamp: int) -> bool: ...
    def get_hits(self, timestamp: int) -> int: ...
```

**Operations:**
1. `hit(timestamp)` — Record one hit. Return True if allowed (total in window ≤ max_hits), else False. Rejected hits are NOT stored.
2. `get_hits(timestamp)` — Return count of hits in window without recording a new hit.

**Constraints:**
- Monotonically non-decreasing timestamps.
- Amortized O(1) time, O(window_sec) memory.
- Handle bursty input: thousands of calls within the same second.

**Implementation:** deque stores timestamps. On each call, pop from left while oldest timestamp is outside the window. Check size against max.

**Example:**
```
rl = RateLimiter(max_hits=3, window_sec=5)
rl.hit(1)   # True
rl.hit(1)   # True
rl.hit(1)   # True
rl.hit(1)   # False  (limit reached)
rl.get_hits(6)  # 0  (all expired)
rl.hit(6)   # True
```

---

## Core 2: Task Queue / Job Runner with Retry & Delay

Build a task queue with enqueue, delay, retry, and in-flight tracking.

```python
import heapq
from typing import Optional

class TaskQueue:
    def __init__(self):
        self.ready = []
        self.delayed = []
        self.inflight = set()
        self.task_info = {}

    def now_ms(self) -> int: ...  # provided by test harness

    def enqueue(self, task_id: str, delay_ms: int = 0) -> None: ...
    def poll(self) -> Optional[str]: ...
    def fail(self, task_id: str, retry_delay_ms: int) -> None: ...
    def succeed(self, task_id: str) -> None: ...
```

**Operations:**
1. `enqueue(task_id, delay_ms)` — Insert task. If delay_ms > 0, task becomes eligible only after delay expires. Ignore duplicate task_ids if still pending.
2. `poll()` — Return next eligible task (FIFO among eligible). Mark as in-flight. Return None if nothing eligible.
3. `fail(task_id, retry_delay_ms)` — Re-schedule in-flight task with new delay. Keeps original enqueue time for ordering.
4. `succeed(task_id)` — Permanently remove task.

**Constraints:**
- All operations O(log n).
- Memory O(n).
- Monotonic millisecond timer via `now_ms()`.

**Implementation hint:** Two heaps — one for ready tasks (sorted by enqueue_time), one for delayed tasks (sorted by eligible_time). On each poll(), first move any newly-eligible tasks from delayed to ready. Use a `removed` set for lazy deletion.

**Example:**
```
q = TaskQueue()
q.enqueue("t1", delay_ms=50)
q.enqueue("t2", delay_ms=0)
q.poll()        # "t2"  (t1 still delayed)
q.succeed("t2")
# after 50 ms...
q.poll()        # "t1"
q.fail("t1", 10)
# after 10 ms...
q.poll()        # "t1" again
q.succeed("t1")
```

---

## Core 3: Interval Merge + Meeting Rooms (Progressive)

Three stages building on each other. Stop wherever time runs out.

**Stage 1 — Merge Intervals (LC 56, ~15 min):**

Given a list of intervals `[[start, end], ...]`, merge all overlapping intervals.

```python
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

Example: `[[1,3],[2,6],[8,10],[15,18]]` → `[[1,6],[8,10],[15,18]]`

**Stage 2 — Meeting Rooms II (LC 253, ~20 min):**

Given meeting time intervals, find the minimum number of conference rooms needed.

```python
def minMeetingRooms(intervals: List[List[int]]) -> int: ...
```

Approach: sort by start time. Use a min-heap tracking end times of active meetings. For each meeting: if it starts after the earliest ending meeting, reuse that room (pop from heap). Push the new end time. Answer = max heap size.

Example: `[[0,30],[5,10],[15,20]]` → 2 rooms needed.

**Stage 3 — Interval Scheduler (~25 min):**

Design a class that manages a calendar of non-overlapping events.

```python
class IntervalScheduler:
    def __init__(self): ...
    def book(self, start: int, end: int) -> bool: ...
    def cancel(self, start: int, end: int) -> bool: ...
    def get_conflicts(self, start: int, end: int) -> List[List[int]]: ...
    def free_slots(self, range_start: int, range_end: int) -> List[List[int]]: ...
```

- `book(start, end)` — Add event if it doesn't overlap existing events. Return True/False.
- `cancel(start, end)` — Remove exact matching event. Return True if found.
- `get_conflicts(start, end)` — Return list of existing events that would overlap.
- `free_slots(range_start, range_end)` — Return available time slots within the range.

Use `sortedcontainers.SortedList` or a list kept sorted with `bisect`.

---

## Non-Core 1: MCP Hello World Server

Build a minimal Model-Context-Protocol server with one tool.

```python
#!/usr/bin/env python3
import json
import sys

def send(msg: dict) -> None:
    data = json.dumps(msg, separators=(',', ':'))
    sys.stdout.write(data + '\n\n')
    sys.stdout.flush()

def main() -> None:
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            break
        if line.strip() == b'':
            continue
        try:
            req = json.loads(line.decode())
        except Exception:
            continue
        # dispatch req
        ...

if __name__ == '__main__':
    main()
```

**Requirements:**
1. Stdio JSON-RPC, messages framed by `\n\n`.
2. Support: `mcp.initialize` → reply with version and capabilities. `mcp.tools/call` → expose tool `hello` that takes `{name: str}` and returns `{greeting: str}`.
3. Ignore notifications (`mcp.initialized`).
4. Log only to stderr.
5. Standard library only.

**Capabilities:**
```json
{"protocolVersion": "2024-11-05", "capabilities": {"tools": true}, "serverInfo": {"name": "hello-mcp", "version": "0.1.0"}}
```

**The point:** understand MCP from the inside. Anthropic FDE builds these for customers.

---

## Non-Core 2: Async Endpoint + Background Job

Build a FastAPI service with async background processing.

```python
from fastapi import FastAPI, BackgroundTasks
import asyncio, aiohttp, time, uuid
from typing import Dict

app = FastAPI()
jobs: Dict[str, dict] = {}

async def worker(job_id: str, urls: list[str], timeout: int) -> None: ...

@app.post("/analyze")
async def analyze(payload: dict, background: BackgroundTasks): ...

@app.get("/status/{job_id}")
async def status(job_id: str): ...
```

**Endpoints:**
1. `POST /analyze` — Accepts `{"urls": ["..."], "timeout": 30}`. Returns immediately: `{"job_id": "uuid", "status": "queued"}`. Spawns background worker.
2. `GET /status/{job_id}` — Returns `{"status": "queued|processing|done|failed", "result": {...}, "error": null}`.

**Worker:** Fetches each URL, measures response time. Max 10 concurrent fetches (`asyncio.Semaphore`). Stores results in `jobs` dict.

**Result shape:**
```json
{"total": 3, "ok": 2, "fail": 1, "details": [{"url": "...", "duration_ms": 123, "status": 200}]}
```

**Keep code ≤ 120 lines.**

---

## Wildcard: Storytelling — Pytheia

*(Talk-through exercise. ~1hr. D.E. Shaw at 2pm — good day to sharpen the narrative.)*

**Q1: "What did you build at Pytheia and why?"** (3 min max)
Origin → Argus perception system → LLM pivot → outcome ($20k → $300k ARR).

**Q2: "Tell me about the pivot decision."** (3 min max)
Why? What data informed it? What did you lose? What did you gain? How did you manage the transition?

**Q3: "What did you learn from Pytheia that you couldn't have learned any other way?"** (2 min)
Self-awareness about building products, selling, hiring, failing.

**Q4: "Why didn't Pytheia work out? / Why did you leave?"** (1 min)
Honest, not defensive, forward-looking.
