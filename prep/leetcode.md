# Leetcode / General Coding Prep

~2 hours/day. Focus on pattern recognition and clean implementation under time pressure.

**Honest assessment:** LC-style pattern matching is the weakest interview skill right now. D.E. Shaw Round 1 showed this. The fix isn't grinding hundreds of problems — it's drilling the 6-8 patterns that cover 90% of what you'll see, and building muscle memory for the data structures behind them.

**Where this applies:** SpaceX take-home (Codility, after recruiter call), any surprise LC round

---

## Priority 1: Patterns You Must Own (Days 1-4)

These are the patterns that show up in >80% of implementation-style interviews. Master these before anything else.

### 1A. Hash Maps / Frequency Counting
The single most important primitive. If you don't know what data structure to use, it's probably a dict.

**Drill:** Given a list, count occurrences, find duplicates, group by key, build lookup tables.

**Practice problems:**
- Two Sum (LC #1) — 5 min max. If this takes longer, the fundamentals need work.
- Group Anagrams (LC #49) — sorting + dict grouping
- Top K Frequent Elements (LC #347) — Counter + heapq

**Pattern to internalize:**
```python
from collections import Counter, defaultdict
counts = Counter(items)
groups = defaultdict(list)
for item in items:
    groups[key(item)].append(item)
```

### 1B. Sliding Window / Two Pointers
Shows up in string problems, subarray problems, and interval problems.

**Drill:** Find longest/shortest substring with property X. Find subarray with sum = k.

**Practice problems:**
- Longest Substring Without Repeating Characters (LC #3)
- Minimum Window Substring (LC #76)
- Container With Most Water (LC #11)

**Pattern to internalize:**
```python
left = 0
for right in range(len(s)):
    # expand window
    while window_invalid():
        # shrink from left
        left += 1
    # update answer
```

### 1C. Sorting + Custom Comparators
Many "medium" problems become trivial if you sort first.

**Drill:** Sort by custom key, merge intervals, meeting rooms.

**Practice problems:**
- Merge Intervals (LC #56) — **critical for Laurion/Scale**
- Meeting Rooms II (LC #253)
- Sort Colors (LC #75) — Dutch national flag

### 1D. Stack-Based Problems
Expression parsing, matching brackets, monotonic stack.

**Practice problems:**
- Valid Parentheses (LC #20)
- `stack_machine.md` (from games/) — verified interview problem
- `expression_parser.md` (from games/) — verified interview problem
- Daily Temperatures (LC #739) — monotonic stack

---

## Priority 2: Trees, Graphs, BFS/DFS (Days 5-7)

These show up in grid problems, dependency resolution, and game implementations.

### 2A. BFS/DFS on Grids
**Drill:** Flood fill, shortest path, connected components.

**Practice problems:**
- Number of Islands (LC #200) — BFS/DFS on grid
- `minesweeper.md` (from games/) — flood fill + grid logic
- `snake.md` (from games/) — BFS pathfinding
- Shortest Path in Binary Matrix (LC #1091)

**Pattern to internalize:**
```python
from collections import deque
def bfs(grid, start):
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
```

### 2B. Tree Traversal
**Practice problems:**
- Binary Tree Level Order Traversal (LC #102)
- `merkle_tree.md` (from games/) — immutable tree + hashing
- Serialize/Deserialize Binary Tree (LC #297)

### 2C. Topological Sort / Dependency Graphs
**Practice problems:**
- Course Schedule (LC #207) — cycle detection
- `spreadsheet.md` (from games/) — dependency graph + eval

---

## Priority 3: Advanced Patterns (Days 8+)

Only if Priority 1 and 2 are solid.

### 3A. Heap / Priority Queue
**Practice problems:**
- `order_book.md` (from games/) — trading firm staple
- Merge K Sorted Lists (LC #23)
- `rate_limiter.md` (from games/) — state management

### 3B. Dynamic Programming (LOW PRIORITY)
Mark's profile doesn't attract DP-heavy interviews. Only prep if a specific company requires it.
- Coin Change (LC #322) — classic bottom-up
- Longest Common Subsequence (LC #1143)

---

## Daily Practice Protocol

**Timer:** Always use a timer. 45 minutes per problem, talk out loud.

**Week 1 Schedule (W08 Thu-Fri + W09):**
| Day | Focus | Time | Problems |
|-----|-------|------|----------|
| Thu 2/20 | (Laurion + SpaceX day — no LC) | — | — |
| Fri 2/21 | Hash maps + sorting | 2 hrs | Two Sum, Group Anagrams, Merge Intervals |
| Sat 2/22 | Sliding window + stack | 2 hrs | LC #3, LC #76, Valid Parens, stack_machine |
| Sun 2/23 | Grids + BFS | 2 hrs | Islands, minesweeper, snake |
| Mon 2/24 | (Scale AI day — review, no new problems) | 1 hr | Review weak spots from Sat/Sun |
| Tue 2/25 | Trees + topo sort | 2 hrs | spreadsheet, merkle_tree, Course Schedule |

**After each problem:**
1. Did I identify the pattern in <5 min? If no, what was the blocker?
2. Did I write clean code on first pass? Where did I get messy?
3. What edge cases did I miss?

---

## The "Build-a-Thing" Problems (Already in Repo)

These are more valuable than pure LC for most of your interviews. See `interview_problems/games/README.md` for full list.

**Priority order for remaining prep:**
1. `poker_hands.md` — #1 Scale AI problem, OOP + card logic
2. `in_memory_database.md` — state management, transactions
3. `interval_scheduler.md` — intervals, #2 Scale AI problem
4. `rate_limiter.md` — sliding window, state management
5. `connect_four.md` — grid logic, verified interview problem
6. `unit_conversion.md` — graph traversal, verified interview problem

**45-minute protocol:** Same as the README — set timer, talk out loud, aim for Stage 3, don't rush past Stage 2.
