# Lab Activity: Module 10 — Dictionaries

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 75–90 minutes

---

## Overview

In this lab you will create dictionaries using literal and constructor syntax, perform all four CRUD operations (create, read, update, delete), compare bracket access versus `.get()`, practice all three iteration patterns, observe membership testing behavior, write dictionary comprehensions, build a word frequency counter, and create a nested dictionary program for student records.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module10
cd module10
```

---

## Part 1 — Creating Dictionaries and Basic Access

```bash
python3
```

### Step 1.1 — Literal Syntax

```python
>>> person = {'name': 'Alice', 'age': 30, 'city': 'Dallas'}
>>> print(person)
{'name': 'Alice', 'age': 30, 'city': 'Dallas'}
>>> type(person)
<class 'dict'>
>>> len(person)
3
```

### Step 1.2 — dict() Constructor

```python
>>> config = dict(host='localhost', port=5432, debug=True)
>>> config
{'host': 'localhost', 'port': 5432, 'debug': True}
```

### Step 1.3 — Empty Dictionary vs Empty Set

```python
>>> empty_dict = {}
>>> type(empty_dict)
<class 'dict'>
>>> empty_set = set()
>>> type(empty_set)
<class 'set'>
```

`{}` always creates an empty dictionary. `set()` creates an empty set.

### Step 1.4 — Reading Values with Bracket Notation

```python
>>> grades = {'Alice': 92, 'Bob': 85, 'Carol': 78}
>>> grades['Alice']
92
>>> grades['Bob']
85
```

### Step 1.5 — KeyError for Missing Keys

```python
>>> grades['Dave']
```

Expected:

```text
KeyError: 'Dave'
```

### Step 1.6 — Safe Access with .get()

```python
>>> grades.get('Dave')
>>> grades.get('Dave', 0)
0
>>> grades.get('Alice', 0)
92
>>> print(grades.get('Dave'))
None
```

`grades.get('Dave')` returns `None` — no crash. `grades.get('Dave', 0)` returns the default `0`.

### Step 1.7 — Adding, Updating, and Deleting

```python
>>> grades['Dave'] = 90        # add new key
>>> grades['Alice'] = 95       # update existing key
>>> grades
{'Alice': 95, 'Bob': 85, 'Carol': 78, 'Dave': 90}

>>> del grades['Carol']        # delete — raises KeyError if missing
>>> grades
{'Alice': 95, 'Bob': 85, 'Dave': 90}

>>> removed = grades.pop('Bob')     # remove and return
>>> removed
85
>>> grades
{'Alice': 95, 'Dave': 90}

>>> grades.pop('nobody', 'not found')   # safe pop with default
'not found'
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the KeyError from Step 1.5, the safe `.get()` results from Step 1.6, and the add/update/delete operations from Step 1.7. Save as `lab10_screenshot_01_crud.png`.

---

## Part 2 — Dictionary Methods and Iteration

```bash
python3
```

### Step 2.1 — keys(), values(), items()

```python
>>> student = {'name': 'Alice', 'grade': 92, 'city': 'Dallas'}
>>> student.keys()
dict_keys(['name', 'grade', 'city'])
>>> student.values()
dict_values(['Alice', 92, 'Dallas'])
>>> student.items()
dict_items([('name', 'Alice'), ('grade', 92), ('city', 'Dallas')])
```

### Step 2.2 — View Objects Are Live

```python
>>> keys_view = student.keys()
>>> print(keys_view)
dict_keys(['name', 'grade', 'city'])
>>> student['gpa'] = 3.8
>>> print(keys_view)
dict_keys(['name', 'grade', 'city', 'gpa'])
```

The view updated automatically when we added `'gpa'`.

### Step 2.3 — Three Iteration Patterns

```python
>>> info = {'name': 'Bob', 'major': 'CS', 'year': 2}
...
>>> # Pattern 1 — keys only
>>> for key in info:
...     print(key)
...
name
major
year

>>> # Pattern 2 — values only
>>> for value in info.values():
...     print(value)
...
Bob
CS
2

>>> # Pattern 3 — key-value pairs
>>> for key, value in info.items():
...     print(f'{key}: {value}')
...
name: Bob
major: CS
year: 2
```

### Step 2.4 — Membership Testing

```python
>>> 'name' in info
True
>>> 'Bob' in info
False
>>> 'Bob' in info.values()
True
>>> 'gpa' in info
False
```

`'Bob' in info` is `False` because `in` tests **keys**, not values. To test values, use `in info.values()`.

### Step 2.5 — update() to Merge Dictionaries

