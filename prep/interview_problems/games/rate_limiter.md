# Rate Limiter

Reported at Scale AI, Stripe, and various tech companies.

**Task:** Build a rate limiter. `allow(client_id, timestamp)` returns `True` if the client is under the request limit for the current time window, `False` otherwise. Each client is tracked independently. Handle edge cases at window boundaries.

```python
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int): ...
    def allow(self, client_id: str, timestamp: float) -> bool: ...
```

## Stage 1 — Fixed window rate limiter (~10 min)
- `allow(client_id, timestamp)` — Return True if under limit, False otherwise.
- Fixed window: divide time into buckets (e.g., 0-60s, 60-120s, ...).
- Track count per client per window. Reset when window changes.
- Simple but has edge case: 100 requests at t=59, 100 more at t=61 = 200 in 2 seconds.

```python
class FixedWindowLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = window_seconds
        self.counts = {}  # (client_id, window_num) -> count

    def allow(self, client_id: str, timestamp: float) -> bool:
        window_num = int(timestamp // self.window)
        key = (client_id, window_num)
        self.counts[key] = self.counts.get(key, 0) + 1
        return self.counts[key] <= self.max_requests
```

- **Problem to identify:** Boundary burst. Client can send 2x limit across a window boundary.

## Stage 2 — Sliding window with deque (~15 min)
- Track exact timestamps of each request per client.
- On each `allow`, remove timestamps older than `window_seconds` ago.
- Count remaining. If under limit, add current timestamp and allow.
- Uses `collections.deque` for O(1) popleft.

```python
from collections import defaultdict, deque

class SlidingWindowLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = defaultdict(deque)  # client_id -> deque of timestamps

    def allow(self, client_id: str, timestamp: float) -> bool:
        q = self.requests[client_id]
        # Evict old timestamps
        while q and q[0] <= timestamp - self.window:
            q.popleft()
        if len(q) < self.max_requests:
            q.append(timestamp)
            return True
        return False
```

- Accurate but O(n) memory per client per window.

## Stage 3 — Token bucket (~15 min)
- Bucket fills at a steady rate (e.g., 10 tokens/sec). Max capacity = burst limit.
- Each request costs 1 token. If tokens available, allow and decrement. Otherwise deny.
- Refill on each `allow` call based on elapsed time (lazy refill).

```python
class TokenBucketLimiter:
    def __init__(self, rate: float, capacity: int):
        self.rate = rate          # tokens per second
        self.capacity = capacity  # max burst
        self.buckets = {}         # client_id -> (tokens, last_refill_time)

    def allow(self, client_id: str, timestamp: float) -> bool:
        if client_id not in self.buckets:
            self.buckets[client_id] = (self.capacity, timestamp)

        tokens, last_time = self.buckets[client_id]
        # Refill
        elapsed = timestamp - last_time
        tokens = min(self.capacity, tokens + elapsed * self.rate)

        if tokens >= 1:
            self.buckets[client_id] = (tokens - 1, timestamp)
            return True
        else:
            self.buckets[client_id] = (tokens, timestamp)
            return False
```

- Advantage: handles bursts naturally. Configurable burst vs sustained rate.

## Stage 4 — Distributed rate limiting (~10 min, discussion)
- Multiple servers need to share rate limit state.
- Options: Redis with INCR + EXPIRE, or centralized limiter service.
- Redis approach: `MULTI / INCR key / EXPIRE key window / EXEC`. Atomic.
- Tradeoff: network latency vs accuracy. Can allow slight over-limit for performance.
- Sliding window in Redis: sorted set with timestamps, `ZRANGEBYSCORE` to count.

## Stage 5 — Tiered limits + backoff (~10 min)
- Different limits for different tiers: free=10/min, pro=100/min, enterprise=1000/min.
- `RateLimiter(tiers={"free": (10, 60), "pro": (100, 60)})`.
- `allow(client_id, tier, timestamp)`.
- Add retry-after header: when denied, return seconds until next allowed request.

```python
def retry_after(self, client_id, timestamp):
    q = self.requests[client_id]
    if len(q) >= self.max_requests:
        return q[0] + self.window - timestamp  # when oldest expires
    return 0
```

## Talking points
- Fixed window vs sliding window vs token bucket — when to use each?
- Fixed: simplest, good enough for most cases. Sliding: most accurate. Token bucket: best for bursty traffic.
- Memory management: for sliding window, old client entries need cleanup (background sweep or LRU on client map).
- Real-world: Cloudflare, API gateways, nginx all use variations of these.
