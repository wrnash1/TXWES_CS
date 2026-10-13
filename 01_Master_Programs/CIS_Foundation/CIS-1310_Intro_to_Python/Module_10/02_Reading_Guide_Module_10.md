# Reading Guide: Module 10 — Dictionaries

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

Welcome to **Module 10 — Dictionaries**. The dictionary is Python's most versatile and widely used data structure. Every time you work with JSON data from a web API, parse a configuration file, count word frequencies, or look up any value by a label rather than a position, you are using dictionary patterns.

The PCAP exam tests dictionaries extensively — more than any other data structure. You will need to know dictionary creation, key access (safe and unsafe), all major methods, all three iteration patterns, membership testing, comprehensions, and the word-frequency accumulator pattern.

This module builds directly on your knowledge of tuples (Module 07). Tuples appear inside dictionaries as both keys and as the pairs returned by `.items()`. Understanding both data structures together is essential for the exam.

---

## 1. High-Yield Glossary

### Dictionary

A **mutable**, **unordered** mapping that stores **key-value pairs**. Each key maps to exactly one value. Dictionaries are defined with curly braces and colons:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Dallas'}
```

Since Python 3.7, dictionaries maintain insertion order — keys come back in the order they were added. The PCAP exam does not test insertion-order behavior, but it is useful to know.

### Key

The identifier used to look up a value in a dictionary. Keys must be **unique** — you cannot have two entries with the same key. If you assign to an existing key, the old value is replaced.

Keys must be **hashable**:

| Type | Can be a key? | Why |
|---|---|---|
| `str` | Yes | Immutable and hashable |
| `int`, `float` | Yes | Immutable and hashable |
| `tuple` | Yes (if contents are hashable) | Immutable |
| `bool` | Yes (`True`/`False` are ints 1/0) | Immutable |
| `list` | **No** | Mutable — not hashable |
| `dict` | **No** | Mutable — not hashable |
| `set` | **No** | Mutable — not hashable |

```python
d = {(1, 2): 'tuple key works'}    # valid
d = {[1, 2]: 'list key fails'}     # TypeError: unhashable type: 'list'
```

### Value

The data associated with a key. Values have no restrictions — they can be any Python object: strings, numbers, lists, other dictionaries, functions, or any custom object.

### Key-Value Pair

A single entry in a dictionary — one key bound to one value. The `.items()` method returns an iterable of key-value pairs as tuples:

```python
grades = {'Alice': 92, 'Bob': 85}
list(grades.items())    # [('Alice', 92), ('Bob', 85)]
```

### Dictionary Creation

Three ways to create a dictionary:

```python
# Literal
d1 = {'a': 1, 'b': 2}

# dict() constructor with keyword arguments
d2 = dict(a=1, b=2)

# dict() from a list of key-value pairs
d3 = dict([('a', 1), ('b', 2)])
```

All three produce the same dictionary.

### Bracket Access — d[key]

The primary way to read a value. Raises `KeyError` if the key does not exist.

```python
grades = {'Alice': 92, 'Bob': 85}
print(grades['Alice'])    # 92
print(grades['Dave'])     # KeyError: 'Dave'
```

Use bracket access when you **expect** the key to exist and want an error if it does not.

### .get(key) and .get(key, default)

Safe lookup method. Returns `None` if the key is missing (never raises `KeyError`). Returns the default value if one is provided.

```python
print(grades.get('Dave'))          # None
print(grades.get('Dave', 0))       # 0
print(grades.get('Alice', 0))      # 92
```

Use `.get()` when the key might not exist and you want to handle that case gracefully.

**PCAP exam rule:** `d[key]` → `KeyError` if missing. `d.get(key)` → `None` if missing. `d.get(key, x)` → `x` if missing.

### Adding and Updating Entries

Assignment handles both:

```python
d = {'a': 1}
d['b'] = 2        # adds new key 'b'
d['a'] = 99       # updates existing key 'a'
```

There is no separate "insert" or "set" method for basic assignment.

### del d[key] and .pop()

```python
d = {'a': 1, 'b': 2, 'c': 3}

