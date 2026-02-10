# mypy: ignore-errors

"""
Implement an in-memory key-value store that supports **nested transactions** 
with *set/get/delete* and *begin/commit/rollback*.

"""


class TxnKVStore:
    _DELETED = object()

    def __init__(self):
        # data: dict = {} # key -> val
        self.data: list[dict[str,str]] = [{}] # pending[layer] = dict: key->val

    def get(self, key: str) -> Optional[str]: 
        for data_i in reversed(self.data):
            if key in data_i:
                if data_i[key] is self._DELETED:
                    return None
                return data_i[key]
        return None 

    def set(self, key: str, value: str) -> None:
        self.data[-1][key] = value 

    def delete(self, key: str) -> None:
        self.data[-1][key] = self._DELETED
        
    def begin(self) -> None: 
        self.data.append({})

    def commit(self) -> None: 
        commit_these = 


    def rollback(self) -> None:
        pass