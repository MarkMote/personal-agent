# Fundamentals Q&A — Morning/Evening Reading

Things you should know cold walking into any technical interview. Read a section in the morning, revisit in the evening. If an answer feels shaky, flag it for active practice.

---

## 1. Data Structures — When and Why

**Q: When do you use a hash map vs a tree map?**
Hash map (Python dict): O(1) average get/put, unordered. Use when you need fast lookup and don't care about order. Tree map (SortedDict from sortedcontainers): O(log n) get/put, maintains sorted key order. Use when you need range queries, min/max key, or iteration in sorted order. Trade-off: hash maps waste memory on sparse keys; tree maps are slower but ordered.

**Q: When do you use a deque vs a list?**
deque (collections.deque): O(1) append/pop from both ends. Use for queues, sliding windows, BFS. list: O(1) append/pop from the right, O(n) from the left. Use when you need random access by index. Never use list as a queue — popping from the left is O(n) because everything shifts.

**Q: When do you use a heap vs sorting?**
Heap (heapq): Use when you need the top-k elements from a stream, or need to repeatedly extract the min/max. O(log n) push/pop, O(n) heapify. Sorting: Use when you need everything ordered once. O(n log n). If you only need the top 5 of 10 million items, a heap of size 5 is O(n log 5) ≈ O(n). Sorting would be O(n log n). Heap wins.

**Q: When do you use a trie?**
When you need prefix-based operations: autocomplete, spell check, IP routing, file system paths. A trie gives O(L) lookup where L is the length of the key, regardless of how many keys are stored. Trade-off: high memory usage compared to a hash map, but prefix queries are impossible with a hash map.

**Q: What's the difference between a stack and a queue? When does it matter?**
Stack: LIFO (last in, first out). Use for: undo operations, matching parentheses, DFS, call stack simulation, backtracking. Queue: FIFO (first in, first out). Use for: BFS, task scheduling, rate limiting, sliding windows. It matters when processing order determines correctness. DFS with a queue gives you BFS. BFS with a stack gives you DFS.

**Q: When do you use a set vs a list for lookups?**
set: O(1) average membership test (`x in s`). list: O(n) membership test. If you're checking membership more than once, convert to a set. Common mistake: using `if x in my_list` inside a loop — that's O(n*m). Use a set and it's O(n).

**Q: What data structure would you use for an LRU cache?**
OrderedDict (Python built-in) for the simple version: O(1) get, put, and move_to_end. For the from-scratch version: hash map + doubly-linked list. The hash map gives O(1) key lookup. The linked list gives O(1) eviction (remove tail) and O(1) promotion (move to head). You need both because neither alone gives you both operations in O(1).

---

## 2. Complexity — What Interviewers Actually Ask

**Q: What's amortized O(1)?**
An operation that's usually O(1) but occasionally O(n), and the expensive operations happen rarely enough that the average over n operations is still O(1) per operation. Example: Python list.append() is O(1) amortized. Usually it just appends. But when the internal array is full, it allocates a new array 2x the size and copies everything — that's O(n). But it only happens every ~n appends, so amortized cost is O(1).

**Q: What's the time complexity of Python's sorted() / list.sort()?**
O(n log n) — Timsort. It's a hybrid merge sort + insertion sort optimized for real-world data (partially sorted arrays). Stable sort (preserves relative order of equal elements). This matters when you sort by multiple keys: sort by the secondary key first, then the primary key, and stability preserves the secondary ordering.

**Q: What's the space complexity of your solution? (How to think about it)**
Count the extra memory beyond the input. A hash map of n items is O(n) space. Recursive DFS on a tree of depth d is O(d) space (call stack). BFS on a tree with max width w is O(w) space (the queue). In-place sorting is O(1) extra space. Merge sort is O(n) extra space. When they ask this, they're testing whether you're aware of memory, not just speed.

**Q: What's the complexity of dict operations in Python?**
Average case: O(1) for get, set, delete, `in`. Worst case: O(n) — hash collisions degrade to linear scan. In practice, Python's dict implementation (open addressing with perturbation) almost never hits worst case. Keys must be hashable (immutable). Two objects that are `__eq__` must have the same `__hash__` or the dict breaks silently.

---

## 3. Python Internals — "Know Your Language"

