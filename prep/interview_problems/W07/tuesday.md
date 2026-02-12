# Tuesday 2/10 — Foundations

---

## Core 1: LRU Cache (LC 146)

Implement a data structure that follows the constraints of a Least Recently Used (LRU) cache.

```python
class LRUCache:
    def __init__(self, capacity: int): ...
    def get(self, key: int) -> int: ...
    def put(self, key: int, value: int) -> None: ...
```

**Operations:**
1. `get(key)` — Return the value if key exists, otherwise return -1. Mark as most recently used.
2. `put(key, value)` — Update or insert. If the cache exceeds capacity, evict the least recently used key before inserting.

**Constraints:**
- 1 <= capacity <= 3000
- Both `get` and `put` must be **O(1)** time.

**Do it twice:**
- **Version A:** Use `collections.OrderedDict` (move_to_end on access, popitem(last=False) for eviction).
- **Version B:** Implement from scratch with a dict + doubly-linked list. Write the Node class, maintain head/tail sentinel nodes.

**Example:**
```
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1
cache.put(4, 4)    # evicts key 1
cache.get(1)       # returns -1
cache.get(3)       # returns 3
cache.get(4)       # returns 4
```

---

## Core 2: In-Memory File System

Design a simple in-memory file system that supports the following operations:

```python
class FileSystem:
    def __init__(self): ...
    def ls(self, path: str) -> List[str]: ...
    def mkdir(self, path: str) -> None: ...
    def add_content(self, path: str, content: str) -> None: ...
    def read_content(self, path: str) -> str: ...
```

**Operations:**
1. `ls(path)` — Return names of files and immediate sub-directories in lexicographic order. If path is a file, return a list containing only the file name.
2. `mkdir(path)` — Create a directory (and any missing parents). Do nothing if it already exists.
3. `add_content(path, content)` — Create the file (and missing parents) if it doesn't exist, then append content.
4. `read_content(path)` — Return the full content of the file at path.

**Constraints:**
- All paths are non-empty strings separated by `/`.
- File and directory names are alphanumeric.
- All operations must be O(d) where d is the depth of the path.

**Implementation hint:** Use a trie where each node represents a directory or file. Each node has a `children` dict and optionally `content` (if it's a file).

**Example:**
```
fs = FileSystem()
fs.mkdir("/a/b/c")
fs.add_content("/a/b/c/d", "hello ")
fs.add_content("/a/b/c/d", "world")
fs.read_content("/a/b/c/d")  # "hello world"
fs.ls("/a/b/c")               # ["d"]
fs.ls("/a/b")                  # ["c"]
```

---

## Core 3: Design HashMap (LC 706)

Design a HashMap without using any built-in hash table libraries.

```python
class MyHashMap:
    def __init__(self): ...
    def put(self, key: int, value: int) -> None: ...
    def get(self, key: int) -> int: ...
    def remove(self, key: int) -> None: ...
```

**Operations:**
1. `put(key, value)` — Insert or update.
2. `get(key)` — Return value or -1 if not found.
3. `remove(key)` — Remove the key if it exists.

**Constraints:**
- 0 <= key, value <= 10^6
- At most 10^4 operations.

**Implementation:** Use an array of buckets with chaining (each bucket is a linked list or Python list of (key, value) pairs). Hash function: `key % num_buckets`.

**Extension (discuss, don't necessarily implement):**
- What happens when load factor exceeds a threshold? → Resize and rehash.
- What's a good initial bucket count? → Prime number, typically 1009 or 2069.
- How does Python's dict differ from this? → Open addressing vs chaining, perturbation probing.

---

## Non-Core 1: Train MNIST MLP End-to-End

Write a complete training pipeline for a 2-layer MLP on MNIST. Single file, no wrappers.

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        ...
    def forward(self, x):
        ...

def train_epoch(model, loader, criterion, optimizer, device): ...
def evaluate(model, loader, device): ...
def main(): ...

if __name__ == "__main__":
    main()
```

**Requirements:**
1. Dataset: `torchvision.datasets.MNIST`, transforms: `ToTensor()`, `Normalize((0.1307,), (0.3081,))`. DataLoader: batch_size=64, shuffle=True for train.
2. Model: `Linear(784, 128)` → `ReLU` → `Linear(128, 10)`. Flatten 28x28 → 784.
3. Loss: `CrossEntropyLoss`. Optimizer: `Adam(lr=1e-3)`.
4. Train 3 epochs. Print loss every 100 batches: `Epoch X, Batch Y, Loss Z.ZZZ`. Use `.train()` mode.
5. Eval after each epoch on test set. Report: `Test Accuracy: XX.XX%`. Use `.eval()` + `torch.no_grad()`.
6. Save `model.state_dict()` to `checkpoint.pth`.

**Target:** ≥95% test accuracy after 3 epochs. Keep code ≤150 lines.

---

## Non-Core 2: PyTorch Debugging Drill

Find and fix all 5 bugs in this training script. Each bug has a category: shape error, exploding loss, bad normalization, device mismatch, or incorrect mode.

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

X = torch.randn(1000, 10)
y = torch.randint(0, 3, (1000,))
dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=32)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 3)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)  # BUG 1: missing final activation?

model = Net()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=10.0)  # BUG 2

for epoch in range(5):
    model.eval()  # BUG 3
    for X_batch, y_batch in loader:
        # BUG 4: device mismatch
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # BUG 5: shape error in custom metric
        acc = (outputs.argmax(dim=1) == y_batch).float().mean()
        print(f"Loss: {loss.item():.4f}, Acc: {acc.item():.4f}")
```

**Task:** For each bug: (1) name the category, (2) provide the one-line fix, (3) explain why it causes the stated symptom. Write your answers in this format:
```
BUG 1: Category = ...
Fix: ...
Why: ...
```

---

## Wildcard: System Design — Document Processing API

*(Talk-through exercise, no coding. ~1hr.)*

You're building an API for a company that needs to ingest thousands of documents (PDFs, CSVs, Word docs) per day, extract structured data, and make it searchable.

**Talk through:**
- How do you handle different file formats? Plugin architecture vs monolith?
- Sync vs async processing? User uploads → gets result later, or blocks?
- Storage: raw files vs extracted text vs structured output. Where does each live?
- Search: full-text vs embeddings vs both? How do you index?
- What breaks at 10x scale? At 100x?
- How would you add a new document type in 6 months without rewriting?


UNDERSTAND: 
- how would i do rag on my thesis