# Expression Parser

D.E. Shaw problem type (Jan 2026).

**Task:** Given a math expression as a string (e.g. `"3 + 5 * 2"`), evaluate it and return the numeric result. Handle operator precedence (`*`/`/` before `+`/`-`) and parentheses.

```python
def evaluate(expression: str) -> float: ...
```

---

## Stage 1 — Single operations (~5 min)
- Parse and evaluate: `"3 + 5"` → 8, `"10 / 2"` → 5.
- Split on spaces. Operator is always the middle token.
- Handle +, -, *, /.

## Stage 2 — Chained operations, left to right (~10 min)
- `"1 + 2 - 4 / 5 * 6"` — evaluate left to right (no precedence yet).
- Tokenize: split on spaces into numbers and operators.
- Walk through tokens: start with first number, apply each operator with next number.

## Stage 3 — Operator precedence (~15 min)
- `*` and `/` bind tighter than `+` and `-`.
- `"1 + 2 * 3"` → 7, not 9.
- **Approach A — Two-pass:**
  1. First pass: scan left to right, evaluate all `*` and `/`, replace the triple (a, op, b) with the result.
  2. Second pass: evaluate remaining `+` and `-` left to right.
- **Approach B — Stack-based:**
  1. Push first number onto stack.
  2. For each (operator, number) pair:
     - If `+`: push +number.
     - If `-`: push -number.
     - If `*`: pop top, push top * number.
     - If `/`: pop top, push top / number.
  3. Sum the stack.
- Stack approach is cleaner and extends better.

## Stage 4 — Parentheses (~15 min)
- `"(1 + 2) * 3"` → 9.
- **Recursive descent:** Write `parse_expr()`, `parse_term()`, `parse_factor()`.
  - `factor` = number | `(` expr `)`
  - `term` = factor ((`*`|`/`) factor)*
  - `expr` = term ((`+`|`-`) term)*
- Or use a stack: when you see `(`, push current state. When you see `)`, pop and combine.

## Stage 5 — Variables + assignment (~10 min)
- `"x = 5"`, then `"x + 3"` → 8.
- Maintain a dict of variable bindings.
- During tokenization, look up variable names in the dict.
- Handle: assignment returns the value, variables can appear anywhere a number can.

## Key insight from D.E. Shaw failure
The Stage 3 stack approach is the one to memorize cold. It handles precedence cleanly without recursion:
```python
def evaluate(expr: str) -> float:
    tokens = expr.split()
    stack = [float(tokens[0])]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = float(tokens[i + 1])
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        elif op == '/':
            stack.append(stack.pop() / num)
        i += 2
    return sum(stack)
```
That's it. 12 lines. Practice until it's muscle memory.
