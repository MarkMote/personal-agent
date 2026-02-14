# Stack Machine / Interpreter

Recently verified Jane Street problem (Jan 2026). Build a stack-based virtual machine.

```python
class StackMachine:
    def __init__(self): ...
    def execute(self, program: list[str]) -> int: ...
```

## Stage 1 — Basic arithmetic operations (~10 min)
- Program is a list of tokens: numbers and operators.
- Numbers get pushed onto the stack.
- Operators pop operands, compute, push result.
- Supported: `PUSH <n>`, `ADD`, `SUB`, `MUL`, `DIV`.
- `execute` returns the top of stack after program completes.

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

- Note: `a - b` not `b - a`. Order matters for SUB and DIV.

## Stage 2 — Stack manipulation + comparison (~10 min)
- `DUP` — Duplicate top of stack.
- `SWAP` — Swap top two elements.
- `POP` — Remove top element.
- `EQ` — Pop two, push 1 if equal, 0 otherwise.
- `GT` — Pop two, push 1 if second > first, 0 otherwise.
- `NOT` — Pop one, push 1 if 0, push 0 if nonzero.

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
```

## Stage 3 — Control flow (jumps + conditionals) (~15 min)
- `LABEL <name>` — Mark a position in the program. No-op at runtime.
- `JMP <name>` — Unconditional jump to label.
- `JZ <name>` — Pop top; jump to label if it was 0.
- `JNZ <name>` — Pop top; jump to label if it was nonzero.

- **Implementation:** First pass to build label→index map. Then execute with an instruction pointer.

```python
def execute(self, program):
    # First pass: find labels
    labels = {}
    for i, token in enumerate(program):
        if token.startswith("LABEL "):
            labels[token.split()[1]] = i

    # Execute
    ip = 0  # instruction pointer
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
            # handle arithmetic/stack ops as before
            self._exec_op(token)
        ip += 1
    return self.stack[-1] if self.stack else None
```

## Stage 4 — Functions + call stack (~15 min)
- `DEF <name>` ... `END` — Define a function (sequence of instructions).
- `CALL <name>` — Push return address, jump to function.
- `RET` — Pop return address, jump back.
- Use a separate call stack (list of return addresses).
- Functions can call other functions (and themselves — recursion!).

```python
# In first pass, also find DEF/END blocks
# call_stack stores return addresses
def call(self, name):
    self.call_stack.append(self.ip + 1)
    self.ip = self.functions[name]

def ret(self):
    self.ip = self.call_stack.pop()
```

## Stage 5 — Variables + local scope (~10 min)
- `STORE <name>` — Pop top, store in named variable.
- `LOAD <name>` — Push variable's value onto stack.
- Local scope per function: each `CALL` creates a new scope. `RET` destroys it.
- Implementation: stack of dicts. `STORE/LOAD` operate on the top dict. `CALL` pushes new dict. `RET` pops.

## Example programs
```python
# Factorial of 5
["5", "1",                     # n=5, result=1
 "LABEL loop",
 "SWAP", "DUP", "1", "EQ",    # if n == 1, done
 "JNZ done",
 "DUP", "SWAP",                # keep n, bring result up
 "MUL",                        # result *= n
 "SWAP", "1", "SUB",           # n -= 1
 "JMP loop",
 "LABEL done",
 "POP"]                        # remove n, result on top
```

## Talking points
- Why two passes (label scan + execute) instead of one? Handles forward jumps cleanly.
- How do you detect infinite loops? Instruction counter limit.
- This is essentially how the Python bytecode interpreter works (cpython's ceval.c).
- Real-world: WebAssembly, JVM, Forth, PostScript are all stack machines.
