# Video Script: CIS-1310 — Introduction to Python

## Module 10 — Dictionaries

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / Python Institute &bull; Python Programming Full Course &bull; Module 10</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=rfscVS0vtbw" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/rfscVS0vtbw" title="freeCodeCamp / Python Institute &bull; Python Programming Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp / Python Institute &bull; Python Programming Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Opening

Welcome back. In Module 07 we covered tuples and sets. In Module 09 we explored scopes and recursion. Now we arrive at one of Python's most used and most powerful data structures — the **dictionary**.

Dictionaries are everywhere. JSON data from web APIs is a dictionary. Configuration files are dictionaries. Every Python object's attributes are stored in a dictionary under the hood. The PCAP exam tests dictionary creation, all the key access methods, iteration patterns, comprehensions, and the difference between a missing-key error and a safe lookup.

Let's work through all of it.

---

## Creating Dictionaries

A **dictionary** maps **keys** to **values**. Think of it like a contact list — each contact name is a key, and the phone number is the value. Looking up a contact by name is instant — you do not scan from the top, you go directly to the name.

```python
# Literal syntax — curly braces, colon separates key from value
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'Dallas'
}

print(person)
print(type(person))
print(len(person))
```

Output:

```text
{'name': 'Alice', 'age': 30, 'city': 'Dallas'}
<class 'dict'>
3
```

```python
# dict() constructor with keyword arguments
config = dict(host='localhost', port=5432, debug=True)
print(config)
```

Output:

```text
{'host': 'localhost', 'port': 5432, 'debug': True}
```

```python
empty = {}
print(type(empty))    # <class 'dict'> — NOT a set
```

An important reminder from Module 07 — `{}` creates an empty **dictionary**, not an empty set. `set()` creates an empty set. This distinction appears on the PCAP exam.

**Keys must be hashable** — strings, integers, floats, and tuples work as keys. Lists and dictionaries cannot be keys because they are mutable and therefore not hashable.

---

## Reading, Adding, and Updating Values

Once you have a dictionary, you need to read values, add new keys, update existing keys, and delete keys. Python's dictionary supports all four operations cleanly.

```python
grades = {'Alice': 92, 'Bob': 85, 'Carol': 78}

print(grades['Alice'])    # 92
print(grades['Bob'])      # 85
```

Output:

```text
92
85
```

Bracket notation reads a value by key. If the key does not exist, Python raises `KeyError`.

```python
print(grades['Dave'])
```

Output:

```text
KeyError: 'Dave'
```

The safe alternative is `.get()`:

```python
print(grades.get('Dave'))          # None — key missing, no crash
print(grades.get('Dave', 0))       # 0 — custom default
print(grades.get('Alice', 0))      # 92 — key exists, returns value
```

Output:

```text
None
0
92
```

`d.get(key)` returns `None` for missing keys. `d.get(key, default)` returns your chosen default. Neither raises `KeyError`. This is a critical PCAP distinction — know when to use bracket notation versus `.get()`.

```python
grades['Dave'] = 90        # add new key
grades['Alice'] = 95       # update existing key
print(grades)
```

Output:

```text
{'Alice': 95, 'Bob': 85, 'Carol': 78, 'Dave': 90}
```

Assignment adds a new key if it does not exist, or overwrites the value if it does. There is no separate `add` method — the same syntax handles both cases.

---

## Deleting Keys

Three ways to remove entries from a dictionary:

```python
scores = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# del — removes the key, raises KeyError if missing
del scores['a']
print(scores)    # {'b': 20, 'c': 30, 'd': 40}

# pop() — removes and RETURNS the value
removed = scores.pop('b')
print(removed)   # 20
print(scores)    # {'c': 30, 'd': 40}

# pop() with default — no KeyError if missing
result = scores.pop('z', 'not found')
print(result)    # not found

# clear() — removes all keys
scores.clear()
print(scores)    # {}
```

`pop()` is especially useful when you need the value AND want to remove the key in one operation. It is the dictionary equivalent of `list.pop()` — except you pop by key, not by index.

---

## Dictionary Methods and Iteration

Dictionaries have three essential iteration methods. Each returns a **view object** — a live window into the dictionary that updates automatically if the dictionary changes.

```python
student = {'name': 'Alice', 'grade': 92, 'city': 'Dallas'}

print(student.keys())     # dict_keys(['name', 'grade', 'city'])
print(student.values())   # dict_values(['Alice', 92, 'Dallas'])
print(student.items())    # dict_items([('name', 'Alice'), ('grade', 92), ('city', 'Dallas')])
```

