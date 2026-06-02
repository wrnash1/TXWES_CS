# Video Script: CIS-1310 — Introduction to Python

## Module 06 — Lists: The Workhorse Data Structure

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - Demonstrate negative indexing by drawing the list with both positive and negative indices on the slide before running the demo.
> - Show the mutability distinction by demonstrating in-place modification vs. reassignment side by side.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 06 | Lists: The Workhorse Data Structure | CIS-1310"]**

"Welcome back. In every module so far, our programs have worked with one value at a time — one score, one name, one number. But real programs work with collections of data: a class roster, a list of prices, a set of sensor readings.

Python's primary tool for ordered collections is the **list**. Lists are arguably the most-used data structure in Python — you will use them in virtually every program you write from this point forward. They are flexible, powerful, and have a rich set of built-in operations that the PCAP exam tests extensively.

This module also introduces **list comprehensions** — a compact, Pythonic way to build lists in a single expression — and covers the core list methods you need to know. Let's go."

---

## [00:45 – 02:30] Creating and Accessing Lists

**[SHOW SLIDE: "Lists — Ordered, Mutable Sequences"]**

"A **list** is an ordered, mutable sequence of items. 'Ordered' means the items have a defined position. 'Mutable' means you can change the contents after creating the list.

You create a list with square brackets:

```python
>>> grades = [88, 72, 95, 61, 83]
>>> names = ['Alice', 'Bob', 'Carol']
>>> mixed = [42, 'hello', 3.14, True]
>>> empty = []
```

Lists can hold any Python value — and they can mix types (though it is usually cleaner to keep one type per list).

### Indexing — Accessing Individual Items

Access items by their **index** — their position in the list, starting at 0.

**[DEMO]**

```python
>>> grades = [88, 72, 95, 61, 83]
>>> grades[0]
88
>>> grades[1]
72
>>> grades[4]
83
```

**Negative indexing** — count from the end:

```python
>>> grades[-1]
83
>>> grades[-2]
61
>>> grades[-5]
88
```

`grades[-1]` is always the last item regardless of list length. This is far more readable than `grades[len(grades) - 1]`.

**IndexError if you go out of bounds:**

```python
>>> grades[10]
IndexError: list index out of range
```

Know your list's length. `len(grades)` tells you — valid indices run from `0` to `len(grades) - 1`."

---

## [02:30 – 04:30] Slicing

**[SHOW SLIDE: "Slicing — Extracting Sublists"]**

"Slicing extracts a portion of a list and returns a new list. The syntax mirrors `range()`: `start:stop:step` — and `stop` is always excluded.

**[DEMO]**

```python
>>> grades = [88, 72, 95, 61, 83]
>>> grades[1:3]
[72, 95]
>>> grades[0:2]
[88, 72]
>>> grades[2:]
[95, 61, 83]
>>> grades[:3]
[88, 72, 95]
>>> grades[:]
[88, 72, 95, 61, 83]
```

`grades[2:]` means 'from index 2 to the end.' `grades[:3]` means 'from the beginning up to but not including index 3.' `grades[:]` creates a copy of the entire list.

**Step in slices:**

```python
>>> grades[::2]
[88, 95, 83]
>>> grades[::-1]
[83, 61, 95, 72, 88]
```

`grades[::-1]` reverses the list — a common Python idiom. Step -1 walks the list from the end to the beginning."

---

## [04:30 – 06:15] Mutability — Modifying Lists

**[SHOW SLIDE: "Mutability — Lists Can Be Changed in Place"]**

"Unlike strings — which are immutable — lists can be modified after creation. You can change an item, add items, or remove items from an existing list object.

**[DEMO — item assignment]**

```python
>>> grades = [88, 72, 95, 61, 83]
>>> grades[1] = 79
>>> grades
[88, 79, 95, 61, 83]
```

**Key list methods:**

