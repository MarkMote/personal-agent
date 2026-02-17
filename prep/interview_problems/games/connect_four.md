# Connect Four

**Task:** Build a Connect Four game on a 6x7 grid. Players take turns dropping pieces into columns. Pieces fall to the lowest empty row. Detect when a player gets 4 in a row (horizontal, vertical, or diagonal).

```python
class ConnectFour:
    def __init__(self, rows: int = 6, cols: int = 7): ...
    def drop(self, col: int, player: int) -> tuple[int, int]: ...
    def check_winner(self) -> int: ...
    def __str__(self) -> str: ...
```

## Stage 1 — Grid + drops (~10 min)
- Initialize `rows x cols` grid filled with 0.
- `drop(col, player)` — Drop piece (player 1 or 2) into column. Falls to lowest empty row. Return (row, col) where it lands. Raise if column full or out of bounds.
- `__str__()` — Print board. `.` for empty, `X` for player 1, `O` for player 2. Row 0 at bottom.

## Stage 2 — Win detection (~15 min)
- `check_winner()` — After each drop, check if the last placed piece creates 4-in-a-row. Check all 4 directions: horizontal, vertical, diagonal-up, diagonal-down. Return winning player (1 or 2) or 0.
- Key insight: only need to check around the last dropped piece, not the whole board.

## Stage 3 — Game loop + draw detection (~10 min)
- `is_full()` — Board completely filled = draw.
- `play(col)` — Manages turn alternation, validates moves, checks win/draw after each drop. Returns game state string: "P1 wins", "P2 wins", "Draw", or "Continue".
- Track whose turn it is internally.

## Stage 4 — Undo + move history (~10 min)
- `undo()` — Remove the last piece placed. Restore turn order. Use a stack of moves.
- `history()` — Return list of (player, row, col) for all moves made.
- Edge case: undo on empty board should raise or no-op.

## Stage 5 — Simple AI opponent (~15 min)
- `best_move(player)` — Pick the best column for `player`.
- Priority: (1) win if possible, (2) block opponent's win, (3) center column preference.
- For each column, simulate a drop and check if it wins. Then simulate opponent's drop and check if it wins.

## Talking points
- Why check only around last piece? O(1) vs O(rows*cols) per move.
- How would you extend to arbitrary board sizes or connect-N?
- How would you add rotation (piece falls sideways)?
