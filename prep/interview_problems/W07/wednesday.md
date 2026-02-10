# Wednesday 2/11 — Trees (Light day: Laurion 1pm, Archer 4pm)

---

## Core 1: Serialize and Deserialize Binary Tree (LC 297)

Design an algorithm to serialize a binary tree to a string and deserialize that string back to the original tree.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str: ...
    def deserialize(self, data: str) -> TreeNode: ...
```

**Approach options:**
- **Preorder DFS:** Serialize as "1,2,null,null,3,4,null,null,5,null,null". Use "null" for missing children. Deserialize by consuming tokens from a queue.
- **BFS (level-order):** Serialize level by level with "null" for missing nodes. Deserialize by processing each level with a queue.

**Constraints:**
- The number of nodes is in range [0, 10^4].
- -1000 <= Node.val <= 1000.

**Example:**
```
    1
   / \
  2   3
     / \
    4   5

serialize → "1,2,null,null,3,4,null,null,5,null,null"  (preorder)
deserialize("1,2,null,null,3,4,null,null,5,null,null") → original tree
```

**Key things to get right:**
- Handle null/empty nodes explicitly.
- Handle empty tree (root is None).
- Deserialize must consume tokens in the right order.

---

## Core 2: Validate BST (LC 98) + Kth Smallest in BST (LC 230)

**Part A — Validate BST:**

Given a binary tree, determine if it is a valid binary search tree.

```python
def isValidBST(self, root: TreeNode) -> bool: ...
```

A valid BST means: for every node, all values in left subtree < node.val, all values in right subtree > node.val (strictly). This must hold for ALL descendants, not just immediate children.

**Approach:** Recursive with min/max bounds. `validate(node, low=-inf, high=inf)`. Left child: update high to node.val. Right child: update low to node.val.

**Common mistake:** Only checking immediate children. The tree `[5,1,6,null,null,3,7]` has 3 in the right subtree of 5, which violates BST property even though 3 < 6.

**Part B — Kth Smallest in BST:**

Given a BST and an integer k, return the kth smallest element.

```python
def kthSmallest(self, root: TreeNode, k: int) -> int: ...
```

**Approach:** In-order traversal (iterative with a stack). Count nodes as you pop them. When count == k, return that node's value.

```
# Iterative in-order traversal pattern:
stack = []
current = root
count = 0
while stack or current:
    while current:
        stack.append(current)
        current = current.left
    current = stack.pop()
    count += 1
    if count == k:
        return current.val
    current = current.right
```

**Key takeaway:** In-order traversal of a BST visits nodes in sorted order. This pattern is used constantly.

---

## Core 3: Construct Binary Tree from Preorder and Inorder (LC 105)

Given two integer arrays `preorder` and `inorder`, construct and return the binary tree.

```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode: ...
```

**Key insight:**
- Preorder's first element is always the root.
- Find that root in inorder — everything to its left is the left subtree, everything to its right is the right subtree.
- Recurse on the left and right portions.

**Optimization:** Build a hash map of `{value: index}` for inorder array for O(1) root lookup instead of O(n) search each time.

**Example:**
```
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]

Root = 3
Left subtree inorder: [9], preorder: [9]
Right subtree inorder: [15,20,7], preorder: [20,15,7]

Result:
    3
   / \
  9  20
    /  \
   15   7
```

**Constraints:**
- 1 <= preorder.length <= 3000
- All values are unique.
- preorder and inorder have the same length.

---

## Non-Core 1: FastAPI Async Endpoint + Pydantic Schemas

Build a single-file async FastAPI service with Pydantic request/response models.

```python
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from datetime import datetime, timezone
import asyncio

app = FastAPI(title="Hello Async")

class HelloQuery(BaseModel):
    name: str = Field("stranger", description="Name to greet")
    delay_ms: int = Field(0, ge=0, description="Artificial I/O delay in ms")

class HelloResponse(BaseModel):
    message: str
    timestamp: str

@app.get("/hello", response_model=HelloResponse)
async def hello(
    name: str = Query("stranger"),
    delay_ms: int = Query(0, ge=0)
) -> HelloResponse:
    if delay_ms > 0:
        await asyncio.sleep(delay_ms / 1000)
    now = datetime.now(timezone.utc).isoformat()
    return HelloResponse(message=f"Hello, {name}!", timestamp=now)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
```

**Requirements:**
1. `GET /hello?name={name}&delay={delay_ms}` — name defaults to "stranger", delay defaults to 0.
2. Response: `{"message": "Hello, <name>!", "timestamp": "2024-11-05T14:23:45.123456+00:00"}`
3. Timestamp must be ISO-8601 UTC.
4. All I/O must be async. Delay simulated with `asyncio.sleep`.
5. Validation errors return 422 automatically.
6. Runnable with `python app.py`.

**Keep it ≤ 60 lines.** The point is to have the FastAPI + Pydantic + async pattern in muscle memory.

---

## Non-Core 2: Inference Utilities

Extend the MNIST model from Day 1 with production-grade inference.

```python
import torch
from datetime import datetime

def set_seed(seed: int) -> None:
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def predict(model: torch.nn.Module, x: torch.Tensor) -> int:
    # Single 28x28 image → predicted class (0-9)
    # Must: .eval(), no_grad(), handle device
    ...

def predict_batch(model: torch.nn.Module, X: torch.Tensor) -> list[int]:
    # Batch of (N, 1, 28, 28) → list of N predicted classes
    ...

def save_checkpoint(model, path: str, metadata: dict) -> None:
    # Save state_dict + metadata (epoch, accuracy, timestamp)
    torch.save({"state_dict": model.state_dict(), "metadata": metadata}, path)

def load_checkpoint(path: str) -> tuple[dict, dict]:
    # Return (state_dict, metadata). Must be portable (loadable on CPU).
    data = torch.load(path, map_location="cpu")
    return data["state_dict"], data["metadata"]
```

**Requirements:**
- All inference moves inputs to the correct device automatically.
- Checkpoint is portable (loadable on CPU even if trained on GPU).
- Keep all 4 functions ≤ 60 lines total.
- Quick exercise — 30-40 min.

---

## Wildcard: Storytelling — Roostr

*(Talk-through exercise, no coding. ~1hr. Practice out loud.)*

**Q1: "What did you build at Roostr and why?"** (3 min max)
Walk through end-to-end: business problem → technical solution → results.

**Q2: "What was the hardest technical problem you solved at Roostr?"** (3 min max)
Pick ONE. Go deep: what made it hard, what you tried, what failed, what worked.

**Q3: "Why are you leaving?"** (1 min max)
Clean, honest, forward-looking. No defensiveness.
