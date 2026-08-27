# Lab Activity: Module 06 — Lists: The Workhorse Data Structure

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 65–80 minutes

---

## Overview

In this lab you will practice list indexing (positive and negative), all forms of slicing, every core list method, the sort vs. sorted distinction, the alias vs. copy distinction, list comprehensions with and without filters, nested list access, and build a complete grade tracker program.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module06
cd module06
```

---

## Part 1 — Indexing and Slicing in the REPL

```bash
python3
```

### Step 1.1 — Create a List and Access by Index

```python
>>> grades = [88, 72, 95, 61, 83, 77, 90]
>>> len(grades)
7
>>> grades[0]
88
>>> grades[1]
72
>>> grades[6]
90
>>> grades[-1]
90
>>> grades[-2]
77
>>> grades[-7]
88
```

Both `grades[6]` and `grades[-1]` give 90 — they point to the same item.

### Step 1.2 — Trigger IndexError

```python
>>> grades[7]
```

Expected:

```text
IndexError: list index out of range
```

Valid positive indices for a 7-element list are 0 through 6.

### Step 1.3 — Slicing

```python
>>> grades[1:3]
[72, 95]
>>> grades[0:4]
[88, 72, 95, 61]
>>> grades[4:]
[83, 77, 90]
>>> grades[:3]
[88, 72, 95]
>>> grades[:]
[88, 72, 95, 61, 83, 77, 90]
>>> grades[::2]
[88, 95, 83, 90]
>>> grades[::-1]
[90, 77, 83, 61, 95, 72, 88]
>>> grades[1:6:2]
[72, 61, 77]
```

### Step 1.4 — Slicing Out-of-Bounds Is Safe

```python
>>> grades[100:]
[]
>>> grades[:100]
[88, 72, 95, 61, 83, 77, 90]
```

Slices do not raise `IndexError` for out-of-range indices — they simply stop at the list boundary.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the IndexError from Step 1.2 and the slice examples from Step 1.3. Save as `lab06_screenshot_01_indexing_slicing.png`.

---

## Part 2 — List Methods in the REPL

```bash
python3
```

### Step 2.1 — append, insert, remove, pop

```python
>>> items = ['apple', 'banana', 'cherry']
>>> items.append('date')
>>> items
['apple', 'banana', 'cherry', 'date']

>>> items.insert(1, 'avocado')
>>> items
['apple', 'avocado', 'banana', 'cherry', 'date']

>>> items.remove('banana')
>>> items
['apple', 'avocado', 'cherry', 'date']

>>> removed = items.pop()
>>> removed
'date'
>>> items
['apple', 'avocado', 'cherry']

>>> removed = items.pop(0)
>>> removed
'apple'
>>> items
['avocado', 'cherry']
```

### Step 2.2 — sort() vs. sorted() — The PCAP Trap

```python
>>> numbers = [5, 2, 8, 1, 9, 3]

>>> # sorted() returns a new list — original unchanged
>>> sorted_copy = sorted(numbers)
>>> sorted_copy
[1, 2, 3, 5, 8, 9]
>>> numbers
[5, 2, 8, 1, 9, 3]

>>> # sort() modifies in place and returns None
>>> result = numbers.sort()
>>> result
>>> type(result)
<class 'NoneType'>
>>> numbers
[1, 2, 3, 5, 8, 9]
```

Entering `result` at the REPL shows nothing (None) — the interactive interpreter does not print None. Use `print(result)` to make it explicit:

```python
>>> numbers2 = [5, 2, 8]
>>> print(numbers2.sort())
None
>>> numbers2
[2, 5, 8]
```

### Step 2.3 — reverse(), index(), count(), extend()

```python
>>> letters = ['c', 'a', 'b', 'a']
>>> letters.reverse()
>>> letters
['a', 'b', 'a', 'c']

>>> letters.index('a')
0
>>> letters.count('a')
2

>>> letters.extend(['d', 'e'])
>>> letters
['a', 'b', 'a', 'c', 'd', 'e']
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing the sort() vs. sorted() demo from Step 2.2 — specifically showing that `sort()` returns None. Save as `lab06_screenshot_02_sort_sorted.png`.

---

## Part 3 — Alias vs. Copy

```bash
python3
```

### Step 3.1 — The Alias Bug

```python
>>> original = [1, 2, 3]
>>> alias = original
>>> id(original)
>>> id(alias)
```

The `id()` values are identical — both names point to the same object.

```python
>>> alias.append(99)
>>> original
[1, 2, 3, 99]
```

Modifying through `alias` changes `original` because they ARE the same list.

### Step 3.2 — Three Ways to Copy

```python
>>> original = [1, 2, 3]

>>> copy1 = original[:]
>>> copy2 = original.copy()
>>> copy3 = list(original)

>>> id(original) == id(copy1)
False
>>> id(original) == id(copy2)
False

>>> copy1.append(99)
>>> copy2.append(88)
>>> copy3.append(77)

>>> original
[1, 2, 3]
>>> copy1
[1, 2, 3, 99]
>>> copy2
[1, 2, 3, 88]
>>> copy3
[1, 2, 3, 77]
```

