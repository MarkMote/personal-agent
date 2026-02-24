# Laurion Coding Prep — Survival Guide

**Interview:** Fri 2/20 11am ET, 1 hour live coding with Yev (Quant Dev)
**Goal:** Show you can work with data fluently in Python and think quantitatively.

---

## TIER 1: Python Data Manipulation (Know Cold)

### Pandas Cheat Sheet

```python
import pandas as pd
import numpy as np

# Load
df = pd.read_csv('trades.csv')

# Inspect
df.head(), df.shape, df.dtypes, df.describe(), df.info()
df.isnull().sum()          # count nulls per column
df.nunique()               # unique values per column

# Filter
df[df['price'] > 100]
df[(df['side'] == 'buy') & (df['qty'] > 50)]
df[df['ticker'].isin(['AAPL', 'GOOG'])]
df.query("price > 100 and side == 'buy'")  # string syntax

# Sort
df.sort_values('price', ascending=False)
df.nlargest(5, 'volume')

# GroupBy (most important)
df.groupby('ticker')['price'].mean()
df.groupby('ticker').agg({'price': ['mean', 'std'], 'volume': 'sum'})
df.groupby(['ticker', 'date']).size()      # count per group

# Pivot
df.pivot_table(values='price', index='date', columns='ticker', aggfunc='mean')

# Merge / Join
pd.merge(trades, prices, on='ticker', how='left')
pd.merge(df1, df2, left_on='id', right_on='trade_id')

# Apply (row-wise or column-wise)
df['return'] = df['price'].pct_change()
df['log_price'] = df['price'].apply(np.log)
df['label'] = df.apply(lambda row: 'big' if row['qty'] > 100 else 'small', axis=1)

# Rolling windows
df['sma_20'] = df['price'].rolling(20).mean()
df['rolling_vol'] = df['return'].rolling(20).std()

# Handle missing data
df.fillna(0)
df.dropna(subset=['price'])
df.ffill()    # forward fill
```

### Common Data Tasks (Practice These)

**Task 1: "Given a DataFrame of trades (ticker, date, price, volume, side), find the top 5 tickers by total volume"**
```python
df.groupby('ticker')['volume'].sum().nlargest(5)
```

**Task 2: "Calculate the VWAP (volume-weighted average price) per ticker"**
```python
df['dollar_volume'] = df['price'] * df['volume']
vwap = df.groupby('ticker')['dollar_volume'].sum() / df.groupby('ticker')['volume'].sum()
```

**Task 3: "Find all tickers where the daily return exceeded 5%"**
```python
df['return'] = df.groupby('ticker')['price'].pct_change()
big_movers = df[df['return'].abs() > 0.05]['ticker'].unique()
```

**Task 4: "Resample intraday data to daily OHLCV"**
```python
daily = df.set_index('timestamp').groupby('ticker').resample('D').agg({
    'price': ['first', 'max', 'min', 'last'],
    'volume': 'sum'
})
```

**Task 5: "Merge trade data with a reference table and flag missing joins"**
```python
merged = pd.merge(trades, ref, on='ticker', how='left', indicator=True)
missing = merged[merged['_merge'] == 'left_only']
```

---

## TIER 1: Returns & P&L (Know Cold)

### Key Formulas

```python
# Simple return
r = (p1 - p0) / p0
# or
df['return'] = df['price'].pct_change()

# Log return (additive over time — preferred in quant finance)
df['log_return'] = np.log(df['price'] / df['price'].shift(1))

# Cumulative return
cumulative = (1 + df['return']).cumprod() - 1

# P&L from a position
# bought 100 shares at $50, sold at $55
pnl = 100 * (55 - 50)  # = $500

# P&L for a series of positions
df['pnl'] = df['qty'] * df['return'] * df['entry_price']

# Annualized return (from daily)
ann_return = df['return'].mean() * 252

# Annualized volatility (from daily)
ann_vol = df['return'].std() * np.sqrt(252)

# Sharpe ratio
sharpe = ann_return / ann_vol
# With risk-free rate:
sharpe = (ann_return - risk_free) / ann_vol
```

### Quick Facts
- **252** trading days per year
- **Sharpe > 1** is good, **> 2** is excellent, **> 3** is rare
- **Log returns** are additive across time, simple returns are not
- **Volatility** = standard deviation of returns (usually annualized)
- **Drawdown** = peak-to-trough decline: `(price - running_max) / running_max`
- **VWAP** = sum(price * volume) / sum(volume)

---

## TIER 2: Probability (Conversational + Code)

### Bayes' Theorem

```
P(A|B) = P(B|A) * P(A) / P(B)
```

**Classic example:** A trading signal fires. Historically:
- Signal fires on 5% of days (P(signal) = 0.05)
- On days the stock goes up >2%, the signal fires 80% of the time (P(signal|up) = 0.80)
- Stock goes up >2% on 10% of days (P(up) = 0.10)

What's the probability the stock is up >2% given the signal fired?
```
P(up|signal) = P(signal|up) * P(up) / P(signal)
             = 0.80 * 0.10 / 0.05
             = 1.60  ← impossible! P(signal) must be wrong or higher

# Real calc: P(signal) = P(signal|up)*P(up) + P(signal|not_up)*P(not_up)
# If P(signal|not_up) = 0.02:
P(signal) = 0.80*0.10 + 0.02*0.90 = 0.08 + 0.018 = 0.098
P(up|signal) = 0.80 * 0.10 / 0.098 = 0.816
```

**In code:**
```python
def bayes(p_b_given_a, p_a, p_b):
    return (p_b_given_a * p_a) / p_b
```

### Expected Value

```
E[X] = sum(x_i * p_i)
```

