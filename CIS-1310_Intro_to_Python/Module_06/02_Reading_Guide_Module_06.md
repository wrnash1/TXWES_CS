# Reading Guide: Module 06 — Lists: The Workhorse Data Structure

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 06 — Lists**. Lists are Python's primary ordered collection type and appear in virtually every Python program. The PCAP exam tests list indexing, slicing, methods (including their return values), mutability, the assignment-vs-copy distinction, and list comprehensions. Master every entry in this guide before starting the lab.

---

## 1. High-Yield Glossary

### List

An ordered, mutable sequence of items enclosed in square brackets. Items are separated by commas. Lists can contain any Python values and can mix types.

```python
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Carol']
mixed = [42, 'hello', 3.14, True, None]
empty = []
```

### Index

The position of an item in a list, starting at 0. Valid positive indices run from `0` to `len(list) - 1`. Accessing an index outside this range raises `IndexError`.

```python
lst = ['a', 'b', 'c', 'd']
#      0    1    2    3      <- positive indices
#     -4   -3   -2   -1     <- negative indices
```

### Negative Index

A shorthand for counting from the end of the list. `-1` is the last item, `-2` is second-to-last, and so on.

```python
lst[-1]    # 'd' — last item
lst[-4]    # 'a' — same as lst[0]
```

### Slicing

Extracts a portion of a list and returns a **new list**. Syntax: `list[start:stop:step]`. The `stop` index is always excluded.

```python
lst = [10, 20, 30, 40, 50]
lst[1:3]     # [20, 30]       — indices 1 and 2
lst[2:]      # [30, 40, 50]   — from index 2 to end
lst[:3]      # [10, 20, 30]   — from start up to (not including) index 3
lst[:]       # [10, 20, 30, 40, 50]  — full copy
lst[::2]     # [10, 30, 50]   — every other item
lst[::-1]    # [50, 40, 30, 20, 10] — reversed
```

### Mutability

Lists are mutable — they can be modified after creation. You can change individual items, add items, remove items, and reorder items without creating a new list object.

```python
lst = [1, 2, 3]
lst[0] = 99       # change item at index 0
lst.append(4)     # add item to end
```

This contrasts with strings and tuples, which are immutable — you cannot change them in place.

### List Methods — Complete Reference

| Method | Description | Returns |
|---|---|---|
| `append(x)` | Add `x` to the end | `None` |
| `insert(i, x)` | Insert `x` before index `i` | `None` |
| `remove(x)` | Remove first occurrence of `x`; `ValueError` if not found | `None` |
| `pop()` | Remove and return last item | Removed item |
| `pop(i)` | Remove and return item at index `i` | Removed item |
| `sort()` | Sort in place (ascending by default) | `None` |
| `sort(reverse=True)` | Sort in place descending | `None` |
| `reverse()` | Reverse in place | `None` |
| `index(x)` | Return index of first `x`; `ValueError` if not found | `int` |
| `count(x)` | Count occurrences of `x` | `int` |
| `extend(lst2)` | Append all items from `lst2` to end | `None` |
| `clear()` | Remove all items | `None` |
| `copy()` | Return a shallow copy | new list |

**PCAP exam trap:** `append()`, `sort()`, `reverse()`, `remove()`, `insert()`, and `extend()` all return `None`. Writing `sorted_list = my_list.sort()` gives you `None`, not the sorted list. Use `sorted(my_list)` to get a new sorted list.

### sort() vs. sorted()

| Feature | `list.sort()` | `sorted(list)` |
|---|---|---|
| Modifies original | Yes | No |
| Returns | `None` | New sorted list |
| Works on | Lists only | Any iterable |

### List Operators

| Operator | Description | Example | Result |
|---|---|---|---|
| `+` | Concatenate two lists | `[1,2] + [3,4]` | `[1,2,3,4]` |
| `*` | Repeat a list | `[0] * 3` | `[0,0,0]` |
| `in` | Test membership | `3 in [1,2,3]` | `True` |
| `not in` | Test non-membership | `5 not in [1,2,3]` | `True` |
| `len()` | Count items | `len([1,2,3])` | `3` |

### List Comprehension

A compact syntax for creating a new list by applying an expression to each item in an iterable, with an optional filter condition.

```python
# Basic — one item per input item
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# With filter — only include items where condition is True
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transform existing list
curved = [score + 5 for score in grades]

# Filter and transform
passing = [score for score in grades if score >= 60]
```