```python
# Keys only (default loop behavior)
for key in student:
    print(key)

print()

# Values only
for value in student.values():
    print(value)

print()

# Key-value pairs
for key, value in student.items():
    print(f'{key}: {value}')
```

Output:

```text
name
grade
city

Alice
92
Dallas

name: Alice
grade: 92
city: Dallas
```

Memorize this: `for k in d` gives you keys. `for v in d.values()` gives you values. `for k, v in d.items()` gives you both. The PCAP exam will show you a loop and ask what it prints — knowing which iteration pattern produces which output is essential.

```python
print('name' in student)     # True — tests KEYS
print('Alice' in student)    # False — 'Alice' is a value, not a key
print('Alice' in student.values())    # True
```

`in` on a dictionary tests for membership in the **keys**. To test values, you must use `in student.values()`.

---

## Dictionary Comprehensions

Just like list comprehensions build lists, **dictionary comprehensions** build dictionaries in one expression.

Syntax: `{key_expression: value_expression for item in iterable}`

```python
squares = {n: n**2 for n in range(1, 6)}
print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
grades = {'Alice': 92, 'Bob': 65, 'Carol': 78, 'Dave': 55, 'Eve': 88}

passing = {name: score for name, score in grades.items() if score >= 70}
print(passing)
```

Output:

```text
{'Alice': 92, 'Carol': 78, 'Eve': 88}
```

```python
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)
```

Output:

```text
{1: 'a', 2: 'b', 3: 'c'}
```

Dictionary comprehensions follow the same logic as list comprehensions — iterable, optional filter, expression for the key, expression for the value. They are concise and readable once the pattern is familiar.

---

## Nested Dictionaries and Word Counter

Dictionaries can contain dictionaries as values. This is how JSON data from APIs is typically structured.

```python
students = {
    'Alice': {'grade': 92, 'city': 'Dallas'},
    'Bob':   {'grade': 85, 'city': 'Austin'},
}

print(students['Alice']['grade'])    # 92
print(students['Bob']['city'])       # Austin

# Add a new nested record
students['Carol'] = {'grade': 78, 'city': 'Houston'}
print(len(students))    # 3
```

The classic dictionary problem: count how many times each word appears in a string.

```python
text = 'the quick brown fox jumps over the lazy dog the fox'
words = text.split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)
```

Output:

```text
{'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
```

This is the most important dictionary pattern on the PCAP exam. Walk through it: if the word is already a key, increment its count. If it is new, initialize the count to 1.

There is a cleaner version using `.get()`:

```python
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
```

Same result, one line. `.get(word, 0)` returns 0 if the word is new, or the current count if it exists. Then add 1 and assign back.

---

## update() and Merging Dictionaries

"

```python
defaults = {'color': 'blue', 'size': 'medium', 'font': 'Arial'}
overrides = {'color': 'red', 'size': 'large'}

defaults.update(overrides)    # merges overrides INTO defaults
print(defaults)
```

Output:

```text
{'color': 'red', 'size': 'large', 'font': 'Arial'}
```

`update()` modifies the dictionary in place. Existing keys are overwritten; new keys are added.

Python 3.9+ also supports the `|` merge operator:

```python
result = defaults | overrides    # creates a NEW dict
```

For older Python, use double-star unpacking:

```python
result = {**defaults, **overrides}
```

Both create a new dictionary rather than modifying either original.

---

## PCAP Exam Tips and Wrap-Up

Key exam take-aways:

**1.** `d[key]` raises `KeyError` for missing keys. `d.get(key)` returns `None`. `d.get(key, default)` returns your default.

**2.** `for k in d` iterates over **keys** only. Use `.items()` for key-value pairs.

**3.** `key in d` tests membership in **keys**. `value in d.values()` tests membership in values.

**4.** Dictionary comprehension syntax: `{k: v for k, v in iterable if condition}`.

**5.** Dictionary keys must be **hashable** — strings, ints, tuples. Lists and dicts cannot be keys.

**6.** `.pop(key)` removes and returns the value. `.pop(key, default)` never raises `KeyError`.

**7.** `{}` is an empty dictionary, not an empty set. Use `set()` for an empty set.

Module 11 covers string methods — Python's deep library of built-in tools for working with text. See you there.

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 10 — Dictionaries]**

---

## Additional Resources

- [Python for Everybody — Chapter 9 (Dictionaries)](https://www.py4e.com/book) — Dr. Severance's dictionary chapter with word-counting examples
- [Official Python Docs — Mapping Types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) — complete dictionary method reference
- [Official Python Docs — Data Structures — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) — tutorial introduction
- [Real Python — Dictionaries in Python](https://realpython.com/python-dicts/) — in-depth guide with examples
