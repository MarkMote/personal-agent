OK we have roughly four days to prep for the anthropic interview. Going to run my thoughts on prepping by you and see what you think. no need to code anything yet. 

Crate templates. Both python files but also can concatenate them into a single searchable doc or nested structure for quick look up 

NOTE: template and projects must be python files that actually run


STEPS
- read the docs and compile the list of what should be in templates 
- do all the templates problems: having at least skimmed docs, should have an idea of how to for each 
- Do projects


Think about in terms of 
- Templates: primitives for each possible thing. Can range from build a tool to build a tool that does this specific thing, to read a pdf, and so on. Just the building blocks 
- Projects, string building blocks together into real agents 

How we should approach this: 
- We will approach it by doing two things:
	- build a list of templates in python
		- can organize multiple primitives into single file, e.g. file io tool calling
	- build a list of projects in python: I will do these after all templates are complete 
- For each of these two/ categories, AI will create a "solution" and "problem" python files. I'll learn by looking at the problem file, attempting it on my own, and then referencing the solution when i get stuck
	- Solution documents: clean implementations of the templates and projects as python files.  
	- Problem documents: structured similarly, but just specifies the things we need to build clearly so that i can attempt things on my own. If i code everything perfectly, the problem documents should match the solution documents more or less at the end. 
- We will prioritize these into a learning plan:
	- ie we need to order the templates and projects so that we can gradually build to more complex things
	- the most basic and fundamental things will be leaned first. e.g. how to call the api, how to call a tool.
	- having these ordered will also mean that if we have to timebox things and not make it to the end, we will have at least covered the basics. 
- How we should put this together
	- reference the information they gave me, speculate about potential problems, make sure we cover all the basics in the docs, look at examples in the cookbooks (good project ideas) and what kind of templates would be required for understanding the building blocks for that. 
	- should be heavily infuenced by Anthropics own docs and examples. We don't need to guess on a lot of this, much of the content is there already 
- Finally: since the interview is open book. I'll be able to come back to the templates during, which will potentially save time as I glue things together ]


I'll keep a set of notes to reference during interviews in addition to the python files. 

Note: we did something similar for a scale ai interview. I'll include an example below 
this interview was of course over somethign different but the format worked 
Note: we also had to create example data to make the projects, i can work with you on that. 

# Scale ai projects

```python
# src/interview_problems/scale/problems/event_stream/problem.py
#
# PROBLEM: Event Stream Analyzer
#
# Given events.json containing user activity events over a 10-hour window (08:00-18:00),
# compute the following:
#
# Part 1 — Stats & Grouping
#   a) Clean the data (remove events with null user or null timestamp)
#   b) Count events per user. Who is the most active user?
#   c) Count events per type. What is the most common event type?
#   d) For each user, compute their purchase rate (purchases / total events)
#
# Part 2 — Time Analysis
#   a) Bucket events into 1-hour windows (08:00-09:00, 09:00-10:00, etc.)
#      Which hour had the most activity?
#   b) Find all idle gaps longer than 30 minutes where no events occurred
#   c) Convert each user's events into "active sessions" — a session is a group
#      of events where each event is within 60 seconds of the previous one.
#      Report: per user, how many sessions and the average session duration.
#   d) Filter to only events between 10:00-14:00, recompute events per user.
#
# Handle messy data: e32 has null user, e37 has null timestamp.
#
# Output as formatted JSON
```