All three copy methods produce independent objects. Modifications to copies do not affect the original.

Exit the REPL:

```python
>>> exit()
```

---

## Part 4 — List Comprehensions

```bash
python3
```

### Step 4.1 — Basic Comprehensions

```python
>>> squares = [x**2 for x in range(1, 6)]
>>> squares
[1, 4, 9, 16, 25]

>>> doubled = [x * 2 for x in [3, 5, 7, 9]]
>>> doubled
[6, 10, 14, 18]

>>> lengths = [len(w) for w in ['Python', 'is', 'awesome']]
>>> lengths
[6, 2, 7]
```

### Step 4.2 — Comprehensions with Filter

```python
>>> evens = [x for x in range(10) if x % 2 == 0]
>>> evens
[0, 2, 4, 6, 8]

>>> odds = [x for x in range(10) if x % 2 != 0]
>>> odds
[1, 3, 5, 7, 9]

>>> grades = [88, 72, 95, 61, 83, 55, 90]
>>> passing = [g for g in grades if g >= 60]
>>> passing
[88, 72, 95, 61, 83, 90]
```

### Step 4.3 — Comprehension vs. for Loop

Confirm that a comprehension and a loop produce identical results:

```python
>>> # Using a loop
>>> loop_result = []
>>> for x in range(5):
...     if x != 2:
...         loop_result.append(x**2)
...
>>> loop_result
[0, 1, 9, 16]

>>> # Using a comprehension
>>> comp_result = [x**2 for x in range(5) if x != 2]
>>> comp_result
[0, 1, 9, 16]

>>> loop_result == comp_result
True
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 3 REQUIRED:** Screenshot showing list comprehension examples from Steps 4.1 and 4.2. Save as `lab06_screenshot_03_comprehensions.png`.

---

## Part 5 — Nested Lists

```bash
python3
```

### Step 5.1 — Create and Access

```python
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>> matrix[0]
[1, 2, 3]
>>> matrix[1]
[4, 5, 6]
>>> matrix[0][0]
1
>>> matrix[1][2]
6
>>> matrix[2][-1]
9
```

### Step 5.2 — Iterate with Nested Loops

```python
>>> for row in matrix:
...     for val in row:
...         print(val, end=' ')
...     print()
...
1 2 3
4 5 6
7 8 9
```

### Step 5.3 — Flatten with a Comprehension

```python
>>> flat = [val for row in matrix for val in row]
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Exit the REPL:

```python
>>> exit()
```

---

## Part 6 — Write grade_tracker.py

### Step 6.1 — Create the Script

```bash
nano grade_tracker.py
```

```python
# grade_tracker.py
# Builds a list of student scores and reports statistics
# Module 06 Lab — CIS-1310

print('=== Student Grade Tracker ===')
print('Enter student scores one at a time.')
print('Type -1 when finished.')
print()

scores = []

while True:
    raw = input('  Score (or -1 to finish): ')

    if not raw.lstrip('-').isdigit():
        print('  Please enter a whole number.')
        continue

    score = int(raw)

    if score == -1:
        break

    if 0 <= score <= 100:
        scores.append(score)
        print(f'  Added. ({len(scores)} score(s) entered)')
    else:
        print(f'  Ignored: {score} is out of range (0-100).')

print()

if not scores:
    print('No valid scores entered.')
else:
    scores.sort()

    total = sum(scores)
    count = len(scores)
    average = total / count
    passing = [s for s in scores if s >= 60]
    failing = [s for s in scores if s < 60]

    print('=== Results ===')
    print(f'  All scores (sorted): {scores}')
    print(f'  Count:    {count}')
    print(f'  Total:    {total}')
    print(f'  Average:  {average:.2f}')
    print(f'  Highest:  {scores[-1]}')
    print(f'  Lowest:   {scores[0]}')
    print(f'  Passing:  {len(passing)} ({passing})')
    print(f'  Failing:  {len(failing)} ({failing})')
```

Save and run:

```bash
python3 grade_tracker.py
```

Sample interaction:

```text
=== Student Grade Tracker ===
Enter student scores one at a time.
Type -1 when finished.

  Score (or -1 to finish): 88
  Added. (1 score(s) entered)
  Score (or -1 to finish): 72
  Added. (2 score(s) entered)
  Score (or -1 to finish): abc
  Please enter a whole number.
  Score (or -1 to finish): 95
  Added. (3 score(s) entered)
  Score (or -1 to finish): 55
  Added. (4 score(s) entered)
  Score (or -1 to finish): -1

=== Results ===
  All scores (sorted): [55, 72, 88, 95]
  Count:    4
  Total:    310
  Average:  77.50
  Highest:  95
  Lowest:   55
  Passing:  3 ([72, 88, 95])
  Failing:  1 ([55])
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `grade_tracker.py` running with at least 4 scores entered, including one rejection. Save as `lab06_screenshot_04_grade_tracker.png`.

---

## Part 7 — List Operations Reference Script

```bash
nano list_ops.py
```

```python
# list_ops.py
# Demonstrates list operators: +, *, in, not in, len
# Module 06 Lab — CIS-1310

