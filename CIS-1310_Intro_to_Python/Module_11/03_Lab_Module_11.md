# Lab Activity: Module 11 — String Methods and Operations

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 70–85 minutes

---

## Overview

In this lab you will demonstrate string immutability, practice all case conversion and testing methods, compare `.find()` versus `.index()`, explore `.split()` edge cases including the whitespace trap, master `.join()` syntax, use `.strip()` and `.replace()` for data cleaning, work with slicing and reversal, inspect `ord()` and `chr()`, and build a complete text processing program.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module11
cd module11
```

---

## Part 1 — Immutability and Case Methods

```bash
python3
```

### Step 1.1 — Immutability Demo

```python
>>> s = 'hello'
>>> s.upper()
'HELLO'
>>> print(s)
hello
```

`.upper()` returned `'HELLO'` but `s` is still `'hello'` — the result was not captured.

```python
>>> s = s.upper()
>>> print(s)
HELLO
```

Now `s` holds the new value.

### Step 1.2 — TypeError on Index Assignment

```python
>>> word = 'cat'
>>> word[0] = 'b'
```

Expected:

```text
TypeError: 'str' object does not support item assignment
```

Fix by building a new string:

```python
>>> word = 'b' + word[1:]
>>> word
'bat'
```

### Step 1.3 — Case Conversion Methods

```python
>>> text = 'hello, world!'
>>> text.upper()
'HELLO, WORLD!'
>>> text.lower()
'hello, world!'
>>> text.capitalize()
'Hello, world!'
>>> text.title()
'Hello, World!'
>>> text.swapcase()
'HELLO, WORLD!'
>>> 'hElLo'.swapcase()
'HeLlO'
```

### Step 1.4 — Boolean Testing Methods

```python
>>> 'HELLO'.isupper()
True
>>> 'Hello'.isupper()
False
>>> 'hello'.islower()
True
>>> 'abc'.isalpha()
True
>>> 'abc123'.isalpha()
False
>>> '12345'.isdigit()
True
>>> 'abc123'.isalnum()
True
>>> '   '.isspace()
True
>>> 'report.pdf'.endswith('.pdf')
True
>>> 'report.pdf'.endswith(('.pdf', '.docx', '.txt'))
True
>>> 'main.py'.startswith('main')
True
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the immutability demo from Step 1.1 (including the unchanged `s`), the TypeError from Step 1.2, and the boolean testing results from Step 1.4. Save as `lab11_screenshot_01_immutability_testing.png`.

---

## Part 2 — Searching: find() vs index()

```bash
python3
```

### Step 2.1 — find() Returns -1 for Missing Substring

```python
>>> s = 'Python programming is fun'
>>> s.find('gram')
10
>>> s.find('java')
-1
>>> s.find('Python')
0
>>> s.find('python')
-1
```

`.find()` is case-sensitive. `'python'` (lowercase) is not in the string.

### Step 2.2 — index() Raises ValueError for Missing Substring

```python
>>> s.index('gram')
10
>>> s.index('java')
```

Expected:

```text
ValueError: substring not found
```

### Step 2.3 — Safe Search Pattern

```python
>>> target = 'java'
>>> pos = s.find(target)
>>> if pos >= 0:
...     print(f'Found at index {pos}')
... else:
...     print(f'"{target}" not found')
...
"java" not found
```

### Step 2.4 — rfind() Finds Last Occurrence

```python
>>> 'banana'.find('a')
1
>>> 'banana'.rfind('a')
5
>>> 'banana'.count('a')
3
```

### Step 2.5 — in Operator for Substring Testing

```python
>>> 'gram' in s
True
>>> 'java' in s
False
>>> 'programming' in s
True
```

`in` tests whether a substring is present. It is equivalent to `s.find(sub) >= 0` but more readable.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing the `.find()` vs `.index()` comparison — including the `ValueError` from Step 2.2 and the safe search pattern from Step 2.3. Save as `lab11_screenshot_02_find_index.png`.

---

## Part 3 — split() and join()

```bash
python3
```

### Step 3.1 — split() With No Argument

```python
>>> sentence = '  the  quick   brown  fox  '
>>> words = sentence.split()
>>> words
['the', 'quick', 'brown', 'fox']
>>> len(words)
4
```

Leading/trailing whitespace ignored. Multiple spaces collapsed to one split.

### Step 3.2 — split() With Separator

```python
>>> csv = 'Alice,92,Dallas'
>>> csv.split(',')
['Alice', '92', 'Dallas']
>>> 'a::b::c'.split('::')
['a', 'b', 'c']
```

### Step 3.3 — The Whitespace Trap (PCAP Exam Topic)

```python
>>> double_space = 'a  b'
>>> double_space.split()
['a', 'b']
>>> double_space.split(' ')
['a', '', 'b']
```

