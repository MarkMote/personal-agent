# Merkle Tree

Reported Jane Street problem.

**Task:** Given a list of data items, build a Merkle tree (binary tree where each node stores the hash of its children). Then implement `get_proof(index)` that returns the minimal set of hashes needed to verify a specific item, and `verify(index, value, proof)` that checks the proof against the root hash.

```python
import hashlib

class MerkleNode:
    def __init__(self, value: str = None, left=None, right=None): ...
    def hash(self) -> str: ...

class MerkleTree:
    def __init__(self, data: list[str]): ...
    def root_hash(self) -> str: ...
    def verify(self, index: int, value: str) -> bool: ...
    def update(self, index: int, new_value: str) -> None: ...
```

## Stage 1 — Leaf hashing + tree construction (~15 min)
- Leaf node: hash = `sha256(value)`.
- Internal node: hash = `sha256(left.hash + right.hash)`.
- `MerkleTree(data)` — Build from a list of strings. Leaves are the data items. If odd number, duplicate the last leaf.
- Build bottom-up: pair leaves, create parents, repeat until one root.
- `root_hash()` — Return the root node's hash.

## Stage 2 — Proof generation (~15 min)
- `get_proof(index)` — Return the list of (hash, side) pairs needed to verify that `data[index]` is in the tree.
- Walk from leaf to root. At each level, include the sibling's hash and whether it's left or right.
- This is the "audit path" — O(log n) hashes.

## Stage 3 — Proof verification (~10 min)
- `verify(index, value, proof)` — Given a value and proof, recompute the root hash and check it matches.
- Start with `sha256(value)`. For each (sibling_hash, side) in proof, combine appropriately and hash. Compare final result to `root_hash()`.
- This is a static method — verifier doesn't need the full tree.

## Stage 4 — Efficient updates (~10 min)
- `update(index, new_value)` — Change a leaf and recompute only the affected path to root.
- Only O(log n) hashes need recomputing, not the whole tree.
- Store parent pointers or use index arithmetic (node i's parent is i//2).

## Talking points
- Why Merkle trees over just hashing all data together? (Can verify individual items without full data)
- Time complexity: build O(n), verify O(log n), update O(log n).
- Real-world uses: Git, Bitcoin, certificate transparency.
- What if the tree is very large and stored on disk? (Only load the proof path)