a = [1, 2, 3]
b = [4, 5, 6]

print('Concatenation:  ', a + b)
print('Repetition:     ', [0] * 5)
print('in operator:    ', 3 in a)
print('not in:         ', 10 not in a)
print('len():          ', len(a))
print()

# List comprehension with zip
names = ['Alice', 'Bob', 'Carol']
scores = [92, 85, 78]
report = [f'{n}: {s}' for n, s in zip(names, scores)]
print('Report:         ', report)
print()

# Reverse without modifying original
original = [1, 2, 3, 4, 5]
reversed_copy = original[::-1]
print('Original:       ', original)
print('Reversed copy:  ', reversed_copy)
```

Save and run:

```bash
python3 list_ops.py
```

Expected output:

```text
Concatenation:   [1, 2, 3, 4, 5, 6]
Repetition:      [0, 0, 0, 0, 0]
in operator:     True
not in:          True
len():           3

Report:          ['Alice: 92', 'Bob: 85', 'Carol: 78']

Original:        [1, 2, 3, 4, 5]
Reversed copy:   [5, 4, 3, 2, 1]
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `list_ops.py` running showing all output. Save as `lab06_screenshot_05_list_ops.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 06 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab06_screenshot_01_indexing_slicing.png` | IndexError and slice examples |
| 2 | `lab06_screenshot_02_sort_sorted.png` | `sort()` returning None vs `sorted()` returning new list |
| 3 | `lab06_screenshot_03_comprehensions.png` | List comprehension examples with and without filter |
| 4 | `lab06_screenshot_04_grade_tracker.png` | `grade_tracker.py` with score entry and results |
| 5 | `lab06_screenshot_05_list_ops.png` | `list_ops.py` all output |

---

## Part 9 — Challenge Exercise

These steps are optional and ungraded. They extend list skills toward real data processing patterns.

### Challenge 9.1 — Matrix Transposition

Write `~/cis1310/module06/matrix_transpose.py` that transposes a 3x3 matrix using nested list comprehensions. Given:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Produce the transposed matrix (rows become columns):

```python
transposed = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

Implement this using a nested list comprehension: `[[row[i] for row in matrix] for i in range(len(matrix[0]))]`. Then write a function `print_matrix(m)` that displays the matrix row by row with consistent column alignment. Compare the original and transposed matrices side-by-side in your output.

---

### Challenge 9.2 — Histogram Generator

Write `~/cis1310/module06/histogram.py` that reads a list of integers from the user (one per line, stopping at a blank input) and displays a horizontal ASCII histogram. For each value `v`, print a bar of `v` asterisks followed by the count:

```text
Value 1: ****** (6)
Value 2: *** (3)
Value 3: ********* (9)
```

Also compute and display: minimum, maximum, mean, median (sort the list and take the middle element — handle both odd and even list lengths), and standard deviation (square root of the average squared deviation from the mean, using only built-in functions without importing `statistics`).

---

### Challenge 9.3 — List Deduplication Three Ways

Write `~/cis1310/module06/dedup.py` that demonstrates three different approaches to removing duplicates from a list while preserving insertion order:

1. A manual loop with an `in` membership check building a new list
2. A list comprehension using `enumerate` that keeps an element only if its current index is the first occurrence
3. Converting to a `dict.fromkeys()` and back to a list (this works because dictionaries preserve insertion order in Python 3.7+)

Test all three on the list `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`. Verify all three produce identical results. Print the method name, the result, and the execution approach for each. This exercise previews the `dict` data structure from Module 10.

---

## Troubleshooting Guide

**`IndexError: list index out of range`.**
Check the list length with `len(lst)`. Valid indices are 0 through `len(lst) - 1`. For a 5-element list, index 5 is out of range.

**`sort()` returned None — where is my sorted list?**
`list.sort()` sorts in place and returns `None`. Use `list.sort()` alone (do not assign it). If you need a new sorted list without modifying the original, use `sorted(list)`.

**After appending to `copy`, `original` also changed.**
You have an alias, not a copy. Use `copy = original[:]` or `copy = original.copy()` to create an independent list.

**List comprehension produces an empty list.**
Check your filter condition. If the condition is never `True` for any item in the iterable, the result is an empty list — not an error.

**`remove()` raises ValueError.**
`remove()` raises `ValueError: list.remove(x): x not in list` if the value is not in the list. Use `if x in lst:` before calling `lst.remove(x)`.
