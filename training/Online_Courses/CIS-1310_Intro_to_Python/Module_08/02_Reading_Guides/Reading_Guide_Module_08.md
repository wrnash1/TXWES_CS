# Reading Guide: Module 8 — Loop Control: break, continue, pass

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Certification Alignment:** PCAP — Certified Associate in Python Programming
**PCAP Exam Section:** Section 3 — Control Flow — Conditional Blocks and Loops
**Estimated Reading Time:** 35–45 minutes
**OER Resources:** [edube.org PE1 Module 3](https://edube.org/) | [Python break/continue](https://docs.python.org/3/reference/simple_stmts.html#break)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use `break` to exit a loop immediately
2. Use `continue` to skip the current iteration and proceed to the next
3. Use `pass` as a placeholder that does nothing
4. Explain how `break` interacts with `for...else` and `while...else`
5. Distinguish between `break` and `continue` with concrete code examples
6. Write clean loop-control patterns for input validation and search problems

---

## Section 1: The break Statement

`break` **immediately exits** the innermost loop — no further iterations occur, and the loop's `else` clause (if any) is **skipped**.

### Syntax

```python
for variable in sequence:
    if condition:
        break       # exit the loop immediately
    # code after break is skipped when break fires
```

### Example — First Even Number

```python
numbers = [1, 3, 7, 8, 11, 14]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
```

**Output:** `First even number: 8`

Once `break` fires, the loop ends. Items 11 and 14 are never visited.

### break in while Loops

```python
while True:
    answer = input("Type 'quit' to exit: ")
    if answer == "quit":
        break
    print(f"You typed: {answer}")
print("Goodbye!")
```

`while True:` creates an infinite loop. `break` is the only way out. This pattern is common for menu-driven programs and input validation.

### break in Nested Loops

`break` exits only the **innermost** loop:

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break           # exits inner loop only
        print(f"i={i}, j={j}")
```

**Output:**
```
i=0, j=0
i=1, j=0
i=2, j=0
```

Each time `j` reaches 1, only the inner loop is broken. The outer loop keeps going.

---

## Section 2: The continue Statement

`continue` **skips the rest of the current iteration** and jumps to the next one. Unlike `break`, the loop does not end — it just skips the current step.

### Syntax

```python
for variable in sequence:
    if condition:
        continue    # skip to next iteration
    # code here only runs when condition is False
```

### Example — Skip Odd Numbers

```python
for i in range(1, 11):
    if i % 2 != 0:
        continue        # skip odd numbers
    print(i)
```

**Output:** `2 4 6 8 10` (each on its own line)

### continue in while Loops

```python
n = 0
while n < 10:
    n += 1
    if n % 3 == 0:
        continue        # skip multiples of 3
    print(n)
```

**Output:** `1 2 4 5 7 8 10` (3, 6, 9 are skipped)

> **PCAP Exam Tip:** With `continue` in a `while` loop, make sure the update statement runs BEFORE `continue`. If the update is after `continue`, the variable never changes and the loop may become infinite.

```python
# DANGEROUS — infinite loop!
n = 0
while n < 5:
    if n == 3:
        continue    # n is never incremented when n == 3!
    print(n)
    n += 1
```

---

## Section 3: break vs. continue — Side-by-Side

```python
# break example: stop at first negative
numbers = [5, 3, -1, 8, -2]
print("break:")
for num in numbers:
    if num < 0:
        break
    print(num)
# Output: 5, 3

print("continue:")
for num in numbers:
    if num < 0:
        continue
    print(num)
# Output: 5, 3, 8
```

| Statement | What it does | Loop ends? | `else` runs? |
|---|---|---|---|
| `break` | Exit loop immediately | Yes | No |
| `continue` | Skip to next iteration | No | Yes (if loop completes) |

---

## Section 4: break and the loop else clause

The `else` clause on `for` and `while` loops runs only when the loop completes **without** a `break`.

```python
# Search with for...else
primes = [2, 3, 5, 7, 11, 13]
target = 6

for p in primes:
    if p == target:
        print(f"{target} is in the prime list")
        break
else:
    print(f"{target} is NOT in the prime list")

# Output: 6 is NOT in the prime list
```

If we search for 7:
```python
target = 7
for p in primes:
    if p == target:
        print(f"{target} is in the prime list")
        break
else:
    print(f"{target} is NOT in the prime list")

# Output: 7 is in the prime list
```

> **PCAP Exam Tip:** `for...else` / `while...else` is a Python-only construct. The `else` runs on normal termination — when the sequence is exhausted (for) or condition is False (while) — never when `break` exits the loop.

---

## Section 5: The pass Statement

`pass` is a **no-operation** placeholder. It does nothing — it just satisfies Python's requirement for an indented block.

### When to Use pass

1. **Stub out code** you plan to write later
2. **Intentionally empty blocks** (empty `if`, empty `except`, empty class body)

```python
for i in range(10):
    if i % 2 == 0:
        pass        # TODO: handle even numbers later
    else:
        print(i)
```

```python
# Empty class placeholder
class MyFutureClass:
    pass
```

```python
# Silently ignore a specific error
try:
    risky_operation()
except ValueError:
    pass    # intentionally ignore ValueError
```

> **Key distinction:** `pass` does nothing and the loop continues normally. `continue` also lets the loop continue, but it explicitly skips the remaining code in the current iteration.

---

## Section 6: Common Loop Control Patterns

### Input Validation with break

```python
while True:
    try:
        age = int(input("Enter age (0-120): "))
        if 0 <= age <= 120:
            break
        print("Out of range. Try again.")
    except ValueError:
        print("Not a number. Try again.")
print(f"Age accepted: {age}")
```

### Filtering with continue

```python
data = [10, -3, 0, 7, -1, 15, 0, 4]
print("Positive numbers only:")
for val in data:
    if val <= 0:
        continue
    print(val)
```

### Search-and-Report with for...else

```python
students = [("Alice", 85), ("Bob", 72), ("Carol", 91)]
target_name = "David"

for name, score in students:
    if name == target_name:
        print(f"{name}: {score}")
        break
else:
    print(f"{target_name} not found in roster.")
```

### Nested Loop with break — Finding a Pair

```python
target = 10
found = False
numbers = [1, 3, 7, 4, 6, 9]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"Pair found: {numbers[i]} + {numbers[j]} = {target}")
            found = True
            break
    if found:
        break
