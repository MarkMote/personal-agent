                                                                                                                     # Interview Prep Queue — W07-W08

**Goal:** Pass Jane Street SWE coding round (Tue 2/17) + build general coding screen fluency.
**Schedule:** 6 prep days (Tue 2/10 – Sun 2/15), Mon 2/16 contingency.
**Daily:** ~3hr neetcode + 3hr core problems + 2hr non-core + 1hr wildcard.

---

## Neetcode 150 — Priority Areas

Do these during your 3hr neetcode blocks. Not scheduled day-by-day — just grind through in priority order.

### Highest Priority (JS first round — data structures, trees, graphs)

**Trees (do all 15)** — JS reports tree problems. Fluency here is non-negotiable.
- Invert Binary Tree, Max Depth, Diameter, Balanced, Same Tree
- Subtree of Another Tree, LCA of BST
- Level Order Traversal, Right Side View, Count Good Nodes
- Validate BST, Kth Smallest in BST
- Construct from Preorder + Inorder
- **Binary Tree Max Path Sum** (hard but good)
- **Serialize and Deserialize Binary Tree** (LC 297) — reported at JS

**Linked List (do all 6)** — LRU cache uses doubly-linked lists, JS loves these.
- Reverse Linked List, Merge Two Sorted Lists
- Reorder List, Remove Nth from End
- Linked List Cycle, Merge K Sorted Lists

**Stack (do 5)** — JS memoization example is stack-ish thinking.
- Valid Parentheses, Min Stack
- Evaluate Reverse Polish Notation
- Generate Parentheses, Daily Temperatures

**Graphs (do all 6)** — topological sort reported at JS.
- Number of Islands, Clone Graph
- Pacific Atlantic Water Flow
- **Course Schedule** (LC 207) — reported at JS
- Course Schedule II (LC 210) — topological sort
- Graph Valid Tree

### Good to Do (general screen fluency)

**Heap/Priority Queue** — load balancer, task queue problems use heaps.
- Kth Largest Element, Last Stone Weight
- K Closest Points, Task Scheduler
- Design Twitter, Find Median from Data Stream

**Sliding Window** — rate limiter, stream processing.
- Best Time to Buy/Sell Stock
- Longest Substring Without Repeating
- Minimum Window Substring

**Two Pointers** — quick wins, useful everywhere.
- Valid Palindrome, Two Sum II, 3Sum, Container With Most Water

**Intervals** — merge intervals reported at JS.
- Insert Interval, Merge Intervals, Non-Overlapping Intervals

### Lower Priority (skip unless time)

- Binary Search (unlikely at JS first round)
- Dynamic Programming (JS says "not clever algorithms")
- Backtracking (unlikely first round)
- Bit Manipulation, Math & Geometry

### Specific LeetCode to Flag

These aren't in neetcode 150 but are directly relevant:
- **LRU Cache (LC 146)** — literally the JS published example
- **LFU Cache (LC 460)** — harder variant, good stretch
- **Design HashMap (LC 706)** — build from scratch
- **Design Add and Search Words (LC 211)** — trie
- **Implement Trie (LC 208)** — file system problems use tries

---

## Daily Schedule

### Day 1 — Tue 2/10: Foundations

**Core (3 problems, ~3hr):**

1. **LRU Cache from scratch** (LC 146)
   Do this FIRST. It's the JS published example. Implement with OrderedDict, then reimplement with dict + doubly-linked list. Know both approaches cold.
   *Takeaway: doubly-linked list + hash map pattern, O(1) get/put, the exact progressive structure JS uses.*

2. **In-Memory File System** (Problem 1 from 00_general)
   Trie-based directory tree. mkdir, ls, add_content, read_content.
   *Takeaway: trie traversal, clean class design, building a system incrementally — pure JS style.*

3. **Design HashMap from scratch** (LC 706)
   Implement put, get, remove with chaining. Then discuss: resize/rehash strategy, load factor.
   *Takeaway: understanding what's under the hood when you use dict. JS cares about "what computation is happening."*

**Non-core (2 problems, ~2hr):**