`.split()` with no argument produces no empty strings. `.split(' ')` with an explicit space produces an empty string between the two consecutive spaces.

```python
>>> '   hello   '.split()
['hello']
>>> '   hello   '.split(' ')
['', '', '', 'hello', '', '', '']
```

### Step 3.4 — join() Syntax

```python
>>> words = ['the', 'quick', 'brown', 'fox']
>>> ' '.join(words)
'the quick brown fox'
>>> '-'.join(words)
'the-quick-brown-fox'
>>> ', '.join(words)
'the, quick, brown, fox'
>>> ''.join(words)
'thequickbrownfox'
```

### Step 3.5 — join() Called on Separator (Not List)

```python
>>> words = ['a', 'b', 'c']
>>> '-'.join(words)
'a-b-c'
>>> words.join('-')
```

Expected:

```text
AttributeError: 'list' object has no attribute 'join'
```

`join` is a string method — called on the separator, not the list.

### Step 3.6 — split/join Round Trip

```python
>>> original = 'hello world foo bar'
>>> words = original.split()
>>> rejoined = ' '.join(words)
>>> original == rejoined
True
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 3 REQUIRED:** Screenshot showing the whitespace trap from Step 3.3 (both versions side-by-side) and the AttributeError from Step 3.5. Save as `lab11_screenshot_03_split_join.png`.

---

## Part 4 — Stripping, Replacing, and Slicing

```bash
python3
```

### Step 4.1 — strip(), lstrip(), rstrip()

```python
>>> messy = '   hello world   '
>>> repr(messy.strip())
"'hello world'"
>>> repr(messy.lstrip())
"'hello world   '"
>>> repr(messy.rstrip())
"'   hello world'"
```

`repr()` shows the string with quotes so you can see exactly where spaces begin and end.

### Step 4.2 — strip() With Character Argument

```python
>>> '---important---'.strip('-')
'important'
>>> 'xxxhelloyyy'.strip('xy')
'hello'
>>> '   ###value###   '.strip().strip('#')
'value'
```

Chained calls — first strip whitespace, then strip hash characters.

### Step 4.3 — replace()

```python
>>> s = 'I like cats. cats are great.'
>>> s.replace('cats', 'dogs')
'I like dogs. dogs are great.'
>>> s.replace('cats', 'dogs', 1)
'I like dogs. cats are great.'
>>> s
'I like cats. cats are great.'
```

Original `s` is unchanged. The last print confirms immutability.

### Step 4.4 — Slicing

```python
>>> s = 'Python'
>>> s[0]
'P'
>>> s[-1]
'n'
>>> s[1:4]
'yth'
>>> s[::-1]
'nohtyP'
>>> s[::2]
'Pto'
>>> 'hello'[100:200]
''
```

Slicing out of range returns an empty string — no `IndexError`.

### Step 4.5 — ord() and chr()

```python
>>> ord('A')
65
>>> ord('a')
97
>>> ord('0')
48
>>> chr(65)
'A'
>>> chr(97)
'a'
>>> 'A' < 'a'
True
>>> ord('B') - ord('A')
1
```

Uppercase letters (65–90) have lower code points than lowercase (97–122).

Exit the REPL:

```python
>>> exit()
```

---

## Part 5 — text_cleaner.py

```bash
nano text_cleaner.py
```

```python
# text_cleaner.py
# Realistic string processing pipeline
# Module 11 Lab — CIS-1310


def clean_line(line):
    '''Strip whitespace, lowercase, remove punctuation.'''
    line = line.strip()
    line = line.lower()
    for char in '.,!?;:\'"()[]{}':
        line = line.replace(char, '')
    return line


def word_frequency(text):
    '''Return a dict mapping each word to its count.'''
    freq = {}
    for word in clean_line(text).split():
        freq[word] = freq.get(word, 0) + 1
    return freq


def summarize(text):
    '''Print a text analysis summary.'''
    cleaned = clean_line(text)
    words = cleaned.split()
    freq = word_frequency(text)

    print(f'Original : {repr(text[:50])}...' if len(text) > 50 else f'Original : {repr(text)}')
    print(f'Cleaned  : {repr(cleaned[:50])}...' if len(cleaned) > 50 else f'Cleaned  : {repr(cleaned)}')
    print(f'Words    : {len(words)}')
    print(f'Unique   : {len(freq)}')
    if words:
        print(f'Longest  : {max(words, key=len)}')
        top = sorted(freq.items(), key=lambda p: p[1], reverse=True)[:3]
        print(f'Top 3    : {top}')


# Sample inputs
lines = [
    '  Python is powerful, flexible, and fun!  ',
    'To be, or not to be: that is the question.',
    '   ',
]

for line in lines:
    summarize(line)
    print()

# Demonstrate split/join pipeline
print('=== Split / Join Pipeline ===')
raw = '   Data Science,  Machine Learning,  Python  '
fields = [f.strip() for f in raw.split(',')]
print('Fields:', fields)
joined = ' | '.join(fields)
print('Joined:', joined)

