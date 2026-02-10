# Thursday 2/12 — System Building I

---

## Core 1: Transactional Key-Value Store

Implement an in-memory key-value store with nested transactions.

```python
class TxnKVStore:
    def __init__(self): ...
    def get(self, key: str) -> Optional[str]: ...
    def set(self, key: str, value: str) -> None: ...
    def delete(self, key: str) -> None: ...
    def begin(self) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
```

**Operations:**
1. `get(key)` — Return most-recently-set value in current transactional context. If deleted, return None. If no transaction, fall back to global store.
2. `set(key, value)` — Upsert in current context only. Does not affect outer contexts until commit.
3. `delete(key)` — Mark as deleted in current context. Subsequent get returns None. Does not delete from outer contexts until commit.
4. `begin()` — Start a new (possibly nested) transaction.
5. `commit()` — Merge innermost transaction into its parent. Raise RuntimeError if no open transaction.
6. `rollback()` — Discard innermost transaction. Raise RuntimeError if no open transaction.

**Implementation hint:** Maintain a stack of dicts. Each `begin()` pushes a new dict. `get()` walks the stack top-to-bottom. `commit()` merges top into the one below. `rollback()` pops the top. Use a sentinel value (like `_DELETED`) to mark deletions.

**Constraints:**
- All keys and values are non-empty strings.
- Max nested transactions ≤ 100.
- All operations O(1) excluding built-in dict ops.

**Example:**
```
store = TxnKVStore()
store.set("a", "1")
store.begin()
store.set("a", "2")
print(store.get("a"))      # "2"
store.rollback()
print(store.get("a"))      # "1"

store.begin()
store.delete("a")
print(store.get("a"))      # None
store.commit()
print(store.get("a"))      # None
```

---

## Core 2: Connect Four

Build a Connect Four game engine from scratch. Progressive — implement stages in order, stop wherever time runs out.

```python
class ConnectFour:
    def __init__(self, rows: int = 6, cols: int = 7): ...
    def drop_piece(self, col: int, player: int) -> bool: ...
    def check_win(self, player: int) -> bool: ...
    def is_full(self) -> bool: ...
    def undo_move(self) -> bool: ...
    def get_valid_columns(self) -> List[int]: ...
    def __str__(self) -> str: ...
```

**Stage 1 — Basic board (15 min):**
- Initialize a `rows x cols` grid (2D list, filled with 0).
- `drop_piece(col, player)` — Drop player's piece (1 or 2) into column. Piece falls to lowest empty row. Return False if column is full.
- `__str__()` — Print the board so you can see it.

**Stage 2 — Win detection (20 min):**
- `check_win(player)` — Check if player has 4 in a row: horizontal, vertical, diagonal (both directions).
- Approach: for each cell, check all 4 directions. Or: only check from the last dropped piece (more efficient).

**Stage 3 — Utilities (10 min):**
- `is_full()` — True if all columns are full.
- `get_valid_columns()` — Return list of columns that aren't full.
- `undo_move()` — Remove the most recently dropped piece. Use a move history stack. Return False if no moves to undo.

**Stage 4 — Play loop (10 min):**
- Write a simple `play()` function that alternates between player 1 and 2, prints the board, and announces the winner.

**Key practice:** Narrate your design decisions out loud as you build. "I'm using a 2D list because...", "For win detection, I'll check from the last move because..."

---

## Core 3: Spreadsheet with Dependency Graph

Implement a spreadsheet that supports cell references, on-demand recomputation, and cycle detection.

```python
class Spreadsheet:
    def __init__(self): ...
    def set(self, cell: str, value: str) -> None: ...
    def get(self, cell: str) -> int: ...
```

**Operations:**
1. `set(cell, value)` — Store a value or formula. Value is either:
   - An integer literal (e.g., `"42"`)
   - A formula: `"=SUM(B1,B2)"` where each argument is a cell identifier (A1-style)
   - If the formula introduces a cycle, raise `ValueError("cycle")` and leave spreadsheet unchanged.
   - Overwriting a cell removes old dependencies and installs new ones.
2. `get(cell)` — Return the evaluated integer value. Empty cells return 0. If a referenced cell has errors, raise `ValueError("bad ref")`.