1. **Train MNIST MLP end-to-end** (Problem 20)
   Write the full training pipeline: Dataset, DataLoader, nn.Module, loss, optimizer, train loop, eval loop, save checkpoint. No wrappers — raw PyTorch.
   *Takeaway: PyTorch muscle memory. You'll need this for JS ML rounds and any ML coding screen. Do it until the training loop is automatic.*

2. **PyTorch Debugging Drill** (Problem 21)
   Given a buggy training script, find and fix 5 bugs (shape error, exploding loss, wrong mode, device mismatch, bad normalization).
   *Takeaway: debugging intuition for common ML failures. Quick exercise — 20 min max.*

**Wildcard (~1hr): System Design — Document Processing API**

You're building an API for a company that needs to ingest thousands of documents (PDFs, CSVs, Word docs) per day, extract structured data, and make it searchable. Talk through:

- How do you handle different file formats? (parsers, plugin architecture vs monolith)
- Sync vs async processing? (user uploads file → gets result later, or blocks?)
- Storage: raw files vs extracted text vs structured output. Where does each live?
- Search: full-text vs embeddings vs both? How do you index?
- What breaks at 10x scale? At 100x? Where are the bottlenecks?
- How would you add a new document type in 6 months without rewriting?

*Intent: this is the Anthropic/Scale FDE problem. Customers show up with messy data and want structured output. Practice talking through the architecture before touching code. Focus on trade-offs and "it depends" answers — interviewers want to see you reason, not memorize an architecture.*

---

### Day 2 — Wed 2/11: Trees (Light day — Laurion 1pm, Archer 4pm)

**Core (3 problems, ~3hr):**

1. **Serialize and Deserialize Binary Tree** (LC 297)
   BFS or preorder approach. Write both serialize and deserialize. Handle nulls cleanly.
   *Takeaway: tree traversal fluency, string parsing, reconstruction — reported at JS.*

2. **Validate BST** (LC 98) + **Kth Smallest in BST** (LC 230)
   Pair these — both use in-order traversal. Do validate with min/max bounds, kth with iterative in-order.
   *Takeaway: in-order traversal is the BST workhorse. Be fast with it.*

3. **Construct Binary Tree from Preorder and Inorder** (LC 105)
   Recursive approach with hash map for O(1) index lookup.
   *Takeaway: understanding tree structure from traversal orders. Tests recursive thinking + index manipulation.*

**Non-core (2 problems, ~2hr):**

1. **FastAPI async endpoint + Pydantic schemas** (Problems 11+12 combined)
   Build GET /hello with query params, async delay, Pydantic request/response models, ISO timestamp. Single file, runnable.
   *Takeaway: FastAPI + Pydantic + async patterns. Anthropic CodeSignal will likely use these. Scale too.*

2. **Inference utilities** (Problem 22)
   Write predict(), predict_batch(), save/load checkpoint, set_seed(). Extend the MNIST model from Day 1.
   *Takeaway: production ML patterns — eval mode, no_grad, device handling, reproducibility. Quick 30-40 min.*

**Wildcard (~1hr): Storytelling — Roostr**

You have interviews today (Laurion, Archer). Warm up the narrative muscle. Answer these out loud (record yourself or talk to a wall), then come to me to sharpen:

1. **"What did you build at Roostr and why?"** — Walk through the system end-to-end in 3 minutes. Start with the business problem (freight forwarding is manual, slow, margin-compressed), then the technical solution (agentic pipeline: emails → parsing → normalized quotes → FSM policy graph → automated workflows). Hit: sole production engineer, Python/FastAPI + Next.js, $1M incremental monthly revenue for one customer.

2. **"What was the hardest technical problem you solved at Roostr?"** — Pick ONE. Go deep. What made it hard? What did you try first? What failed? What worked? What would you do differently?

3. **"Why are you leaving?"** — Practice the clean version: "Roostr is operating with revenue and I'm on great terms with my cofounder. But it's in a sales/ops scaling phase now. I'm more excited about building hard technical systems than running a logistics operation. Rather than raise more capital into a domain that isn't my deepest conviction, this felt like the right moment."

*Intent: interviewers at every company will ask about Roostr. The difference between "good" and "great" answers is crispness. 3 minutes max per answer. No rambling. Practice cutting the story short, not extending it.*

