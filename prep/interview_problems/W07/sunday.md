# Sunday 2/15 — Timed Mocks + Review

---

## Core 1: TIMED MOCK #1 — LRU Cache with TTL (45 min)

**Rules:** Open a blank CoderPad (coderpad.io/sandbox). Start timer. Talk out loud the entire time. No looking anything up. Write runnable Python.

Implement an LRU cache that also supports per-key TTL (time-to-live).

```python
from collections import OrderedDict
from typing import Optional

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = OrderedDict()  # key -> (value, expiry_time or None)

    def _now(self) -> int:
        # In real code this would be time.time()
        # For testing, inject a mock clock
        ...

    def get(self, key: str) -> Optional[str]: ...
    def put(self, key: str, value: str, ttl: Optional[int] = None) -> None: ...
    def size(self) -> int: ...
```

**Operations:**
1. `get(key)` — Return value and mark as most-recently-used. If key doesn't exist or has expired, return None and remove the expired entry.
2. `put(key, value, ttl)` — Insert or update. `ttl` is optional seconds; if omitted, key never expires. If cache exceeds capacity, evict the LRU non-expired item. Expired items are silently removed on access.
3. `size()` — Return count of non-expired keys currently stored.

**Constraints:**
- 1 ≤ capacity ≤ 10^4.
- All operations O(1) amortized.
- Memory O(capacity).
- Assume monotonically non-decreasing timestamps.

**Edge cases:**
```python
cache = LRUCache(2)
cache.put("a", "1", ttl=5)  # expires at now()+5
cache.put("b", "2")         # never expires
cache.get("a")              # "1"
cache.put("c", "3")         # evicts "b" (LRU among non-expired), not "a"
cache.size()                # 2
# after 5 seconds...
cache.get("a")              # None (expired)
cache.size()                # 1 (only "c" remains)
```

**After finishing:** review your code. What would you refactor? What's the complexity? What edge cases did you miss?

---

## Core 2: TIMED MOCK #2 — Pick ONE (45 min)

Same rules: blank CoderPad, timer, talk out loud, no references.

### Option A: Merkle Tree

Build a tree where each leaf node holds data, and each internal node holds the hash of its children's hashes.

```python
import hashlib

class MerkleTree:
    def __init__(self, data: List[str]): ...
    def get_root_hash(self) -> str: ...
    def verify(self, index: int, data: str) -> bool: ...
    def get_proof(self, index: int) -> List[tuple]: ...
```

**Stage 1 — Build the tree (~15 min):**
- Leaves: `hash(data_item)` for each item.
- Internal nodes: `hash(left_child_hash + right_child_hash)`.
- If odd number of nodes at a level, duplicate the last one.
- Store as a list (like a binary heap) or as actual tree nodes.

**Stage 2 — Root hash (~5 min):**
- `get_root_hash()` — Return the root's hash. This is the "fingerprint" of all the data.

**Stage 3 — Proof and verify (~20 min):**
- `get_proof(index)` — Return the list of (hash, side) pairs needed to verify that data[index] is in the tree. "side" is "left" or "right" indicating which side the sibling hash goes on.
- `verify(index, data)` — Recompute the root hash using the data and its proof. Return True if it matches the stored root.

**Why this matters:** Merkle trees are used in git, blockchain, and distributed systems for efficient data verification. JS candidate reported "tree class with hash functions" as an interview question.

### Option B: Text Editor with Undo/Redo

Build a simple text editor with cursor, insert, delete, and undo/redo.

```python
class TextEditor:
    def __init__(self): ...
    def insert(self, char: str) -> None: ...
    def delete(self) -> Optional[str]: ...
    def move_left(self) -> None: ...
    def move_right(self) -> None: ...
    def get_text(self) -> str: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...
```

**Stage 1 — Basic editing (~15 min):**
- Maintain text as a list of characters and a cursor position (index).
- `insert(char)` — Insert at cursor position, advance cursor.
- `delete()` — Delete character before cursor (backspace). Return deleted char or None.
- `move_left()` / `move_right()` — Move cursor. Clamp to bounds.
- `get_text()` — Return full text as string.

