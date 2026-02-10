# mypy: ignore-errors

# create a data structure that could represent a filesystem
"""
-------------------------------------------------
Problem 1169. Design In-Memory File System
-------------------------------------------------
Design a simple in-memory file system that supports the following operations:

1. `ls(path: str) -> List[str]`  
   Return the names of files and immediate sub-directories contained in the directory at the given path.  
   - The contents must be returned in **lexicographic order**.  
   - If `path` is a file path, return a list containing only the file name.

2. `mkdir(path: str) -> None`  
   Create a directory (and any missing parent directories) for the given path.  
   - Leading `/` is optional; treat `/a/b` and `a/b` as the same path.  
   - Do nothing if the directory already exists.

3. `add_content(path: str, content: str) -> None`  
   Create the file (and any missing parent directories) if it does not exist, then append the given content to the file.  
   - If the file already exists, the new content is appended.

4. `read_content(path: str) -> str`  
   Return the full content of the file at the given path.

Constraints
-----------
- All paths are non-empty strings.  
- Path components are separated by `/`.  
- File and directory names are alphanumeric.  
- All operations must be O(d) where d is the depth of the path.  
- You may assume no concurrent calls.

You must implement the class:

```python
class FileSystem:
    def __init__(self): ...
    def ls(self, path: str) -> List[str]: ...
    def mkdir(self, path: str) -> None: ...
    def add_content(self, path: str, content: str) -> None: ...
    def read_content(self, path: str) -> str: ...
```

-------------------------------------------------
Next step
-------------------------------------------------
When you’re ready, tell me which operation you’d like to tackle first, and I’ll walk you through the data-structure choices and the code, line by line.

"""


class Node: 
    def __init__(self) -> None:
        self.is_file: bool = False         
        self.content: str = ""
        self.children = {} # nameStr->Node


class FileSystem: 
    def __init__(self) -> None:
        # initialize root 
        self.root = Node() 

    def path2list(self, path : str)-> list:
        clean_path = path.strip("/")

        if not clean_path:
            return []
        
        return clean_path.split("/")



    def mkdir(self, path: str) -> None: 
        # get things like "a/b/c" -> parse to ["a", "b", "c"]
        dpath = self.path2list(path)

        curr = self.root

        # now we go down through directories 
        for dir in dpath:
            if dir not in curr.children:
                curr.children[dir] = Node()

            # make the child of current node the curr node 
            curr = curr.children[dir]


    def ls(self, path: str = "") -> list[str]: 
        # print children of path end
        # traverse until at end of path, then print children 
        dpath = self.path2list(path)

        print(f"dpath {dpath}")


        if len(dpath) == 0:
            return list(self.root.children.keys())
        
        curr = self.root

        for d in dpath:
            # print(f"d: {d}")
            if d in curr.children:
                curr = curr.children[d]            
            else: 
                return []

        if curr.is_file:
            return [dpath[-1]]
            
        return list(sorted(curr.children.keys()))

    def add_content(self, path: str, content: str) -> None:
        # create a file and any missing dirs
        """
        examples: dpath = ["file.text"] 
        """

        # mkdir if we need to
        self.mkdir(path)

        # go to the second to last 
        curr = self.root
        dpath = self.path2list(path) # "a/b/c" -> ['a', 'b', 'c']
        for d in dpath:
            if d in curr.children:
                curr = curr.children[d]            
        
        curr.is_file = True 
        curr.content = curr.content + content

    def read_content(self, path: str) -> str: 
        
        curr = self.root
        dpath = self.path2list(path) # "a/b/c" -> ['a', 'b', 'c']
        for d in dpath:
            if d in curr.children:
                curr = curr.children[d]    

        
        return curr.content




# sanity check 
print("start")
fs = FileSystem()
s = "/a/b/c/d/e"
fs.mkdir(s)

print(fs.ls("a/b"))

fs.add_content("file.txt", "hello world")
print(fs.ls())
fs.add_content("a/b/file.txt", "hello world")
print(fs.ls("a/b"))
content_str = fs.read_content("a/b/file.txt")
print(f"\ncontent: {content_str }")