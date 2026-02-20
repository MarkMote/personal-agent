# Scale AI — Templates & Primitives

Reference sheet for structured data processing interviews. Most foundational at top.

**Practice data files (in `prep/scale/`):**
- `example_data.json` — annotation sessions with workers, timestamps, overlaps, edge cases
- `event_stream.json` — 30 timestamped user events for stream analysis
- `structured_dataset.json` — 20 categorized records with values for stats/grouping

---

## 1. Load JSON

```python
import json

# From file
with open("prep/scale/example_data.json") as f:
    data = json.load(f)

# Extract the sessions list from nested structure
records = data["sessions"]
print(f"Loaded {len(records)} sessions")

# From a flat JSON array (event_stream.json)
with open("prep/scale/event_stream.json") as f:
    events = json.load(f)
print(f"Loaded {len(events)} events")
```

## 2. Navigate Nested Structures

```python
# Using records from example_data.json
for record in records:
    worker = record.get("worker_id", "unknown")
    items = record.get("items_labeled", 0)

    # Nested safe access (metadata can be null in this dataset)
    meta = record.get("metadata") or {}
    region = meta.get("region", "unspecified")

# Filter out records with missing required fields
clean = [r for r in records if r.get("start") and r.get("end")]
print(f"Cleaned: {len(records)} -> {len(clean)}")
```

## 3. Parse Timestamps

```python
from datetime import datetime, timedelta, timezone

def parse_ts(ts_str):
    """Parse ISO timestamp with Z suffix."""
    return datetime.fromisoformat(ts_str.replace("Z", "+00:00"))

# Parse all sessions from example_data.json
for r in clean:
    r["start_dt"] = parse_ts(r["start"])
    r["end_dt"] = parse_ts(r["end"])
    print(f"{r['session_id']}: {r['start_dt']} -> {r['end_dt']}")

# Other formats you might see:
# datetime.strptime("2024-01-15 09:00:00", "%Y-%m-%d %H:%M:%S")
# datetime.fromtimestamp(1705312800, tz=timezone.utc)

# Common format strings:
# "%Y-%m-%dT%H:%M:%SZ"      — ISO with Z
# "%Y-%m-%d %H:%M:%S"       — space separated
# "%m/%d/%Y %I:%M %p"       — US format with AM/PM
```

## 4. Time Duration Math

```python
# Using parsed sessions from example_data.json
for r in clean:
    duration = r["end_dt"] - r["start_dt"]
    minutes = duration.total_seconds() / 60
    print(f"{r['session_id']}: {minutes:.0f} min")
```

## 5. Sort Intervals

```python
# Sort cleaned sessions by start time
clean.sort(key=lambda r: r["start_dt"])
for r in clean:
    print(f"{r['session_id']} ({r['worker_id']}): {r['start_dt'].strftime('%H:%M')} - {r['end_dt'].strftime('%H:%M')}")
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

# Test with worker w1 from example_data.json
w1 = [r for r in clean if r["worker_id"] == "w1"]
w1_intervals = [(r["start_dt"], r["end_dt"]) for r in w1]
w1_intervals.sort(key=lambda x: x[0])
w1_merged = merge_intervals(w1_intervals)
for s, e in w1_merged:
    print(f"  {s.strftime('%H:%M')} - {e.strftime('%H:%M')} ({(e-s).total_seconds()/60:.0f} min)")
total_active = sum((e - s).total_seconds() / 60 for s, e in w1_merged)
print(f"Total active: {total_active:.0f} min")
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

# Test with w1's merged intervals
w1_gaps = compute_gaps(w1_merged)
for s, e in w1_gaps:
    print(f"  Gap: {s.strftime('%H:%M')} - {e.strftime('%H:%M')} ({(e-s).total_seconds()/60:.0f} min)")
total_idle = sum((e - s).total_seconds() / 60 for s, e in w1_gaps)
print(f"Total idle: {total_idle:.0f} min")
```

## 8. Group By Key

```python
from collections import defaultdict

# Group cleaned sessions by worker
by_worker = defaultdict(list)
for record in clean:
    by_worker[record["worker_id"]].append(record)

for worker_id, sessions in by_worker.items():
    print(f"{worker_id}: {len(sessions)} sessions")
```

## 9. Basic Statistics

```python
# Compute durations for all clean sessions
durations_min = [(r["end_dt"] - r["start_dt"]).total_seconds() / 60 for r in clean]

total = sum(durations_min)
count = len(durations_min)
mean_val = total / count
minimum = min(durations_min)
maximum = max(durations_min)
sorted_vals = sorted(durations_min)
median_val = sorted_vals[count // 2] if count % 2 == 1 else (sorted_vals[count//2 - 1] + sorted_vals[count//2]) / 2

print(f"Sessions: {count}, Mean: {mean_val:.1f} min, Median: {median_val:.1f} min, Min: {minimum:.0f}, Max: {maximum:.0f}")

# Or use statistics module
from statistics import mean, median, stdev
print(f"Mean: {mean(durations_min):.1f}, Median: {median(durations_min):.1f}, Stdev: {stdev(durations_min):.1f}")
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
    total_items = sum(s.get("items_labeled", 0) for s in sessions)
    active_hrs = sum(durations) / 60

    return {
        "worker_id": worker_id,
        "num_sessions": len(sessions),
        "total_active_min": sum(durations),
        "avg_session_min": sum(durations) / len(durations) if durations else 0,
        "total_idle_min": sum(gap_durations),
        "longest_session_min": max(durations) if durations else 0,
        "longest_gap_min": max(gap_durations) if gap_durations else 0,
        "total_items": total_items,
        "items_per_hour": total_items / active_hrs if active_hrs > 0 else 0,
    }

# Run on all workers from example_data.json
for worker_id, sessions in by_worker.items():
    summary = summarize_worker(worker_id, sessions)
    print(f"\n{worker_id}:")
    for k, v in summary.items():
        print(f"  {k}: {v:.1f}" if isinstance(v, float) else f"  {k}: {v}")
```

## 11. Output as JSON

```python
result = {"workers": [summarize_worker(w, s) for w, s in by_worker.items()]}
print(json.dumps(result, indent=2, default=str))
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
