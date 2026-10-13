# Video Script: CIS-1310 — Introduction to Python

## Module 07 — Tuples, Sets, and Advanced Sorting

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - Draw the Venn diagram for set operations on the slide before showing the code.
> - Contrast the tuple immutability error with successful list modification side by side.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 07 | Tuples, Sets, and Advanced Sorting | CIS-1310"]**

"Welcome back. Module 06 gave you a deep understanding of lists — Python's mutable, ordered sequence. This module introduces two more sequence types that complete the picture: **tuples** and **sets**.

Tuples are lists you cannot change — immutable sequences that carry a guarantee: the data stays exactly as it was created. Sets are unordered collections that enforce uniqueness — no duplicates allowed. Both are tested on the PCAP exam, and both solve real problems that lists cannot solve cleanly.

We will also cover advanced sorting — using the `key` parameter with `sorted()` and `lambda` functions to sort by computed criteria rather than just natural order. Let's go."

---

## [00:45 – 03:30] Tuples — Immutable Sequences

**[SHOW SLIDE: "Tuples — Ordered, Immutable Sequences"]**

"A **tuple** is an ordered, immutable sequence. It looks like a list but uses parentheses instead of square brackets.

**[DEMO — creating tuples]**

```python
>>> point = (3, 7)
>>> rgb = (255, 128, 0)
>>> empty_tuple = ()
>>> single = (42,)    # note the trailing comma — required for single-item tuple
>>> type(point)
<class 'tuple'>
```

That trailing comma for a single-item tuple is a very common PCAP exam question. Without it, Python treats `(42)` as just a parenthesized integer, not a tuple:

```python
>>> type((42))
<class 'int'>
>>> type((42,))
<class 'tuple'>
```

**[DEMO — indexing and slicing work the same]**

```python
>>> rgb = (255, 128, 0)
>>> rgb[0]
255
>>> rgb[-1]
0
>>> rgb[1:]
(128, 0)
```

### Immutability

You cannot change a tuple after creation. Trying to assign to an index raises `TypeError`:

**[DEMO]**

```python
>>> rgb[0] = 100
TypeError: 'tuple' object does not support item assignment
```

This is by design. Tuples are used when data should not change — coordinates, RGB values, database rows, function return values. The immutability is a contract: whoever receives this tuple knows the data is fixed.

### Tuple Packing and Unpacking

**Packing:** assigning multiple values into a tuple.

```python
>>> point = 3, 7    # parentheses are optional
>>> point
(3, 7)
```

**Unpacking:** assigning a tuple's items to individual variables.

```python
>>> x, y = point
>>> x
3
>>> y
7
```

This is the same swap syntax from Module 03: `a, b = b, a`. Python creates a tuple on the right, then unpacks it into the variables on the left."

---

## [03:30 – 04:45] Tuples vs. Lists — When to Use Each

**[SHOW SLIDE: "Tuple vs. List — Choosing the Right Type"]**

"| Feature | List | Tuple |
|---|---|---|
| Mutable | Yes | No |
| Syntax | `[...]` | `(...)` |
| Use when | Data changes | Data is fixed |
| As dict key | No | Yes |
| Memory | Slightly more | Slightly less |

Use tuples for data that represents a fixed record — a coordinate, a date, a database row. Use lists when you need to add, remove, or modify items after creation.

A practical rule: if the collection has semantic meaning where order and position matter and never changes — like `(latitude, longitude)` — use a tuple. If it's a dynamic collection of similar items that may grow or shrink — use a list."

---

## [04:45 – 07:30] Sets — Unordered Collections of Unique Items

**[SHOW SLIDE: "Sets — No Duplicates, No Order"]**

"A **set** is an unordered collection of unique items. The key word is unique — if you add the same value twice, it only appears once.

**[DEMO — creating sets]**

```python
>>> colors = {'red', 'green', 'blue'}
>>> type(colors)
<class 'set'>
>>> colors
{'red', 'green', 'blue'}    # order may vary — sets have no guaranteed order
```

**Creating a set from a list — removes duplicates automatically:**

```python
>>> numbers = [1, 2, 2, 3, 3, 3, 4]
>>> unique = set(numbers)
>>> unique
{1, 2, 3, 4}
```

This is one of the most useful set tricks: `set(list)` removes all duplicates in one operation.

**Creating an empty set — you cannot use `{}` (that creates an empty dict):**

```python
>>> empty_set = set()
>>> type(empty_set)
<class 'set'>
>>> type({})
<class 'dict'>
```

### Set Operations

Sets support the mathematical operations from set theory:

**[DEMO]**

```python
>>> a = {1, 2, 3, 4}
>>> b = {3, 4, 5, 6}

>>> a | b    # union — all elements in either set
{1, 2, 3, 4, 5, 6}

>>> a & b    # intersection — elements in both sets
{3, 4}

>>> a - b    # difference — in a but not in b
{1, 2}

>>> a ^ b    # symmetric difference — in one but not both
{1, 2, 5, 6}

>>> 3 in a    # membership test — O(1), faster than list
True
```

### Set Methods

```python
>>> colors = {'red', 'green'}
>>> colors.add('blue')
>>> colors
{'red', 'green', 'blue'}

>>> colors.remove('red')    # raises KeyError if not found
>>> colors.discard('yellow')    # no error if not found
>>> colors
{'green', 'blue'}
```

Sets are unordered — you cannot index them. Use sets when you need uniqueness guarantees, fast membership testing, or set arithmetic."

---

## [07:30 – 09:30] Sorting with the key Parameter

**[SHOW SLIDE: "Advanced Sorting — key Parameter"]**

