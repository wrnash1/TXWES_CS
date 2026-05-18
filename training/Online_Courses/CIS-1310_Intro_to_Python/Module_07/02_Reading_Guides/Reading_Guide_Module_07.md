# Reading Guide: Module 7 — For Loops and range()

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Certification Alignment:** PCAP — Certified Associate in Python Programming
**PCAP Exam Section:** Section 3 — Control Flow — Conditional Blocks and Loops
**Estimated Reading Time:** 45–55 minutes
**OER Resources:** [edube.org PE1 Module 3](https://edube.org/) | [Python for Loops](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) | [range()](https://docs.python.org/3/library/stdtypes.html#range)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Write a `for` loop to iterate over a sequence
2. Use `range()` with one, two, and three arguments to control loop repetition
3. Use a negative step to count down
4. Iterate over strings character-by-character
5. Apply `enumerate()` to get both index and value from a sequence
6. Use `zip()` to iterate over two sequences in parallel
7. Write and trace nested `for` loops
8. Use the `for...else` construct correctly

---

## Section 1: The `for` Loop

A `for` loop **iterates over a sequence** — it visits each item one at a time. Unlike `while`, which repeats based on a condition, `for` repeats based on the items in a collection.

### Syntax

```python
for variable in sequence:
    # loop body — indented
    statement1
    statement2
# code here runs after the loop ends
```

On each iteration, `variable` is bound to the next item in `sequence`. The loop ends when all items have been visited.

### Simple Example

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

The loop variable `fruit` holds `"apple"` on iteration 1, `"banana"` on iteration 2, and `"cherry"` on iteration 3.

---

## Section 2: The `range()` Function

`range()` generates a sequence of integers without storing them all in memory. It is the most common way to control how many times a `for` loop runs.

### Three Forms of range()

| Form | Description | Example | Values Produced |
|---|---|---|---|
| `range(stop)` | 0 up to (not including) stop | `range(5)` | 0, 1, 2, 3, 4 |
| `range(start, stop)` | start up to (not including) stop | `range(2, 7)` | 2, 3, 4, 5, 6 |
| `range(start, stop, step)` | start to stop, counting by step | `range(0, 10, 2)` | 0, 2, 4, 6, 8 |

> **Critical Rule:** `range()` is **exclusive** at the stop value — `range(5)` gives 0–4, not 0–5. This is one of the most common off-by-one errors for beginners.

### range(stop) — Count from Zero

```python
for i in range(5):
    print(i)
```

**Output:** `0 1 2 3 4` (each on a new line)

### range(start, stop) — Custom Start

```python
for i in range(1, 6):
    print(i)
```

**Output:** `1 2 3 4 5`

This is useful when you want to display 1-based numbering.

### range(start, stop, step) — Custom Step

```python
for i in range(0, 20, 5):
    print(i)
```

**Output:** `0 5 10 15`

### Negative Step — Counting Down

```python
for i in range(10, 0, -1):
    print(i)
```

**Output:** `10 9 8 7 6 5 4 3 2 1`

> **PCAP Exam Tip:** For a countdown from n to 1, use `range(n, 0, -1)`. For a countdown from n to 0 (inclusive), use `range(n, -1, -1)`. The stop value is always excluded.

### Empty range()

If the range produces no values, the loop body never executes:

```python
for i in range(5, 2):    # start > stop with positive step → empty
    print("never printed")
```

No output — the loop body runs zero times.

---

## Section 3: Iterating Over Strings

Strings are sequences of characters. A `for` loop visits each character:

```python
word = "Python"
for char in word:
    print(char)
```

**Output:**
```
P
y
t
h
o
n
```

### Counting Characters

```python
word = "Mississippi"
count = 0
for char in word:
    if char == "s":
        count += 1
print(f"Number of 's': {count}")   # 4
```

---

## Section 4: The enumerate() Function

`enumerate()` adds a counter to an iterable. It returns pairs of `(index, value)`:

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

**Output:**
```
0: apple
1: banana
2: cherry
```

### Custom Start Index

```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

**Output:**
```
1. apple
2. banana
3. cherry
```

> **Why use enumerate() instead of range(len(...))?**  
> `for i, val in enumerate(items)` is cleaner and more Pythonic than `for i in range(len(items)): val = items[i]`. Both work, but `enumerate()` is preferred in Python code.

---

## Section 5: The zip() Function

`zip()` combines two (or more) iterables into pairs, stopping at the shortest:

```python
names = ["Alice", "Bob", "Carol"]
scores = [92, 85, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**Output:**
```
Alice: 92
Bob: 85
Carol: 78
```

### zip() Stops at the Shortest

```python
a = [1, 2, 3, 4, 5]
b = ["x", "y", "z"]

for x, y in zip(a, b):
    print(x, y)
```

**Output:**
```
1 x
2 y
3 z
```

Items 4 and 5 from `a` are ignored because `b` runs out first.

---

## Section 6: Nested for Loops

A `for` loop inside another `for` loop is a **nested loop**. The inner loop runs completely for every single iteration of the outer loop.

### Multiplication Table

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end="\t")
    print()    # newline after each row
```

**Output:**
```
1	2	3	
2	4	6	
3	6	9	
```

### Counting Total Iterations

For `range(m)` outer and `range(n)` inner: the body runs **m × n** times total.

```python
count = 0
for i in range(3):
    for j in range(4):
        count += 1
print(count)   # 12 = 3 × 4
```

### Triangle Pattern

```python
for row in range(1, 6):
    print("*" * row)
```

**Output:**
```
*
**
***
****
*****
```

---

## Section 7: The for...else Construct

Like `while`, a `for` loop can have an `else` clause. The `else` block runs **after the loop completes normally** (all items visited). It does **not** run if the loop exits via `break`.

```python
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in the list.")
```

**Output:** `4 not found in the list.`

This is the primary use case for `for...else`: detecting whether a search loop found what it was looking for.

> **PCAP Exam Tip:** The `else` clause on a loop is Python-specific — most languages do not have it. Know that it runs on **normal termination** (all items exhausted), never on `break`.

---

## Section 8: Common for Loop Patterns

### Summing a Sequence

```python
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")   # 150
```

### Finding a Maximum

```python
numbers = [34, 67, 12, 89, 45]
max_val = numbers[0]    # start with first element
for num in numbers:
    if num > max_val:
        max_val = num
print(f"Max: {max_val}")   # 89
```

### Building a String

```python
letters = ["H", "e", "l", "l", "o"]
result = ""
for letter in letters:
    result += letter
print(result)   # Hello
```

### Counting with range and Accumulator

```python
total = 0
for i in range(1, 101):    # 1 to 100 inclusive
    total += i
print(total)   # 5050
```

---

## Section 9: for vs. while — When to Use Each

| Situation | Use |
|---|---|
| Known number of iterations | `for` with `range()` |
| Iterating over a sequence | `for` |
| Unknown number of iterations | `while` |
| Input validation | `while True:` |
| Loop depends on user action | `while` |

> **Rule of thumb:** If you know at the start how many times to loop, use `for`. If you don't, use `while`.

---

## Section 10: Tracing a for Loop

To trace a `for` loop, track the loop variable and any accumulator across each iteration.

**Trace this loop:**

```python
total = 0
for i in range(1, 5):
    total += i * 2
print(total)
```

| Iteration | i | i * 2 | total (after) |
|---|---|---|---|
| 1 | 1 | 2 | 2 |
| 2 | 2 | 4 | 6 |
| 3 | 3 | 6 | 12 |
| 4 | 4 | 8 | 20 |

Output: `20`

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| **`for` loop** | Iterates over each item in a sequence exactly once |
| **`range()`** | Generates a sequence of integers; exclusive at the stop value |
| **`enumerate()`** | Returns (index, value) pairs from a sequence |
| **`zip()`** | Combines two sequences into pairs; stops at the shorter |
| **Nested loop** | A loop inside another loop; inner body runs m × n times total |
| **`for...else`** | `else` block runs after loop completes normally (not via `break`) |
| **Off-by-one error** | Using `range(n)` instead of `range(1, n+1)` when you meant 1 to n inclusive |

---

## External Resources

| Resource | Link | What to Study |
|---|---|---|
| Python `for` Statement | [docs.python.org/3/reference/compound_stmts.html#the-for-statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) | Full syntax |
| `range()` Built-in | [docs.python.org/3/library/stdtypes.html#range](https://docs.python.org/3/library/stdtypes.html#range) | All three forms, behavior |
| `enumerate()` | [docs.python.org/3/library/functions.html#enumerate](https://docs.python.org/3/library/functions.html#enumerate) | Index + value iteration |
| `zip()` | [docs.python.org/3/library/functions.html#zip](https://docs.python.org/3/library/functions.html#zip) | Parallel iteration |
| edube.org PE1 Module 3 | [edube.org](https://edube.org/) | For loops section |

---

## Self-Check Review Questions

1. What values does `range(3, 10, 2)` produce?
2. How many times does `for i in range(5, 5):` execute?
3. What is the difference between `for i in range(5)` and `for i in range(1, 6)`?
4. Write a loop to print every third number from 0 to 30 inclusive.
5. When does the `else` clause of a `for...else` loop execute?
6. What does `enumerate(["a", "b", "c"], start=1)` yield?
7. If `a = [1, 2, 3]` and `b = [10, 20]`, what does `list(zip(a, b))` produce?

---

*Next Module → Module 8: Loop Control — break, continue, pass*