---

### Day 3 — Thu 2/12: System Building I

**Core (3 problems, ~3hr):**

1. **Transactional Key-Value Store** (Problem 2)
   Nested begin/commit/rollback with stack of dicts. Handle delete-as-tombstone.
   *Takeaway: stack-based state management, transaction semantics. Classic "build a thing with progressive complexity" — exactly JS style.*

2. **Connect Four**
   Build from scratch: Board class, drop_piece(), check_win() (horizontal, vertical, both diagonals), is_full(). Then add: undo_move(), get_valid_columns().
   *Takeaway: 2D grid manipulation, game state, win detection — reported by JS candidates. Practice narrating design decisions as you go.*

3. **Spreadsheet with Dependency Graph** (Problem 7)
   set() stores formulas or values, get() evaluates with dependency resolution. Cycle detection via DFS coloring.
   *Takeaway: graph modeling in a non-obvious context, topological evaluation, cycle detection. Strong JS-style progressive problem.*

**Non-core (2 problems, ~2hr):**

1. **ReAct Agent Loop** (Problem 9)
   Build the Thought→Action→Observation loop with injected LLM callable. Parse tool calls with regex, dispatch to mock tools, stop on "Final Answer."
   *Takeaway: core agentic pattern. Anthropic FDE builds these for customers. Understand the loop, parsing, error handling.*

2. **Log Parser & Aggregator** (Problem 4)
   Parse structured log strings, store in memory, query by time window with group-by aggregation. Sort by count descending.
   *Takeaway: string parsing, time-range filtering, aggregation — Scale-style data wrangling.*

**Wildcard (~1hr): System Design — LLM Agent Orchestration Platform**

A company wants to let their internal teams define and run multi-step LLM agent workflows (think: "research this topic → summarize → draft email → get approval → send"). Design the platform.

- What's the execution model? DAG of steps? Linear chain? How do you handle branching/conditionals?
- How are tools registered and invoked? (tool registry, schema validation, sandboxing)
- How do you handle failures mid-workflow? (retry, fallback, human-in-the-loop escalation)
- Where does state live during execution? (in-memory, database, event log)
- Observability: how do you debug a failed workflow 3 days later?
- How do you evaluate whether the agent did a good job? (evals, golden datasets, human review)

*Intent: this IS the Anthropic FDE job. You'll be building exactly this for customers. It's also the Scale FDAI job. Show you can think about agentic systems architecturally, not just implement a ReAct loop. Focus on failure modes and observability — that's what separates production thinking from toy demos.*

---

### Day 4 — Fri 2/13: System Building II (D.E. Shaw at 2pm)

**Core (3 problems, ~3hr):**

1. **Sliding Window Rate Limiter** (Problem 3)
   deque-based, hit() + get_hits(), handle bursts within same second.
   *Takeaway: deque as sliding window, amortized O(1), clean time-series pattern. Quick warmup — 30-40 min.*

2. **Task Queue / Job Runner** (Problem 8)
   Heap-based with delay, in-flight tracking, fail/retry, succeed/remove.
   *Takeaway: heap + state machine combination, handling multiple entity states. Production system pattern.*

3. **Interval Merge + Meeting Rooms**
   Three stages: (a) Merge Intervals (LC 56), (b) Meeting Rooms II — min rooms needed (LC 253), (c) design an interval scheduler that handles add/remove/query-overlap.
   *Takeaway: interval problems are reported at JS. Progressive build from simple sort+merge to full scheduler.*

**Non-core (2 problems, ~2hr):**

1. **MCP Hello World Server** (Problem 10)
   Stdio JSON-RPC server with initialize + tools/call. One tool: hello(name) → greeting. Standard library only.
   *Takeaway: understand MCP protocol from the inside. Anthropic FDE literally builds these for customers. Even a basic one teaches the framing.*

2. **Async Endpoint + Background Job** (Problem 17)
   POST /analyze spawns background worker fetching URLs. GET /status/{job_id} returns progress. asyncio.Semaphore for concurrency.
   *Takeaway: async patterns, background tasks, job state management. Directly relevant to Scale and Anthropic coding rounds.*

