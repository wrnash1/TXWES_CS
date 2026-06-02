# Video Script: CIS-1310 — Introduction to Python

## Module 10 — Dictionaries

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - Show the phone book / contact list analogy on a slide before the first demo.
> - Emphasize the KeyError vs `.get()` distinction — this is a guaranteed PCAP exam topic.
> - Run the word_counter.py demo live so students see the accumulator pattern emerge naturally.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 09 | Dictionaries | CIS-1310"]**

"Welcome back. In Module 07 we covered tuples and sets. In Module 09 we explored scopes and recursion. Now we arrive at one of Python's most used and most powerful data structures — the **dictionary**.

Dictionaries are everywhere. JSON data from web APIs is a dictionary. Configuration files are dictionaries. Every Python object's attributes are stored in a dictionary under the hood. The PCAP exam tests dictionary creation, all the key access methods, iteration patterns, comprehensions, and the difference between a missing-key error and a safe lookup.

Let's work through all of it."

---

## [00:45 – 03:00] Creating Dictionaries

**[SHOW SLIDE: "Dictionaries — Key-Value Pairs"]**

"A **dictionary** maps **keys** to **values**. Think of it like a contact list — each contact name is a key, and the phone number is the value. Looking up a contact by name is instant — you do not scan from the top, you go directly to the name.

**[DEMO]**

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

**[DEMO — dict() constructor]**

```python
# dict() constructor with keyword arguments
config = dict(host='localhost', port=5432, debug=True)
print(config)
```

Output:

```text
{'host': 'localhost', 'port': 5432, 'debug': True}
```

**[DEMO — empty dictionary]**

```python
empty = {}
print(type(empty))    # <class 'dict'> — NOT a set
```

[PAUSE]

An important reminder from Module 07 — `{}` creates an empty **dictionary**, not an empty set. `set()` creates an empty set. This distinction appears on the PCAP exam.

**Keys must be hashable** — strings, integers, floats, and tuples work as keys. Lists and dictionaries cannot be keys because they are mutable and therefore not hashable."

---

## [03:00 – 05:30] Reading, Adding, and Updating Values

**[SHOW SLIDE: "CRUD Operations on Dictionaries"]**

"Once you have a dictionary, you need to read values, add new keys, update existing keys, and delete keys. Python's dictionary supports all four operations cleanly.

**[DEMO — reading values]**

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

**[DEMO — KeyError]**

```python
print(grades['Dave'])
```

Output:

```text
KeyError: 'Dave'
```

The safe alternative is `.get()`:

**[DEMO — .get()]**

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

**[DEMO — adding and updating]**

```python
grades['Dave'] = 90        # add new key
grades['Alice'] = 95       # update existing key
print(grades)
```

Output:

```text
{'Alice': 95, 'Bob': 85, 'Carol': 78, 'Dave': 90}
```

Assignment adds a new key if it does not exist, or overwrites the value if it does. There is no separate `add` method — the same syntax handles both cases."

---

## [05:30 – 07:00] Deleting Keys

**[SHOW SLIDE: "Removing Keys — del, pop, clear"]**

"Three ways to remove entries from a dictionary:

**[DEMO]**

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

[PAUSE]

`pop()` is especially useful when you need the value AND want to remove the key in one operation. It is the dictionary equivalent of `list.pop()` — except you pop by key, not by index."

---

## [07:00 – 09:30] Dictionary Methods and Iteration

**[SHOW SLIDE: "keys(), values(), items() — View Objects"]**

"Dictionaries have three essential iteration methods. Each returns a **view object** — a live window into the dictionary that updates automatically if the dictionary changes.

**[DEMO — keys, values, items]**

```python
student = {'name': 'Alice', 'grade': 92, 'city': 'Dallas'}

print(student.keys())     # dict_keys(['name', 'grade', 'city'])
print(student.values())   # dict_values(['Alice', 92, 'Dallas'])
print(student.items())    # dict_items([('name', 'Alice'), ('grade', 92), ('city', 'Dallas')])
```