# Demonstrate startswith/endswith filtering
print('\n=== File Extension Filter ===')
files = ['report.pdf', 'data.csv', 'script.py', 'notes.txt', 'archive.tar.gz']
python_files = [f for f in files if f.endswith('.py')]
data_files = [f for f in files if f.endswith(('.csv', '.txt'))]
print('Python files:', python_files)
print('Data files:', data_files)
```

Save and run:

```bash
python3 text_cleaner.py
```

Expected output:

```text
Original : '  Python is powerful, flexible, and fun!  '
Cleaned  : 'python is powerful flexible and fun'
Words    : 6
Unique   : 6
Longest  : powerful
Top 3    : [('python', 1), ('is', 1), ('powerful', 1)]

Original : 'To be, or not to be: that is the question.'
Cleaned  : 'to be or not to be that is the question'
Words    : 9
Unique   : 8
Longest  : question
Top 3    : [('to', 2), ('be', 2), ('or', 1)]

Original : '   '
Cleaned  : ''
Words    : 0
Unique   : 0

=== Split / Join Pipeline ===
Fields: ['Data Science', 'Machine Learning', 'Python']
Joined: Data Science | Machine Learning | Python

=== File Extension Filter ===
Python files: ['script.py']
Data files: ['data.csv', 'notes.txt']
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `text_cleaner.py` running and showing the complete output. Save as `lab11_screenshot_04_text_cleaner.png`.

---

## Part 6 — string_ops.py

```bash
nano string_ops.py
```

```python
# string_ops.py
# Demonstrates string operators, formatting, and ord/chr
# Module 11 Lab — CIS-1310


# String operators
a = 'Hello'
b = ', World!'
print(a + b)          # concatenation
print(a * 3)          # repetition
print('ell' in a)     # membership
print(len(a + b))     # length

# Padding and alignment
header = 'RESULTS'
print(header.center(30, '='))
rows = [('Alice', 92), ('Bob', 85), ('Carol', 78)]
for name, score in rows:
    print(f'{name:<10} {score:>5}')

# ord / chr — build a simple Caesar cipher
def caesar_encrypt(text, shift):
    '''Encrypt text using Caesar cipher (letters only).'''
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)

plain = 'Hello, Python!'
encrypted = caesar_encrypt(plain, 3)
decrypted = caesar_encrypt(encrypted, -3)

print(f'\nCaesar cipher (shift=3):')
print(f'  Plain    : {plain}')
print(f'  Encrypted: {encrypted}')
print(f'  Decrypted: {decrypted}')
print(f'  Match    : {plain == decrypted}')
```

Save and run:

```bash
python3 string_ops.py
```

Expected output:

```text
Hello, World!
HelloHelloHello
True
13
=========RESULTS=========
Alice         92
Bob           85
Carol         78

Caesar cipher (shift=3):
  Plain    : Hello, Python!
  Encrypted: Khoor, Sbwkrq!
  Decrypted: Hello, Python!
  Match    : True
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `string_ops.py` running and showing the complete output. Save as `lab11_screenshot_05_string_ops.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 11 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab11_screenshot_01_immutability_testing.png` | Immutability demo, TypeError, boolean testing |
| 2 | `lab11_screenshot_02_find_index.png` | find() vs index() and ValueError |
| 3 | `lab11_screenshot_03_split_join.png` | Whitespace trap and join AttributeError |
| 4 | `lab11_screenshot_04_text_cleaner.png` | text_cleaner.py full output |
| 5 | `lab11_screenshot_05_string_ops.png` | string_ops.py full output |

---

## Troubleshooting Guide

**String method has no visible effect — value is unchanged.**
You forgot to capture the return value. Strings are immutable — every method returns a new string. Use `s = s.method()` to keep the result.

**ValueError from .index() on a substring you expected to find.**
`.index()` is case-sensitive. `'Hello'.index('hello')` raises `ValueError`. Use `.lower()` on both the string and the search term, or switch to `.find()` for safe lookups.

**`.join()` raises AttributeError or TypeError.**
`AttributeError`: you called `.join()` on the list instead of the separator. Syntax must be `separator.join(list)`. `TypeError`: one or more elements in the iterable is not a string. Convert all elements with a list comprehension: `sep.join(str(x) for x in items)`.

**`.split(' ')` produces unexpected empty strings.**
Use `.split()` with no argument if you want to split on any whitespace and ignore multiple consecutive spaces. Use `.split(' ')` only when you need exact single-space splitting and are aware that consecutive spaces produce empty strings.

**`text_cleaner.py` output mismatches — extra punctuation not removed.**
The `for char in '.,!?;:\'"()[]{}':` loop only removes the characters listed. Add any additional punctuation characters to the string literal inside the loop.