```

Because `break` only exits the inner loop, a flag variable (`found`) is used to also break the outer loop.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| **`break`** | Immediately exits the innermost loop; `else` clause is skipped |
| **`continue`** | Skips remaining code in current iteration; loop continues with next |
| **`pass`** | No-op placeholder; satisfies syntax requirement without doing anything |
| **Loop `else`** | Runs after normal loop termination; skipped when `break` exits the loop |
| **Infinite loop** | A loop that never terminates naturally; typically requires `break` to exit |

---

## External Resources

| Resource | Link | What to Study |
|---|---|---|
| `break` and `continue` | [docs.python.org/3/reference/simple_stmts.html#break](https://docs.python.org/3/reference/simple_stmts.html#break) | Full specification |
| `pass` statement | [docs.python.org/3/reference/simple_stmts.html#pass](https://docs.python.org/3/reference/simple_stmts.html#pass) | When and why |
| edube.org PE1 Module 3 | [edube.org](https://edube.org/) | break/continue section |

---

## Self-Check Review Questions

1. What is the difference between `break` and `continue`?
2. If a `for` loop has an `else` clause and a `break` fires, does `else` run?
3. What is the output of: `for i in range(5): if i == 3: break; print(i)`?
4. What is the output of: `for i in range(5): if i == 3: continue; print(i)`?
5. What does `pass` do? Why would you use it?
6. In a nested loop, which loop does `break` exit?

---

*Next Module → Module 9: Lists*