```python
>>> defaults = {'color': 'blue', 'size': 'medium', 'font': 'Arial'}
>>> overrides = {'color': 'red', 'weight': 'bold'}
>>> defaults.update(overrides)
>>> defaults
{'color': 'red', 'size': 'medium', 'font': 'Arial', 'weight': 'bold'}
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing the three iteration patterns from Step 2.3 and the membership testing results from Step 2.4. Save as `lab10_screenshot_02_iteration.png`.

---

## Part 3 — Dictionary Comprehensions

```bash
python3
```

### Step 3.1 — Basic Comprehension

```python
>>> squares = {n: n**2 for n in range(1, 6)}
>>> squares
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Step 3.2 — Comprehension With Filter

```python
>>> scores = {'Alice': 92, 'Bob': 65, 'Carol': 78, 'Dave': 55, 'Eve': 88}
>>> passing = {name: score for name, score in scores.items() if score >= 70}
>>> passing
{'Alice': 92, 'Carol': 78, 'Eve': 88}
```

### Step 3.3 — Invert a Dictionary

```python
>>> original = {'a': 1, 'b': 2, 'c': 3}
>>> inverted = {v: k for k, v in original.items()}
>>> inverted
{1: 'a', 2: 'b', 3: 'c'}
```

### Step 3.4 — Comprehension From Two Lists

```python
>>> keys = ['x', 'y', 'z']
>>> values = [10, 20, 30]
>>> paired = {k: v for k, v in zip(keys, values)}
>>> paired
{'x': 10, 'y': 20, 'z': 30}
```

`zip()` pairs elements from both lists, and the comprehension builds the dictionary.

### Step 3.5 — Validate That dict != list comprehension

```python
>>> list_comp = [n**2 for n in range(5)]
>>> dict_comp = {n: n**2 for n in range(5)}
>>> type(list_comp)
<class 'list'>
>>> type(dict_comp)
<class 'dict'>
```

Exit the REPL:

```python
>>> exit()
```

---

## Part 4 — Word Frequency Counter

```bash
nano word_counter.py
```

```python
# word_counter.py
# Classic dictionary accumulator pattern
# Module 10 Lab — CIS-1310


def count_words(text):
    '''Return a frequency dictionary for words in text.'''
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def top_words(freq, n=5):
    '''Return the n most common words as a sorted list of (word, count) tuples.'''
    return sorted(freq.items(), key=lambda pair: pair[1], reverse=True)[:n]


# Test with sample text
sample = (
    'the quick brown fox jumps over the lazy dog '
    'the fox ran quickly the dog barked at the fox'
)

freq = count_words(sample)

print('All word counts:')
for word, count in sorted(freq.items()):
    print(f'  {word:<12} {count}')

print(f'\nTotal unique words: {len(freq)}')
print(f'Total words: {sum(freq.values())}')

print('\nTop 5 most common words:')
for word, count in top_words(freq, 5):
    print(f'  {word:<12} {count}')

# Demonstrate .get() safely
test_word = 'cat'
print(f'\nCount of "{test_word}": {freq.get(test_word, 0)}')
```

Save and run:

```bash
python3 word_counter.py
```

Expected output:

```text
All word counts:
  at           1
  barked       1
  brown        1
  dog          2
  fox          3
  jumps        1
  lazy         1
  over         1
  quick        1
  quickly      1
  ran          1
  the          5

Total unique words: 12
Total words: 17

Top 5 most common words:
  the          5
  fox          3
  dog          2
  at           1
  barked       1

Count of "cat": 0
```

> **SCREENSHOT 3 REQUIRED:** Screenshot of `word_counter.py` running with the complete output. Save as `lab10_screenshot_03_word_counter.png`.

---

## Part 5 — Student Grades Program (Nested Dictionaries)

```bash
nano student_grades.py
```