del d['a']              # removes 'a', raises KeyError if missing
val = d.pop('b')        # removes 'b' and RETURNS its value (2)
val = d.pop('z', -1)    # returns -1 if 'z' is missing — no KeyError
```

`.pop(key)` removes and returns. `.pop(key, default)` is safe for missing keys.

### .keys(), .values(), .items() — View Objects

These three methods return **view objects** — live, dynamic windows into the dictionary. They reflect any changes made to the dictionary after they were created.

```python
d = {'x': 10, 'y': 20}
k = d.keys()     # dict_keys(['x', 'y'])
d['z'] = 30
print(k)         # dict_keys(['x', 'y', 'z']) — automatically updated
```

| Method | Returns | Type |
|---|---|---|
| `.keys()` | All keys | `dict_keys` view |
| `.values()` | All values | `dict_values` view |
| `.items()` | All (key, value) tuples | `dict_items` view |

To get a plain list, wrap in `list()`: `list(d.keys())`.

### Iterating Over a Dictionary

Three standard patterns — memorize all three:

```python
d = {'name': 'Alice', 'grade': 92}

# Pattern 1 — keys only (default iteration)
for key in d:
    print(key)

# Pattern 2 — values only
for value in d.values():
    print(value)

# Pattern 3 — key-value pairs
for key, value in d.items():
    print(f'{key}: {value}')
```

The PCAP exam will show one of these patterns and ask what it prints.

### Membership Testing with in

`in` on a dictionary tests for membership in the **keys**:

```python
d = {'name': 'Alice', 'age': 30}
print('name' in d)          # True — key exists
print('Alice' in d)         # False — 'Alice' is a value, not a key
print('Alice' in d.values()) # True
```

This is a frequent exam trap. `'x' in d` tests keys. `'x' in d.values()` tests values.

### .update(other)

Merges `other` dictionary into the target dictionary in place. Existing keys are overwritten; new keys are added.

```python
config = {'color': 'blue', 'size': 'small'}
config.update({'color': 'red', 'weight': 10})
print(config)    # {'color': 'red', 'size': 'small', 'weight': 10}
```

### .setdefault(key, default)

Returns the value for a key. If the key does not exist, it **inserts** the key with the default value and returns the default. Useful for building dictionaries where missing keys should be initialized automatically.

```python
d = {}
d.setdefault('count', 0)    # inserts 'count': 0
d['count'] += 1
print(d)    # {'count': 1}
```

### Dictionary Comprehension

A concise way to build a dictionary from an iterable:

```python
{key_expr: value_expr for item in iterable}
{key_expr: value_expr for item in iterable if condition}
```

```python
squares = {n: n**2 for n in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

passing = {name: score for name, score in grades.items() if score >= 70}
```

### Nested Dictionary

A dictionary whose values are themselves dictionaries. This is how JSON data from APIs is typically structured.

```python
students = {
    'Alice': {'grade': 92, 'city': 'Dallas'},
    'Bob':   {'grade': 85, 'city': 'Austin'},
}

print(students['Alice']['grade'])    # 92 — double bracket access
```

### Word Frequency Counter (Accumulator Pattern)

The classic dictionary pattern on the PCAP exam:

```python
text = 'the fox the fox the dog'
words = text.split()

# Version 1 — explicit if/else
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Version 2 — using .get() (more Pythonic)
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)    # {'the': 3, 'fox': 2, 'dog': 1}
```

---

## 2. Dictionary Methods — Complete Reference Table

| Method | Description | Returns | Raises |
|---|---|---|---|
| `d[key]` | Read value | Value | `KeyError` if missing |
| `d[key] = v` | Add or update | Nothing | — |
| `d.get(key)` | Safe read | Value or `None` | Never |
| `d.get(key, x)` | Safe read with default | Value or `x` | Never |
| `del d[key]` | Delete key | Nothing | `KeyError` if missing |
| `d.pop(key)` | Remove and return | Value | `KeyError` if missing |
| `d.pop(key, x)` | Remove and return, safe | Value or `x` | Never |
| `d.keys()` | All keys (view) | `dict_keys` | — |
| `d.values()` | All values (view) | `dict_values` | — |
| `d.items()` | All (key, value) pairs (view) | `dict_items` | — |
| `d.update(other)` | Merge `other` into `d` | Nothing | — |
| `d.setdefault(key, x)` | Get or insert default | Value or `x` | — |
| `d.clear()` | Remove all entries | Nothing | — |
| `d.copy()` | Shallow copy | New dict | — |
| `len(d)` | Number of key-value pairs | `int` | — |
| `key in d` | Membership test (keys) | `bool` | — |

---

## 3. Common Error Patterns to Memorize

**Pattern 1 — KeyError from bracket access on missing key:**

```python
d = {'a': 1}
print(d['b'])    # KeyError: 'b'
```

Fix: Use `d.get('b')` or `d.get('b', default)`.

**Pattern 2 — Testing a value with `in` instead of a key:**

```python
d = {'name': 'Alice'}
print('Alice' in d)    # False — 'Alice' is a value, not a key
```

Fix: Use `'Alice' in d.values()` to test values.

**Pattern 3 — Using a list as a dictionary key:**

```python
d = {[1, 2]: 'value'}    # TypeError: unhashable type: 'list'
```

Fix: Use a tuple instead: `d = {(1, 2): 'value'}`.

**Pattern 4 — Modifying a dictionary while iterating over it:**

```python
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    if d[key] < 2:
        del d[key]    # RuntimeError: dictionary changed size during iteration
