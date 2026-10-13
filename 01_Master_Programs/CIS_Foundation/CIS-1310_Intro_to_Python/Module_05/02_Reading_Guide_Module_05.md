# Reading Guide: Module 05 — Loops: Iteration with while and for

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-1310 &BULL; INTRODUCTION TO PYTHON PROGRAMMING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 05 — Loops: Iteration with while and for**. Loops are one of the most powerful tools in programming — they allow a small amount of code to process large amounts of data. A loop that sums 10,000 numbers looks identical to one that sums 10.

The PCAP exam tests both `while` and `for` loops extensively: range() behavior, break/continue semantics, the loop else clause, enumerate(), zip(), and the accumulator pattern. Master every entry in this guide before starting the lab.

---

## 1. High-Yield Glossary

### Iteration

A single pass through a loop body. Each time the loop body executes, that is one iteration. A loop that runs its body five times performs five iterations.

### while Loop

Repeats its body as long as its condition is `True`. The condition is checked before each iteration.

```python
while condition:
    body
```

If the condition is `False` on the very first check, the body never runs. If the condition never becomes `False`, the loop runs forever (**infinite loop**).

### Infinite Loop

A loop that never terminates because its condition never becomes `False`. Usually a bug — but `while True:` combined with `break` is a legitimate pattern for menus and event listeners.

```python
while True:
    # only exits via break or return
    ...
```

Interrupt an infinite loop in the terminal with `Ctrl+C`, which raises `KeyboardInterrupt`.

### Loop Variable

The variable that controls a loop's progress. In a `while` loop, the programmer is responsible for updating it inside the loop body. In a `for` loop, Python assigns it automatically on each iteration.

### for Loop

Iterates over each item in an **iterable** (a sequence or other object that can produce items one at a time). Python automatically assigns each item to the loop variable and advances to the next item after each iteration.

```python
for variable in iterable:
    body
```

Common iterables: `str`, `list`, `tuple`, `range`, `dict`, `set`.

### range() Function

Produces a sequence of integers. Three call signatures:

| Call | Produces | Example |
|---|---|---|
| `range(stop)` | 0, 1, ..., stop-1 | `range(5)` → 0,1,2,3,4 |
| `range(start, stop)` | start, start+1, ..., stop-1 | `range(2, 6)` → 2,3,4,5 |
| `range(start, stop, step)` | start, start+step, ..., < stop | `range(0, 10, 3)` → 0,3,6,9 |

**Critical rule:** `stop` is always **excluded**. `range(5)` gives five values: 0 through 4, not 0 through 5.

**Counting down:** Use a negative step: `range(10, 0, -1)` → 10,9,8,7,6,5,4,3,2,1.

`range()` does not produce a list — it produces a `range` object that generates values on demand. Use `list(range(5))` if you need an actual list.

### break Statement

Immediately exits the innermost loop, regardless of the loop condition.

```python
while True:
    value = int(input('Enter 0 to quit: '))
    if value == 0:
        break    # exits the while loop
    print(value)
```

In nested loops, `break` only exits the loop it is directly inside.

### continue Statement

Skips the rest of the current iteration and immediately returns to the loop condition check (for `while`) or the next item (for `for`).

```python
for n in range(10):
    if n % 2 == 0:
        continue    # skip even numbers
    print(n)        # only odd numbers reach here
```

### Loop else Clause

Both `while` and `for` loops support an `else` clause that runs **only if the loop was not terminated by `break`**.

```python
for item in collection:
    if condition(item):
        break
else:
    # runs only if break was never hit
    print('not found')
```

If `break` executes, the `else` is skipped. If the loop exhausts the iterable normally, `else` runs. This pattern is used for search operations — "did we find it or not?"

### Accumulator Pattern

A programming pattern where a variable is initialized before a loop and updated (accumulated) on each iteration to build a cumulative result.

```python
total = 0               # initialize accumulator
for score in scores:
    total += score      # accumulate
average = total / len(scores)
```

Accumulators can compute sums, products, counts, running maximums/minimums, or concatenate strings.

### enumerate()

A built-in function that adds an automatic integer counter to any iterable. Returns `(index, value)` pairs.

```python
for i, name in enumerate(['Alice', 'Bob', 'Carol']):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Carol
```

Optional `start` parameter: `enumerate(names, start=1)` begins counting at 1.

