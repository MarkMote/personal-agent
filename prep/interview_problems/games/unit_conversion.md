# Unit Conversion Graph

Jane Street's actual mock interview problem (published video at janestreet.com/mock-interview/).

## The Problem

You're given a set of "conversion facts" like:
- 1 meter = 3.28 feet
- 1 foot = 12 inches
- 1 hour = 60 minutes

These facts are provided as tuples: `("m", 3.28, "ft")` meaning "1 m equals 3.28 ft."

Your job: build a system that can answer conversion queries, including ones that require chaining multiple facts together. For example, even though you were never told the relationship between meters and inches directly, you can figure it out: meters → feet → inches.

**The key insight:** This is a graph problem. Each unit is a node, each fact is an edge with a weight (the conversion factor). Converting between units = finding a path through the graph and multiplying the weights along the way.

## What you build

```python
class UnitConverter:
    def __init__(self): ...
    def add_fact(self, from_unit: str, quantity: float, to_unit: str) -> None: ...
    def convert(self, value: float, from_unit: str, to_unit: str) -> float: ...
```

- `add_fact("m", 3.28, "ft")` — registers that 1 m = 3.28 ft (and implicitly, 1 ft = 1/3.28 m)
- `convert(10, "m", "ft")` → 32.8
- `convert(10, "m", "in")` → 393.6 (chains through feet)
- `convert(1, "m", "kg")` → error (no path between length and mass)

## Stage 1 — Direct conversions (~10 min)
- `add_fact` stores the relationship (and its inverse).
- `convert` looks up the direct factor and multiplies. Only handles cases where a single fact connects the two units.
- Raise if no direct conversion exists (for now).

## Stage 2 — Multi-hop conversions (~15 min)
- Now handle chaining: if you know `m → ft` and `ft → in`, you can convert `m → in`.
- Search through the graph (BFS) to find a path. Multiply conversion factors along the way.
- Raise if no path exists (e.g., converting between unrelated unit families).

```python
from collections import deque

def convert(self, value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    visited = {from_unit}
    queue = deque([(from_unit, 1.0)])
    while queue:
        unit, factor = queue.popleft()
        for neighbor, rate in self.graph[unit].items():
            if neighbor == to_unit:
                return value * factor * rate
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, factor * rate))
    raise ValueError(f"No conversion path from {from_unit} to {to_unit}")
```

## Stage 3 — Conflicting facts + precision (~10 min)
- What if someone adds `m → ft = 3.28` and later `m → ft = 3.281`?
- Options: overwrite, average, raise error. Discuss tradeoffs.
- Floating point: accumulated multiplication introduces error. When should you warn?
- Add `can_convert(from, to) -> bool` that checks reachability without computing.

## Stage 4 — Batch queries + caching (~10 min)
- `convert_batch(queries: list[tuple]) -> list[float]` — Many queries at once.
- Cache discovered paths: once you find `m → in`, store the direct factor so future queries are O(1).
- Invalidation: if a new fact is added, which cached paths need updating?
- Simple approach: clear cache on any `add_fact`. Better: only clear paths involving modified edges.

## Stage 5 — Dimensional analysis (~10 min)
- Support compound units: `"m/s"` to `"ft/min"`.
- Parse compound units into numerator and denominator units.
- Convert each component independently and combine.
- E.g., `m/s → ft/min`: convert m→ft (×3.28) and s→min (÷60) → multiply by 3.28 × 60.

## Talking points
- Why BFS over DFS? Shortest path = fewest multiplications = least floating point error.
- This is a weighted graph problem. Could also use Floyd-Warshall to precompute all pairs.
- Real-world: Google's unit converter, currency exchange rates (same structure).
