# mypy: ignore-errors

from typing import Optional

class TxnKVStore:
    # Sentinel to distinguish "deleted" from "not set in this layer"
    _DELETED = object()
    
    def __init__(self):
        self.base = {}          # committed key-value store
        self.txn_stack = []     # stack of transaction deltas
    
    def get(self, key: str) -> Optional[str]:
        # Search from innermost transaction outward
        for delta in reversed(self.txn_stack):
            if key in delta:
                value = delta[key]
                return None if value is self._DELETED else value
        return self.base.get(key)
    
    def set(self, key: str, value: str) -> None:
        if self.txn_stack:
            self.txn_stack[-1][key] = value
        else:
            self.base[key] = value
    
    def delete(self, key: str) -> None:
        if self.txn_stack:
            self.txn_stack[-1][key] = self._DELETED
        else:
            self.base.pop(key, None)
    
    def begin(self) -> None:
        self.txn_stack.append({})
    
    def commit(self) -> bool:
        if not self.txn_stack:
            raise RuntimeError("No open transaction")
        
        delta = self.txn_stack.pop()
        target = self.txn_stack[-1] if self.txn_stack else self.base
        
        for key, value in delta.items():
            if value is self._DELETED:
                if target is self.base:
                    target.pop(key, None)
                else:
                    target[key] = self._DELETED
            else:
                target[key] = value
        return True
    
    def rollback(self) -> bool:
        if not self.txn_stack:
            raise RuntimeError("No open transaction")
        
        self.txn_stack.pop()
        return True