```python
# src/interview_problems/scale/problems/event_stream/solution.py
import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

DATA_DIR = Path(__file__).parent


# ==================== LOAD & CLEAN ====================

with open(DATA_DIR / "events.json") as f:
    raw = json.load(f)

window_start = datetime.fromisoformat(raw["window"]["start"].replace("Z", "+00:00"))
window_end = datetime.fromisoformat(raw["window"]["end"].replace("Z", "+00:00"))


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


# Clean: remove null user or null timestamp
events = [
    e for e in raw["events"]
    if e.get("user") is not None
    and e.get("ts") is not None
]

# Parse timestamps
for e in events:
    e["dt"] = parse_ts(e["ts"])

print(f"Cleaned: {len(raw['events'])} -> {len(events)} events")


# ==================== PART 1: STATS & GROUPING ====================

# 1b) Events per user
by_user = defaultdict(list)
for e in events:
    by_user[e["user"]].append(e)

print("\nEvents per user:")
for user, user_events in sorted(by_user.items()):
    print(f"  {user}: {len(user_events)}")

most_active = max(by_user, key=lambda u: len(by_user[u]))
print(f"Most active: {most_active} ({len(by_user[most_active])} events)")


# 1c) Events per type
by_type = defaultdict(int)
for e in events:
    by_type[e["type"]] += 1

print("\nEvents per type:")
for t, count in sorted(by_type.items(), key=lambda x: -x[1]):
    print(f"  {t}: {count}")

most_common = max(by_type, key=lambda t: by_type[t])
print(f"Most common: {most_common} ({by_type[most_common]})")


# 1d) Purchase rate per user
print("\nPurchase rates:")
for user, user_events in sorted(by_user.items()):
    purchases = sum(1 for e in user_events if e["type"] == "purchase")
    rate = purchases / len(user_events)
    print(f"  {user}: {purchases}/{len(user_events)} = {rate:.1%}")


# ==================== PART 2: TIME ANALYSIS ====================

# 2a) Bucket into 1-hour windows
def hour_bucket(dt):
    return dt.replace(minute=0, second=0, microsecond=0)


hourly = defaultdict(int)
for e in events:
    hourly[hour_bucket(e["dt"])] += 1

print("\nEvents per hour:")
for hour in sorted(hourly):
    print(f"  {hour.strftime('%H:%M')}: {hourly[hour]}")

peak_hour = max(hourly, key=lambda h: hourly[h])
print(f"Peak hour: {peak_hour.strftime('%H:%M')} ({hourly[peak_hour]} events)")


# 2b) Idle gaps > 30 minutes
sorted_events = sorted(events, key=lambda e: e["dt"])

gaps = []
for i in range(1, len(sorted_events)):
    prev_dt = sorted_events[i - 1]["dt"]
    curr_dt = sorted_events[i]["dt"]
    gap_min = (curr_dt - prev_dt).total_seconds() / 60
    if gap_min > 30:
        gaps.append((prev_dt, curr_dt, gap_min))

print(f"\nIdle gaps > 30 min:")
for start, end, mins in gaps:
    print(f"  {start.strftime('%H:%M')} - {end.strftime('%H:%M')} ({mins:.0f} min)")


# 2c) Active sessions — events within 60 sec of each other
def build_sessions(user_events, threshold_sec=60):
    sorted_evts = sorted(user_events, key=lambda e: e["dt"])
    if not sorted_evts:
        return []

    sessions = []
    session_start = sorted_evts[0]["dt"]
    session_end = sorted_evts[0]["dt"]

    for e in sorted_evts[1:]:
        if (e["dt"] - session_end).total_seconds() <= threshold_sec:
            session_end = e["dt"]
        else:
            sessions.append((session_start, session_end))
            session_start = e["dt"]
            session_end = e["dt"]

    sessions.append((session_start, session_end))
    return sessions


print("\nActive sessions per user:")
for user in sorted(by_user):
    sessions = build_sessions(by_user[user])
    durations = [(e - s).total_seconds() for s, e in sessions]
    avg_dur = sum(durations) / len(durations) if durations else 0
    print(f"  {user}: {len(sessions)} sessions, avg duration {avg_dur:.0f}s")


# 2d) Filter to 10:00-14:00, recompute per user
filter_start = parse_ts("2024-03-01T10:00:00Z")
filter_end = parse_ts("2024-03-01T14:00:00Z")

filtered = [e for e in events if filter_start <= e["dt"] <= filter_end]

filtered_by_user = defaultdict(int)
for e in filtered:
    filtered_by_user[e["user"]] += 1

print(f"\nEvents per user (10:00-14:00 only):")
for user, count in sorted(filtered_by_user.items(), key=lambda x: -x[1]):
    print(f"  {user}: {count}")


# ==================== OUTPUT ====================

report = {
    "total_clean_events": len(events),
    "most_active_user": most_active,
    "most_common_type": most_common,
    "peak_hour": peak_hour.strftime("%H:%M"),
    "idle_gaps_over_30min": len(gaps),
    "users": {}
}

for user in sorted(by_user):
    user_events = by_user[user]
    sessions = build_sessions(user_events)
    purchases = sum(1 for e in user_events if e["type"] == "purchase")
    durations = [(e - s).total_seconds() for s, e in sessions]

    report["users"][user] = {
        "total_events": len(user_events),
        "purchases": purchases,
        "purchase_rate": round(purchases / len(user_events), 3),
        "num_sessions": len(sessions),
        "avg_session_duration_sec": round(sum(durations) / len(durations)) if durations else 0,
    }

print(f"\n{json.dumps(report, indent=2)}")

with open(DATA_DIR / "report.json", "w") as f:
    json.dump(report, f, indent=2)


if __name__ == "__main__":
    pass
```