"The built-in `sorted()` function and `list.sort()` accept an optional `key` parameter — a function that computes a sort key for each element.

**[DEMO — sort strings by length]**

```python
>>> words = ['banana', 'apple', 'fig', 'cherry', 'date']
>>> sorted(words)
['apple', 'banana', 'cherry', 'date', 'fig']    # alphabetical default

>>> sorted(words, key=len)
['fig', 'date', 'apple', 'banana', 'cherry']    # by string length
```

`key=len` tells `sorted()` to call `len(word)` on each word and sort by that computed value, rather than by the word itself.

**[DEMO — sort by a specific field in a list of tuples]**

```python
>>> students = [('Alice', 88), ('Bob', 72), ('Carol', 95)]
>>> sorted(students, key=lambda s: s[1])
[('Bob', 72), ('Alice', 88), ('Carol', 95)]    # sort by score
```

That `lambda` is a new concept — let me explain it."

---

## [09:30 – 11:00] Lambda Functions

**[SHOW SLIDE: "Lambda — Anonymous Functions"]**

"A **lambda** is a small, anonymous (unnamed) function defined in a single expression. The syntax is:

```python
lambda parameters: expression
```

It is not a complete function definition — it is a shorthand for a simple one-liner that you only need in one place.

**[DEMO]**

```python
>>> double = lambda x: x * 2
>>> double(5)
10

>>> add = lambda x, y: x + y
>>> add(3, 4)
7
```

You would not normally assign a lambda to a variable like `double = lambda x: x * 2` — if you need a reusable function, just use `def`. Lambdas shine as inline `key` functions:

```python
>>> students = [('Alice', 88), ('Bob', 72), ('Carol', 95), ('Dave', 95)]

>>> # Sort by score descending, then by name ascending
>>> sorted(students, key=lambda s: (-s[1], s[0]))
[('Carol', 95), ('Dave', 95), ('Alice', 88), ('Bob', 72)]
```

The negation `-s[1]` flips the sort order for the score so that higher scores come first, while `s[0]` (the name) sorts alphabetically as a tiebreaker.

Lambda functions are tested on the PCAP exam — you need to be able to read a lambda and predict what it returns."

---

## [11:00 – 12:30] Comprehensions — Set and Generator

**[SHOW SLIDE: "Set Comprehensions and Generators"]**

"Module 06 introduced list comprehensions. The same syntax works for sets — replace square brackets with curly braces:

```python
>>> squares_set = {x**2 for x in range(1, 6)}
>>> squares_set
{1, 4, 9, 16, 25}
```

A set comprehension automatically removes duplicates:

```python
>>> {len(word) for word in ['cat', 'dog', 'fish', 'bat']}
{3, 4}    # 'cat', 'dog', 'bat' all have length 3 — only one 3 in the set
```

**Generator expressions** use parentheses instead of brackets and produce values lazily (on demand) rather than building the full list in memory:

```python
>>> gen = (x**2 for x in range(1, 6))
>>> gen
<generator object <genexpr> at 0x...>
>>> list(gen)
[1, 4, 9, 16, 25]
```

Generators are memory-efficient for large sequences — they compute each value only when needed. This is important in production code processing millions of records."

---

## [12:30 – 13:45] Putting It Together — Student Roster Analyzer

**[DEMO — live code]**

"Let me write a program that uses tuples, sets, and advanced sorting together:

```python
# roster_analyzer.py
# Module 07 Lab — CIS-1310

students = [
    ('Alice', 'Math', 92),
    ('Bob', 'CS', 85),
    ('Carol', 'Math', 78),
    ('Dave', 'CS', 95),
    ('Eve', 'Math', 88),
]

# Unique majors using a set comprehension
majors = {major for _, major, _ in students}
print(f'Majors offered: {sorted(majors)}')

# Sort by score descending
top_students = sorted(students, key=lambda s: -s[2])
print('\nRankings:')
for rank, (name, major, score) in enumerate(top_students, start=1):
    print(f'  {rank}. {name} ({major}): {score}')

# Average score using a generator expression
total = sum(score for _, _, score in students)
average = total / len(students)
print(f'\nClass average: {average:.1f}')
```

This uses tuple unpacking in `for` loops, set comprehensions, lambda sort keys, `enumerate()`, and a generator expression for the sum — all in one concise program."

---

## [13:45 – 15:00] PCAP Exam Tips and Wrap-Up

**[SHOW SLIDE: "Module 07 — PCAP Alignment"]**

"Key exam take-aways:

**1.** Single-item tuple requires a trailing comma: `(42,)` is a tuple. `(42)` is just an integer.

**2.** Tuples are immutable — assigning to an index raises `TypeError`.

**3.** `{}` creates an empty **dict**, not a set. Use `set()` for an empty set.

**4.** Sets are unordered and contain only unique elements. Duplicate values are silently dropped.

**5.** Set operators: `|` (union), `&` (intersection), `-` (difference), `^` (symmetric difference).

**6.** Lambda syntax: `lambda params: expression`. Returns the expression value when called.

**7.** `key=` parameter in `sorted()`: the function is called on each element; elements are sorted by the result.

Module 08 covers functions — the most important module for writing reusable, organized code. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 07 — Tuples, Sets, and Advanced Sorting]**

---

## Additional Resources

- [Python for Everybody — Chapter 10](https://www.py4e.com/book) — Tuples
- [Official Python Docs — Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Official Python Docs — Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Official Python Docs — Sorting How-To](https://docs.python.org/3/howto/sorting.html)
- [Python for Everybody Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Episode 10 (Tuples)