**Wildcard (~1hr): Storytelling — Pytheia**

D.E. Shaw call is at 2pm. Good day to sharpen the Pytheia narrative. Answer these out loud, then come to me to refine:

1. **"What did you build at Pytheia and why?"** — 3-minute version. Start with the origin (CV/robotics background → saw opportunity in multi-camera perception), the pivot (Argus 3D perception → LLM-driven data pipelines → demand forecasting SaaS), the outcome ($20k investment → $300k ARR, 2.5 years). Hit: CEO role, sold the product, built the tech, made the pivot decision.

2. **"Tell me about a hard pivot or strategic decision."** — The Pytheia pivot is your best story here. Why did you pivot? What data informed the decision? What did you lose by pivoting? What did you gain? How did you manage the team through it?

3. **"What did you learn from Pytheia that you couldn't have learned any other way?"** — This is the founder question. They want to hear self-awareness. What do you know now about building products, selling, hiring, failing, that you didn't know from your PhD?

4. **"Why didn't Pytheia work out? / Why did you leave?"** — Practice the honest version. Not defensive, not blamey. What was the market reality? What would you do differently?

*Intent: Pytheia is older and more complex to explain (CV startup → LLM pivot → left to start Roostr). The risk is rambling or sounding like you're justifying. Practice making the story SHORTER, not longer. 2-3 minutes max. The pivot is the interesting part — lean into it.*

---

### Day 5 — Sat 2/14: Games + Graphs

**Core (3 problems, ~3hr):**

1. **Tetris-lite**
   Build incrementally: (a) Board class — 10-wide grid, (b) drop a 1x1 block into a column, (c) row clearing + gravity, (d) add standard pieces (L, T, I, O), (e) collision detection on drop. Stop wherever time runs out.
   *Takeaway: 2D grid manipulation, gravity/physics simulation, progressive build — reported by JS candidates. Practice narrating each stage transition.*

2. **Least-Loaded Load Balancer** (Problem 5)
   Heap with lazy deletion. add_server, remove_server, assign_task, update_load. Break ties by server_id.
   *Takeaway: heap with invalidation pattern (mark-and-skip). Common in system design interviews.*

