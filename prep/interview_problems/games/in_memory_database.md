# In-Memory Key-Value Database

Anthropic's canonical CodeSignal problem. Also reported at Scale AI and Rippling. The exact format Anthropic uses for their coding assessment.

```python
class Database:
    def __init__(self): ...
    def set(self, key: str, field: str, value: str) -> None: ...
    def get(self, key: str, field: str) -> str | None: ...
    def delete(self, key: str, field: str) -> bool: ...
```

## Stage 1 — Basic CRUD (~10 min)
- `set(key, field, value)` — Store value at key/field. Overwrite if exists.
- `get(key, field)` — Return value or None.
- `delete(key, field)` — Remove field from key. Return True if existed, False otherwise.
- Storage: `dict[str, dict[str, str]]` — nested dicts.

```python
class Database:
    def __init__(self):
        self.data = {}  # key -> {field: value}

    def set(self, key: str, field: str, value: str) -> None:
        if key not in self.data:
            self.data[key] = {}
        self.data[key][field] = value

    def get(self, key: str, field: str) -> str | None:
        return self.data.get(key, {}).get(field)

    def delete(self, key: str, field: str) -> bool:
        if key in self.data and field in self.data[key]:
            del self.data[key][field]
            if not self.data[key]:  # clean up empty keys
                del self.data[key]
            return True
        return False
```

## Stage 2 — Scan with filters (~15 min)
- `scan(key)` — Return all field-value pairs for a key as a dict.
- `scan_prefix(key, prefix)` — Return fields starting with prefix.
- `scan_filter(key, field, op, value)` — Filter by comparison. `op` in ["<", ">", "=="].
  - Compare as strings lexicographically, or as numbers if both parseable.

```python
def scan(self, key: str) -> dict:
    return dict(self.data.get(key, {}))

def scan_prefix(self, key: str, prefix: str) -> dict:
    return {f: v for f, v in self.data.get(key, {}).items()
            if f.startswith(prefix)}
```

## Stage 3 — TTL (time-to-live) (~15 min)
- `set_at(key, field, value, timestamp)` — Set with a timestamp.
- `set_ttl(key, field, value, timestamp, ttl)` — Expires `ttl` seconds after `timestamp`.
- `get_at(key, field, timestamp)` — Return value only if not expired at given timestamp.
- Store expiry alongside value: `{field: (value, expiry_time | None)}`.
- Don't use real time — all operations take a timestamp parameter (testable).

```python
class Database:
    def __init__(self):
        self.data = {}  # key -> {field: (value, expiry | None)}

    def set_at(self, key, field, value, timestamp, ttl=None):
        if key not in self.data:
            self.data[key] = {}
        expiry = timestamp + ttl if ttl else None
        self.data[key][field] = (value, expiry)

    def get_at(self, key, field, timestamp):
        entry = self.data.get(key, {}).get(field)
        if entry is None:
            return None
        value, expiry = entry
        if expiry is not None and timestamp >= expiry:
            del self.data[key][field]  # lazy cleanup
            return None
        return value
```

## Stage 4 — Backup and restore (~15 min)
- `backup(timestamp)` — Snapshot current state at given timestamp.
- `restore(timestamp)` — Revert to most recent backup at or before timestamp.
- Store backups as `list[(timestamp, snapshot)]`. Snapshot = deep copy of data.
- `restore` uses binary search to find the right backup.
- After restore, new operations build on restored state. Future backups still accessible.

```python
import copy
import bisect

class Database:
    def __init__(self):
        self.data = {}
        self.backups = []  # [(timestamp, snapshot)]
        self.backup_times = []  # for bisect

    def backup(self, timestamp):
        snapshot = copy.deepcopy(self.data)
        self.backups.append((timestamp, snapshot))
        self.backup_times.append(timestamp)

    def restore(self, timestamp):
        idx = bisect.bisect_right(self.backup_times, timestamp) - 1
        if idx < 0:
            return  # no backup before this time
        _, snapshot = self.backups[idx]
        self.data = copy.deepcopy(snapshot)
```

## Stage 5 — Transactions (BEGIN / COMMIT / ROLLBACK) (~15 min)
- `begin()` — Start a transaction. Nested transactions supported.
- `commit()` — Apply changes from current transaction to parent.
- `rollback()` — Discard changes from current transaction.
- Implementation: stack of snapshots. `begin` pushes a copy. `rollback` pops. `commit` pops and merges into parent.

```python
def begin(self):
    self.tx_stack.append(copy.deepcopy(self.data))

def commit(self):
    if not self.tx_stack:
        raise RuntimeError("No transaction")
    self.tx_stack.pop()  # discard savepoint, keep current data

def rollback(self):
    if not self.tx_stack:
        raise RuntimeError("No transaction")
    self.data = self.tx_stack.pop()  # restore savepoint
```

## Talking points
- Deep copy vs copy-on-write for snapshots? Deep copy is simple. COW is more efficient but complex.
- Lazy vs eager TTL cleanup? Lazy (check on get) is simpler. Eager (background sweep) saves memory.
- How would you shard this across machines? Consistent hashing on key.
