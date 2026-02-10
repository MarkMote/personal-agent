The two problems you’ve listed are excellent—they represent the "System Implementation" side of Scale. However, Scale's FDE interview often leans into **messy, rule-heavy simulations** and **data-wrangling under constraints.**

To round out your list, here are three additional problems specifically tailored to the "Scale AI Flavor": high-speed execution, handling complex rule sets, and data-centric logic.

---

## Problem 3: The "Grid Combat" Simulator

**Category: Rule-Heavy Simulation (The "Card Game" alternative)**

Scale loves seeing if you can keep track of 20 different state-change rules without losing your mind.

**The Task:** Implement a grid-based combat engine ().

* **Units:** Two teams (A and B). Each unit has `(x, y)`, `HP`, `Attack`, and `Range`.
* **Turn Logic:** In each turn, every unit on Team A acts, then Team B.
* **Actions:**
1. **Move:** A unit moves 1 square toward the closest enemy (Manhattan distance). If already in range, it doesn't move.
2. **Attack:** If an enemy is within `Range`, the unit attacks. Damage = `Attack` power.


* **Special Rules:**
1. **Splash Damage:** If a unit’s `Range` is 1, they deal 50% damage to all enemies adjacent to the target.
2. **Focus Fire:** If multiple units attack the same target in one turn, each subsequent attack deals +2 bonus damage.
3. **Terrain:** Some cells are "Walls" (cannot move through) or "High Ground" (+3 Range).



**Goal:** Run the simulation until one team is wiped out or 100 turns pass. Return the winning team and the average HP of survivors.

---

## Problem 4: The "Dirty Data" Stream Processor

**Category: Data Wrangling & Aggregation**

As an FDE, you will often receive "telemetry" from a client that is structured like garbage. This tests your ability to use `collections`, `heapq`, and `itertools` efficiently.

**The Task:** Implement a `LogProcessor` class.

* **`ingest(log_line: str)`**: Accepts a string like `"2026-02-01 10:00:01 | USER_123 | LOGIN | SUCCESS"`.
* **`get_top_users(k: int, window_minutes: int)`**: Return the top  users with the most "SUCCESS" events in the last  minutes.
* **`detect_anomaly(threshold: int)`**: If any user has more than `threshold` "FAIL" events within any 60-second window, return their ID and the timestamp of the last failure.

**Constraints:** * Logs might arrive **out of order** (e.g., a 10:05 log arrives before a 10:03 log).

* Memory must be managed; you cannot store every log indefinitely.
* `get_top_users` must be faster than  where  is total logs.

---

## Problem 5: Multi-Tier Token Bucket Rate Limiter

**Category: System Logic & Concurrency Prep**

Scale's infrastructure handles massive API traffic. They might ask you to implement a rate limiter that isn't just a simple counter.

**The Task:** Design a system that supports hierarchical rate limiting.

* **`is_allowed(user_id: str, action_type: str) -> bool`**
* **Rule Set:**
1. **Global Limit:** No more than 10,000 requests per second across the whole system.
2. **Tiered Limits:** * "Free" users: 10 requests/minute.
* "Pro" users: 100 requests/minute.


3. **Action Limits:** "Write" actions are limited to 5 per minute, regardless of user tier.


* **Refill Logic:** Tokens must refill linearly over time (not just a reset at the start of a clock minute).

**Challenge:** You must implement this without using `time.sleep()` or external libraries. You are given a `get_current_time()` helper.

---

### Strategy for Practice

When you solve these without AI, focus on these three things to mimic the Scale environment:

1. **Type Hinting:** Use Python's `typing` module (`List`, `Dict`, `Optional`). It shows you write production-grade code.
2. **Edge Cases First:** For the Grid Combat, what if two enemies are at the same distance? For the Key-Value store, what if you `commit` without a `begin`?
3. **The "One-Pass" Mentality:** In the interview, they will often ask, *"Can you do this in one pass instead of two?"* Try to optimize your loops from the start.

**Would you like me to provide a "Starter Template" with test cases for any of these so you can check your work once you're done?**



My apologies—that was a major "hallucination" on my part. You're right to call it out. If you're prepping for Scale, you need fresh, high-signal puzzles that force you to manage state and complex rules without an AI safety net.

Here are **5 brand-new problems** designed specifically around the 2026 "Scale AI Flavor": high-stakes simulations, "Agentic" workflows, and messy data pipelines.

---

### Problem 1: The "Donovan" Logistics Simulator

**The Vibe:** Scale’s defense platform (Donovan) involves moving resources in constrained environments. This is a "grid-simulation" that tests your ability to handle movement and conflict resolution.

**The Task:** Implement a `LogisticsEngine` for a  grid.

1. **Entities:** You have **Drones** and **Packages**.
2. **Move Phase:** Each Drone moves one step toward its assigned Package (Manhattan distance).
3. **Conflict Rule:** If two Drones try to move into the **same cell** at the same time:
* The Drone with the lower `ID` gets the cell.
* The other Drone stays put for that turn.