Reading a comprehension: "Build a list of `[expression]` for each `[variable]` in `[iterable]` where `[condition]`."

### Reference vs. Copy

Assigning a list to another variable creates a **reference** (alias) — both variables point to the same list object. Modifying through either variable modifies the shared object.

```python
a = [1, 2, 3]
b = a           # b and a point to the SAME list
b.append(4)
print(a)        # [1, 2, 3, 4] — a was modified!
```

To create an independent copy, use any of these:

```python
b = a[:]          # slice copy
b = a.copy()      # .copy() method
b = list(a)       # list() constructor
```

### Nested List

A list that contains other lists as elements. Commonly used to represent 2D data (tables, matrices, game boards).

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0]       # [1, 2, 3]
matrix[1][2]    # 6  (row 1, column 2)
```

---

## 2. Indexing and Slicing Reference

```python
lst = ['a', 'b', 'c', 'd', 'e']
#      0    1    2    3    4      (positive)
#     -5   -4   -3   -2   -1     (negative)

lst[0]       # 'a'
lst[-1]      # 'e'
lst[1:3]     # ['b', 'c']
lst[:2]      # ['a', 'b']
lst[3:]      # ['d', 'e']
lst[:]       # ['a', 'b', 'c', 'd', 'e']  (copy)
lst[::2]     # ['a', 'c', 'e']  (every 2nd)
lst[::-1]    # ['e', 'd', 'c', 'b', 'a']  (reversed)
lst[1:4:2]   # ['b', 'd']  (indices 1 and 3)
```

---

## 3. List Comprehension Tracing Practice

Predict the output of each comprehension before verifying:

**Expression 1:**

```python
[x * 2 for x in [1, 2, 3, 4, 5]]
```

Result: `[2, 4, 6, 8, 10]`

**Expression 2:**

```python
[x for x in range(1, 10) if x % 3 == 0]
```

Result: `[3, 6, 9]`

**Expression 3:**

```python
[len(word) for word in ['Python', 'is', 'fun']]
```

Result: `[6, 2, 3]`

**Expression 4:**

```python
[x**2 for x in range(5) if x != 2]
```

Result: `[0, 1, 9, 16]` — 4 is skipped because `x=2` is excluded by the filter.

---

## 4. Common Error Patterns to Memorize

**Pattern 1 — Assigning the return value of a mutating method:**

```python
lst = [3, 1, 2]
lst = lst.sort()    # lst is now None
print(lst)           # None — not [1, 2, 3]
```

Fix: `lst.sort()` without assignment, or `lst = sorted([3, 1, 2])`.

**Pattern 2 — IndexError from off-by-one:**

```python
lst = [1, 2, 3]
print(lst[3])    # IndexError — valid indices are 0, 1, 2
```

**Pattern 3 — Modifying a list alias:**

```python
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)    # [1, 2, 3, 4] — both are affected
```

**Pattern 4 — remove() raises ValueError for missing items:**

```python
lst = [1, 2, 3]
lst.remove(5)    # ValueError: list.remove(x): x not in list
```

**Pattern 5 — Slice out-of-bounds is safe, index is not:**

```python
lst = [1, 2, 3]
lst[10]      # IndexError
lst[10:]     # [] — no error, returns empty list
```

---

## 5. Certification Exam Tips

**Tip 1 — Indices start at 0, stop is excluded in slices.**
`lst[1:3]` gives items at positions 1 and 2 — not 3. Off-by-one errors are the most common list mistake.

**Tip 2 — Mutating methods return None.**
`append()`, `insert()`, `remove()`, `sort()`, `reverse()`, `clear()` all return `None`. Do not assign their results.

**Tip 3 — `list.sort()` vs. `sorted(list)`.**
`list.sort()` modifies in place, returns `None`. `sorted(list)` returns a new sorted list, original unchanged.

**Tip 4 — Alias vs. copy.**
`b = a` is an alias — both point to the same list. Use `b = a[:]`, `b = a.copy()`, or `b = list(a)` for an independent copy.

**Tip 5 — List comprehension reads left to right.**
`[x**2 for x in range(5) if x > 2]` → compute `x**2` for each `x` in `range(5)` where `x > 2`. Values: x=3→9, x=4→16. Result: `[9, 16]`.

**Tip 6 — `in` tests membership, not index.**
`5 in [1, 3, 5, 7]` returns `True`. To get the index, use `lst.index(5)`.

**Tip 7 — Negative indexing.**
`lst[-1]` is the last item. `lst[-n]` is equivalent to `lst[len(lst) - n]`.

---

## 6. Beyond the Exam — Real-World Context

**Why is list mutability both powerful and dangerous?**
Mutability lets you build a list incrementally — `append()` inside a loop is how you collect data. But shared references (the alias problem) cause real bugs in production code. Python developers use `copy()` when passing lists to functions to prevent accidental modification of the caller's data.

**List comprehensions in data science.**
In data science and machine learning, list comprehensions are ubiquitous:

```python
# Normalize scores to 0.0–1.0 range
normalized = [s / 100.0 for s in scores]