```

Fix: Iterate over a copy of the keys: `for key in list(d.keys()):`.

**Pattern 5 — Confusing `{}` with `set()`:**

```python
empty = {}
print(type(empty))    # <class 'dict'> — NOT a set
```

Fix: Use `set()` for an empty set.

---

## 4. Certification Exam Tips

**Tip 1 — KeyError vs None vs custom default.**
Three behaviors, one concept: `d['x']` → `KeyError` if missing; `d.get('x')` → `None` if missing; `d.get('x', 0)` → `0` if missing. Exam questions often ask which behavior a specific method produces.

**Tip 2 — `for k in d` iterates over keys, not key-value pairs.**
A common exam trap shows `for item in d:` and asks what `item` contains. The answer is a key, not a tuple. To get tuples, you must use `d.items()`.

**Tip 3 — `in` tests keys by default.**
`'x' in d` is equivalent to `'x' in d.keys()`. To test values, you must write `'x' in d.values()`. This distinction appears frequently on the exam.

**Tip 4 — `.items()` returns `(key, value)` tuples.**
When you write `for k, v in d.items():`, the unpacking happens because each item is a tuple. You could also write `for pair in d.items(): print(pair[0], pair[1])` — same result, less readable.

**Tip 5 — Dictionary comprehension produces a dict, not a list.**
`{k: v for ...}` produces a `dict`. `[x for ...]` produces a `list`. The curly braces with a colon in the expression make it a dict comprehension.

**Tip 6 — `.pop(key)` raises `KeyError` if key is missing, but `.pop(key, default)` does not.**
The two-argument form of `pop()` is the safe alternative — analogous to `.get()` for reading.

**Tip 7 — Word frequency counter is the classic PCAP dictionary question.**
Know both versions: the `if key in d` version and the `.get(key, 0) + 1` version. The exam may show either and ask for the output for a given input string.

---

## 5. Beyond the Exam — Real-World Context

**Dictionaries and JSON.**
The `json` module converts between Python dictionaries and JSON text in both directions. `json.loads(text)` parses a JSON string into a Python dict. `json.dumps(d)` converts a dict back to a JSON string. Every REST API interaction you will ever do in Python involves this conversion.

**Counting with collections.Counter.**
Python's `collections` module provides `Counter`, a specialized dictionary subclass that counts hashable objects automatically. `Counter(words)` builds a frequency dictionary in one call. This is the production-ready version of the manual word-counter loop — but the manual version is what the PCAP exam tests, and understanding the Counter requires understanding the pattern it replaces.

**Dictionaries as dispatch tables.**
You saw dispatch tables in Module 08's `calculator.py` — a dictionary where keys are operator symbols and values are function objects. This pattern replaces `if-elif` chains and is used extensively in parsers, state machines, and command routers.

**Configuration management.**
Real applications store settings in dictionaries loaded from `.json`, `.yaml`, or `.toml` config files. Understanding dictionary access patterns is not optional — it is the foundation of how Python applications are configured.

---

## 6. Required Readings and Videos

**Required Reading — Chapter 9:**
Read Chapter 9 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). This chapter covers dictionaries with word-counting examples that directly mirror PCAP exam questions.

**Required Reading — Official Python Docs:**
Read [Data Structures — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) and the [Mapping Types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) reference for a complete list of all dictionary methods.

**Supplemental Video:**
Watch Episodes 9 and 10 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance builds word-counting programs that are the exact pattern tested on the PCAP exam.

---

## 7. Supplemental Resources

**1. Official Python 3 Docs — Mapping Types: dict**
[https://docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
The complete reference for all dictionary methods with signatures, return types, and exception behavior. Covers `.get()`, `.pop()`, `.setdefault()`, `.update()`, `.items()`, `.keys()`, `.values()`, and the merge/update operators `|` and `|=` added in Python 3.9.

**2. Official Python 3 Docs — Data Structures: Dictionaries**
[https://docs.python.org/3/tutorial/datastructures.html#dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
The tutorial section on dictionaries with examples of all three iteration patterns, dictionary comprehensions, and `dict()` constructor usage. Written for new Python programmers and directly aligned with PCAP exam content.

**3. Python for Everybody — Chapter 9: Dictionaries**
[https://www.py4e.com/html3/09-dictionaries](https://www.py4e.com/html3/09-dictionaries)
Free textbook chapter with step-by-step word-frequency counter examples, histogram construction, and loop-based patterns. Includes self-check exercises. The word-counter pattern in this chapter matches the classic PCAP exam question format exactly.

**4. Real Python — Dictionaries in Python**
[https://realpython.com/python-dicts/](https://realpython.com/python-dicts/)
A comprehensive free article covering dict creation, all methods, iteration, comprehensions, nested dictionaries, and `OrderedDict`/`Counter`/`defaultdict` from `collections`. The sections on `.setdefault()` and dict comprehensions are particularly relevant to PCAP exam preparation.

**5. Real Python — How to Iterate Through a Dictionary in Python**
[https://realpython.com/iterate-through-dictionary-python/](https://realpython.com/iterate-through-dictionary-python/)
Focused article on all iteration patterns: keys, values, `.items()`, filtered iteration, and dictionary comprehensions. Includes comparison tables and performance notes. Directly relevant to the three PCAP-tested iteration patterns.

---

## 8. Study Checklist

- [ ] Watch the Module 10 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially `.get()` vs bracket access, iteration patterns, and `in` membership testing.
- [ ] Work through the Dictionary Methods reference table — know what each method returns and when it raises errors.
- [ ] Memorize both versions of the word frequency counter.
- [ ] Work through the 5 Common Error Patterns — run each one in the REPL and observe the error.
- [ ] Read Chapter 9 of *Python for Everybody* at py4e.com.
- [ ] Read the Data Structures — Dictionaries page in the official Python 3 docs.
- [ ] Review all 7 Certification Exam Tips in Section 4.
- [ ] Proceed to the Module 10 Lab Activity.
