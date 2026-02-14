# Snake

Build the classic Snake game engine. Progressive stages.

```python
from collections import deque

class Snake:
    def __init__(self, rows: int = 20, cols: int = 20): ...
    def move(self, direction: str) -> str: ...
    def place_food(self) -> tuple[int, int]: ...
    def __str__(self) -> str: ...
```

## Stage 1 — Grid + snake movement (~10 min)
- Snake starts at center, length 1, facing right.
- `move(direction)` — direction is "U", "D", "L", "R". Move head one step. Remove tail (constant length). Return "ok", "wall" (game over), or "self" (game over).
- Snake body stored as `deque` of (row, col). Head is front, tail is back.
- Body cells tracked in a `set` for O(1) collision check.

## Stage 2 — Food + growth (~10 min)
- `place_food()` — Random empty cell. Return coordinates.
- When head lands on food: don't remove tail (snake grows by 1). Place new food.
- Track score (number of foods eaten).

## Stage 3 — Wrap-around mode (~5 min)
- Instead of wall death, snake wraps to opposite side.
- `move()` uses modular arithmetic: `new_row % rows`, `new_col % cols`.
- Only self-collision kills.

## Stage 4 — Replay + serialization (~10 min)
- Record every move as a list of directions.
- `replay(moves: list[str])` — Reset board and replay a sequence. Return final score.
- `serialize() -> str` — JSON snapshot of full game state (board, snake body, food, score).
- `deserialize(state: str) -> Snake` — Class method to restore from snapshot.

## Stage 5 — Simple AI (~15 min)
- `auto_move()` — Pick the best direction to move toward food without dying.
- BFS from head to food, avoiding body cells. Return first step of shortest path.
- If no path exists (trapped), pick any safe direction.
- Edge case: what if all directions kill you? Return any direction (game over anyway).

## Talking points
- Why deque + set instead of just a list? O(1) append/pop + O(1) membership check.
- BFS for pathfinding vs greedy (always move toward food). When does greedy fail? (Snake traps itself)
- How would you handle multiple snakes? (Simultaneous moves, collision resolution)