## Scale AI templates

```python 
# src/interview_problems/scale/templates/intervals.py
from datetime import datetime


#########################
## Sample data
#########################

raw_intervals = [
    ("2024-01-15T10:00:00Z", "2024-01-15T10:45:00Z"),
    ("2024-01-15T09:00:00Z", "2024-01-15T09:30:00Z"),
    ("2024-01-15T09:15:00Z", "2024-01-15T10:15:00Z"),
    ("2024-01-15T13:00:00Z", "2024-01-15T14:00:00Z"),
]


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


intervals = [(parse_ts(s), parse_ts(e)) for s, e in raw_intervals]


#########################
## Sort by start time (required before merge)
#########################

intervals.sort(key=lambda x: x[0])

print("Sorted:")
for s, e in intervals:
    print(f"  {s.strftime('%H:%M')} - {e.strftime('%H:%M')}")


#########################
## Merge overlapping intervals
#########################

def merge_intervals(intervals):
    """intervals must be sorted by start."""
    if not intervals:
        return []
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # overlap or adjacent
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


merged = merge_intervals(intervals)

print("\nMerged:")
for s, e in merged:
    mins = (e - s).total_seconds() / 60
    print(f"  {s.strftime('%H:%M')} - {e.strftime('%H:%M')} ({mins:.0f} min)")

total_active = sum((e - s).total_seconds() / 60 for s, e in merged)
print(f"Total active: {total_active:.0f} min")


#########################
## Compute gaps between intervals
#########################

def compute_gaps(intervals):
    """intervals must be sorted and non-overlapping (run merge first)."""
    gaps = []
    for i in range(1, len(intervals)):
        gap_start = intervals[i - 1][1]
        gap_end = intervals[i][0]
        if gap_end > gap_start:
            gaps.append((gap_start, gap_end))
    return gaps


gaps = compute_gaps(merged)

print("\nGaps:")
for s, e in gaps:
    mins = (e - s).total_seconds() / 60
    print(f"  {s.strftime('%H:%M')} - {e.strftime('%H:%M')} ({mins:.0f} min)")

total_idle = sum((e - s).total_seconds() / 60 for s, e in gaps)
print(f"Total idle: {total_idle:.0f} min")


#########################
## Tests — edge cases an interviewer would expect you to handle
#########################

def test_merge_intervals():
    p = parse_ts

    # Empty input
    assert merge_intervals([]) == []

    # Single interval — nothing to merge
    assert merge_intervals([(p("2024-01-15T09:00:00Z"), p("2024-01-15T10:00:00Z"))]) == \
        [(p("2024-01-15T09:00:00Z"), p("2024-01-15T10:00:00Z"))]

    # No overlap — all intervals are disjoint
    no_overlap = [(p("2024-01-15T09:00:00Z"), p("2024-01-15T10:00:00Z")),
                  (p("2024-01-15T11:00:00Z"), p("2024-01-15T12:00:00Z"))]
    assert merge_intervals(no_overlap) == no_overlap

    # Full overlap — one interval contains the other
    contained = [(p("2024-01-15T09:00:00Z"), p("2024-01-15T12:00:00Z")),
                 (p("2024-01-15T10:00:00Z"), p("2024-01-15T11:00:00Z"))]
    assert merge_intervals(contained) == [(p("2024-01-15T09:00:00Z"), p("2024-01-15T12:00:00Z"))]

    # Adjacent — end of one equals start of next (should merge)
    adjacent = [(p("2024-01-15T09:00:00Z"), p("2024-01-15T10:00:00Z")),
                (p("2024-01-15T10:00:00Z"), p("2024-01-15T11:00:00Z"))]
    assert merge_intervals(adjacent) == [(p("2024-01-15T09:00:00Z"), p("2024-01-15T11:00:00Z"))]

    # Chain of overlaps — A overlaps B, B overlaps C → all merge into one
    chain = [(p("2024-01-15T09:00:00Z"), p("2024-01-15T10:00:00Z")),
             (p("2024-01-15T09:30:00Z"), p("2024-01-15T10:30:00Z")),
             (p("2024-01-15T10:15:00Z"), p("2024-01-15T11:00:00Z"))]
    assert merge_intervals(chain) == [(p("2024-01-15T09:00:00Z"), p("2024-01-15T11:00:00Z"))]

    # Zero-duration interval
    zero = [(p("2024-01-15T09:00:00Z"), p("2024-01-15T09:00:00Z")),
            (p("2024-01-15T10:00:00Z"), p("2024-01-15T11:00:00Z"))]
    assert len(merge_intervals(zero)) == 2  # no overlap, stays separate

    print("All merge tests passed")


def test_compute_gaps():
    p = parse_ts

    # No gaps (single interval)
    assert compute_gaps([(p("2024-01-15T09:00:00Z"), p("2024-01-15T10:00:00Z"))]) == []

    # One gap between two intervals
    two = [(p("2024-01-15T09:00:00Z"), p("2024-01-15T10:00:00Z")),
           (p("2024-01-15T11:00:00Z"), p("2024-01-15T12:00:00Z"))]
    gaps = compute_gaps(two)
    assert len(gaps) == 1
    assert (gaps[0][1] - gaps[0][0]).total_seconds() / 60 == 60

    # Adjacent intervals — no gap
    adjacent = [(p("2024-01-15T09:00:00Z"), p("2024-01-15T10:00:00Z")),
                (p("2024-01-15T10:00:00Z"), p("2024-01-15T11:00:00Z"))]
    assert compute_gaps(adjacent) == []

    # Empty input
    assert compute_gaps([]) == []

    print("All gap tests passed")


test_merge_intervals()
test_compute_gaps()


if __name__ == "__main__":
    pass

```


