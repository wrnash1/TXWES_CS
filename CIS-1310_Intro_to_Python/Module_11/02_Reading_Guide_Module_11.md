# Reading Guide: Module 11 — String Methods and Operations

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 11 — String Methods and Operations**. Python strings are one of the most feature-rich built-in types in the language. Every program processes text — reading files, validating input, parsing data, formatting output. Python's string methods make all of this concise and readable.

The PCAP exam tests string methods more heavily than almost any other topic. You need to know what each method returns, what happens when a search fails, the exact difference between `.split()` and `.split(' ')`, and the fact that strings are immutable. These are not obscure edge cases — they are the core of how Python handles text.

This module also revisits slicing (introduced in Module 06 for lists) in the context of strings, and introduces `ord()` and `chr()` for working with Unicode code points.

---

## 1. High-Yield Glossary

### String Immutability

Strings in Python cannot be changed after they are created. No string method modifies the original — every method returns a **new string**.

```python
s = 'hello'
s.upper()        # returns 'HELLO' — result discarded
print(s)         # hello — UNCHANGED

s = s.upper()    # now we capture the result
print(s)         # HELLO
```

**PCAP exam rule:** If a string method is called and the return value is not assigned to a variable, the original string is unchanged. The exam will test this repeatedly.

You cannot assign to a character by index:

```python
word = 'cat'
word[0] = 'b'    # TypeError: 'str' object does not support item assignment
```

To "change" a character, build a new string: `'b' + word[1:]` → `'bat'`.

### String Indexing and Slicing

Identical to list indexing and slicing (Module 06):

```python
s = 'Python'
s[0]       # 'P' — zero-based index
s[-1]      # 'n' — last character
s[1:4]     # 'yth' — stop index EXCLUDED
s[:3]      # 'Pyt'
s[3:]      # 'hon'
s[::2]     # 'Pto' — every other character
s[::-1]    # 'nohtyP' — reversed string
```

Slicing never raises `IndexError`. Out-of-range bounds are silently clamped.

### Case Conversion Methods

| Method | Description | Example |
|---|---|---|
| `.upper()` | All characters uppercase | `'hello'.upper()` → `'HELLO'` |
| `.lower()` | All characters lowercase | `'HELLO'.lower()` → `'hello'` |
| `.capitalize()` | First character upper, rest lower | `'hello world'.capitalize()` → `'Hello world'` |
| `.title()` | First character of each word upper | `'hello world'.title()` → `'Hello World'` |
| `.swapcase()` | Swap upper↔lower for every character | `'Hello'.swapcase()` → `'hELLO'` |

### Boolean Testing Methods

All return `True` or `False`:

| Method | Returns True when... |
|---|---|
| `.isupper()` | All cased characters are uppercase |
| `.islower()` | All cased characters are lowercase |
| `.isalpha()` | All characters are letters (no digits, spaces) |
| `.isdigit()` | All characters are digits |
| `.isalnum()` | All characters are letters or digits |
| `.isspace()` | All characters are whitespace |
| `.startswith(prefix)` | String starts with `prefix` |
| `.endswith(suffix)` | String ends with `suffix` |

```python
'HELLO'.isupper()          # True
'Hello123'.isalpha()       # False — digits present
'Hello123'.isalnum()       # True — letters and digits only
'report.pdf'.endswith(('.pdf', '.docx'))   # True — tuple of options
```

`.startswith()` and `.endswith()` accept a **tuple** of strings to test multiple options.

### .find(sub) and .index(sub)

Both search for a substring and return the index of the first occurrence.

**Critical difference:**

| Method | Substring found | Substring NOT found |
|---|---|---|
| `.find(sub)` | Returns the index | Returns `-1` |
| `.index(sub)` | Returns the index | Raises `ValueError` |

```python
s = 'Python programming'
s.find('gram')     # 10
s.find('java')     # -1 — safe, no exception
s.index('gram')    # 10
s.index('java')    # ValueError: substring not found
```

Use `.find()` when the substring might be absent. Use `.index()` when absence should be an error.

Safe search pattern with `.find()`:

```python
pos = s.find('gram')
if pos >= 0:
    print(f'Found at index {pos}')
else:
    print('Not found')
```

**rfind() and rindex()** search from the right (last occurrence):

```python
'banana'.find('a')    # 1 — first 'a'
'banana'.rfind('a')   # 5 — last 'a'
```

### .count(sub)

