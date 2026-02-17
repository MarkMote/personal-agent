# Spreadsheet Engine

**Task:** Build a spreadsheet. Cells hold numbers, strings, or formulas (e.g. `"=A1+B2"`). `get(cell)` evaluates the cell's value, resolving any references to other cells. Handle dependency chains and detect circular references.

```python
class Spreadsheet:
    def __init__(self, rows: int = 26, cols: int = 10): ...
    def set(self, cell: str, value: str) -> None: ...
    def get(self, cell: str) -> float | str: ...
```

## Stage 1 — Static values (~10 min)
- `set("A1", "42")` — Store value in cell.
- `get("A1")` → `42.0` (if numeric) or `"hello"` (if text).
- Cell names: column letter + row number. "A1", "B3", "Z10".
- Parse cell name: `col = ord(cell[0]) - ord('A')`, `row = int(cell[1:]) - 1`.
- Storage: 2D dict or dict keyed by cell name.

```python
class Spreadsheet:
    def __init__(self):
        self.cells = {}  # cell_name -> raw value (str)
        self.cache = {}  # cell_name -> computed value

    def set(self, cell: str, value: str):
        self.cells[cell] = value
        self.cache.pop(cell, None)  # invalidate

    def get(self, cell: str):
        if cell not in self.cells:
            return None
        raw = self.cells[cell]
        try:
            return float(raw)
        except ValueError:
            return raw
```

## Stage 2 — Formulas with cell references (~15 min)
- `set("A1", "5")`, `set("A2", "10")`, `set("A3", "=A1+A2")` → `get("A3")` returns 15.
- Formulas start with `=`. Support `+`, `-`, `*`, `/` and cell references.
- Tokenize the formula, replace cell references with their values, evaluate.

```python
import re

def evaluate(self, cell: str) -> float:
    raw = self.cells.get(cell, "0")
    if not raw.startswith("="):
        return float(raw) if raw.replace(".", "").replace("-", "").isdigit() else raw

    formula = raw[1:]  # strip '='
    # Replace cell refs with their values
    def resolve(match):
        ref = match.group(0)
        return str(self.evaluate(ref))

    resolved = re.sub(r'[A-Z]\d+', resolve, formula)
    return eval(resolved)  # simple but works; discuss security tradeoffs
```

- Note: `eval` is fine for an interview. Mention you'd use a proper parser in production.

## Stage 3 — Circular reference detection (~15 min)
- `set("A1", "=B1")`, `set("B1", "=A1")` → circular reference error.
- Build dependency graph: for each formula cell, record which cells it references.
- On `get`, do DFS/BFS and track visited. If you revisit a cell in the current evaluation chain, raise `CircularReferenceError`.

```python
def evaluate(self, cell, visited=None):
    if visited is None:
        visited = set()
    if cell in visited:
        raise ValueError(f"Circular reference: {cell}")
    visited.add(cell)

    raw = self.cells.get(cell, "0")
    if not raw.startswith("="):
        return float(raw)

    formula = raw[1:]
    refs = re.findall(r'[A-Z]\d+', formula)
    values = {}
    for ref in refs:
        values[ref] = self.evaluate(ref, visited.copy())

    for ref, val in values.items():
        formula = formula.replace(ref, str(val))
    return eval(formula)
```

## Stage 4 — Change propagation (~15 min)
- When A1 changes, all cells that depend on A1 must recompute.
- Build a reverse dependency map: `dependents[cell]` = set of cells whose formula references `cell`.
- On `set`, invalidate the cell's cache AND all transitive dependents.
- Topological sort for evaluation order if doing batch recomputation.

```python
from collections import defaultdict

class Spreadsheet:
    def __init__(self):
        self.cells = {}
        self.cache = {}
        self.deps = defaultdict(set)     # cell -> cells it depends on
        self.rev_deps = defaultdict(set)  # cell -> cells that depend on it

    def set(self, cell, value):
        # Remove old dependencies
        for dep in self.deps[cell]:
            self.rev_deps[dep].discard(cell)

        self.cells[cell] = value

        # Build new dependencies
        if value.startswith("="):
            refs = set(re.findall(r'[A-Z]\d+', value[1:]))
            self.deps[cell] = refs
            for ref in refs:
                self.rev_deps[ref].add(cell)
        else:
            self.deps[cell] = set()

        self._invalidate(cell)

    def _invalidate(self, cell):
        self.cache.pop(cell, None)
        for dep in self.rev_deps[cell]:
            self._invalidate(dep)
```

## Stage 5 — Range functions (~10 min)
- `=SUM(A1:A5)` — Sum of a range.
- `=AVG(A1:A5)` — Average of a range.
- Parse range notation: expand `A1:A5` into `[A1, A2, A3, A4, A5]`.
- `=MIN(...)`, `=MAX(...)`, `=COUNT(...)`.

## Talking points
- `eval()` in production: huge security risk (code injection). Use a proper parser or ast.literal_eval for numbers only.
- Why cache + invalidation vs recompute every time? Large spreadsheets with deep dependency chains.
- This is essentially how Excel/Google Sheets work internally. Google Sheets uses a DAG for dependency tracking.
