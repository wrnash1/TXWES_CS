# Reading Guide: Module 07 — Tuples, Sets, and Advanced Sorting

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 07 — Tuples, Sets, and Advanced Sorting**. This module completes Python's core built-in sequence and collection types. Tuples enforce immutability; sets enforce uniqueness; the `key` parameter and lambda functions unlock flexible sorting for complex data. The PCAP exam tests all of these concepts directly.

---

## 1. High-Yield Glossary

### Tuple

An ordered, **immutable** sequence enclosed in parentheses. Once created, a tuple cannot be modified — no item assignment, no append, no remove.

```python
point = (3, 7)
rgb = (255, 128, 0)
empty = ()
single = (42,)    # trailing comma required for single-item tuple
```

Tuples support indexing, negative indexing, slicing, `len()`, `in`, and iteration — the same read operations as lists. They do not support any mutating operations.

### Single-Item Tuple

A tuple with exactly one element **must** have a trailing comma. Without it, Python treats the parentheses as grouping, not as a tuple literal.

```python
>>> type((42))
<class 'int'>     # just a parenthesized integer
>>> type((42,))
<class 'tuple'>   # tuple with one element
```

This is one of the most frequently tested PCAP facts.

### Immutability

The property of not being modifiable after creation. Strings and tuples are immutable. Lists and dicts are mutable.

```python
t = (1, 2, 3)
t[0] = 99    # TypeError: 'tuple' object does not support item assignment
```

You can read from a tuple but cannot write to it.

### Tuple Packing

Creating a tuple by placing values separated by commas. Parentheses are optional.

```python
pair = 10, 20       # same as pair = (10, 20)
triple = 1, 2, 3
```

### Tuple Unpacking

Assigning a tuple's items to individual variables in a single statement. The number of variables must match the number of items.

```python
x, y = (3, 7)
name, score = ('Alice', 92)
a, b, c = (1, 2, 3)
```

**Extended unpacking with `*`:**

```python
first, *rest = (1, 2, 3, 4, 5)
# first = 1, rest = [2, 3, 4, 5]
```

### Tuple vs. List Comparison

| Feature | List | Tuple |
|---|---|---|
| Mutable | Yes | No |
| Ordered | Yes | Yes |
| Syntax | `[...]` | `(...)` |
| Can modify items | Yes | No |
| Can use as dict key | No | Yes |
| Use case | Dynamic collection | Fixed record |

### Set

An unordered collection of unique, hashable items enclosed in curly braces. Sets do not maintain insertion order and cannot contain duplicates.

```python
colors = {'red', 'green', 'blue'}
primes = {2, 3, 5, 7, 11}
```

**Creating a set from a list** (removes duplicates):

```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)    # {1, 2, 3}
```

**Empty set — must use `set()`, NOT `{}`:**

```python
empty_set = set()     # correct
empty_dict = {}       # this is an empty DICT, not a set
```

### Set Operators and Methods

| Operation | Operator | Method |
|---|---|---|
| Union (elements in either) | `a \| b` | `a.union(b)` |
| Intersection (elements in both) | `a & b` | `a.intersection(b)` |
| Difference (in a, not in b) | `a - b` | `a.difference(b)` |
| Symmetric difference (in one, not both) | `a ^ b` | `a.symmetric_difference(b)` |
| Is subset of | `a <= b` | `a.issubset(b)` |
| Is superset of | `a >= b` | `a.issuperset(b)` |

**Mutating methods:**

```python
s = {1, 2, 3}
s.add(4)           # add one element
s.remove(2)        # remove; raises KeyError if absent
s.discard(10)      # remove; no error if absent
s.pop()            # remove and return an arbitrary element
s.clear()          # remove all elements
```

### Lambda Function

A small anonymous function defined with the `lambda` keyword. Can have any number of parameters but only a single expression as its body.

```python
lambda parameters: expression
```

**Examples:**

```python
square = lambda x: x**2
square(5)    # 25

add = lambda x, y: x + y
add(3, 4)    # 7
```

Lambdas do not use `return` — the expression value is returned implicitly. Use lambdas for short one-off functions, especially as the `key` argument to `sorted()`. For reusable functions, use `def`.

### sorted() with key Parameter

The `key` parameter accepts a function that is called on each element to produce its sort key. Elements are ordered by their computed key, not by the elements themselves.