Returns the number of non-overlapping occurrences of `sub` in the string.

```python
'banana'.count('a')     # 3
'banana'.count('an')    # 2
'aaa'.count('aa')       # 1 — non-overlapping: finds first, skips ahead
```

### .strip(), .lstrip(), .rstrip()

Remove characters from the ends of a string:

```python
'   hello   '.strip()      # 'hello' — both ends
'   hello   '.lstrip()     # 'hello   ' — left only
'   hello   '.rstrip()     # '   hello' — right only
```

With an argument, strips any of the specified characters (not a substring):

```python
'---important---'.strip('-')      # 'important'
'xxhelloxx'.strip('x')           # 'hello'
'abcHELLOcba'.strip('abc')       # 'HELLO' — any of 'a', 'b', 'c'
```

### .replace(old, new) and .replace(old, new, count)

Returns a new string with all occurrences of `old` replaced by `new`. The optional third argument limits the number of replacements.

```python
s = 'cat cat cat'
s.replace('cat', 'dog')       # 'dog dog dog'
s.replace('cat', 'dog', 2)    # 'dog dog cat' — only first 2
```

Case-sensitive. The original `s` is unchanged.

### .split() and .split(sep)

Splits the string and returns a **list** of substrings.

**No argument — whitespace splitting:**

```python
'  the  quick  brown  '.split()    # ['the', 'quick', 'brown']
```

Splits on any whitespace (spaces, tabs, newlines). Multiple consecutive whitespace characters are treated as one. Leading and trailing whitespace is ignored.

**With separator argument:**

```python
'a,b,c'.split(',')        # ['a', 'b', 'c']
'a::b::c'.split('::')     # ['a', 'b', 'c']
```

**PCAP exam trap — `.split()` vs `.split(' ')`:**

```python
'a  b'.split()      # ['a', 'b'] — no empty string
'a  b'.split(' ')   # ['a', '', 'b'] — empty string from double space
```

With an explicit `' '` separator, every single space is a delimiter. Two consecutive spaces produce an empty string between them. This is a tested exam distinction.

**Optional `maxsplit` argument:**

```python
'a:b:c:d'.split(':', 2)    # ['a', 'b', 'c:d'] — only first 2 splits
```

### .join(iterable)

Concatenates an iterable of strings, placing the calling string between each element. Returns one string.

```python
' '.join(['the', 'quick', 'fox'])     # 'the quick fox'
'-'.join(['a', 'b', 'c'])             # 'a-b-c'
', '.join(['one', 'two', 'three'])    # 'one, two, three'
''.join(['a', 'b', 'c'])              # 'abc' — no separator
```

**Syntax: called on the SEPARATOR, not the list.**

```python
# CORRECT
', '.join(['a', 'b'])

# WRONG — join is a string method, not a list method
['a', 'b'].join(', ')    # AttributeError: 'list' object has no attribute 'join'
```

All elements in the iterable must be strings. If any element is not a string, `TypeError` is raised.

### .format() and f-strings

Both produce formatted strings:

```python
name = 'Alice'
score = 92

# f-string (Python 3.6+)
print(f'{name} scored {score:.1f}')

# .format() method
print('{} scored {:.1f}'.format(name, score))
```

Both produce: `Alice scored 92.0`

### .center(), .ljust(), .rjust(), .zfill()

Padding and alignment methods:

```python
'hello'.center(11)        # '   hello   '
'hello'.ljust(10)         # 'hello     '
'hello'.rjust(10)         # '     hello'
'42'.zfill(5)             # '00042' — zero-pad on left
```

### in Operator for Strings

Tests whether a substring exists anywhere in the string:

```python
'gram' in 'Python programming'    # True
'java' in 'Python programming'    # False
'py' in 'Python'                  # False — case-sensitive
'Py' in 'Python'                  # True
```

### ord() and chr()

`ord(character)` returns the integer Unicode code point for a single character.
`chr(integer)` returns the character for a given code point.

```python
ord('A')    # 65
ord('a')    # 97
ord('0')    # 48
chr(65)     # 'A'
chr(97)     # 'a'
```

Useful for: checking if a character is a letter vs digit, building ciphers, sorting by character value.

```python
# All uppercase letters are 65–90, lowercase are 97–122
print(ord('A') < ord('a'))    # True — uppercase sorts before lowercase in ASCII
```

---

## 2. String Methods Reference Table