**[DEMO — iterating]**

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

[PAUSE]

Memorize this: `for k in d` gives you keys. `for v in d.values()` gives you values. `for k, v in d.items()` gives you both. The PCAP exam will show you a loop and ask what it prints — knowing which iteration pattern produces which output is essential.

**[DEMO — membership testing]**

```python
print('name' in student)     # True — tests KEYS
print('Alice' in student)    # False — 'Alice' is a value, not a key
print('Alice' in student.values())    # True
```

`in` on a dictionary tests for membership in the **keys**. To test values, you must use `in student.values()`."

---

## [09:30 – 11:00] Dictionary Comprehensions

**[SHOW SLIDE: "Dictionary Comprehensions"]**

"Just like list comprehensions build lists, **dictionary comprehensions** build dictionaries in one expression.

Syntax: `{key_expression: value_expression for item in iterable}`

**[DEMO — basic comprehension]**

```python
squares = {n: n**2 for n in range(1, 6)}
print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**[DEMO — comprehension with filter]**

```python
grades = {'Alice': 92, 'Bob': 65, 'Carol': 78, 'Dave': 55, 'Eve': 88}

passing = {name: score for name, score in grades.items() if score >= 70}
print(passing)
```

Output:

```text
{'Alice': 92, 'Carol': 78, 'Eve': 88}
```

**[DEMO — inverting a dictionary]**

```python
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)
```

Output:

```text
{1: 'a', 2: 'b', 3: 'c'}
```

[PAUSE]

Dictionary comprehensions follow the same logic as list comprehensions — iterable, optional filter, expression for the key, expression for the value. They are concise and readable once the pattern is familiar."

---

## [11:00 – 13:00] Nested Dictionaries and Word Counter

**[SHOW SLIDE: "Nested Dictionaries and the Accumulator Pattern"]**

"Dictionaries can contain dictionaries as values. This is how JSON data from APIs is typically structured.

**[DEMO — nested dict]**

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

**[DEMO — word frequency counter]**

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

[PAUSE]

This is the most important dictionary pattern on the PCAP exam. Walk through it: if the word is already a key, increment its count. If it is new, initialize the count to 1.

There is a cleaner version using `.get()`:

```python
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
```

Same result, one line. `.get(word, 0)` returns 0 if the word is new, or the current count if it exists. Then add 1 and assign back."

---

## [13:00 – 14:15] update() and Merging Dictionaries

**[SHOW SLIDE: "Merging Dictionaries — update() and **unpacking"]**

"**[DEMO]**

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

Both create a new dictionary rather than modifying either original."

---

## [14:15 – 15:00] PCAP Exam Tips and Wrap-Up

**[SHOW SLIDE: "Module 10 — PCAP Alignment"]**

"Key exam take-aways:

**1.** `d[key]` raises `KeyError` for missing keys. `d.get(key)` returns `None`. `d.get(key, default)` returns your default.

**2.** `for k in d` iterates over **keys** only. Use `.items()` for key-value pairs.

**3.** `key in d` tests membership in **keys**. `value in d.values()` tests membership in values.

**4.** Dictionary comprehension syntax: `{k: v for k, v in iterable if condition}`.

**5.** Dictionary keys must be **hashable** — strings, ints, tuples. Lists and dicts cannot be keys.

**6.** `.pop(key)` removes and returns the value. `.pop(key, default)` never raises `KeyError`.

**7.** `{}` is an empty dictionary, not an empty set. Use `set()` for an empty set.

Module 11 covers string methods — Python's deep library of built-in tools for working with text. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 10 — Dictionaries]**

---

## Additional Resources

- [Python for Everybody — Chapter 9 (Dictionaries)](https://www.py4e.com/book) — Dr. Severance's dictionary chapter with word-counting examples
- [Official Python Docs — Mapping Types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) — complete dictionary method reference
- [Official Python Docs — Data Structures — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) — tutorial introduction
- [Real Python — Dictionaries in Python](https://realpython.com/python-dicts/) — in-depth guide with examples
