# State Machine Simulator

Build a configurable state machine. Reported Jane Street pattern.

```python
class StateMachine:
    def __init__(self, initial_state: str): ...
    def add_transition(self, from_state: str, event: str, to_state: str, action=None): ...
    def process(self, event: str) -> str: ...
    def history(self) -> list[tuple[str, str, str]]: ...
```

## Stage 1 — Basic transitions (~10 min)
- `add_transition(from, event, to)` — Register a transition. Store as dict of dicts: `{state: {event: to_state}}`.
- `process(event)` — If current state has a transition for this event, move to new state. Return new state. If no transition, raise or return current state.
- Track current state.

## Stage 2 — Actions + history (~10 min)
- `add_transition(from, event, to, action)` — action is an optional callable that fires on transition.
- `process(event)` — Execute action (if any) during transition.
- `history()` — Return list of (from_state, event, to_state) for all transitions taken.

## Stage 3 — Guards + conditional transitions (~15 min)
- `add_transition(from, event, to, guard=None)` — guard is a callable returning bool. Transition only fires if guard returns True.
- Multiple transitions from same (state, event) with different guards. First matching guard wins.
- Store transitions as `{state: {event: [(to, guard, action), ...]}}`.
- Error if no guard matches.

## Stage 4 — Hierarchical states (~15 min)
- States can contain sub-state machines. E.g., "Active" contains "Playing" and "Paused".
- Entering a parent state enters its initial sub-state.
- Events are handled by the deepest active state first. If unhandled, bubble up to parent.
- `current_state()` returns full path: "Active.Playing".

## Stage 5 — Serialization + replay (~10 min)
- `serialize()` — Dump current state + transition table to JSON.
- `replay(events: list[str])` — Reset to initial, process all events, return final state.
- `validate()` — Check for unreachable states, missing transitions, dead ends.

## Example: Turnstile
```python
sm = StateMachine("locked")
sm.add_transition("locked", "coin", "unlocked")
sm.add_transition("unlocked", "push", "locked")
sm.add_transition("locked", "push", "locked")      # no-op
sm.add_transition("unlocked", "coin", "unlocked")   # no-op

sm.process("coin")   # → "unlocked"
sm.process("push")   # → "locked"
```

## Example: Traffic Light
```python
sm = StateMachine("red")
sm.add_transition("red", "timer", "green")
sm.add_transition("green", "timer", "yellow")
sm.add_transition("yellow", "timer", "red")
sm.add_transition("red", "emergency", "red")      # stay red
sm.add_transition("green", "emergency", "red")     # go to red
sm.add_transition("yellow", "emergency", "red")    # go to red
```

## Talking points
- Why dict of dicts instead of a flat list of tuples? O(1) lookup vs O(n) scan.
- Guard ordering matters — how would you make it deterministic? (Priority, or error on ambiguity)
- Real-world: HTTP protocol, game AI, workflow engines, regex engines.
