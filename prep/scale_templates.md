# Scale AI — Templates & Primitives

Reference sheet for structured data processing interviews. Most foundational at top.

---

## 1. Load JSON

```python
import json

# From string
data = json.loads('{"key": "value"}')

# From file
with open("data.json") as f:
    data = json.load(f)

# From nested JSON — extract a list of records
records = data["results"]  # or data["data"]["sessions"] etc.
```

## 2. Navigate Nested Structures

```python
# Safe access with defaults
worker = record.get("worker_id", "unknown")
items = record.get("items_labeled", 0)

# Nested safe access
meta = record.get("metadata", {})
region = meta.get("region", "unspecified")

# Filter out records with missing required fields
clean = [r for r in records if r.get("start") and r.get("end")]
```

## 3. Parse Timestamps

```python
from datetime import datetime, timedelta, timezone

# ISO format (most common)
dt = datetime.fromisoformat("2024-01-15T09:00:00Z".replace("Z", "+00:00"))

# Custom format
dt = datetime.strptime("2024-01-15 09:00:00", "%Y-%m-%d %H:%M:%S")

# Unix timestamp
dt = datetime.fromtimestamp(1705312800, tz=timezone.utc)

# Common formats to know:
# "%Y-%m-%dT%H:%M:%SZ"      — ISO with Z
# "%Y-%m-%d %H:%M:%S"       — space separated
# "%m/%d/%Y %I:%M %p"       — US format with AM/PM
```

## 4. Time Duration Math

```python
start = datetime.fromisoformat("2024-01-15T09:00:00+00:00")
end = datetime.fromisoformat("2024-01-15T09:45:00+00:00")

duration = end - start                    # timedelta
seconds = duration.total_seconds()        # 2700.0
minutes = duration.total_seconds() / 60   # 45.0
hours = duration.total_seconds() / 3600   # 0.75
```

## 5. Sort Intervals

```python
# intervals = [(start_dt, end_dt), ...]
intervals.sort(key=lambda x: x[0])

# From records
sessions = [(r["start_dt"], r["end_dt"], r) for r in records]
sessions.sort(key=lambda x: x[0])
```

## 6. Merge Overlapping Intervals

```python
def merge_intervals(intervals):
    """intervals = [(start, end), ...] — must be sorted by start."""
    if not intervals:
        return []
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # overlap
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged

# Total active time from merged intervals
total = sum((end - start).total_seconds() for start, end in merged)
```

## 7. Compute Gaps Between Intervals

```python
def compute_gaps(intervals):
    """intervals = [(start, end), ...] — must be sorted and non-overlapping."""
    gaps = []
    for i in range(1, len(intervals)):
        gap_start = intervals[i-1][1]
        gap_end = intervals[i][0]
        if gap_end > gap_start:
            gaps.append((gap_start, gap_end))
    return gaps

# Total idle time
idle = sum((end - start).total_seconds() for start, end in gaps)
```

## 8. Group By Key

```python
from collections import defaultdict

# Group records by a field
by_worker = defaultdict(list)
for record in records:
    by_worker[record["worker_id"]].append(record)

# Now process per group
for worker_id, sessions in by_worker.items():
    ...
```

## 9. Basic Statistics (no imports needed)

```python
values = [45, 30, 60, 15, 90]

total = sum(values)
count = len(values)
mean = total / count
minimum = min(values)
maximum = max(values)
sorted_vals = sorted(values)
median = sorted_vals[count // 2] if count % 2 == 1 else (sorted_vals[count//2 - 1] + sorted_vals[count//2]) / 2

# Or use statistics module
from statistics import mean, median, stdev
```

## 10. Build Summary Dict

```python
def summarize_worker(worker_id, sessions):
    intervals = [(s["start_dt"], s["end_dt"]) for s in sessions]
    intervals.sort(key=lambda x: x[0])
    merged = merge_intervals(intervals)
    gaps = compute_gaps(merged)

    durations = [(end - start).total_seconds() / 60 for start, end in merged]
    gap_durations = [(end - start).total_seconds() / 60 for start, end in gaps]

    return {
        "worker_id": worker_id,
        "num_sessions": len(sessions),
        "total_active_min": sum(durations),
        "avg_session_min": sum(durations) / len(durations) if durations else 0,
        "total_idle_min": sum(gap_durations),
        "longest_session_min": max(durations) if durations else 0,
        "longest_gap_min": max(gap_durations) if gap_durations else 0,
    }
```

## 11. Output as JSON

```python
import json

result = {"workers": [summarize_worker(w, s) for w, s in by_worker.items()]}
print(json.dumps(result, indent=2, default=str))  # default=str handles datetimes
```

## 12. Edge Cases Checklist

- [ ] Missing/null fields → `.get()` with defaults
- [ ] Zero-length intervals (start == end) → filter or handle
- [ ] Unsorted input → always sort before merge
- [ ] Single record per group → avoid division by zero
- [ ] Timestamps crossing midnight → timedelta handles this fine
- [ ] Timezone-aware vs naive datetimes → don't mix, pick one
- [ ] Duplicate records → deduplicate by (worker, start, end) if needed
- [ ] Empty input → return empty results, don't crash