```python
words = ['banana', 'fig', 'apple', 'cherry']
sorted(words, key=len)
# ['fig', 'apple', 'banana', 'cherry']  — sorted by string length
```

**With a lambda key:**

```python
students = [('Alice', 88), ('Bob', 72), ('Carol', 95)]
sorted(students, key=lambda s: s[1])
# [('Bob', 72), ('Alice', 88), ('Carol', 95)]  — sorted by score
```

**Reverse sort:**

```python
sorted(students, key=lambda s: s[1], reverse=True)
# [('Carol', 95), ('Alice', 88), ('Bob', 72)]  — descending by score
```

### Set Comprehension

A comprehension that produces a set (unordered, unique results). Uses `{...}` with a `for` clause.

```python
squares = {x**2 for x in range(1, 6)}
# {1, 4, 9, 16, 25}

word_lengths = {len(w) for w in ['cat', 'dog', 'fish', 'bat']}
# {3, 4}  — only unique lengths
```

### Generator Expression

A comprehension that produces values lazily (one at a time, on demand) using parentheses. Does not build the full sequence in memory — useful for large data sets.

```python
gen = (x**2 for x in range(1000000))  # no memory allocated yet
total = sum(gen)                        # values computed as needed
```

---

## 2. Tuple Immutability — What It Means and What It Does Not Mean

A tuple is immutable, which means you cannot change the tuple object itself. However, if the tuple contains a mutable object (like a list), that mutable object can still be modified.

```python
t = ([1, 2], [3, 4])
t[0] = [9, 9]      # TypeError — cannot reassign tuple element
t[0].append(99)    # OK — modifying the LIST inside the tuple
t                  # ([1, 2, 99], [3, 4])
```

This is a subtle distinction. The tuple's slots cannot be reassigned, but if a slot holds a mutable object, that object's internal state can change.

---

## 3. Set Properties — PCAP Exam Reference

```python
s = {1, 2, 3, 3, 2}
# {1, 2, 3} — duplicates dropped silently

# Sets are unordered — do NOT assume any particular order
# You cannot index a set: s[0] raises TypeError

# Membership test is O(1) — much faster than list search for large data
1000 in set(range(10000))   # fast
1000 in list(range(10000))  # slower (scans from the beginning)
```

---

## 4. Lambda Tracing Practice

Predict the output of each expression before verifying:

**Expression 1:**

```python
f = lambda x: x * 3
f(4)
```

Result: `12`

**Expression 2:**

```python
g = lambda x, y: x if x > y else y
g(5, 8)
```

Result: `8` — the lambda returns the larger of the two values.

**Expression 3:**

```python
names = ['Charlie', 'Alice', 'Bob']
sorted(names, key=lambda n: n[-1])
```

Result: `['Alice', 'Charlie', 'Bob']` — sorted by the last character: `'e'`, `'e'`, `'b'`... wait, let me trace this. `'Charlie'[-1]='e'`, `'Alice'[-1]='e'`, `'Bob'[-1]='b'`. Sorting by last char: `'b' < 'e'`, so `'Bob'` comes first. Among `'Charlie'` and `'Alice'` with the same key `'e'`, Python maintains their original relative order (stable sort). Result: `['Bob', 'Charlie', 'Alice']`.

**Expression 4:**

```python
data = [(3, 'c'), (1, 'a'), (2, 'b')]
sorted(data, key=lambda x: x[0])
```

Result: `[(1, 'a'), (2, 'b'), (3, 'c')]` — sorted by the first element of each tuple.

---

## 5. Common Error Patterns to Memorize

**Pattern 1 — `(42)` is not a tuple:**

```python
t = (42)
type(t)    # int — forgot the trailing comma
```

Fix: `t = (42,)`

**Pattern 2 — Modifying a tuple raises TypeError:**

```python
t = (1, 2, 3)
t.append(4)    # AttributeError: 'tuple' object has no attribute 'append'
t[0] = 9       # TypeError: 'tuple' object does not support item assignment
```

**Pattern 3 — `{}` creates a dict, not a set:**

```python
s = {}
type(s)    # dict — NOT a set
s = set()  # correct empty set
```

**Pattern 4 — Sets have no order, cannot be indexed:**

```python
s = {3, 1, 2}
s[0]    # TypeError: 'set' object is not subscriptable
```