```python
>>> grades.append(90)    # add to the end
>>> grades
[88, 79, 95, 61, 83, 90]

>>> grades.insert(0, 100)    # insert at index 0
>>> grades
[100, 88, 79, 95, 61, 83, 90]

>>> grades.remove(61)    # remove first occurrence of 61
>>> grades
[100, 88, 79, 95, 83, 90]

>>> grades.pop()    # remove and return the last item
90
>>> grades
[100, 88, 79, 95, 83]

>>> grades.pop(0)    # remove and return item at index 0
100
>>> grades
[88, 79, 95, 83]
```

**Sorting:**

```python
>>> grades.sort()    # in-place sort (modifies the list)
>>> grades
[79, 83, 88, 95]

>>> grades.sort(reverse=True)    # descending
>>> grades
[95, 88, 83, 79]

>>> sorted(grades)    # returns NEW sorted list, original unchanged
[79, 83, 88, 95]
>>> grades    # still in descending order
[95, 88, 83, 79]
```

The distinction between `list.sort()` (modifies the original) and `sorted(list)` (returns a new list) is tested on the PCAP exam."

---

## [06:15 – 07:30] List Methods — Full Reference

**[SHOW SLIDE: "Core List Methods"]**

"Here are the methods you must know for the PCAP exam:

| Method | What it does | Returns |
|---|---|---|
| `append(x)` | Add `x` to the end | `None` |
| `insert(i, x)` | Insert `x` at index `i` | `None` |
| `remove(x)` | Remove first occurrence of `x` | `None` |
| `pop(i)` | Remove and return item at index `i` | The removed item |
| `sort()` | Sort in place | `None` |
| `reverse()` | Reverse in place | `None` |
| `index(x)` | Return index of first occurrence of `x` | int |
| `count(x)` | Count occurrences of `x` | int |
| `extend(lst)` | Append all items from `lst` | `None` |
| `clear()` | Remove all items | `None` |
| `copy()` | Return a shallow copy | new list |

A critical PCAP trap: methods like `append()`, `sort()`, and `reverse()` return `None`. Assigning them: `new_list = my_list.sort()` gives you `None`, not the sorted list."

---

## [07:30 – 09:00] List Operations — in, len, +, *

**[SHOW SLIDE: "List Operators"]**

**[DEMO]**

```python
>>> grades = [88, 72, 95, 61, 83]
>>> len(grades)
5

>>> 95 in grades
True
>>> 100 in grades
False

>>> 100 not in grades
True

>>> [1, 2] + [3, 4]
[1, 2, 3, 4]

>>> [0] * 5
[0, 0, 0, 0, 0]
```

`in` tests membership — it works on lists, strings, and other sequences. `+` concatenates two lists into a new one. `*` repeats a list — `[0] * 5` is a quick way to create a fixed-size list initialized to zero."

---

## [09:00 – 11:00] List Comprehensions

**[SHOW SLIDE: "List Comprehensions — Build Lists in One Expression"]**

"A **list comprehension** creates a new list by applying an expression to each item in an iterable. It is the most Pythonic way to transform or filter a list.

**Syntax:**

```python
[expression for variable in iterable]
[expression for variable in iterable if condition]
```

**[DEMO — basic comprehension]**

```python
>>> squares = [x**2 for x in range(1, 6)]
>>> squares
[1, 4, 9, 16, 25]
```

This replaces:

```python
squares = []
for x in range(1, 6):
    squares.append(x**2)
```

Same result, more readable.

**[DEMO — comprehension with filter]**

```python
>>> evens = [x for x in range(10) if x % 2 == 0]
>>> evens
[0, 2, 4, 6, 8]
```

**[DEMO — transform a list]**

```python
>>> grades = [88, 72, 95, 61, 83]
>>> curved = [g + 5 for g in grades]
>>> curved
[93, 77, 100, 66, 88]
```

**[DEMO — filter and transform]**

```python
>>> passing = [g for g in grades if g >= 60]
>>> passing
[88, 72, 95, 61, 83]
```

List comprehensions are concise, readable, and faster than equivalent `for` loops in many cases. They are tested on the PCAP exam — know how to read and trace them."

---

