# mypy: ignore-errors

from typing import List

class Node:
    def __init__(self):
        self.children = {}  # name -> Node
        self.content = ""   # empty string means directory, non-empty or is_file means file
        self.is_file = False

class FileSystem:
    def __init__(self):
        self.root = Node()
    
    def _parse_path(self, path: str) -> List[str]:
        """Convert path string to list of components."""
        path = path.strip("/")
        return path.split("/") if path else []
    
    def _traverse(self, path: str, create: bool = False) -> Node:
        """Traverse to node at path. Optionally create missing directories."""
        node = self.root
        for part in self._parse_path(path):
            if part not in node.children:
                if not create:
                    return None
                node.children[part] = Node()
            node = node.children[part]
        return node

    def ls(self, path: str = "/") -> List[str]:
        node = self._traverse(path)
        if node is None:
            return []
        if node.is_file:
            return [self._parse_path(path)[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path, create=True)

    def add_content(self, path: str, content: str) -> None:
        node = self._traverse(path, create=True)
        node.is_file = True
        node.content += content

    def read_content(self, path: str) -> str:
        node = self._traverse(path)
        return node.content if node else ""