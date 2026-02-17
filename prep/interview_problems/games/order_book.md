# Order Book / Matching Engine

Trading firm staple. Confirmed at Jane Street (onsite) and general quant finance interviews.

**Task:** Build a limit order book. Buy and sell orders come in with a price and quantity. When a new order's price crosses the other side (buy price >= best ask, or sell price <= best bid), match and fill orders by price-time priority. Support cancellation and querying best bid/ask.

```python
from collections import defaultdict
from sortedcontainers import SortedDict

class OrderBook:
    def __init__(self): ...
    def add_order(self, order_id: int, side: str, price: float, qty: int) -> list: ...
    def cancel_order(self, order_id: int) -> bool: ...
    def best_bid(self) -> float | None: ...
    def best_ask(self) -> float | None: ...
```

## Stage 1 — Add orders to the book (~10 min)
- `add_order(order_id, side, price, qty)` — side is "buy" or "sell".
- Buy orders (bids): sorted by price descending (highest first). Sell orders (asks): sorted by price ascending (lowest first).
- No matching yet — just store orders.
- Data structure: `SortedDict` keyed by price, values are lists of `(order_id, qty)` (FIFO queue per price level).

```python
from collections import deque
from sortedcontainers import SortedDict

class Order:
    def __init__(self, order_id, side, price, qty):
        self.order_id = order_id
        self.side = side
        self.price = price
        self.qty = qty

class OrderBook:
    def __init__(self):
        self.bids = SortedDict()  # price -> deque of Orders
        self.asks = SortedDict()  # price -> deque of Orders
        self.orders = {}          # order_id -> Order (for O(1) cancel)

    def add_order(self, order_id, side, price, qty):
        order = Order(order_id, side, price, qty)
        self.orders[order_id] = order
        book = self.bids if side == "buy" else self.asks
        if price not in book:
            book[price] = deque()
        book[price].append(order)
```

## Stage 2 — Order matching (~20 min)
- When a buy order comes in, check if it crosses the best ask (buy price >= lowest ask price).
- Match against the best ask price, FIFO within that price level.
- Partial fills: if buy qty > ask qty, fill the ask completely and continue matching.
- Return list of fills: `[(buy_id, sell_id, fill_price, fill_qty), ...]`.
- Remaining unfilled quantity goes on the book as a resting order.

```python
def add_order(self, order_id, side, price, qty):
    fills = []
    remaining = qty

    if side == "buy":
        while remaining > 0 and self.asks:
            best_ask_price = self.asks.keys()[0]  # lowest ask
            if price < best_ask_price:
                break  # no cross
            ask_queue = self.asks[best_ask_price]
            while remaining > 0 and ask_queue:
                ask_order = ask_queue[0]
                fill_qty = min(remaining, ask_order.qty)
                fills.append((order_id, ask_order.order_id, best_ask_price, fill_qty))
                remaining -= fill_qty
                ask_order.qty -= fill_qty
                if ask_order.qty == 0:
                    ask_queue.popleft()
                    del self.orders[ask_order.order_id]
            if not ask_queue:
                del self.asks[best_ask_price]

    # Mirror logic for sell side (match against bids, highest first)

    if remaining > 0:
        # Place remaining as resting order
        order = Order(order_id, side, price, remaining)
        self.orders[order_id] = order
        book = self.bids if side == "buy" else self.asks
        if price not in book:
            book[price] = deque()
        book[price].append(order)

    return fills
```

## Stage 3 — Cancel orders in O(1) (~10 min)
- `cancel_order(order_id)` — Remove from book.
- Naive: scan all price levels to find the order. O(n).
- Better: `self.orders` maps order_id → Order object. Mark order as cancelled. Skip cancelled orders during matching.
- Lazy deletion: don't remove from the deque immediately. Check `order.cancelled` when you pop.

## Stage 4 — Market data queries (~10 min)
- `best_bid()` / `best_ask()` — Highest bid price / lowest ask price. O(1) with SortedDict.
- `spread()` — best_ask - best_bid.
- `depth(side, levels=5)` — Return top N price levels with aggregate qty per level.
- `volume_at_price(price)` — Total qty at a given price level.

## Stage 5 — Market orders + order types (~10 min)
- Market order: no price limit, fill at best available prices until filled or book empty.
- IOC (Immediate or Cancel): fill what you can, cancel the rest. Never rests on book.
- FOK (Fill or Kill): fill entirely or not at all. Check if enough liquidity exists first.

## Talking points
- Why SortedDict over a plain dict? O(log n) access to best price vs O(n) scan.
- Price-time priority: first by best price, then FIFO at same price. This is standard for most exchanges.
- How would you handle millions of orders per second? Lock-free queues, separate matching threads per symbol, batch updates.
- What about `sortedcontainers` not being in stdlib? Mention it, offer to use `heapq` as alternative (but less clean for this problem).
