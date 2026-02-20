# Scale AI — Practice Exercises

Use with `example_data.json`. Answers at the bottom.

---

## Exercise 1: Load and Clean (templates 1-2)

Load `example_data.json`. Extract the sessions list. Filter out sessions that have:
- null `end` timestamp
- zero-length duration (start == end)

Print how many sessions you started with and how many survived cleaning.

---

## Exercise 2: Parse Timestamps (template 3-4)

For each clean session, parse `start` and `end` into datetime objects. Add `duration_min` (float) to each record. Print the 3 longest sessions.

---

## Exercise 3: Group and Sort (templates 5, 8)

Group sessions by `worker_id`. For each worker, sort their sessions by start time. Print each worker's session count and their chronological session IDs.

---

## Exercise 4: Merge Intervals (template 6)

For each worker, merge their overlapping sessions. Print:
- worker_id
- number of raw sessions vs merged intervals
- total active minutes (from merged)

Note: w1 has overlapping sessions (s001 and s002). After merge those should become one interval 09:00-10:15.

---

## Exercise 5: Compute Gaps (template 7)

For each worker, compute the gaps between their merged intervals. Print:
- worker_id
- number of gaps
- total idle minutes
- longest gap in minutes

---

## Exercise 6: Full Summary (templates 9-11)

For each worker, produce a summary dict with:
- num_sessions, total_active_min, avg_session_min
- total_idle_min, longest_gap_min
- total_items_labeled, items_per_hour

Output the result as formatted JSON.

---

## Exercise 7: Cross-Worker Stats (template 9)

Across all workers, compute:
- Who labeled the most items total?
- Who had the highest items/hour rate?
- What was the busiest hour of the day? (most concurrent sessions)
- What's the overall median session duration?

---

## Exercise 8: Group by Task Type

Pivot the data by `task_type` instead of `worker_id`. For each task type compute:
- total sessions, total items labeled
- average duration
- average items per session

---

## Expected Answers

### Exercise 1
- Started with: 12 sessions
- After cleaning: 10 (removed s005 zero-length, s011 null end)

### Exercise 4 — Worker w1
- Raw sessions: 4 (s001, s002, s007, s010)
- s001 (09:00-09:45) + s002 (09:30-10:15) merge → 09:00-10:15 (75 min)
- s007 (13:00-14:00) stays → 60 min
- s010 (23:30-00:30) stays → 60 min
- Merged intervals: 3
- Total active: 195 min

### Exercise 4 — Worker w2
- Raw sessions: 3 (s003, s012, s004, s008)
- s003 (08:00-08:30) + s012 (08:15-08:45) merge → 08:00-08:45 (45 min)
- s004 (10:00-11:30) + s008 (11:00-11:45) merge → 10:00-11:45 (105 min)
- Merged intervals: 2
- Total active: 150 min

### Exercise 5 — Worker w1
- Gaps: 09:00-10:15 → 13:00-14:00 → 23:30-00:30
- Gap 1: 10:15 to 13:00 = 165 min
- Gap 2: 14:00 to 23:30 = 570 min
- Total idle: 735 min
- Longest gap: 570 min

### Exercise 5 — Worker w2
- Gap: 08:45 to 10:00 = 75 min
- Total idle: 75 min

### Exercise 6 — Worker w1
- num_sessions: 4, total_active: 195 min, avg_session: 48.75 min
- total_items: 86, items_per_hour: 86 / (195/60) = 26.5/hr

### Exercise 6 — Worker w3
- s006 (14:00-15:30) + s009 (15:00-16:00) merge → 14:00-16:00 (120 min)
- total_items: 70, items_per_hour: 35/hr
