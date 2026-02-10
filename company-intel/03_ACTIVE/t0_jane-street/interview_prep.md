# Jane Street — Interview Prep

## Round 1: SWE Coding (Tue 2/17 10:30am)

### What this round IS
- Standard SWE coding interview on CoderPad
- Progressive problem that builds in complexity (3 stages typical)
- Interviewer is a standard SWE — no ML context
- 35-60 min, block full hour

### What they evaluate
1. **Clean, bug-free code** — Part 1 should be quick and correct
2. **Communication** — talk through your thinking, explain trade-offs
3. **Proactive issue identification** — notice problems before being asked
4. **Complexity analysis** — know Big-O of what you're writing
5. **Code organization** — good abstractions, clear naming

### What they do NOT evaluate
- Clever algorithmic tricks or "aha" moments
- Mental math or probability (that's later rounds)
- ML knowledge (that's later rounds)
- OCaml (use Python)

### The pattern (from their published blog example)
Their blog walkthrough uses a memoization problem:
- **Stage 1:** Implement basic functionality (caching with hash table). Get this done fast and clean.
- **Stage 2:** Identify and solve a deeper issue (memory management → FIFO eviction, O(1))
- **Stage 3:** Harder variant (LRU cache → doubly-linked list for O(1) operations)

Most passing candidates nail stages 1-2. Stage 3 separates strong from exceptional.

The actual question will be different, but expect this progressive structure.

### Specific problems reported by candidates (from Glassdoor, LeetCode, Blind, Exponent, etc.)

**Phone screen / first round:**
- Memoization → FIFO cache → LRU cache (their published example, now retired)
- Implement Connect Four via a game state class
- Build a tree class with hash functions for each node (Merkle tree)
- Tetris — 2D matrix manipulation, piece placement and row clearing
- Interval scheduling
- State machine simulation
- Serialize/Deserialize a binary tree
- Course prerequisites (topological sort / graph)
- String hashing / frequency counting (palindrome rearrangement)

**Onsite coding rounds (later, but shows their style):**
- Build a video player API
- Build Tetris from scratch
- Open-ended system-building problems, not leetcode puzzles

**Pattern across all reports:** They give you something to BUILD, starting simple and adding constraints. It's "implement a system" not "solve this DP riddle." Multi-part, open-ended, no single correct answer. Hints are offered and expected to be taken.

### What this means: algorithms vs system design?

**Neither, exactly. It's "build a thing cleanly."** The first round is:
- Medium difficulty, NOT hard leetcode
- Multi-part (2-3 stages building on each other)
- Tests data structure fluency, code quality, and communication
- More like pair-programming than an exam
- Interviewer gives hints — taking them is expected and good
- "Asking questions and accepting hints is more important than finding solutions independently"
- Totally normal not to finish — they care about the journey

**It's NOT:**
- Tricky DP/graph theory puzzles
- System design whiteboarding (no "design Twitter")
- Probability or math (that's later rounds)
- Algo bingo (no obscure algorithms needed)

### Prep plan (priority order)

**1. Practice building things on CoderPad (MOST IMPORTANT)**
The best prep is literally: open CoderPad, pick a problem, build it from scratch, talk out loud.
- Implement an LRU cache from scratch (their published example)
- Implement Connect Four (game state, move validation, win detection)
- Implement a simple Tetris (piece placement, row clearing, gravity)
- Serialize/deserialize a binary tree
- Build a basic interval scheduler
These are not about memorizing — they're about fluency building things step by step.

**2. Python data structures — be fast and fluent**
- dict, defaultdict, Counter, OrderedDict
- list, deque (from collections), heapq
- set operations
- Know the time complexity of every operation you use
- Be able to implement: linked list, hash map, tree, queue, stack from scratch

**3. Think out loud (practice this explicitly)**
- State the approach before coding
- When you see an issue, say it: "this has O(n) lookup, which will be a problem at scale"
- When there are trade-offs, name them: "we could do X for simplicity or Y for performance"
- If you'd refactor something in production, mention it even if you don't implement it
- Ask clarifying questions early — "should I handle the case where...?"
- Accept hints gracefully — don't treat them as failure signals

**4. Code quality habits**
- Clear variable names
- Helper functions where they make sense
- Handle edge cases (empty input, None, etc.)
- Write real, runnable code — not pseudocode
- Type hints optional but show you think about types

**5. Patterns to be comfortable with**
- Hashing and caching (most common)
- Linked lists (singly and doubly)
- Trees and tree traversal (BFS/DFS)
- 2D arrays / matrices
- Recursion with memoization
- Graph basics (topological sort, BFS/DFS)
- State machines
- Serialization / deserialization

### Mock drill (do at least 2 before the interview)
1. Open a blank CoderPad (coderpad.io/sandbox)
2. Pick a "build" problem you haven't done recently (Connect Four, Tetris row clearing, interval merger)
3. Set a 45-minute timer
4. Talk out loud the ENTIRE time (to an empty room if needed)
5. Write real, runnable Python — test it
6. After solving stage 1, ask yourself: "what's wrong with this? what would break at scale?"
7. Then extend it (add a constraint, improve complexity, add a feature)

### Jane Street's own prep resources
- [ML Interview Guide (PDF)](https://www.janestreet.com/static/pdfs/ml-interview-guide.pdf) — for later rounds
- [Preparing for a SWE Interview](https://www.janestreet.com/preparing-for-a-software-engineering-interview/) — written walkthrough
- [What a Jane Street Dev Interview Is Like (blog)](https://blog.janestreet.com/what-a-jane-street-dev-interview-is-like/) — the memo example
- [Mock Interview Video](https://www.janestreet.com/mock-interview/) — 34-min recorded mock with debrief

---

## Later Rounds: ML-Focused (dates TBD)

### ML Engineer focus
- Write code that trains a model (tree-based or neural net)
- Justify every choice: model, loss, metrics, hyperparameters
- Implementation and workflow focus (training, serving, monitoring)
- Open-source tool knowledge
- Code efficiency — what's happening under the hood

### Prep for ML rounds (start after 2/17)
- [ ] PyTorch training loop from scratch (Dataset, DataLoader, nn.Module, optimizer)
- [ ] Train a simple model on a Kaggle dataset end-to-end in 45 min
- [ ] Gradient-boosted trees (XGBoost/LightGBM) — API and theory
- [ ] Random forests — when to use, how they work
- [ ] Loss functions — cross-entropy, MSE, when to use what
- [ ] Regularization — L1/L2/dropout/batch norm, mathematical intuition
- [ ] Evaluation metrics — precision/recall/F1/AUC, when each matters
- [ ] Data pipeline: collection → cleaning → feature engineering → train → eval → serve → monitor
- [ ] Be ready to explain: "what computation is happening under the hood" for any framework call

### Data science rounds
- [ ] Exploratory data analysis workflow
- [ ] Feature engineering intuitions
- [ ] When to use what model type
- [ ] Handling missing data, outliers, class imbalance
