# Interval Scheduler

Build a meeting room / interval scheduling system. Reported Jane Street problem.

```python
class Scheduler:
    def __init__(self): ...
    def book(self, start: int, end: int) -> bool: ...
    def cancel(self, start: int, end: int) -> bool: ...
    def next_available(self, duration: int) -> int: ...
```

## Stage 1 — Booking + conflict detection (~10 min)
- `book(start, end)` — Add interval [start, end). Return True if no conflict. Return False and don't book if it overlaps any existing booking.
- Store bookings in a sorted list (by start time).
- Conflict check: new interval overlaps existing if `new.start < existing.end and new.end > existing.start`.
- Brute force: check all bookings. O(n) per book.

## Stage 2 — Efficient conflict check with bisect (~10 min)
- Use `bisect` to find insertion point. Only need to check the booking before and after the insertion point.
- Or use a sorted list (SortedList from sortedcontainers, or maintain sorted manually).
- O(log n) conflict check.

## Stage 3 — Multiple rooms (~15 min)
- `Scheduler(num_rooms)` — K rooms available.
- `book(start, end)` — Assign to any available room. Return room number, or -1 if all rooms have conflicts.
- Track bookings per room, or use a min-heap of (next_available_time, room_id).
- Greedy: assign to the room that becomes free earliest before the new start time.

## Stage 4 — Recurring events (~10 min)
- `book_recurring(start, end, interval, count)` — Book the same slot repeating every `interval` units, `count` times.
- Must check ALL occurrences for conflicts before booking any.
- If any occurrence conflicts, book none (atomic).
- Return list of booked intervals, or empty list on conflict.

## Stage 5 — Gap finding + suggestions (~10 min)
- `next_available(duration)` — Find the earliest time slot of length `duration` that doesn't conflict with anything.
- Walk through bookings in order. Check gaps between consecutive bookings.
- Also check before the first booking and after the last.
- `suggest(duration, after)` — Find next 3 available slots of given duration after a given time.

## Talking points
- Sorted list vs interval tree? When is each appropriate?
- How would you handle time zones?
- What if bookings can be "tentative" vs "confirmed"? (Two-phase booking)
- Google Calendar does this at massive scale — what changes? (Sharding by user, eventual consistency)
