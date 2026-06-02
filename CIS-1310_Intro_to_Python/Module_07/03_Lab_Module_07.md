# Lab Activity: Module 07 — Tuples, Sets, and Advanced Sorting

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 65–80 minutes

---

## Overview

In this lab you will create and work with tuples (including the single-item trap), trigger and understand `TypeError` from tuple modification, practice tuple packing and unpacking, build and operate on sets, use set operations for deduplication and intersection, write lambda functions as sort keys, sort complex data by multiple criteria, and build a complete student roster analyzer.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module07
cd module07
```

---

## Part 1 — Tuples in the REPL

```bash
python3
```

### Step 1.1 — Create Tuples

```python
>>> point = (3, 7)
>>> point
(3, 7)
>>> type(point)
<class 'tuple'>

>>> rgb = (255, 128, 0)
>>> empty = ()
>>> len(empty)
0

>>> # Tuple from an iterable
>>> t = tuple([1, 2, 3])
>>> t
(1, 2, 3)
```

### Step 1.2 — The Single-Item Trap

```python
>>> a = (42)
>>> type(a)
<class 'int'>
>>> a
42

>>> b = (42,)
>>> type(b)
<class 'tuple'>
>>> b
(42,)
```

Without the trailing comma, Python sees `(42)` as a parenthesized expression, not a tuple. This is a critical PCAP exam fact.

### Step 1.3 — Indexing and Slicing (Same as Lists)

```python
>>> rgb = (255, 128, 0)
>>> rgb[0]
255
>>> rgb[-1]
0
>>> rgb[1:]
(128, 0)
>>> len(rgb)
3
>>> 128 in rgb
True
```

### Step 1.4 — Immutability — Trigger TypeError

```python
>>> rgb[0] = 100
```

Expected:

```text
TypeError: 'tuple' object does not support item assignment
```

```python
>>> rgb.append(255)
```

Expected:

```text
AttributeError: 'tuple' object has no attribute 'append'
```

Tuples are immutable — there is no assignment, append, insert, remove, or sort operation.

### Step 1.5 — Tuple Packing and Unpacking

```python
>>> # Packing (parentheses are optional)
>>> pair = 10, 20
>>> pair
(10, 20)
>>> type(pair)
<class 'tuple'>

>>> # Unpacking
>>> x, y = pair
>>> x
10
>>> y
20

>>> # Unpacking in a for loop
>>> students = [('Alice', 92), ('Bob', 85), ('Carol', 78)]
>>> for name, score in students:
...     print(f'{name}: {score}')
...
Alice: 92
Bob: 85
Carol: 78

>>> # Extended unpacking
>>> first, *rest = (1, 2, 3, 4, 5)
>>> first
1
>>> rest
[2, 3, 4, 5]
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the single-item tuple trap (Step 1.2) and the TypeError from tuple modification (Step 1.4). Save as `lab07_screenshot_01_tuples.png`.

---

## Part 2 — Sets in the REPL

```bash
python3
```

### Step 2.1 — Create Sets

```python
>>> colors = {'red', 'green', 'blue'}
>>> type(colors)
<class 'set'>
>>> colors

>>> # Empty set — must use set(), NOT {}
>>> empty_set = set()
>>> type(empty_set)
<class 'set'>
>>> empty_dict = {}
>>> type(empty_dict)
<class 'dict'>
```

Note: the displayed order of set elements may vary each run — sets have no guaranteed order.

### Step 2.2 — Deduplication with set()

```python
>>> numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
>>> unique = set(numbers)
>>> unique
{1, 2, 3, 4}
>>> sorted_unique = sorted(unique)
>>> sorted_unique
[1, 2, 3, 4]
```

Converting a list to a set removes all duplicates. Converting back to a sorted list gives a clean deduplicated, ordered result.

### Step 2.3 — Set Operations

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {4, 5, 6, 7, 8}

>>> a | b    # union — all elements in either
{1, 2, 3, 4, 5, 6, 7, 8}

>>> a & b    # intersection — elements in both
{4, 5}

>>> a - b    # difference — in a, not in b
{1, 2, 3}

>>> b - a    # difference — in b, not in a
{6, 7, 8}

>>> a ^ b    # symmetric difference — in one but not both
{1, 2, 3, 6, 7, 8}
```

### Step 2.4 — Membership Testing

```python
>>> colors = {'red', 'green', 'blue'}
>>> 'red' in colors
True
>>> 'yellow' in colors
False
>>> 'yellow' not in colors
True
```

### Step 2.5 — Set Methods

```python
>>> fruits = {'apple', 'banana'}
>>> fruits.add('cherry')
>>> fruits
{'apple', 'banana', 'cherry'}

>>> fruits.remove('banana')
>>> fruits
{'apple', 'cherry'}