## [11:00 – 12:15] Copying Lists — Shallow vs. Deep

**[SHOW SLIDE: "Copying Lists — The Assignment Trap"]**

"This is one of the most common list bugs, and it appears on the PCAP exam.

**[DEMO]**

```python
>>> original = [1, 2, 3]
>>> alias = original    # alias points to the SAME list
>>> alias.append(4)
>>> original
[1, 2, 3, 4]
```

`alias = original` does NOT create a new list. Both variables point to the same list object. Modifying through `alias` modifies `original`.

To get a true copy:

```python
>>> original = [1, 2, 3]
>>> copy1 = original[:]          # slice copy
>>> copy2 = original.copy()      # .copy() method
>>> copy3 = list(original)       # list() constructor

>>> copy1.append(99)
>>> original    # unchanged
[1, 2, 3]
```

Any of these three methods creates a new independent list. The `id()` function confirms they are different objects:

```python
>>> id(original)
140234567890
>>> id(copy1)
140234567912
```

Different memory addresses — different objects."

---

## [12:15 – 13:30] Nested Lists

**[SHOW SLIDE: "Nested Lists — Lists Inside Lists"]**

"Lists can contain other lists. A nested list is commonly used to represent a table or grid.

**[DEMO]**

```python
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>> matrix[0]
[1, 2, 3]
>>> matrix[1][2]
6
>>> matrix[2][0]
7
```

`matrix[1][2]` means: take item at index 1 from `matrix` (which is `[4, 5, 6]`), then take item at index 2 from that (which is `6`).

Nested lists are iterable:

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

This nested loop pattern is the foundation of 2D data processing — grids, game boards, pixel arrays."

---

## [13:30 – 14:30] Putting It Together — Student Grade Tracker

**[DEMO — live code]**

"Let me build a grade tracker using everything from this module:

```python
# grade_tracker.py
# Module 06 Lab — CIS-1310

scores = []
print('Enter student scores (type -1 to finish):')

while True:
    score = int(input('  Score: '))
    if score == -1:
        break
    if 0 <= score <= 100:
        scores.append(score)
    else:
        print('  Ignored — out of range.')

if scores:
    scores.sort()
    total = sum(scores)
    average = total / len(scores)

    print(f'\n  Scores (sorted): {scores}')
    print(f'  Count:  {len(scores)}')
    print(f'  Total:  {total}')
    print(f'  Avg:    {average:.2f}')
    print(f'  High:   {scores[-1]}')
    print(f'  Low:    {scores[0]}')
else:
    print('No valid scores entered.')
```

This program dynamically builds a list with `append()`, sorts it in place, uses negative indexing to get min/max after sorting, and uses `sum()` — a built-in that works on any numeric list."

---

## [14:30 – 15:15] PCAP Exam Tips and Wrap-Up

**[SHOW SLIDE: "Module 06 — PCAP Alignment"]**

"Key exam take-aways:

**1.** List indices start at 0. Valid range: 0 to `len(list) - 1`. Negative indices count from the end — `-1` is the last item.

**2.** Slicing: `stop` is excluded. `list[1:3]` gives items at index 1 and 2, not 3.

**3.** `list.sort()` modifies in place and returns `None`. `sorted(list)` returns a new list.

**4.** Methods like `append()`, `insert()`, `remove()`, `reverse()` return `None` — do not assign their return value.

**5.** `alias = original` creates a reference, not a copy. Modifications through `alias` affect `original`.

**6.** List comprehension syntax: `[expr for var in iterable]` and `[expr for var in iterable if condition]`.

**7.** `in` tests membership. `len()` returns element count. `+` concatenates. `*` repeats.

Module 07 covers advanced list operations — sorting with key functions, list comprehensions in depth, and introduces tuples and sets. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 06 — Lists: The Workhorse Data Structure]**

---

## Additional Resources

- [Python for Everybody — Chapter 8](https://www.py4e.com/book) — Lists
- [Official Python Docs — Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Official Python Docs — List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Python for Everybody Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Episodes 10–11 (Lists)