**Q: What is the GIL and when does it matter?**
The Global Interpreter Lock prevents multiple threads from executing Python bytecode simultaneously. One thread runs at a time. It matters for CPU-bound work: threading won't speed up number crunching. It does NOT matter for I/O-bound work: while one thread waits on a network call or file read, another thread can run. Solutions for CPU parallelism: multiprocessing (separate processes, no shared GIL), or use C extensions (NumPy releases the GIL during array operations).

**Q: Threading vs multiprocessing vs asyncio — when do you use each?**
- **asyncio**: I/O-bound work with many concurrent connections (web servers, API calls, database queries). Single thread, cooperative multitasking. Best for: lots of waiting.
- **threading**: I/O-bound work where you need simpler code than async (or legacy code). Multiple threads, GIL limits CPU parallelism. Best for: simple concurrency.
- **multiprocessing**: CPU-bound work (data processing, model training, image manipulation). Separate processes, no GIL. Best for: actual parallel computation. Higher memory cost (each process has its own memory space).

**Q: How does Python's dict work internally?**
Open addressing hash table. When you insert a key, Python computes hash(key), maps it to an index in an internal array, and stores the key-value pair there. On collision (two keys map to same index), it probes to the next open slot using a perturbation sequence. Load factor is kept below ~2/3 by resizing (doubling) the table. This is why dicts use more memory than you'd expect — they're at most 2/3 full. Since Python 3.7, dicts maintain insertion order (implementation detail promoted to language guarantee).

**Q: What's a generator and why would you use one?**
A function that uses `yield` instead of `return`. It produces values lazily — one at a time, on demand. The function's state is suspended between yields. Use when: processing large datasets that don't fit in memory, infinite sequences, or when you only need one element at a time. Memory: O(1) regardless of how many values it produces, vs O(n) for building a list. Example: `range(1_000_000_000)` is a lazy range object, not a list of a billion integers.

**Q: What does `@decorator` actually do?**
Syntactic sugar for wrapping a function. `@dec def f(): ...` is equivalent to `f = dec(f)`. A decorator is any callable that takes a function and returns a function (or callable). Common uses: timing, logging, caching (@functools.lru_cache), access control, retry logic. Use `@functools.wraps(fn)` inside your decorator to preserve the original function's name and docstring.

**Q: What are `__slots__`?**
A class-level declaration that tells Python "these are the only attributes instances will have." Replaces the per-instance `__dict__` with a fixed-size struct. Benefits: ~30-40% less memory per instance, slightly faster attribute access. Trade-off: no dynamic attributes, no `__dict__`, slightly more rigid. Use when you have millions of instances of a simple class (like nodes in a graph or entries in a cache).

**Q: Explain `with` / context managers.**
`with open(f) as file:` ensures cleanup (file.close()) even if an exception occurs. A context manager implements `__enter__` (setup, return the resource) and `__exit__` (cleanup, handle exceptions). Use `@contextlib.contextmanager` for simple cases: everything before `yield` is `__enter__`, everything after is `__exit__`. Use for: file handles, database connections, locks, temporary state changes, timing blocks.

---

## 4. Trees and Graphs — Patterns to Know

**Q: What are the three depth-first traversals and when do you use each?**
- **Preorder** (root, left, right): Use to serialize/copy a tree. Visit root first.
- **Inorder** (left, root, right): Use on BSTs — gives sorted order. This is how you validate a BST or find kth smallest.
- **Postorder** (left, right, root): Use when you need children processed before parent (delete tree, calculate directory sizes, evaluate expression trees).

**Q: BFS vs DFS — when do you use which?**
- **BFS** (queue-based): shortest path in unweighted graphs, level-order traversal, finding nearest X. Space: O(width of tree/graph).
- **DFS** (stack/recursion): detecting cycles, topological sort, path finding, backtracking. Space: O(depth of tree/graph).
Rule of thumb: BFS for shortest path, DFS for exploring all paths or detecting structure (cycles, components).

**Q: How do you detect a cycle in a directed graph?**
DFS with three states: WHITE (unvisited), GRAY (in current path), BLACK (fully processed). If you visit a GRAY node, there's a cycle. This is the standard approach for topological sort with cycle detection. Alternative: Kahn's algorithm (BFS) — if the topological sort doesn't include all nodes, there's a cycle.