>>> fruits.discard('mango')    # no error even though 'mango' is not in the set
>>> fruits.remove('mango')     # KeyError!
```

Expected:

```text
KeyError: 'mango'
```

Use `discard()` when you are not sure if the element exists. Use `remove()` when you expect it to be present.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing set operations from Step 2.3 (union, intersection, difference, symmetric difference). Save as `lab07_screenshot_02_sets.png`.

---

## Part 3 — Lambda and Advanced Sorting

```bash
python3
```

### Step 3.1 — Lambda Basics

```python
>>> double = lambda x: x * 2
>>> double(5)
10
>>> double(3)
6

>>> add = lambda x, y: x + y
>>> add(4, 7)
11

>>> is_even = lambda n: n % 2 == 0
>>> is_even(4)
True
>>> is_even(7)
False
```

### Step 3.2 — Sorting with key=

```python
>>> words = ['banana', 'fig', 'cherry', 'apple', 'date']

>>> # Default alphabetical
>>> sorted(words)
['apple', 'banana', 'cherry', 'date', 'fig']

>>> # Sort by length
>>> sorted(words, key=len)
['fig', 'date', 'apple', 'banana', 'cherry']

>>> # Sort by last character
>>> sorted(words, key=lambda w: w[-1])
['banana', 'apple', 'date', 'fig', 'cherry']
```

### Step 3.3 — Sorting Tuples by Field

```python
>>> students = [('Alice', 88), ('Bob', 72), ('Carol', 95), ('Dave', 88)]

>>> # Sort by score ascending
>>> sorted(students, key=lambda s: s[1])
[('Bob', 72), ('Alice', 88), ('Dave', 88), ('Carol', 95)]

>>> # Sort by score descending
>>> sorted(students, key=lambda s: s[1], reverse=True)
[('Carol', 95), ('Alice', 88), ('Dave', 88), ('Bob', 72)]

>>> # Sort by score descending, then by name ascending (tiebreaker)
>>> sorted(students, key=lambda s: (-s[1], s[0]))
[('Carol', 95), ('Alice', 88), ('Dave', 88), ('Bob', 72)]
```

The negated score `-s[1]` flips the sort direction for the score. `s[0]` (name) is the tiebreaker in ascending order. `'Alice'` comes before `'Dave'` among the two scores of 88.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 3 REQUIRED:** Screenshot showing the advanced sorting examples from Step 3.3 — especially the tiebreaker sort. Save as `lab07_screenshot_03_sorting.png`.

---

## Part 4 — Set Comprehensions and Generators

```bash
python3
```

### Step 4.1 — Set Comprehension

```python
>>> squares_set = {x**2 for x in range(1, 6)}
>>> squares_set
{1, 4, 9, 16, 25}

>>> word_lengths = {len(w) for w in ['cat', 'dog', 'fish', 'elephant', 'ant', 'fox']}
>>> word_lengths
{3, 4, 8}
```

Set comprehensions automatically drop duplicates. `'cat'`, `'dog'`, and `'fox'` all have length 3, but only one `3` appears in the set.

### Step 4.2 — Generator Expression

```python
>>> # List comprehension — builds the whole list in memory
>>> squares_list = [x**2 for x in range(1, 6)]
>>> squares_list
[1, 4, 9, 16, 25]

>>> # Generator — produces values on demand
>>> gen = (x**2 for x in range(1, 6))
>>> gen
<generator object <genexpr> at 0x...>

>>> # Convert to list to see all values
>>> list(gen)
[1, 4, 9, 16, 25]

>>> # Use directly in sum() — no intermediate list created
>>> total = sum(x**2 for x in range(1, 6))
>>> total
55
```

Exit the REPL:

```python
>>> exit()
```

---

## Part 5 — Write roster_analyzer.py

### Step 5.1 — Create the Script

```bash
nano roster_analyzer.py
```

```python
# roster_analyzer.py
# Uses tuples, sets, lambda sorting, and set comprehensions
# Module 07 Lab — CIS-1310

students = [
    ('Alice', 'Math', 92),
    ('Bob', 'CS', 85),
    ('Carol', 'Math', 78),
    ('Dave', 'CS', 95),
    ('Eve', 'Physics', 88),
    ('Frank', 'Math', 72),
    ('Grace', 'CS', 91),
]

# --- Unique majors using set comprehension
majors = {major for _, major, _ in students}
print('=== Department Overview ===')
print(f'Departments: {sorted(majors)}')
print(f'Total students: {len(students)}')

# --- Students per department
print()
print('=== Students by Department ===')
for major in sorted(majors):
    dept_students = [name for name, m, _ in students if m == major]
    print(f'  {major}: {dept_students}')

# --- Rankings (sort by score descending, name ascending for ties)
top = sorted(students, key=lambda s: (-s[2], s[0]))
print()
print('=== Rankings (High to Low) ===')
for rank, (name, major, score) in enumerate(top, start=1):
    print(f'  {rank:2}. {name:<8} ({major:<8}) {score}')