**Example:** A trade has 60% chance of making $1000 and 40% chance of losing $800.
```
E[X] = 0.6 * 1000 + 0.4 * (-800) = 600 - 320 = $280
```

Should you take it? Yes — positive expected value.

### Distributions Cheat Sheet

| Distribution | When to use | Python |
|---|---|---|
| **Normal** | Continuous, symmetric (returns, errors) | `np.random.normal(mu, sigma, n)` |
| **Bernoulli** | Single yes/no event (trade wins or loses) | `np.random.binomial(1, p)` |
| **Binomial** | Count of successes in n trials | `np.random.binomial(n, p, size)` |
| **Poisson** | Count of events per time period (trades/hour) | `np.random.poisson(lam, size)` |
| **Uniform** | Equal probability across range | `np.random.uniform(low, high, size)` |

**Normal: 68-95-99.7 rule**
- 68% within 1σ, 95% within 2σ, 99.7% within 3σ
- A "3-sigma event" = 0.3% probability = very rare

### Conditional Probability

```
P(A and B) = P(A|B) * P(B)
P(A or B) = P(A) + P(B) - P(A and B)
```

Independent events: `P(A and B) = P(A) * P(B)`

**Quick brain teaser format:**
"You flip a fair coin 10 times. What's the probability of getting exactly 7 heads?"
```python
from math import comb
p = comb(10, 7) * (0.5**7) * (0.5**3)  # = 0.1172
# Or: scipy.stats.binom.pmf(7, 10, 0.5)
```

---

## TIER 2: Basic Stats in Code

```python
import numpy as np

data = np.array([...])

# Central tendency
np.mean(data)
np.median(data)

# Spread
np.std(data)          # population std
np.std(data, ddof=1)  # sample std (use this one)
np.var(data)
np.percentile(data, [25, 50, 75])  # quartiles

# Correlation
np.corrcoef(x, y)[0, 1]
# or with pandas:
df[['a', 'b']].corr()

# Covariance
np.cov(x, y)[0, 1]
```

### Key Concepts (1-liner answers)

**Correlation vs causation:** Correlation measures linear relationship (-1 to 1). Doesn't imply one causes the other. Spurious correlations are everywhere.

**p-value:** Probability of seeing this result (or more extreme) if the null hypothesis is true. p < 0.05 = "statistically significant" by convention. Not the probability the hypothesis is true.

**Central Limit Theorem:** Average of many independent samples → normal distribution, regardless of the underlying distribution. Bigger n → tighter distribution around the true mean.

**Law of Large Numbers:** As sample size grows, sample mean → true mean.

**Overfitting:** Model fits noise in the data, not the signal. Too many parameters relative to data. In finance: a backtest that looks amazing but fails live.

**Look-ahead bias:** Using future information in a backtest. Cardinal sin in quant finance. e.g., using tomorrow's close to decide today's trade.

---

## TIER 2: Monte Carlo Simulation

Pattern: generate random samples, compute statistic, repeat.

```python
# Estimate probability that a portfolio loses >10% in a year
n_sims = 100_000
annual_returns = np.random.normal(0.08, 0.15, n_sims)  # 8% mean, 15% vol
prob_loss_10 = np.mean(annual_returns < -0.10)
print(f"P(loss > 10%): {prob_loss_10:.4f}")

# Simulate a random walk (stock price)
n_days = 252
daily_return = np.random.normal(0.0003, 0.01, n_days)  # ~8% annual, ~16% vol
price_path = 100 * np.cumprod(1 + daily_return)
```

**When to reach for Monte Carlo:** When the analytical solution is hard or unknown. "Just simulate it" is always a valid approach and shows practical instincts.

---

## TIER 3: Time Series (Good to Have)

```python
# Moving averages
df['sma_20'] = df['price'].rolling(20).mean()
df['ema_20'] = df['price'].ewm(span=20).mean()

# Autocorrelation (does today's return predict tomorrow's?)
df['return'].autocorr(lag=1)

# Stationarity intuition:
# Stationary = statistics don't change over time (mean, variance are constant)
# Stock prices: NOT stationary (they trend)
# Stock returns: approximately stationary
# You almost always model returns, not prices
```

---

## COLLECTIONS & DATA STRUCTURES (Python Fundamentals)

In case the problem is more algorithmic:

```python
from collections import Counter, defaultdict, deque
from heapq import nlargest, nsmallest

# Counter — frequency counting
c = Counter(['a', 'b', 'a', 'c', 'a'])  # Counter({'a': 3, 'b': 1, 'c': 1})
c.most_common(2)  # [('a', 3), ('b', 1)]

# defaultdict — no KeyError
d = defaultdict(list)
d['key'].append(1)  # works even if 'key' didn't exist

# deque — O(1) append/pop from both ends
q = deque([1, 2, 3])
q.appendleft(0)

# Sorting
sorted(data, key=lambda x: x['price'], reverse=True)

# Dict comprehension
{k: v for k, v in items if v > 0}

# Zip
dict(zip(keys, values))
list(zip(dates, prices))

# Enumerate
for i, val in enumerate(data):
    ...
```

---

## MINDSET FOR THE INTERVIEW

1. **Think out loud.** Yev wants to see how you reason, not just the answer.
2. **Clarify before coding.** "What format is the input? What should the output look like? Any edge cases?"
3. **Start simple, then optimize.** Get a working solution first. Mention optimizations you'd make.
4. **Name things well.** `daily_returns` not `dr`. Production-quality naming signals seniority.
5. **Use pandas when it's natural.** Don't write a for loop to compute a column mean.
6. **If you don't know something, say so and reason through it.** "I haven't worked with that exact metric, but my instinct is..." — this is what Sarkis valued.
7. **Connect to your experience.** If the problem involves data pipelines, briefly mention Roostr's approach.
