# Minesweeper

Build a Minesweeper game engine. Progressive stages.

```python
class Minesweeper:
    def __init__(self, rows: int, cols: int, num_mines: int): ...
    def reveal(self, row: int, col: int) -> str: ...
    def flag(self, row: int, col: int) -> None: ...
    def __str__(self) -> str: ...
```

## Stage 1 — Board setup + mine placement (~10 min)
- Initialize grid. Place `num_mines` randomly (no duplicates).
- For each non-mine cell, compute adjacency count (number of neighboring mines, 8-directional).
- Two grids: `mines` (bool) and `counts` (int). Or single grid with sentinel for mines.
- First reveal should never be a mine — if it is, relocate the mine.

## Stage 2 — Reveal + flood fill (~15 min)
- `reveal(row, col)` — If mine: return "boom" (game over). If count > 0: reveal that cell, return "ok". If count == 0: flood fill — recursively reveal all adjacent 0-count cells and their non-mine neighbors.
- BFS or DFS for flood fill. Track revealed cells in a set.
- Return "win" if all non-mine cells are revealed.

## Stage 3 — Flagging + win condition (~10 min)
- `flag(row, col)` — Toggle flag on unrevealed cell. Can't flag revealed cells.
- Win condition: all mines flagged AND all non-mine cells revealed. OR just all non-mine cells revealed (standard rules).
- `remaining_mines()` — num_mines minus number of flags placed (can go negative if player over-flags).

## Stage 4 — First-click guarantee (~10 min)
- Mines aren't placed until first reveal.
- After first click, place mines avoiding the clicked cell AND its neighbors (so first click always opens a region).
- Recompute adjacency counts after placement.

## Stage 5 — Solver / hint system (~15 min)
- `hint()` — Find a cell that is safe to reveal based on current information.
- Simple logic: if a revealed cell's count equals its flagged neighbors, all other unrevealed neighbors are safe.
- Inverse: if a revealed cell's unrevealed neighbor count equals (count - flagged neighbors), all unrevealed neighbors are mines.
- Return one safe cell, or None if logic can't determine one (would need guessing).

## Talking points
- Flood fill: BFS vs DFS? Stack overflow risk with DFS on large boards.
- Why defer mine placement to first click? UX and fairness.
- How would you make this multiplayer? (Shared board, turn-based reveals, competitive scoring)
