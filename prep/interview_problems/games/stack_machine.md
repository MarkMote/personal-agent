# Stack Machine / Interpreter

Recently verified Jane Street problem (Jan 2026).

---

## The Prompt

Build a stack-based virtual machine. You'll be given a program as a list of string tokens. Implement `execute(program)` that runs the program and returns the top of the stack.

```python
class StackMachine:
    def __init__(self): ...
    def execute(self, program: list[str]) -> int: ...
```

The interviewer will add features in stages:

**Stage 1 — Basic arithmetic (~10 min)**
- Numeric tokens get pushed onto the stack.
- Operator tokens pop two operands, compute, push the result.
- Operators: `ADD`, `SUB`, `MUL`, `DIV` (integer division).
- Return the top of the stack when the program ends.
- Example: `["3", "4", "ADD"]` → `7`
- Example: `["10", "3", "SUB"]` → `7` (second-from-top minus top)

**Stage 2 — Stack manipulation + comparison (~10 min)**
- `DUP` — duplicate top of stack.
- `SWAP` — swap top two elements.
- `POP` — remove top element.
- `EQ` — pop two, push 1 if equal, 0 otherwise.
- `GT` — pop two, push 1 if second > first, 0 otherwise.
- `NOT` — pop one, push 1 if 0, push 0 if nonzero.

**Stage 3 — Control flow (~15 min)**
- `LABEL <name>` — mark a position. No-op at runtime.
- `JMP <name>` — unconditional jump.
- `JZ <name>` — pop top; jump if it was 0.
- `JNZ <name>` — pop top; jump if it was nonzero.

**Stage 4 — Functions (~15 min)**
- `DEF <name>` ... `END` — define a function.
- `CALL <name>` — push return address, jump to function.
- `RET` — pop return address, jump back.
- Functions can call other functions (including themselves).

**Stage 5 — Variables + local scope (~10 min)**
- `STORE <name>` — pop top, store in variable.
- `LOAD <name>` — push variable value onto stack.
- Each `CALL` creates a new scope; `RET` destroys it.

---

## Solutions

### Stage 1

```python
class StackMachine:
    def __init__(self):
        self.stack = []

    def execute(self, program: list[str]) -> int:
        for token in program:
            if token.lstrip("-").isdigit():
                self.stack.append(int(token))
            elif token == "ADD":
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a + b)
            elif token == "SUB":
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a - b)
            elif token == "MUL":
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a * b)
            elif token == "DIV":
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a // b)
        return self.stack[-1]
```

Key: pop order matters. `b` is the top (popped first), `a` is second. So `SUB` computes `a - b` (second minus top), matching RPN convention.

### Stage 2

Add to the token dispatch:

```python
elif token == "DUP":
    self.stack.append(self.stack[-1])
elif token == "SWAP":
    self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
elif token == "POP":
    self.stack.pop()
elif token == "EQ":
    b, a = self.stack.pop(), self.stack.pop()
    self.stack.append(1 if a == b else 0)
elif token == "GT":
    b, a = self.stack.pop(), self.stack.pop()
    self.stack.append(1 if a > b else 0)
elif token == "NOT":
    self.stack.append(1 if self.stack.pop() == 0 else 0)
```

### Stage 3

Big structural change: switch from a `for` loop to a `while` loop with an instruction pointer. Do a first pass to build a label→index map.

```python
def execute(self, program):
    # First pass: find labels
    labels = {}
    for i, token in enumerate(program):
        if token.startswith("LABEL "):
            labels[token.split()[1]] = i

    # Execute with instruction pointer
    ip = 0
    while ip < len(program):
        token = program[ip]
        if token.startswith("LABEL"):
            ip += 1
            continue
        elif token.startswith("JMP"):
            ip = labels[token.split()[1]]
            continue
        elif token.startswith("JZ"):
            val = self.stack.pop()
            if val == 0:
                ip = labels[token.split()[1]]
                continue
        elif token.startswith("JNZ"):
            val = self.stack.pop()
            if val != 0:
                ip = labels[token.split()[1]]
                continue
        else:
            self._exec_op(token)  # stages 1+2 dispatch
        ip += 1
    return self.stack[-1] if self.stack else None
```

Why two passes? Forward jumps — a `JMP end` needs to know where `LABEL end` is before reaching it.

### Stage 4

First pass also maps `DEF <name>` → index. `END` acts like `RET`. Separate call stack for return addresses.

```python
def __init__(self):
    self.stack = []
    self.call_stack = []  # return addresses
    self.functions = {}   # name → instruction index

# In first pass, also find DEF/END blocks:
# if token.startswith("DEF "):
#     self.functions[token.split()[1]] = i + 1  # jump past DEF

# In execute loop:
elif token.startswith("CALL"):
    self.call_stack.append(ip + 1)
    ip = self.functions[token.split()[1]]
    continue
elif token == "RET" or token == "END":
    ip = self.call_stack.pop()
    continue
elif token.startswith("DEF"):
    # skip function body during normal execution
    while program[ip] != "END":
        ip += 1
    ip += 1
    continue
```

### Stage 5

Stack of dicts for scoped variables. `CALL` pushes a new dict, `RET` pops it.

```python
def __init__(self):
    self.stack = []
    self.call_stack = []
    self.functions = {}
    self.scopes = [{}]  # global scope

# CALL also does: self.scopes.append({})
# RET also does:  self.scopes.pop()

elif token.startswith("STORE"):
    name = token.split()[1]
    self.scopes[-1][name] = self.stack.pop()
elif token.startswith("LOAD"):
    name = token.split()[1]
    self.stack.append(self.scopes[-1][name])
```

---

## Example Programs

```python
# Reverse Polish: (3 + 4) * 2 = 14
["3", "4", "ADD", "2", "MUL"]

# Countdown: 5 + 4 + 3 + 2 + 1 = 15 (stages 1-3, sentinel trick)
["0", "5",                         # sentinel=0, n=5
 "LABEL loop",
 "DUP", "0", "EQ",                 # n == 0?
 "JNZ sum_phase",
 "DUP", "1", "SUB",                # push n-1
 "JMP loop",
 "LABEL sum_phase",                # stack: [0, 5, 4, 3, 2, 1, 0]
 "POP",                            # drop the 0
 "LABEL sum_loop",
 "ADD",                            # add top two
 "SWAP", "DUP", "0", "EQ",         # is next value the sentinel?
 "JNZ done",
 "SWAP",
 "JMP sum_loop",
 "LABEL done",
 "POP"]                            # remove sentinel

# Factorial of 5 = 120 (stages 1-5, uses STORE/LOAD)
["5", "STORE n",
 "1", "STORE result",
 "LABEL loop",
 "LOAD n", "1", "EQ",
 "JNZ done",
 "LOAD result", "LOAD n", "MUL", "STORE result",
 "LOAD n", "1", "SUB", "STORE n",
 "JMP loop",
 "LABEL done",
 "LOAD result"]
```

Note: factorial with only stages 1-3 (no variables) is much harder — you can't easily access values buried in the stack with just DUP/SWAP. The STORE/LOAD version is what you'd actually write.

---

## Talking Points
- Why two passes (label scan + execute) instead of one? Handles forward jumps.
- How to detect infinite loops? Instruction counter limit.
- This is essentially how cpython's bytecode interpreter works (ceval.c).
- Real-world stack machines: WebAssembly, JVM, Forth, PostScript.