3. **Course Schedule I + II** (LC 207 + 210)
   First: can you finish all courses? (cycle detection via BFS/Kahn's). Second: return a valid ordering (topological sort).
   *Takeaway: topological sort — reported at JS. Know both BFS (Kahn's) and DFS approaches.*

**Non-core (2 problems, ~2hr):**

1. **Async Tool-Calling Agent** (Problem 14)
   Like Problem 9 but async, with JSON parsing, Pydantic validation, timeouts, error handling (invalid JSON, missing tool, tool crash).
   *Takeaway: production-grade agentic loop. Error handling and graceful degradation are what separate interview answers from toy implementations.*

2. **Dirty Data Stream Processor** (Scale 05, Problem 4)
   Ingest out-of-order log lines, get_top_users(k, window), detect_anomaly(threshold). Handle out-of-order timestamps.
   *Takeaway: stream processing with time windows, heap for top-k, sliding window for anomaly detection. Pure Scale interview style.*

**Wildcard (~1hr): System Design — Model Evaluation Pipeline**

You're building an internal platform for evaluating LLM quality. The team runs hundreds of eval jobs per week across different models, prompts, and datasets. Design the system.

- What's the data model? (eval job → dataset → examples → predictions → scores)
- How do you handle different eval types? (exact match, LLM-as-judge, human review, custom metrics)
- How do you detect regressions? (model A was better last week, now it's worse — alert)
- How do you store and compare results across runs? (versioning, dashboards, diffs)
- How do you scale to thousands of examples? (parallel execution, batching, cost management)
- What's the interface? CLI? Web UI? API that plugs into CI/CD?

*Intent: Scale literally builds this (SEAL). Anthropic cares about evals deeply. Even Jane Street evaluates model quality on trading signals. This is the system design problem that connects ML knowledge to engineering. Focus on the data model and the comparison/regression story — that's what's hard, not the execution.*

---

### Day 6 — Sun 2/15: Timed Mocks + Review

**Core (3 sessions, ~3hr):**

1. **TIMED MOCK #1** (45 min on CoderPad)
   Pick ONE you haven't done: LRU Cache with TTL (Problem 6), or a fresh LeetCode medium you haven't seen.
   Rules: blank CoderPad, timer running, talk out loud the entire time, write runnable Python, no looking anything up.
   *Takeaway: simulate the actual interview. The talking-out-loud habit is the single most important thing to practice.*

2. **TIMED MOCK #2** (45 min on CoderPad)
   Pick another: Merkle Tree (tree + hash, build a tree where each node's hash = hash of children), or Design a Text Editor with undo/redo (stack-based, insert/delete/cursor).
   Same rules: timer, talk out loud, no references.
   *Takeaway: second rep. You want the format to feel automatic by Tuesday.*

3. **Review weakest area** (30-60 min)
   Look back at the week. Which problem type felt shakiest? Redo one problem from scratch. Or do 2-3 quick neetcode problems in your weakest section.
   *Takeaway: patch the gap. Don't cram new material — reinforce.*

**Non-core (2 problems, ~2hr):**

1. **Minimal RAG Pipeline** (Problem 15)
   Chunk text (sentence boundaries), embed with sentence-transformers, store in FAISS, retrieve top-k, generate answer with citations. Add fallback for low-confidence.
   *Takeaway: end-to-end RAG understanding. Anthropic FDE builds these. Even a basic version teaches the retrieval → generation → citation flow.*

2. **File Upload + Parsing** (Problem 19)
   FastAPI POST /upload with multipart form. Accept CSV/JSON only, parse streaming, return preview. Clean up temp files.
   *Takeaway: file handling, streaming parse, error codes (413, 415). Practical production pattern for Scale/Anthropic coding rounds.*

**Wildcard (~1hr): Python Depth — "Know Your Language"**

Jane Street says "know your language." This is the day to make sure you do. Work through these questions — explain each one out loud as if teaching someone. Come to me if any feel shaky.

**Concepts to explain clearly:**
1. **The GIL** — What is it? Why does it exist? When does it matter? When does it NOT matter? (I/O-bound vs CPU-bound. Threading vs multiprocessing vs asyncio.)
2. **Generators and itertools** — What's a generator? How is `yield` different from `return`? When would you use one? Write a generator that produces Fibonacci numbers. Explain `itertools.chain`, `islice`, `groupby`.
3. **Decorators** — Write a timing decorator from scratch. Write a memoization decorator. Explain `functools.wraps`. When do you use `@property`?
4. **Context managers** — What does `with` do? Write a custom context manager (both class-based and `@contextmanager`). When would you use one in production?
5. **`__slots__`, `__hash__`, `__eq__`** — When do you define these? Why does `__hash__` matter for dict keys? What happens if two objects are `__eq__` but have different `__hash__`?
6. **Async internals** — What's the event loop? What does `await` actually do? Difference between `asyncio.gather` and `asyncio.create_task`? When would you use `asyncio.Queue`?

*Intent: if the JS interviewer asks "what's the time complexity of that dict lookup?" or "what happens under the hood when you iterate this generator?" — you want a crisp, confident answer. This isn't about memorizing trivia. It's about demonstrating that you understand your primary tool deeply.*

---

## Mon 2/16 — Contingency

- Don't cram new problems.
- Re-do any problem that felt weak during the week.
- Quick Python refresher: collections module (defaultdict, Counter, deque, OrderedDict), itertools, heapq API.
- Review Jane Street prep notes: `company-intel/03_ACTIVE/t0_jane-street/interview_prep.md`
- Get a good night's sleep.

---

## Tue 2/17 — Interview Day

- **10:30am ET:** Jane Street SWE coding round (Zoom + CoderPad, 35-60 min)
- Morning: light warmup — do ONE easy neetcode problem (5-10 min) just to get fingers moving. Don't do anything hard.
- Review: talk out loud, ask questions, name trade-offs, accept hints gracefully.
- Zoom link and CoderPad details in `company-intel/03_ACTIVE/t0_jane-street/jane-street.md`