# Filter out missing values
clean = [x for x in data if x is not None]
```

Libraries like NumPy and pandas provide even faster array operations, but list comprehensions are the foundation you build from.

**sum(), min(), max() work on any numeric list.**
Python's built-in functions `sum()`, `min()`, and `max()` accept any iterable, including lists. In practice, you rarely write accumulator loops for these specific operations:

```python
total = sum(scores)
maximum = max(scores)
minimum = min(scores)
```

These are shorthand for the accumulator patterns you built in Module 05.

---

## 7. Required Readings and Videos

**Required Reading — Chapter 8:**
Read Chapter 8 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). The chapter covers lists, list methods, and iteration patterns.

**Required Reading — Official Python Docs:**
Read [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) and [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) in the official Python 3 tutorial.

**Required Video:**
Watch Episodes 10–11 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).

---

## 8. Lab and Command Preview

| Task | What You Will Do |
|---|---|
| Indexing REPL | Access items by positive and negative index, trigger IndexError |
| Slicing REPL | Practice all slice forms including step and reverse |
| Mutating methods | Use append, insert, remove, pop, sort, reverse |
| sort vs. sorted trap | Observe None return from sort() in REPL |
| Alias vs. copy | Demonstrate the shared reference bug and three copy methods |
| List comprehensions | Build comprehensions with and without filter conditions |
| `grade_tracker.py` | Input-loop that builds a list, sorts it, and computes statistics |
| Nested list | Access 2D matrix elements with double indexing |

---

## 9. Supplemental Resources

**1. Official Python 3 Docs — More on Lists**
[https://docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
The official tutorial section on all list methods with concise descriptions and examples. The full method table covers `append`, `extend`, `insert`, `remove`, `pop`, `clear`, `index`, `count`, `sort`, `reverse`, and `copy`. Essential PCAP reference.

**2. Official Python 3 Docs — List Comprehensions**
[https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
Covers list comprehension syntax including nested comprehensions and filter conditions. Includes comparisons to equivalent `for` loop code — useful for understanding what the comprehension evaluates.

**3. Python for Everybody — Chapter 8: Lists**
[https://www.py4e.com/html3/08-lists](https://www.py4e.com/html3/08-lists)
Free textbook chapter covering lists, list methods, string splitting, parsing, and iteration. Includes exercises and self-check questions. The section on aliasing and references is particularly relevant to the copy/alias trap.

**4. Real Python — Python's list Data Type: A Deep Dive**
[https://realpython.com/python-list/](https://realpython.com/python-list/)
A comprehensive article covering list creation, indexing, slicing, methods, comprehensions, and performance considerations. Goes deeper than the exam requirements — good for students who want to understand the internal implementation.

**5. Real Python — When to Use a List Comprehension in Python**
[https://realpython.com/list-comprehension-python/](https://realpython.com/list-comprehension-python/)
Explains when list comprehensions are more readable than equivalent loops, when to avoid them (complex logic), and how they relate to generator expressions, `map()`, and `filter()`. Builds professional Python style habits.

---

## 9. Study Checklist

- [ ] Watch the Module 06 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially the methods table and return values.
- [ ] Work through the list comprehension tracing practice in Section 3.
- [ ] Work through the Common Error Patterns in Section 4.
- [ ] Read Chapter 8 of *Python for Everybody* at py4e.com.
- [ ] Read the More on Lists and List Comprehensions pages in the Official Python 3 Docs.
- [ ] Watch Episodes 10–11 of the Python for Everybody playlist.
- [ ] Review all 7 Certification Exam Tips in Section 5.
- [ ] Preview the lab tasks in Section 8.
- [ ] Proceed to the Module 06 Lab Activity.