```python
# student_grades.py
# Nested dictionaries for student records
# Module 10 Lab — CIS-1310


def create_roster():
    '''Return a sample student roster as a nested dictionary.'''
    return {
        'Alice': {'grades': [92, 88, 95, 91], 'major': 'CS', 'year': 3},
        'Bob':   {'grades': [75, 82, 68, 79], 'major': 'Math', 'year': 2},
        'Carol': {'grades': [98, 95, 100, 97], 'major': 'CS', 'year': 4},
        'Dave':  {'grades': [60, 55, 70, 65], 'major': 'English', 'year': 1},
        'Eve':   {'grades': [88, 91, 85, 90], 'major': 'CS', 'year': 2},
    }


def average(grades):
    '''Return the average of a list of grades.'''
    return sum(grades) / len(grades)


def print_report(roster):
    '''Print a formatted grade report.'''
    print(f'{"Name":<10} {"Major":<10} {"Year":<6} {"Average":<10} {"Status"}')
    print('-' * 50)
    for name, info in sorted(roster.items()):
        avg = average(info['grades'])
        status = 'Passing' if avg >= 70 else 'At Risk'
        print(f'{name:<10} {info["major"]:<10} {info["year"]:<6} {avg:<10.1f} {status}')


def cs_students(roster):
    '''Return a dict of only CS students.'''
    return {name: info for name, info in roster.items()
            if info['major'] == 'CS'}


def class_average(roster):
    '''Return the average grade across all students.'''
    all_averages = [average(info['grades']) for info in roster.values()]
    return sum(all_averages) / len(all_averages)


# Run the program
roster = create_roster()

print('=== Full Grade Report ===')
print_report(roster)

print('\n=== CS Students Only ===')
cs = cs_students(roster)
print_report(cs)

print(f'\nClass average (all students): {class_average(roster):.1f}')
print(f'Class average (CS only): {class_average(cs):.1f}')

# Demonstrate safe lookup
print('\n=== Safe Lookup Demos ===')
name = 'Frank'
record = roster.get(name)
if record is None:
    print(f'{name} is not in the roster.')

# Add a new student
roster['Frank'] = {'grades': [80, 85, 78, 82], 'major': 'CS', 'year': 1}
print(f'Added Frank. Roster now has {len(roster)} students.')
```

Save and run:

```bash
python3 student_grades.py
```

Expected output:

```text
=== Full Grade Report ===
Name       Major      Year   Average    Status
--------------------------------------------------
Alice      CS         3      91.5       Passing
Bob        Math       2      76.0       Passing
Carol      CS         4      97.5       Passing
Dave       English    1      62.5       At Risk
Eve        CS         2      88.5       Passing

=== CS Students Only ===
Name       Major      Year   Average    Status
--------------------------------------------------
Alice      CS         3      91.5       Passing
Carol      CS         4      97.5       Passing
Eve        CS         2      88.5       Passing

Class average (all students): 83.2
Class average (CS only): 92.5

=== Safe Lookup Demos ===
Frank is not in the roster.
Added Frank. Roster now has 6 students.
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `student_grades.py` running and showing the complete output. Save as `lab10_screenshot_04_student_grades.png`.

---

## Part 6 — Hashable Keys Exploration

```bash
python3
```

### Step 6.1 — Valid Key Types

```python
>>> # String keys
>>> d = {'name': 'Alice'}
>>> d['name']
'Alice'

>>> # Integer keys
>>> d = {1: 'one', 2: 'two', 3: 'three'}
>>> d[2]
'two'

>>> # Tuple keys
>>> location = {(40.7128, -74.0060): 'New York City'}
>>> location[(40.7128, -74.0060)]
'New York City'
```

### Step 6.2 — Invalid Key Types

```python
>>> d = {[1, 2]: 'value'}
```

Expected:

```text
TypeError: unhashable type: 'list'
```

```python
>>> d = {{1: 2}: 'value'}
```

Expected:

```text
TypeError: unhashable type: 'dict'
```

### Step 6.3 — Boolean Keys (int Subtype Trap)

```python
>>> d = {True: 'yes', False: 'no'}
>>> d[1]
'yes'
>>> d[0]
'no'
```

`True` and `False` are integers `1` and `0` in Python. `d[1]` and `d[True]` access the same slot.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 5 REQUIRED:** Screenshot showing the hashable key tests from Steps 6.1–6.2, including the TypeError for the list key. Save as `lab10_screenshot_05_hashable_keys.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 10 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab10_screenshot_01_crud.png` | KeyError, .get() safe access, add/update/delete |
| 2 | `lab10_screenshot_02_iteration.png` | Three iteration patterns and membership testing |
| 3 | `lab10_screenshot_03_word_counter.png` | word_counter.py complete output |
| 4 | `lab10_screenshot_04_student_grades.png` | student_grades.py complete output |
| 5 | `lab10_screenshot_05_hashable_keys.png` | Hashable key types and TypeError for list key |

---

## Part 9 — Challenge Exercise

These steps are optional and ungraded. They extend the core lab concepts to real-world dictionary patterns.

### Step 9.1 — Inverted Index Builder

An inverted index maps each unique word to the list of positions (line numbers) where it appears. This is the core data structure behind search engines and `grep`-style tools.

```bash
nano inverted_index.py
```

```python
# inverted_index.py
# Build an inverted index from a multi-line text

text = '''the quick brown fox
the fox jumped high
a quick brown dog
the dog and the fox'''

index = {}
for line_num, line in enumerate(text.strip().split('\n'), start=1):
    for word in line.split():
        word = word.lower()
        if word not in index:
            index[word] = []
        index[word].append(line_num)