**Q: What's topological sort and when do you need it?**
Linear ordering of nodes in a DAG such that for every edge u→v, u appears before v. Use for: dependency resolution (build systems, package managers, course prerequisites, spreadsheet formulas). Two approaches: DFS (reverse postorder) or BFS (Kahn's algorithm — repeatedly remove nodes with no incoming edges).

**Q: How do you find the lowest common ancestor (LCA)?**
For a BST: walk down from root. If both nodes are less, go left. If both greater, go right. Otherwise, current node is LCA. O(h) time. For a general binary tree: recursive — if current node is null or matches either target, return it. Recurse left and right. If both return non-null, current node is LCA. If only one returns non-null, that's the LCA. O(n) time.

---

## 5. System Design Concepts

**Q: What's the CAP theorem in plain English?**
In a distributed system, you can only guarantee two of three: Consistency (every read gets the most recent write), Availability (every request gets a response), Partition tolerance (system works despite network failures). Since network partitions always happen in practice, you're really choosing between consistency (CP — reject requests when uncertain) and availability (AP — serve stale data rather than fail). Most real systems choose AP with eventual consistency.

**Q: What's the difference between horizontal and vertical scaling?**
Vertical: bigger machine (more CPU, RAM). Simple, no code changes, but has a ceiling. Horizontal: more machines. Requires distributed architecture (load balancing, data partitioning, consistency protocols) but scales infinitely. Almost always prefer horizontal for production systems because vertical has a hard limit and a single point of failure.

**Q: How does a load balancer work? What algorithms exist?**
Distributes requests across servers. Algorithms: round-robin (simple rotation), least connections (send to least busy), weighted (some servers handle more), consistent hashing (route by key, minimizes redistribution when servers change). Health checks remove dead servers. Can be L4 (TCP level) or L7 (HTTP level — can route by URL, headers, cookies).

**Q: What's a message queue and when do you use one?**
Decouples producers from consumers. Producer sends a message, consumer processes it later. Use when: work is slow or unreliable (sending emails, processing images, calling external APIs), you need to handle traffic spikes (queue absorbs the burst), or you need to decouple services. Examples: Redis, RabbitMQ, Kafka. Key concepts: at-least-once vs exactly-once delivery, dead letter queues for failed messages, backpressure.

**Q: What's caching and what are the invalidation strategies?**
Store frequently accessed data in a fast layer (memory) to avoid hitting a slow layer (database, API). Strategies: TTL (time-to-live — expires after N seconds, simple but stale data possible), write-through (update cache on every write, consistent but slower writes), write-behind (update cache now, write to DB async, fast but data loss risk), cache-aside (app manages cache, most flexible). "There are only two hard things in computer science: cache invalidation and naming things."

**Q: What's rate limiting and how do you implement it?**
Restrict how many requests a client can make in a time window. Algorithms: fixed window (count per minute, simple but burst-prone at window boundaries), sliding window (deque of timestamps, smooth but more memory), token bucket (tokens refill at a rate, allows controlled bursts, most common in production), leaky bucket (requests queue and drain at fixed rate, smooth output).

---

## 6. ML Fundamentals

**Q: Explain backpropagation in one paragraph.**
Forward pass: input flows through the network, producing an output and a loss. Backward pass: compute the gradient of the loss with respect to every weight by applying the chain rule from the output layer back to the input layer. Each layer computes its local gradient and passes it backward. The optimizer then updates each weight by stepping in the direction that reduces the loss (gradient descent). The key insight: you can compute all gradients in one backward pass (same cost as the forward pass) because the chain rule decomposes into local operations.

**Q: What's the difference between SGD, SGD+momentum, and Adam?**
- **SGD**: Update weights by `w -= lr * gradient`. Simple, noisy, can get stuck in local minima.
- **SGD+momentum**: Maintain a running average of gradients (velocity). Smooths out noise, accelerates through flat regions. Like a ball rolling downhill with inertia.
- **Adam**: Adaptive learning rate per parameter. Maintains both momentum (first moment) and squared gradient history (second moment). Automatically scales the step size — parameters with large gradients get smaller steps. Default choice for most deep learning. Less sensitive to learning rate tuning.

**Q: What's overfitting and how do you prevent it?**
Model memorizes training data instead of learning general patterns. Test performance is much worse than training performance. Prevention: more data (best), regularization (L1/L2 weight penalty), dropout (randomly zero neurons during training), early stopping (stop training when validation loss stops improving), data augmentation, simpler model (fewer parameters). Diagnosis: plot train loss vs validation loss over epochs — divergence = overfitting.

**Q: L1 vs L2 regularization — what's the difference?**
- **L1** (Lasso): Adds `λ * Σ|w|` to loss. Pushes weights to exactly zero — produces sparse models. Use for feature selection.
- **L2** (Ridge): Adds `λ * Σw²` to loss. Pushes weights toward zero but never exactly zero — produces small weights. Use for preventing any single feature from dominating.
- **Intuition**: L1 has a diamond-shaped constraint region (corners at axes = sparse solutions). L2 has a circular constraint region (no corners = weights shrink uniformly).

**Q: What's dropout and why does it work?**
During training, randomly set each neuron's output to zero with probability p (typically 0.1-0.5). During inference, use all neurons but scale outputs by (1-p). Why it works: forces the network to be redundant — no single neuron can be relied on. Acts like training an ensemble of sub-networks. Prevents co-adaptation (neurons that only work in combination with specific other neurons).

**Q: Explain the bias-variance tradeoff.**
- **Bias**: error from underfitting (model too simple to capture the pattern).
- **Variance**: error from overfitting (model too sensitive to training data noise).
- Simple models: high bias, low variance (consistently wrong in the same way).
- Complex models: low bias, high variance (fits training data perfectly, fails on new data).
- Goal: find the sweet spot. As model complexity increases, bias decreases and variance increases. Total error is U-shaped — minimum is where they balance.

**Q: When would you use a tree-based model vs a neural network?**
- **Tree-based** (Random Forest, XGBoost, LightGBM): tabular data, structured features, small-to-medium datasets. Handles missing values, mixed types, feature interactions automatically. Less tuning needed. Interpretable (feature importance). Often wins on Kaggle for tabular data.
- **Neural network**: images, text, audio, sequential data. Learns representations from raw data. Needs more data and compute. Less interpretable. Dominates unstructured data.
- Rule of thumb: if your data fits in a CSV and has meaningful column names, try XGBoost first.

**Q: What are precision, recall, and F1?**
- **Precision**: of all items you predicted positive, what fraction are actually positive? High precision = few false positives. Important when: cost of false positive is high (spam filter marking real email as spam).
- **Recall**: of all actual positives, what fraction did you predict? High recall = few false negatives. Important when: cost of missing a positive is high (cancer screening).
- **F1**: harmonic mean of precision and recall. Balances both. Use when you care about both false positives and false negatives equally.
- Trade-off: increasing the classification threshold increases precision but decreases recall.

---

## 7. LLM and Agentic Systems

**Q: How does a transformer work at a high level?**
Input text is tokenized into subword tokens, each mapped to an embedding vector. The self-attention mechanism allows every token to attend to every other token, computing relevance weights. Multi-head attention runs this in parallel across different "heads" that learn different relationships. Feed-forward layers process each position independently. Layers are stacked (GPT-4 has ~120 layers). Output: a probability distribution over the next token. Key innovation: attention replaces recurrence — enables parallelization and captures long-range dependencies.

**Q: What is RAG and when do you use it?**
Retrieval-Augmented Generation: instead of relying solely on the LLM's trained knowledge, you retrieve relevant documents from an external store and include them in the prompt. Pipeline: query → embed → search vector store → retrieve top-k chunks → inject into prompt → generate answer. Use when: knowledge changes frequently, domain-specific data, need citations/provenance, want to reduce hallucination. Key decisions: chunk size, embedding model, retrieval method (dense vs sparse vs hybrid), re-ranking.

**Q: What's an agent (in the LLM sense)?**
An LLM that can take actions in a loop: observe → think → act → observe result → think again. The ReAct pattern: LLM generates a "Thought" (reasoning), then an "Action" (tool call), receives an "Observation" (tool result), and repeats until it has enough information to produce a final answer. Key components: tool definitions, action parsing, execution environment, stopping criteria, error handling. Production challenges: tool failures, infinite loops, cost control, evaluation.

**Q: What's MCP (Model Context Protocol)?**
Anthropic's protocol for connecting LLMs to external tools and data sources. A server exposes "tools" (functions the LLM can call) and "resources" (data the LLM can read). Communication is via JSON-RPC over stdio. The LLM client discovers available tools, decides when to call them, and processes results. MCP standardizes what was previously ad-hoc tool integration — one protocol that works across different LLM providers.

**Q: What are evals and why do they matter?**
Evaluations measure how well an LLM performs on specific tasks. Types: exact match (does the output match the gold answer?), LLM-as-judge (use another LLM to rate quality), human evaluation (gold standard but slow/expensive), task-specific metrics (code: does it pass tests? SQL: does it return correct results?). Why they matter: you can't improve what you can't measure. Before changing a prompt, model, or pipeline, you need a baseline. Regression detection: did this change make things worse? Evals are the tests of the LLM world.

**Q: What's prompt engineering? What are the key techniques?**
Designing the input to an LLM to get better outputs. Techniques: few-shot examples (show 2-3 examples of desired input→output), chain-of-thought ("think step by step"), system prompts (set the persona/context), structured output (ask for JSON with a schema), role assignment ("you are a senior engineer reviewing code"). Advanced: prompt chaining (output of one prompt feeds into the next), self-consistency (sample multiple answers, take majority vote), retrieval-augmented prompting (RAG).

**Q: How do you handle hallucination in production?**
Hallucination: the LLM generates plausible but false information. Mitigation strategies: RAG (ground responses in retrieved facts), constrained generation (force output to match a schema or known set), confidence scoring (if the model is uncertain, say "I don't know"), fact-checking (cross-reference with a knowledge base), citation requirements (force the model to cite sources, then verify them), human review for high-stakes outputs.

---

## 8. Concurrency and Async

**Q: What is async/await in Python? How does it work?**
Cooperative multitasking within a single thread. `async def` defines a coroutine. `await` suspends the coroutine and yields control back to the event loop, which can run other coroutines. The event loop manages which coroutine runs when. Key: nothing runs in parallel — but while one coroutine waits on I/O (network, disk), another can run. This is why it's great for I/O-bound work (web servers, API calls) but useless for CPU-bound work.

**Q: What's asyncio.gather vs asyncio.create_task?**
- `asyncio.gather(*coros)`: Run multiple coroutines concurrently, wait for all to finish, return all results. Use when you have a batch of independent operations.
- `asyncio.create_task(coro)`: Schedule a coroutine to run in the background. Returns a Task object you can await later (or not). Use when you want to fire-and-forget or need more control over task lifecycle.
- Key difference: gather waits for everything. create_task lets you do other work before awaiting.

**Q: What's a race condition? How do you prevent it?**
Two concurrent operations access shared state, and the result depends on timing. Example: two threads read a counter as 5, both increment to 6, but the correct answer should be 7. Prevention: locks/mutexes (only one thread accesses at a time), atomic operations, immutable data structures, message passing (share nothing, communicate by sending messages). In async Python: use `asyncio.Lock` when multiple coroutines access shared mutable state.

**Q: What's a deadlock?**
Two or more threads/processes are each waiting for the other to release a resource. Neither can proceed. Classic example: Thread A holds Lock 1, wants Lock 2. Thread B holds Lock 2, wants Lock 1. Both wait forever. Prevention: always acquire locks in the same order, use timeouts, avoid holding multiple locks, use higher-level constructs (queues, async patterns).

---

## 9. Production Engineering — Quick Hits

**Q: How would you debug a production system that's suddenly slow?**
1. Check metrics: CPU, memory, disk I/O, network. Is the machine overloaded?
2. Check logs: any errors, warnings, or unusual patterns?
3. Check external dependencies: database slow? API timeout? Network issue?
4. Profile: where is time being spent? Add timing to key operations.
5. Check recent changes: did a deployment just happen? New config? Data volume increase?
6. Reproduce: can you replicate the slowness with specific inputs?
The order matters — start broad (is the machine healthy?) then narrow down.

**Q: What's the difference between latency and throughput?**
- **Latency**: time for a single request (ms). "How long does one request take?"
- **Throughput**: requests per second. "How many can I handle?"
They're related but not the same. You can have low latency and low throughput (one fast worker). You can have high latency and high throughput (batch processing). Optimizing for one often hurts the other (batching increases throughput but adds latency for individual requests).

**Q: What's idempotency and why does it matter in APIs?**
An operation is idempotent if performing it multiple times has the same effect as performing it once. GET is idempotent (reading doesn't change state). PUT is idempotent (setting a value to X twice = setting it once). POST is NOT idempotent (creating a resource twice = two resources). Why it matters: network failures cause retries. If your POST handler isn't idempotent, retries create duplicates. Fix: use idempotency keys — client sends a unique ID with each request, server checks if it's already been processed.

**Q: What's a circuit breaker pattern?**
If a downstream service is failing, stop calling it temporarily instead of piling up timeouts. States: CLOSED (normal, requests pass through), OPEN (service is down, fail fast without calling), HALF-OPEN (try one request to see if service recovered). Prevents cascading failures — without it, one slow service can make your whole system slow by eating up all your connection/thread pool.