### zip()

A built-in function that pairs items from two or more iterables by position. Stops at the shortest iterable.

```python
for name, score in zip(['Alice', 'Bob'], [92, 85]):
    print(name, score)
# Alice 92
# Bob 85
```

### Nested Loop

A loop inside another loop. The inner loop runs to completion for every single iteration of the outer loop.

```python
for i in range(3):      # outer: 3 iterations
    for j in range(3):  # inner: 3 iterations per outer
        print(i, j)     # 9 total prints
```

---

## 2. while vs. for — When to Use Each

| Use `while` when... | Use `for` when... |
|---|---|
| You don't know in advance how many iterations are needed | You are iterating over a known sequence or collection |
| You need to loop until a condition changes | You need to process every item in a list |
| You are waiting for user input or an event | You are counting a fixed number of times with `range()` |
| You need a `while True` + `break` menu pattern | You need index-value pairs with `enumerate()` |

---

## 3. range() Reference — PCAP Exam Traps

```python
range(5)           # 0, 1, 2, 3, 4   — 5 values, starts at 0, stop excluded
range(1, 6)        # 1, 2, 3, 4, 5   — 5 values, stop 6 excluded
range(0, 10, 2)    # 0, 2, 4, 6, 8   — even numbers up to 8
range(10, 0, -1)   # 10, 9, ..., 1   — countdown, stops before 0
range(10, 0, -2)   # 10, 8, 6, 4, 2  — countdown by 2
range(3, 3)        # empty — start equals stop
range(5, 0)        # empty — no positive step from 5 to 0
```

**Counting iterations from range:** `len(range(start, stop, step))` = `ceil((stop - start) / step)`. The simplest shortcut: just count the values.

---

## 4. Loop else — The Most-Tested Unusual Feature

```python
# else runs — no break was hit
for n in [1, 3, 5]:
    if n == 2:
        break
else:
    print('2 not found')   # prints

# else does NOT run — break was hit
for n in [1, 2, 3]:
    if n == 2:
        break
else:
    print('2 not found')   # does not print
```

**Exam trick:** The exam will show a loop with a `break` inside a condition and ask whether the `else` clause runs. Trace the loop: if `break` fires, `else` is skipped.

---

## 5. Common Error Patterns to Memorize

**Pattern 1 — Infinite loop (missing update):**

```python
count = 0
while count < 5:
    print(count)
    # forgot: count += 1 — loops forever
```

**Pattern 2 — Off-by-one with range():**

```python
for i in range(5):
    print(i)   # prints 0-4, NOT 1-5
```

To print 1–5: `range(1, 6)`.

**Pattern 3 — break only exits one level:**

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break    # only exits the inner for loop
    print(i)         # outer loop continues normally
```

**Pattern 4 — continue skips to next iteration, not next line:**

```python
for n in range(5):
    if n == 2:
        continue
    print(n)    # prints 0, 1, 3, 4 — skips 2