```python
# src/interview_problems/scale/templates_manual/intervals.py


#########################
## 1. Parse and sort — parse these raw interval strings into datetimes, sort by start time
#########################

raw_intervals = [
    ("2024-01-15T10:00:00Z", "2024-01-15T10:45:00Z"),
    ("2024-01-15T09:00:00Z", "2024-01-15T09:30:00Z"),
    ("2024-01-15T09:15:00Z", "2024-01-15T10:15:00Z"),
    ("2024-01-15T13:00:00Z", "2024-01-15T14:00:00Z"),
]


#########################
## 2. Merge overlapping — write merge_intervals(intervals) that combines overlapping/adjacent intervals.
# Input must be sorted.
#########################



#########################
## 3. Compute gaps — write compute_gaps(intervals)
#  that finds the gaps between non-overlapping intervals. 
# Input must be sorted and merged.
#########################



#########################
## 4. Compute totals — calculate total active time and total idle time in minutes
#########################
```


---


Here are the instructions we got from anthropic:
"
As a next step, we'd like you to do a technical interview in Python. This technical interview will test your familiarity with Agents, prompting LLMs, and coding with LLMs as building blocks. The interview will be completed in a virtual coding environment like Colab that your interviewer will send you at the start of the interview. No account setup is required in advance. This interview is open book, and we ask that you share your entire screen through Google Meet. You should be conceptually familiar with Tool Use and Agents and how they are handled in our API. If you haven't tried our tool using API previously, please take time to test it out before your scheduled interview.
"