**Stage 2 — Undo/Redo (~25 min):**
- Maintain an undo stack and a redo stack.
- Each action (insert, delete) pushes an inverse operation onto the undo stack.
- `undo()` — Pop from undo stack, execute the inverse, push to redo stack.
- `redo()` — Pop from redo stack, execute, push to undo stack.
- Any new edit clears the redo stack.

**Why this matters:** Stack-based state management, command pattern. Tests the same skills as the transactional KV store but in a different context.

---

## Core 3: Review Weakest Area (30-60 min)

Look back at the week:
- Which problem type felt shakiest?
- Where did you get stuck longest?
- What data structure operations felt slow or uncertain?

Options:
- Redo one problem from scratch (without looking at your previous solution).
- Do 2-3 quick neetcode problems in your weakest section.
- Review the fundamentals_qa.md section that felt least solid.

**Don't cram new material. Reinforce.**

---

## Non-Core 1: Minimal RAG Pipeline

Build an offline RAG system: chunk, embed, store, retrieve, generate.

```python
class RAG:
    def __init__(self, index_dir: str = "faiss_index"): ...
    def build(self, documents: list[dict], chunk_size: int = 256, overlap: int = 50) -> None: ...
    def query(self, question: str, top_k: int = 5, rerank: bool = False) -> dict: ...
```

**Requirements:**
1. `build(documents)` — documents are `[{"id": str, "text": str}]`. Chunk text respecting sentence boundaries (use `nltk.sent_tokenize`). Embed with `sentence-transformers` (`all-MiniLM-L6-v2`, dim=384). Store in FAISS `IndexFlatIP` (cosine similarity).
2. `query(question)` — Embed question, retrieve top-k chunks, return:
   ```json
   {"answer": "...", "citations": [{"doc_id": "...", "chunk_id": 0, "score": 0.87, "text": "..."}], "fallback": false}
   ```
3. Fallback: if best score < 0.35, return "I don't know." with empty citations and `fallback: true`.

**Dependencies:** `sentence-transformers`, `faiss-cpu`, `nltk`, `numpy`.

**The point:** Understand the full RAG pipeline end-to-end. Even a basic version teaches chunking → embedding → retrieval → generation → citation.

---

## Non-Core 2: File Upload + Parsing

Add a file upload endpoint to a FastAPI app.

```python
from fastapi import FastAPI, UploadFile, HTTPException

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile): ...
```

**Requirements:**
1. Accept multipart form with field `file` (max 10 MB).
2. Accept only `.csv` and `.json` MIME types. Return 415 for wrong type, 413 for too large.
3. Save to temp directory with UUID filename.
4. Parse:
   - CSV → `{"rows": int, "columns": ["col1", ...], "preview": [{...}, ...]}` (first 5 rows)
   - JSON → `{"type": "object|array", "size": int, "keys": [...] | null}`
5. Clean up temp file after parsing (`try/finally`).
6. Streaming parse (csv.DictReader) to avoid RAM blowup.

**Keep handler ≤ 80 lines.**

---

## Wildcard: Python Depth — "Know Your Language"

*(Study + practice, ~1hr. Explain each concept out loud as if teaching.)*

**1. The GIL**
- What is it? Why? When does it matter (CPU-bound)? When not (I/O-bound)?
- Threading vs multiprocessing vs asyncio — when to use each?

**2. Generators and itertools**
- What's `yield` vs `return`? Write a Fibonacci generator.
- `itertools.chain`, `islice`, `groupby` — what does each do?

**3. Decorators**
- Write a timing decorator from scratch.
- Write a memoization decorator. Explain `functools.wraps`.

**4. Context managers**
- Write a custom context manager (class-based and `@contextmanager`).
- When would you use one in production?

**5. Dunder methods**
- `__slots__`: when and why?
- `__hash__` + `__eq__`: rules for dict keys.
- `__repr__` vs `__str__`: when is each called?

**6. Async internals**
- What's the event loop? What does `await` do?
- `asyncio.gather` vs `asyncio.create_task` — difference?
- `asyncio.Queue` — when would you use it?

**If anything feels shaky, look it up and write a 3-line example. Understanding > memorization.**