# Print all entries sorted alphabetically
print('Inverted Index:')
for word in sorted(index):
    print(f'  {word:10s}: lines {index[word]}')

# Look up specific words
print('\nSearch results:')
for query in ['fox', 'the', 'cat']:
    result = index.get(query, [])
    if result:
        print(f'  "{query}" found on lines: {result}')
    else:
        print(f'  "{query}" not found')
```

```bash
python3 inverted_index.py
```

Observe that `'the'` appears on lines 1, 2, and 4. The `setdefault` method can replace the `if word not in index` guard — rewrite the inner loop using `index.setdefault(word, []).append(line_num)` and verify identical output.

### Step 9.2 — Dictionary-Based Grade Book with Statistics

Build a grade book that computes per-student statistics and class-wide rankings using dictionary methods and `sorted()` with a `key` function.

```bash
nano gradebook.py
```

```python
# gradebook.py
# Grade book with statistics and ranking

grades = {
    'Alice':  [88, 92, 95, 79, 84],
    'Bob':    [72, 68, 75, 80, 70],
    'Carol':  [95, 98, 92, 96, 99],
    'Dave':   [60, 55, 63, 58, 65],
    'Eve':    [85, 88, 82, 90, 87],
}


def average(scores):
    return sum(scores) / len(scores)


# Build summary dict: {name: {'avg': ..., 'high': ..., 'low': ...}}
summary = {
    name: {
        'avg':  round(average(scores), 1),
        'high': max(scores),
        'low':  min(scores),
    }
    for name, scores in grades.items()
}

# Print ranked by average (descending)
print(f'{"Rank":<5} {"Name":<8} {"Avg":>6} {"High":>6} {"Low":>6}')
print('-' * 35)
ranked = sorted(summary.items(), key=lambda pair: pair[1]['avg'], reverse=True)
for rank, (name, stats) in enumerate(ranked, start=1):
    print(f'{rank:<5} {name:<8} {stats["avg"]:>6} {stats["high"]:>6} {stats["low"]:>6}')

# Class statistics
all_avgs = [s['avg'] for s in summary.values()]
print(f'\nClass average: {average(all_avgs):.1f}')
print(f'Top student:   {ranked[0][0]}')
print(f'Needs support: {ranked[-1][0]}')
```

```bash
python3 gradebook.py
```

Notice the use of a dictionary comprehension to build the summary and `sorted()` with a nested lambda key (`pair[1]['avg']`) to rank by a field inside a nested dict.

### Step 9.3 — Two-Pass Text Analyzer

Write a program that reads a multi-line string and computes: total words, unique words, top 5 most frequent words, and average word length — all using dictionary operations without importing any additional modules.

```bash
nano text_analyzer.py
```

```python
# text_analyzer.py
# Two-pass text analysis using only dict operations

passage = '''To be or not to be that is the question
Whether tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them to die to sleep'''

words = passage.lower().split()

# Pass 1: build frequency dict
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Pass 2: compute stats
total_words = len(words)
unique_words = len(freq)
avg_length = sum(len(w) for w in words) / total_words
top5 = sorted(freq.items(), key=lambda p: p[1], reverse=True)[:5]

print(f'Total words:   {total_words}')
print(f'Unique words:  {unique_words}')
print(f'Average length: {avg_length:.2f} characters')
print(f'\nTop 5 most frequent:')
for word, count in top5:
    bar = '#' * count
    print(f'  {word:<12} {count:>3}  {bar}')
```

```bash
python3 text_analyzer.py
```

Extend the program: add a third pass that builds a dictionary mapping word length to a list of unique words of that length, then print all lengths with more than 2 unique words.

---

## Troubleshooting Guide

**`KeyError` when accessing a dictionary value.**
The key does not exist in the dictionary. Use `d.get(key)` or `d.get(key, default)` for safe access, or check `if key in d:` before accessing.

**`TypeError: unhashable type: 'list'` when using a list as a key.**
Lists are mutable and cannot be dictionary keys. Use a tuple instead: `(1, 2)` instead of `[1, 2]`.

**`RuntimeError: dictionary changed size during iteration.`**
You tried to add or delete keys inside a `for key in d:` loop. Iterate over a snapshot instead: `for key in list(d.keys()):`.

**`in` operator returns False when you expect True.**
Remember that `key in d` tests **keys**, not values. To test whether a value exists, use `value in d.values()`.

**`word_counter.py` output does not match — words are not sorted.**
The `sorted(freq.items())` call sorts alphabetically by key (word). If you sort by count for the "top words", make sure you are using `key=lambda pair: pair[1], reverse=True`.
