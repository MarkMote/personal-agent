# Blackjack

**Task:** Build a Blackjack game. Deal cards from a shuffled deck, compute hand values (aces count as 11 or 1 to avoid busting), and run a game loop where players hit or stand.

```python
class Deck:
    def __init__(self): ...
    def shuffle(self) -> None: ...
    def draw(self) -> str: ...

class Hand:
    def __init__(self): ...
    def add(self, card: str) -> None: ...
    def value(self) -> int: ...
    def is_bust(self) -> bool: ...

class Blackjack:
    def __init__(self): ...
    def deal(self) -> None: ...
    def hit(self) -> str: ...
    def stand(self) -> str: ...
```

## Stage 1 — Deck + card values (~10 min)
- `Deck`: 52 cards as strings like "2H", "KS", "AD" (rank + suit).
- `shuffle()` — Random shuffle (use `random.shuffle`).
- `draw()` — Pop and return top card. Raise if empty.
- Card values: 2-10 face value, J/Q/K = 10, A = 11 or 1 (flexible).

## Stage 2 — Hand scoring with soft aces (~15 min)
- `Hand.value()` — Sum card values. Aces count as 11 unless that busts, then count as 1. Multiple aces: greedily downgrade from 11 → 1 as needed.
- `is_bust()` — value > 21.
- This is the tricky part. Track number of aces counted as 11. While bust and aces-as-11 > 0, subtract 10.

## Stage 3 — Game flow (~15 min)
- `deal()` — Two cards each to player and dealer. Dealer's second card is face-down.
- `hit()` — Player draws a card. Return result: "bust" or card drawn.
- `stand()` — Dealer plays: hits on 16 or below, stands on 17+. Compare hands. Return "player wins", "dealer wins", or "push".
- Check for natural blackjack (21 on deal) for both sides.

## Stage 4 — Betting + bankroll (~10 min)
- Player starts with bankroll (e.g., 1000).
- `place_bet(amount)` — Before deal. Validate against bankroll.
- Payouts: win = 1:1, blackjack = 3:2, push = return bet.
- Track bet per round, update bankroll on resolution.

## Stage 5 — Multi-deck shoe + card counting (~10 min)
- `Shoe(num_decks=6)` — Multiple shuffled decks together.
- `cards_remaining()` — How many left.
- `running_count()` — Hi-Lo system: 2-6 = +1, 7-9 = 0, 10-A = -1. Track as cards are drawn.
- `true_count()` — running_count / decks_remaining.

## Talking points
- Why track aces separately instead of trying all combinations? (2^n explosion)
- Shoe penetration and reshuffling — when/how to reshuffle?
- How would you simulate millions of hands to test a strategy? (Monte Carlo)