# --- Statistics using generator expressions
scores = [score for _, _, score in students]
avg = sum(scores) / len(scores)
print()
print('=== Statistics ===')
print(f'  Average: {avg:.1f}')
print(f'  Highest: {max(scores)}')
print(f'  Lowest:  {min(scores)}')
print(f'  Passing: {sum(1 for s in scores if s >= 60)}')

# --- Find students with above-average scores
above_avg = [(name, score) for name, _, score in students if score > avg]
above_avg_sorted = sorted(above_avg, key=lambda s: -s[1])
print()
print(f'=== Above Average (>{avg:.1f}) ===')
for name, score in above_avg_sorted:
    print(f'  {name}: {score}')
```

Save and run:

```bash
python3 roster_analyzer.py
```

Expected output:

```text
=== Department Overview ===
Departments: ['CS', 'Math', 'Physics']
Total students: 7

=== Students by Department ===
  CS: ['Bob', 'Dave', 'Grace']
  Math: ['Alice', 'Carol', 'Frank']
  Physics: ['Eve']

=== Rankings (High to Low) ===
   1. Dave     (CS      ) 95
   2. Alice    (Math    ) 92
   3. Grace    (CS      ) 91
   4. Eve      (Physics ) 88
   5. Bob      (CS      ) 85
   6. Carol    (Math    ) 78
   7. Frank    (Math    ) 72

=== Statistics ===
  Average: 86.1
  Highest: 95
  Lowest:  72
  Passing: 7

=== Above Average (>86.1) ===
  Dave: 95
  Alice: 92
  Grace: 91
  Eve: 88
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `roster_analyzer.py` running showing all output sections. Save as `lab07_screenshot_04_roster_analyzer.png`.

---

## Part 6 — Set Real-World Use Case

```bash
nano set_demo.py
```

```python
# set_demo.py
# Demonstrates real-world set use: tag intersection and deduplication
# Module 07 Lab — CIS-1310

# Article tags
article_a = {'python', 'programming', 'beginner', 'tutorial'}
article_b = {'python', 'data-science', 'tutorial', 'statistics'}
article_c = {'java', 'programming', 'advanced', 'oop'}

all_tags = article_a | article_b | article_c
shared_a_b = article_a & article_b
python_only = article_a - article_b

print('=== Tag Analysis ===')
print(f'All unique tags: {sorted(all_tags)}')
print(f'Tags in both A and B: {sorted(shared_a_b)}')
print(f'Tags in A but not B: {sorted(python_only)}')

# Deduplication use case
raw_ids = [101, 102, 103, 102, 104, 101, 105, 103]
unique_ids = sorted(set(raw_ids))
print(f'\nRaw IDs:    {raw_ids}')
print(f'Unique IDs: {unique_ids}')
print(f'Duplicates removed: {len(raw_ids) - len(unique_ids)}')
```

Save and run:

```bash
python3 set_demo.py
```

Expected output:

```text
=== Tag Analysis ===
All unique tags: ['advanced', 'beginner', 'data-science', 'java', 'oop', 'programming', 'python', 'statistics', 'tutorial']
Tags in both A and B: ['python', 'tutorial']
Tags in A but not B: ['beginner', 'programming']

Raw IDs:    [101, 102, 103, 102, 104, 101, 105, 103]
Unique IDs: [101, 102, 103, 104, 105]
Duplicates removed: 3
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `set_demo.py` running. Save as `lab07_screenshot_05_set_demo.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 07 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab07_screenshot_01_tuples.png` | Single-item tuple trap and TypeError from modification |
| 2 | `lab07_screenshot_02_sets.png` | Set operations: union, intersection, difference, symmetric difference |
| 3 | `lab07_screenshot_03_sorting.png` | Advanced sorting with lambda key and tiebreaker |
| 4 | `lab07_screenshot_04_roster_analyzer.png` | `roster_analyzer.py` full output |
| 5 | `lab07_screenshot_05_set_demo.png` | `set_demo.py` tag analysis and deduplication |

---

## Troubleshooting Guide

**`(42)` is an int, not a tuple.**
The trailing comma is required for a single-element tuple: `(42,)`. Without it, Python treats the parentheses as grouping for operator precedence, not as a tuple literal.

**`TypeError` when trying to modify a tuple.**
Tuples are immutable. If you need to modify the data, convert to a list first: `lst = list(my_tuple)`, modify the list, then convert back if needed: `my_tuple = tuple(lst)`.

**`{}` created a dict instead of a set.**
`{}` always creates an empty dictionary. Use `set()` for an empty set, or `{1, 2, 3}` for a set with initial values.

**`TypeError: 'set' object is not subscriptable`.**
Sets cannot be indexed. If you need a specific element, iterate over the set or convert it to a sorted list first.

**Sort order is unexpected with lambda key.**
Trace the lambda manually: what does `lambda s: (-s[1], s[0])` produce for each element? Python sorts tuples lexicographically — first by the first element, then the second as a tiebreaker. Negating a number reverses its sort direction.
