# Scale AI Coding Prep

Structured data processing, JSON parsing, time/interval manipulation, and statistics.

**Interview:** Mon 2/24 9:30am ET. ~55 min, two parts (~25 min each).

**From their prep guide** (`prep/scale/interview_prep.md`):
- Data processing, time-based calculations, structured problem-solving
- Structured dataset → compute relevant statistics
- JSON data, basic data manipulations, interval calculations
- Implementation-heavy, NOT algorithmically complex
- Time at end to refactor and discuss testing strategies

This is NOT the OOP/rule-heavy format that older Scale reports suggest. The actual interview is data wrangling + time intervals + statistics. Clean modular code under time pressure.

---

## PART A: Core Skills (Drill These First)

### A1. JSON Parsing + Nested Data Extraction
You'll be handed a JSON blob and asked to extract, transform, and compute.

**Drill these operations until they're automatic:**
```python
import json
from collections import defaultdict

# Parse
data = json.loads(raw_string)

# Nested access with safety
value = data.get("key", {}).get("nested", default)

# Iterate structured records
for record in data["items"]:
    name = record["name"]
    ts = record.get("timestamp", 0)

# Group by a field
groups = defaultdict(list)
for record in data:
    groups[record["category"]].append(record)

# Flatten nested lists
flat = [item for sublist in nested for item in sublist]
```

**Practice:** Write a function that takes raw JSON and returns:
1. Count of records per category
2. Average of a numeric field per category
3. The record with the max value of field X

Time target: <10 min for all three.

### A2. Datetime / Time Manipulation
Scale's prep guide explicitly mentions time-based calculations and time intervals.

**Drill these:**
```python
from datetime import datetime, timedelta

# Parse ISO timestamp
dt = datetime.fromisoformat("2026-02-18T14:30:00")

# Parse Unix timestamp
dt = datetime.fromtimestamp(1708200600)

# Time difference
delta = dt2 - dt1
hours = delta.total_seconds() / 3600

# Generate time ranges
start = datetime(2026, 2, 18, 9, 0)
times = [start + timedelta(hours=i) for i in range(8)]

# Check if timestamp is within range
in_range = start <= ts <= end
```

### A3. Interval Merging / Gap Finding
Prep guide says "overlapping or sequential conditions" — this is intervals.

**Merge overlapping intervals:**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
```

**Find gaps between intervals:**
```python
def find_gaps(intervals, range_start, range_end):
    intervals.sort()
    gaps = []
    current = range_start
    for start, end in intervals:
        if start > current:
            gaps.append((current, start))
        current = max(current, end)
    if current < range_end:
        gaps.append((current, range_end))
    return gaps
```

**Compute overlap between two intervals:**
```python
def overlap(a, b):
    start = max(a[0], b[0])
    end = min(a[1], b[1])
    return max(0, end - start)
```

**Practice problems:**
- `interval_scheduler.md` (from games/) — #2 Scale AI problem, "Party Times"
- Merge Intervals (LC #56)
- Meeting Rooms II (LC #253)
- Employee Free Time (LC #759)

### A4. Computing Statistics from Data
Basic aggregation that should be instant:

```python
import statistics
from collections import Counter

values = [record["value"] for record in data]

# Basics
mean = sum(values) / len(values)
median = statistics.median(values)
mode = Counter(values).most_common(1)[0][0]
std_dev = statistics.stdev(values)

# Percentiles
sorted_vals = sorted(values)
p95 = sorted_vals[int(len(sorted_vals) * 0.95)]

# Rolling average
def rolling_avg(values, window):
    result = []
    for i in range(len(values) - window + 1):
        result.append(sum(values[i:i+window]) / window)
    return result

# Group statistics
from itertools import groupby
for key, group in groupby(sorted(data, key=keyfunc), key=keyfunc):
    group_values = list(group)
    # compute stats per group
```

---

## PART B: Practice Problems (Prioritized for Mon 2/24)

### B1. Data Processing + Time Intervals (matches prep guide exactly)

**Problem: Event Stream Analyzer** (custom — practice in 25 min)
Given JSON event data with timestamps:
1. Count events per hour, find peak hour
2. Compute rolling 5-minute event rate
3. Find gaps >5 min where no events occurred
4. Merge overlapping "active sessions" (events within 30 sec of each other)

**Problem: Structured Dataset Statistics** (custom — practice in 25 min)
Given a JSON dataset of records with categories, timestamps, and numeric values:
1. Group by category, compute mean/median/count per group
2. Filter to a time window, recompute
3. Find which category had the highest growth rate between two time periods
4. Handle missing values gracefully

### B2. From Existing Repo (closest matches to prep guide)

1. `interval_scheduler.md` — intervals + scheduling, **most aligned with prep guide**
2. `rate_limiter.md` — time-based state management, sliding window
3. Log Parser & Aggregator (from `00_general_problems.md`) — parse structured data, filter by time, group and sort
4. `poker_hands.md` — still good practice for structured data + rules (historically #1 most reported Scale problem)
5. `in_memory_database.md` — nested state management

### B3. From original/05_scale.md (if time)

6. Dirty Data Stream Processor — out-of-order logs, top-k users, anomaly detection
7. Agentic Workflow Orchestrator — DAG execution (may be less relevant given new prep guide)
8. Grid Combat Simulator — rule-heavy simulation (may be less relevant)

---

## PART C: Interview Day Checklist (Mon 2/24)

**Night before (Sun 2/23):**
- [ ] Do one full 25-min practice problem (interval_scheduler or rate_limiter)
- [ ] Review: `datetime`, `json`, `collections` (Counter, defaultdict, deque)
- [ ] Review: `statistics`, `itertools.groupby`, `bisect`
- [ ] Skim this doc's Part A code snippets

**Morning of:**
- [ ] 20-min warm-up: parse some JSON, compute group stats, merge intervals
- [ ] Review edge cases: empty data, missing fields, out-of-order timestamps, division by zero

**During the interview:**
- Ask clarifying questions before coding
- Talk through approach first — they want to see your thinking
- Break into helper functions immediately (they call this out in prep guide)
- Clear naming conventions — `compute_stats()` not `f()`
- Handle edge cases: missing values, empty groups, boundary timestamps
- Save 3-5 min at end for refactoring + testing discussion
- Be ready to discuss: "what tests would you write?" and "what would break this?"

---

## Key Libraries to Know Cold

```python
# Data processing
import json
from collections import Counter, defaultdict, deque, OrderedDict
from datetime import datetime, timedelta, timezone
from itertools import groupby, chain
import bisect
import heapq
import re
import csv
import statistics

# Useful patterns
# bisect for sorted insertion / binary search in sorted lists
# heapq for top-k, priority queues
# deque for sliding windows, BFS
# OrderedDict for LRU cache
```