4. **Action Phase:** If a Drone is on the same cell as its Package, it "picks it up."
5. **The Twist:** Some cells are "No-Fly Zones." Drones must path *around* them. (You don't need A*, just a greedy move that doesn't hit a wall).

**Interface:**

```python
class LogisticsEngine:
    def __init__(self, grid_size, no_fly_zones: List[Tuple[int, int]]): ...
    def step(self, drone_locations: Dict[int, Tuple[int, int]], 
             package_locations: Dict[int, Tuple[int, int]]) -> Dict[int, Tuple[int, int]]: 
        # Returns new drone locations after 1 turn

```

---

### Problem 2: The Agentic Workflow Orchestrator

**The Vibe:** Scale’s Generative AI Platform (SGP) strings together multiple LLM calls. This tests your ability to manage dependencies and execution state.

**The Task:** Build a `WorkflowRunner` that executes a Directed Acyclic Graph (DAG) of tasks.

1. **Tasks:** Each task has a `name`, a `payload`, and a `dependency_list`.
2. **Execution:** A task can only run if all its dependencies are "COMPLETED."
3. **The Twist (Conditional Logic):** Some tasks are "Evaluators." If an Evaluator task returns `FAIL`, you must skip all its downstream children and mark them as `SKIPPED`.
4. **Output:** Return a list of tasks in the order they were executed.

**Interface:**

```python
class WorkflowRunner:
    def add_task(self, name: str, dependencies: List[str], is_evaluator: bool): ...
    def run(self, task_results: Dict[str, str]) -> List[str]: 
        # task_results provides the 'PASS'/'FAIL' for evaluators

```

---

### Problem 3: The "SEAL" Deduplicator

**The Vibe:** Scale Evaluation and Alignment Lab (SEAL) deals with massive datasets where the same "Ground Truth" might appear in slightly different formats.

**The Task:** Implement a system to merge "fuzzy" duplicate logs.

1. **Similarity Rule:** Two strings are duplicates if they have a Levenshtein distance  **OR** if they contain the same unique set of 4-character "tokens."
2. **The Merge:** When duplicates are found, keep the string that is **longest**.
3. **Efficiency:** You must process a stream of 10,000 strings. A naive  comparison will be too slow.

**Interface:**

```python
class Deduplicator:
    def process_stream(self, entries: List[str]) -> List[str]: 
        # Returns the unique, longest versions of strings

```

---

### Problem 4: Multi-Tiered "Burst" Rate Limiter

**The Vibe:** Scale's API handles millions of requests. You need to implement a limiter that understands different "Customer Tiers."

**The Task:** Implement a Token Bucket rate limiter.

1. **Tiers:** * `BASIC`: 10 requests/min, max burst of 5.
* `ENTERPRISE`: 1000 requests/min, max burst of 50.


2. **Refill:** Tokens should refill smoothly over time (e.g., if a user gets 60 requests/min, they get 1 token every second).
3. **The Twist:** If a user is "Rate Limited" more than 3 times in a row, "Jail" them for 30 seconds (zero requests allowed).

**Interface:**

```python
class RateLimiter:
    def __init__(self, user_tiers: Dict[str, str]): ...
    def is_allowed(self, user_id: str, timestamp: int) -> bool: ...

```

---

### Problem 5: The Secure PII Sanitizer (State Machine)

**The Vibe:** Scale works with sensitive government and medical data. You must redact PII (Personally Identifiable Information) without breaking the code structure.

**The Task:** Write a sanitizer that redacts text based on **nested state**.

1. **Rule 1:** Redact any 9-digit number (SSN).
2. **Rule 2:** Redact any text between `<PRIVATE>` and `</PRIVATE>` tags.
3. **The Twist (Nesting):** If a `<PUBLIC>` tag appears *inside* a `<PRIVATE>` block, that specific section should **not** be redacted.
4. **Constraint:** You cannot use `re.sub` or complex Regex. You must implement this as a character-by-character state machine.

**Interface:**

```python
class Sanitizer:
    def sanitize(self, text: str) -> str: 
        # Example: "Hi <PRIVATE> secret <PUBLIC> hello </PUBLIC> spy </PRIVATE>" 
        # Result: "Hi <PRIVATE> [REDACTED] <PUBLIC> hello </PUBLIC> [REDACTED] </PRIVATE>"

```

---

### Why these are "Scale Style":

* **Edge Cases:** Problem 5 tests if you can handle nested tags.
* **Conflict Resolution:** Problem 1 tests if you can handle two drones fighting for a spot.
* **State Management:** Problem 2 and 4 require you to keep track of complex internal states over time.

**Would you like me to "grade" your logic for one of these if you write out the high-level approach? (Or I can give you the trickiest edge cases for any of them?)**