**Pattern 5 — `remove()` raises KeyError on missing element:**

```python
s = {1, 2, 3}
s.remove(5)    # KeyError: 5
s.discard(5)   # no error — use discard when unsure
```

---

## 6. Certification Exam Tips

**Tip 1 — Single-item tuple needs a comma.**
`(5,)` is a tuple. `(5)` is an integer. This is tested explicitly on the PCAP exam.

**Tip 2 — Tuples raise TypeError on modification.**
Any attempt to assign, append, insert, or remove from a tuple raises `TypeError` (item assignment) or `AttributeError` (no such method).

**Tip 3 — `{}` is always a dict literal, never an empty set.**
`{}` = empty dict. `set()` = empty set. `{1, 2, 3}` = set of three integers.

**Tip 4 — Sets discard duplicates silently.**
`set([1, 2, 2, 3])` = `{1, 2, 3}`. No error or warning is raised.

**Tip 5 — Lambda returns the expression, not a statement.**
`lambda x: x + 1` is valid. `lambda x: return x + 1` is a `SyntaxError` — lambdas do not use `return`.

**Tip 6 — sorted() with key= does not change the original.**
`sorted()` always returns a new list. The `key` function is called once per element to determine sort order but does not transform the output — the original elements appear in the result, sorted by their key values.

**Tip 7 — Set operators use symbols: `|`, `&`, `-`, `^`.**
Know what each produces. Union (`|`) = all elements in either set. Intersection (`&`) = only elements in both.

---

## 7. Beyond the Exam — Real-World Context

**Why use tuples instead of lists?**
Tuples communicate intent: "this data is a fixed record, do not modify it." A function returning `(latitude, longitude)` tells the caller these two values go together and neither should be changed. Tuples are also usable as dictionary keys (since they are immutable and hashable), while lists cannot be used as keys.

**Sets for deduplication in production.**
Converting a list to a set is the fastest way to remove duplicates in Python. This pattern appears in data pipelines, log analysis, database lookups, and user permission systems: `allowed = set(user.permissions) & set(required_permissions)`.

**Sorting in real applications.**
Production codebases sort complex objects by multiple criteria constantly. A leaderboard sorts by score descending, then by player name ascending for ties. An inventory system sorts by expiration date, then by quantity. The `key` parameter and `lambda` make these multi-criterion sorts clean and readable without having to write custom comparison logic.

---

## 8. Required Readings and Videos

**Required Reading — Chapter 10:**
Read Chapter 10 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). The chapter covers tuples and their role in Python programs.

**Required Reading — Official Python Docs:**
Read [Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) and [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets) in the official Python 3 tutorial. Also read the [Sorting How-To](https://docs.python.org/3/howto/sorting.html) guide.

**Required Video:**
Watch Episode 10 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance covers tuples and their use in Python.

---

## 9. Lab and Command Preview

| Task | What You Will Do |
|---|---|
| Tuple creation | Create tuples with and without trailing comma, observe types |
| Single-item tuple trap | Confirm `(42)` is int and `(42,)` is tuple |
| Tuple immutability | Attempt modification, observe TypeError |
| Tuple packing/unpacking | Pack values, unpack to variables, use in for loop |
| Set creation | Create sets, add/remove elements, test membership |
| Set operations | Practice union, intersection, difference, symmetric difference |
| Deduplication | Convert list with duplicates to set, then back to sorted list |
| Lambda functions | Write lambdas, use as key= in sorted() |
| Advanced sorting | Sort list of tuples by second element, then reverse |
| `roster_analyzer.py` | Full program using all module concepts |

---

## 10. Study Checklist

- [ ] Watch the Module 07 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially the single-item tuple rule and set operators.
- [ ] Work through the Lambda Tracing Practice in Section 4.
- [ ] Work through the Common Error Patterns in Section 5.
- [ ] Read Chapter 10 of *Python for Everybody* at py4e.com.
- [ ] Read the Tuples, Sets, and Sorting How-To pages in the Official Python 3 Docs.
- [ ] Watch Episode 10 of the Python for Everybody playlist.
- [ ] Review all 7 Certification Exam Tips in Section 6.
- [ ] Preview the lab tasks in Section 9.
- [ ] Proceed to the Module 07 Lab Activity.