**Implementation:**
- `graph`: dict mapping cell → set of cells it depends on.
- `formula`: dict mapping cell → raw formula string.
- `val`: dict mapping cell → cached integer value.
- Cycle detection: before accepting a new formula, do a DFS from the cell through its new dependencies. If you reach the cell again, it's a cycle.
- Evaluation: recursive — to evaluate a cell, evaluate all its dependencies first (topological order).

**Constraints:**
- Cell identifiers are Excel-style (A1, B3, etc.).
- Total cells ≤ 1000, dependencies per cell ≤ 10.
- Operations must be O(V+E) in the dependency graph.

**Example:**
```
sheet = Spreadsheet()
sheet.set("A1", "=SUM(B1,B2)")
sheet.set("B1", "10")
sheet.set("B2", "20")
sheet.get("A1")  # 30

sheet.set("B2", "=A1")  # raises ValueError("cycle")
sheet.get("B2")          # still 20 (unchanged)
```

---

## Non-Core 1: ReAct Agent Loop

Build a ReAct-style agent that alternates Thought → Action → Observation until Final Answer.

```python
import re
from typing import Callable

class ReActAgent:
    def __init__(self, llm: Callable[[str], str]):
        self.llm = llm

    def run(self, prompt: str, max_steps: int = 5) -> str: ...
    def _execute(self, action: str, arg: str) -> str: ...
```

**Contract:**
1. `llm` is an injected callable: takes the full prompt so far, returns next LLM text.
2. Loop: append user prompt → generate Thought → generate Action → execute tool → append Observation → repeat.
3. Stop when LLM emits a line starting with `Final Answer:` (case-insensitive). Return everything after that prefix.
4. If `max_steps` exceeded, raise `RuntimeError("max steps")`.

**Tools:**
- `search(query)` — returns mock result string.
- `calculate(expr)` — returns `str(eval(expr))` (assume safe arithmetic).

**Parsing:** Use regex `^Action: (\w+)\((.+?)\)$` to extract tool name and argument.

**Example trace:**
```
Thought: I need to find the capital of France.
Action: search(capital of France)
Observation: Paris is the capital city of France.
Thought: Now I know the answer.
Final Answer: Paris
```

**Key things to get right:**
- Build the prompt string incrementally (append each step).
- Handle malformed actions (tool not found, bad regex match).
- The LLM is mocked — focus on the loop logic, not the LLM.

---

## Non-Core 2: Log Parser & Aggregator

Build a log ingestion and query system.

```python
from collections import defaultdict
from typing import List

class LogAggregator:
    def __init__(self):
        self.logs = []

    def ingest(self, log: str) -> None: ...
    def query(self, start: int, end: int, group_by: str) -> List[str]: ...
```

**Operations:**
1. `ingest(log)` — Parse a log string: `<timestamp> "<level>" <component> "<message>"`. Store parsed entry. Silently ignore invalid format.
2. `query(start, end, group_by)` — Return aggregated counts in time window [start, end] inclusive.
   - `group_by` is `"level"` or `"component"`.
   - Output format: `"<group>:<count>"` sorted by descending count, then alphabetically for ties.

**Constraints:**
- Up to 10^5 ingest calls.
- Query must be O(k + g log g) where k = logs in window, g = number of groups.
- Memory O(n).

**Example:**
```
agg = LogAggregator()
agg.ingest('1620001010 "INFO" auth "login-ok"')
agg.ingest('1620001011 "ERROR" db "conn-fail"')
agg.ingest('1620001012 "INFO" auth "logout"')
agg.query(1620001010, 1620001012, "level")
# ['INFO:2', 'ERROR:1']
```

**Optimization hint:** Store logs sorted by timestamp. Use `bisect` for efficient range queries.

---

## Wildcard: System Design — LLM Agent Orchestration Platform

*(Talk-through exercise, no coding. ~1hr.)*

A company wants internal teams to define and run multi-step LLM agent workflows (e.g., "research topic → summarize → draft email → get approval → send").

**Talk through:**
- Execution model: DAG of steps? Linear chain? Branching/conditionals?
- Tool registry: how are tools registered, validated, sandboxed?
- Failure handling: retry, fallback, human-in-the-loop escalation?
- State: where does execution state live during a run?
- Observability: how do you debug a failed workflow 3 days later?
- Evaluation: how do you know if the agent did a good job?