```

---

## 6. Certification Exam Tips

**Tip 1 — range() excludes stop.**
`range(1, 5)` = 1, 2, 3, 4. The value 5 is never produced. This is the single most-tested range() fact.

**Tip 2 — Loop else runs only without break.**
If the loop body never hits `break`, the `else` clause runs after the loop ends. If `break` fires at any point, `else` is skipped entirely.

**Tip 3 — break exits only the innermost loop.**
In nested loops, `break` only exits the loop it is directly inside. The outer loop continues.

**Tip 4 — continue skips to next iteration.**
`continue` does not exit the loop — it ends the current iteration early and re-evaluates the condition (while) or moves to the next item (for).

**Tip 5 — enumerate() returns (index, value) tuples.**
`for i, val in enumerate(lst):` — both `i` and `val` are available. Without unpacking: `for pair in enumerate(lst):` gives tuples like `(0, 'Alice')`.

**Tip 6 — zip() stops at the shortest input.**
`zip([1,2,3], ['a','b'])` produces `(1,'a'), (2,'b')` — the third element `3` is dropped because the second list is exhausted.

**Tip 7 — A for loop over a string iterates characters.**
`for c in 'abc':` gives `'a'`, then `'b'`, then `'c'`. Strings are iterable character by character.

---

## 7. Beyond the Exam — Real-World Context

**Why does Python have both while and for?**
They serve genuinely different use cases. `for` loops are safer — they cannot infinite-loop because they iterate a finite iterable. `while` loops are necessary when you do not know how many iterations are needed. Web servers use `while True:` to keep listening for requests. File readers use `while line:` to process until end of file.

**The accumulator pattern is everywhere.**
The sum-and-average accumulator from this module is the conceptual foundation of database aggregation (SQL's `SUM`, `AVG`, `COUNT`), spreadsheet formulas, analytics dashboards, and machine learning loss functions. Every time you see "total" or "running average" in software, there is an accumulator underneath.

**enumerate() exists because Python designers hate index arithmetic.**
Before `enumerate()`, you would write `for i in range(len(lst)): val = lst[i]`. That is error-prone and unreadable. `enumerate()` makes the index available without the index-based lookup, which is one reason Python code is cleaner than equivalent code in older languages.

---

## 8. Required Readings and Videos

**Required Reading — Chapter 5:**
Read Chapter 5 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). The chapter covers both `while` and `for` loops with examples.

**Required Reading — Official Python Docs:**
Read the [`for` statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) and [`range()` built-in](https://docs.python.org/3/library/stdtypes.html#range) pages in the official Python 3 documentation.

**Required Video:**
Watch Episodes 8–9 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance covers loops and iteration with live examples.

---

## 9. Supplemental Resources

**1. Official Python 3 Docs — The for Statement**
[https://docs.python.org/3/reference/compound_stmts.html#the-for-statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
Authoritative specification for the `for` loop, `break`, `continue`, and the `else` clause. The formal grammar definition clarifies exactly when `else` executes. Essential reading before the PCAP exam.

**2. Official Python 3 Docs — range()**
[https://docs.python.org/3/library/stdtypes.html#range](https://docs.python.org/3/library/stdtypes.html#range)
The complete `range()` specification including all three argument forms, negative steps, membership testing, and slicing. The note on memory efficiency (ranges are lazy sequences) is tested on PCAP.

**3. Python for Everybody — Chapter 5: Iteration**
[https://www.py4e.com/html3/05-iterations](https://www.py4e.com/html3/05-iterations)
Dr. Severance's free chapter on `while` and `for` loops, accumulator patterns, `break`, and `continue`. Includes self-check exercises and auto-graded practice problems directly relevant to this module.

**4. Real Python — Python for Loops: The Definitive Guide**
[https://realpython.com/python-for-loop/](https://realpython.com/python-for-loop/)
Comprehensive free article covering `for` loops, `range()`, `enumerate()`, `zip()`, nested loops, comprehensions (preview), and the `else` clause. The section on `enumerate()` and `zip()` is particularly well-illustrated.

**5. Real Python — How to Use the Python while Loop**
[https://realpython.com/python-while-loop/](https://realpython.com/python-while-loop/)
Covers `while` loops, infinite loop patterns, `break`/`continue`/`else`, and common pitfalls like missing increment statements. The section on `while True` with `break` is directly applicable to the guessing game lab.

---

## 10. Lab and Command Preview

| Task | What You Will Do |
|---|---|
| while counting loop | Count 1–10 with `while`, trace each iteration manually |
| Input validation loop | Re-prompt until valid score is entered |
| break demo | Exit `while True` loop with break |
| continue demo | Skip even numbers in a for loop |
| for over range | Use range(start, stop, step) in multiple configurations |
| for over string | Iterate characters and count vowels |
| Loop else | Search a list with for-else to detect not-found |
| Accumulator | Sum and average a list of scores |
| enumerate and zip | Print index-value pairs and paired lists |
| `guessing_game.py` | Complete game: random number, while loop, break on win, else on loss |

---

## 10. Study Checklist

- [ ] Watch the Module 05 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially range() behavior and loop else.
- [ ] Work through the range() reference table in Section 3 — trace each one by hand.
- [ ] Work through the Common Error Patterns in Section 5.
- [ ] Read Chapter 5 of *Python for Everybody* at py4e.com.
- [ ] Read the for statement and range() pages in the Official Python 3 Docs.
- [ ] Watch Episodes 8–9 of the Python for Everybody playlist.
- [ ] Review all 7 Certification Exam Tips in Section 6.
- [ ] Preview the lab tasks in Section 9.
- [ ] Proceed to the Module 05 Lab Activity.
