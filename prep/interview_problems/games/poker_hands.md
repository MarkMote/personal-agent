# Poker Hand Validator

Scale AI's most frequently reported tech screen problem. OOP + card game logic.

```python
class Card:
    def __init__(self, rank: str, suit: str): ...

class Hand:
    def __init__(self, cards: list[Card]): ...
    def classify(self) -> str: ...
```

## Stage 1 — Card model + basic validation (~10 min)
- `Card(rank, suit)` — rank in ["A","2"..."10","J","Q","K"], suit in ["H","D","C","S"].
- `Hand(cards)` — Validate exactly 5 cards. Check for duplicate cards. Raise on invalid.
- `hand.ranks` — Return sorted list of rank values (A=1, J=11, Q=12, K=13). Or A=14 for high ace.
- `hand.suits` — Return list of suits.

```python
RANK_VALUES = {"A": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
               "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = RANK_VALUES[rank]

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))
```

## Stage 2 — Hand classification (~20 min)
- `classify()` returns the best hand type. Priority (highest first):
  1. **Straight Flush** — 5 consecutive ranks, all same suit
  2. **Four of a Kind** — 4 cards same rank
  3. **Full House** — 3 of one rank + 2 of another
  4. **Flush** — all same suit
  5. **Straight** — 5 consecutive ranks (any suits)
  6. **Three of a Kind** — 3 same rank
  7. **Two Pair** — 2 different pairs
  8. **One Pair** — 2 same rank
  9. **High Card** — nothing

- Use `collections.Counter` on rank values for grouping.
- Check flush: `len(set(suits)) == 1`.
- Check straight: `max(values) - min(values) == 4 and len(set(values)) == 5`. Special case: A-2-3-4-5 (wheel).

```python
from collections import Counter

class Hand:
    def __init__(self, cards: list[Card]):
        if len(cards) != 5:
            raise ValueError("Hand must have 5 cards")
        if len(set(cards)) != 5:
            raise ValueError("Duplicate cards")
        self.cards = cards
        self.values = sorted([c.value for c in cards])
        self.suits = [c.suit for c in cards]
        self.counts = Counter(self.values)

    def is_flush(self) -> bool:
        return len(set(self.suits)) == 1

    def is_straight(self) -> bool:
        if self.values == [2, 3, 4, 5, 14]:  # wheel
            return True
        return (max(self.values) - min(self.values) == 4
                and len(set(self.values)) == 5)

    def classify(self) -> str:
        flush = self.is_flush()
        straight = self.is_straight()
        groups = sorted(self.counts.values(), reverse=True)

        if straight and flush:
            return "Straight Flush"
        if groups == [4, 1]:
            return "Four of a Kind"
        if groups == [3, 2]:
            return "Full House"
        if flush:
            return "Flush"
        if straight:
            return "Straight"
        if groups == [3, 1, 1]:
            return "Three of a Kind"
        if groups == [2, 2, 1]:
            return "Two Pair"
        if groups == [2, 1, 1, 1]:
            return "One Pair"
        return "High Card"
```

## Stage 3 — Hand comparison / ranking (~15 min)
- Given two hands, determine the winner.
- Same hand type → tiebreak by kickers.
- `hand_rank()` returns a tuple for comparison: `(type_rank, tiebreakers...)`.
- E.g., Full House with 3 Kings and 2 Fives: `(6, 13, 5)`.
- Python tuple comparison handles this naturally.

```python
def hand_rank(self) -> tuple:
    # Sort count groups: [(count, value), ...] sorted by count desc, then value desc
    groups = sorted(self.counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    ranks = [v for v, c in groups]

    if self.is_straight() and self.is_flush():
        return (8, max(self.values))
    if groups[0][1] == 4:
        return (7, *ranks)
    if groups[0][1] == 3 and groups[1][1] == 2:
        return (6, *ranks)
    if self.is_flush():
        return (5, *sorted(self.values, reverse=True))
    if self.is_straight():
        return (4, max(self.values))
    if groups[0][1] == 3:
        return (3, *ranks)
    if groups[0][1] == 2 and groups[1][1] == 2:
        return (2, *ranks)
    if groups[0][1] == 2:
        return (1, *ranks)
    return (0, *sorted(self.values, reverse=True))
```

## Stage 4 — Wildcards / Jokers (~10 min)
- Add joker card that can be any rank+suit.
- `classify()` must try all possible joker values and return the best hand.
- With 1 joker: iterate 52 possible cards, classify each, return best.
- With 2 jokers: iterate all pairs (52×51). Or be smarter — a hand with 2 jokers is at minimum Three of a Kind.

## Stage 5 — N-player game simulation (~10 min)
- `Deck` class, shuffle, deal 5 to each of N players.
- `play_round(n_players)` — Deal, classify each hand, determine winner(s). Handle ties.
- `simulate(n_rounds, n_players)` — Run many rounds, track win distribution.

## Talking points
- Why Counter + sorted groups instead of checking each hand type separately? Single classification logic, no special cases.
- Wheel straight (A-2-3-4-5) is the most common edge case to miss.
- How would you extend to Texas Hold'em (7 cards, best 5)? Iterate all C(7,5)=21 combinations.