| Category | Method | Returns | Notes |
|---|---|---|---|
| Case | `.upper()` | New string | All uppercase |
| Case | `.lower()` | New string | All lowercase |
| Case | `.capitalize()` | New string | First char only |
| Case | `.title()` | New string | First of each word |
| Case | `.swapcase()` | New string | Swap case |
| Test | `.isupper()` | bool | All cased chars upper |
| Test | `.islower()` | bool | All cased chars lower |
| Test | `.isalpha()` | bool | All letters |
| Test | `.isdigit()` | bool | All digits |
| Test | `.isalnum()` | bool | All letters or digits |
| Test | `.isspace()` | bool | All whitespace |
| Test | `.startswith(x)` | bool | Accepts tuple |
| Test | `.endswith(x)` | bool | Accepts tuple |
| Search | `.find(sub)` | int | `-1` if not found |
| Search | `.rfind(sub)` | int | Last occurrence, `-1` if not found |
| Search | `.index(sub)` | int | `ValueError` if not found |
| Search | `.rindex(sub)` | int | Last occurrence, `ValueError` if not found |
| Search | `.count(sub)` | int | Non-overlapping count |
| Clean | `.strip(chars)` | New string | Both ends |
| Clean | `.lstrip(chars)` | New string | Left end |
| Clean | `.rstrip(chars)` | New string | Right end |
| Transform | `.replace(old, new)` | New string | All occurrences |
| Transform | `.replace(old, new, n)` | New string | First `n` occurrences |
| Split | `.split()` | list | Whitespace, no empties |
| Split | `.split(sep)` | list | Each sep is delimiter |
| Split | `.split(sep, n)` | list | Max `n` splits |
| Join | `sep.join(iterable)` | New string | All elements must be str |
| Pad | `.center(w)` | New string | Centered in width `w` |
| Pad | `.ljust(w)` | New string | Left-aligned |
| Pad | `.rjust(w)` | New string | Right-aligned |
| Pad | `.zfill(w)` | New string | Zero-padded on left |

---

## 3. Common Error Patterns to Memorize

**Pattern 1 — Discarding the return value of a string method:**

```python
s = 'hello world'
s.upper()           # WRONG — return value discarded
print(s)            # hello world — UNCHANGED

s = s.upper()       # CORRECT
print(s)            # HELLO WORLD
```

**Pattern 2 — Using .index() when the substring might be absent:**

```python
# DANGEROUS — raises ValueError if 'x' not in s
pos = s.index('x')

# SAFE — returns -1 if 'x' not in s
pos = s.find('x')
if pos >= 0:
    print(f'Found at {pos}')
```

**Pattern 3 — Calling .join() on the list instead of the separator:**

```python
# WRONG — list has no .join() method
['a', 'b', 'c'].join('-')    # AttributeError

# CORRECT — separator is the caller
'-'.join(['a', 'b', 'c'])    # 'a-b-c'
```

**Pattern 4 — Expecting .split(' ') to behave like .split():**

```python
'a  b'.split()      # ['a', 'b'] — no empty string
'a  b'.split(' ')   # ['a', '', 'b'] — empty string present
```

**Pattern 5 — Trying to modify a string by index:**

```python
s = 'hello'
s[0] = 'H'    # TypeError: 'str' object does not support item assignment

# Fix: build a new string
s = 'H' + s[1:]    # 'Hello'
```

---

## 4. Certification Exam Tips

**Tip 1 — Every string method returns a new string.**
The most commonly tested concept in this module. The exam shows code that calls a method without capturing the return value, then asks for the variable's value. It is always the original.

**Tip 2 — `.find()` returns `-1`; `.index()` raises `ValueError`.**
These two look identical when the substring is found. The difference only shows when the substring is absent. The exam tests this by showing one method used in a missing-substring scenario.

**Tip 3 — `.split()` vs `.split(' ')` produces different results with multiple spaces.**
No-argument `.split()` is forgiving — multiple spaces, tabs, newlines are all treated as one delimiter. Explicit `.split(' ')` is strict — every single space creates a split point.

**Tip 4 — `.join()` is called on the separator.**
`'-'.join(words)` is correct. `words.join('-')` is an `AttributeError`. This backwards syntax is one of the most frequently tested string traps on the PCAP exam.

**Tip 5 — Slicing never raises `IndexError`.**
`'hello'[100:200]` returns `''` — an empty string. Single-character indexing (`s[100]`) does raise `IndexError`. The exam distinguishes slicing from indexing.

**Tip 6 — `.strip(chars)` removes any of the listed characters, not the substring.**
`'abcHELLOcba'.strip('abc')` removes any of `'a'`, `'b'`, `'c'` from both ends — not the substring `'abc'`. The result is `'HELLO'`.

**Tip 7 — `ord()` and `chr()` appear in character-comparison questions.**
`ord('A')` = 65, `ord('a')` = 97. Uppercase letters have lower code points than lowercase. `'A' < 'a'` is `True` in Python string comparison because it uses code points.

---

## 5. Beyond the Exam — Real-World Context

**CSV and data parsing.**
Every data science pipeline starts with reading text. `.split(',')` parses CSV lines. `.strip()` cleans whitespace from field values. `.replace()` normalizes inconsistent formatting. Understanding these methods is the foundation of data cleaning.

**Input validation.**
`.isdigit()`, `.isalpha()`, `.isalnum()`, `.startswith()`, and `.endswith()` are your first line of defense before converting user input to numbers or passing it to a database. Checking `user_input.isdigit()` before calling `int(user_input)` prevents `ValueError` entirely.

**Log parsing.**
Server logs are text files — one line per event. `.split()` breaks a line into fields. `.find()` locates error markers. `.startswith()` filters lines by log level. Building a log analyzer is a real-world Python project that uses every string method in this module.

**String methods and performance.**
String concatenation with `+` in a loop (`s = s + new_piece`) creates a new string on every iteration — slow for large data. The correct pattern is to accumulate pieces in a list and `.join()` at the end: `result = ''.join(pieces)`. This is significantly faster because `.join()` pre-allocates the exact memory needed.

---

## 6. Required Readings and Videos

**Required Reading — Chapter 6:**
Read Chapter 6 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). This chapter covers string operations and parsing patterns. Pay close attention to the loop-over-string examples and the parsing exercises.

**Required Reading — Official Python Docs:**
Read [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods) in the Python 3 standard library documentation. This is the complete reference for every method tested on the PCAP exam.

**Supplemental Video:**
Watch Episode 6 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance covers string parsing with real data examples.

---

## 7. Supplemental Resources

**1. Official Python 3 Docs — String Methods**
[https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
The complete reference for every string method with precise signatures, return types, and edge-case behavior. This is the authoritative source for PCAP exam questions on string methods — every method in the exam's topic list is documented here.

**2. Python for Everybody — Chapter 6: Strings**
[https://www.py4e.com/html3/06-strings](https://www.py4e.com/html3/06-strings)
Free textbook chapter covering string indexing, slicing, iteration, immutability, and parsing patterns with step-by-step examples. The looping-over-strings section and the parsing exercises mirror PCAP exam question formats exactly.

**3. Real Python — Python String Formatting Best Practices**
[https://realpython.com/python-string-formatting/](https://realpython.com/python-string-formatting/)
A free article comparing all Python string formatting approaches: `%` operator, `.format()`, f-strings, and template strings. The f-string section covers format specs (alignment, width, precision) that appear on the PCAP exam.

**4. Official Python 3 Docs — Text Processing Services**
[https://docs.python.org/3/library/text.html](https://docs.python.org/3/library/text.html)
Overview of Python's text processing capabilities beyond the built-in string type, including `re` (regular expressions), `textwrap`, and `unicodedata`. Useful for understanding where string methods fit in the broader ecosystem.

**5. Real Python — Python String Immutability**
[https://realpython.com/python-strings/](https://realpython.com/python-strings/)
A comprehensive free article on Python strings covering indexing, slicing, all major methods, immutability, and encoding. The section on `ord()` and `chr()` and Unicode code points is directly relevant to PCAP exam questions on character arithmetic.

---

## 8. Study Checklist

- [ ] Watch the Module 11 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — pay special attention to `.find()` vs `.index()`, `.split()` edge cases, and `.join()` syntax.
- [ ] Work through the String Methods Reference Table — cover the Returns column and test yourself.
- [ ] Work through all 5 Common Error Patterns in the REPL and observe each error.
- [ ] Read Chapter 6 of *Python for Everybody* at py4e.com.
- [ ] Read the String Methods page in the official Python 3 docs.
- [ ] Review all 7 Certification Exam Tips in Section 4.
- [ ] Proceed to the Module 11 Lab Activity.
