# Video Script: CIS-1310 — Introduction to Python

## Module 11 — String Methods and Operations

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - Show the immutability demo before any method demos — it resets the student's mental model.
> - Emphasize `.find()` vs `.index()` side-by-side — this is a guaranteed PCAP trap.
> - Emphasize `.join()` syntax — called on the separator, not the list. Show the wrong way first.
> - Run `text_cleaner.py` live so students see a realistic string-processing pipeline.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 11 | String Methods and Operations | CIS-1310"]**

"Welcome back. We have used strings since Module 01 — printing them, concatenating them, using f-strings. This module goes deeper: the full library of string methods that Python gives you for searching, cleaning, splitting, joining, and transforming text.

String processing is everywhere. Every time you read a CSV file, parse a log line, validate user input, or clean data pulled from a web API, you are applying string methods. The PCAP exam tests these heavily — especially immutability, `.find()` versus `.index()`, `.split()` edge cases, and `.join()` syntax.

Let's cover all of it."

---

## [00:45 – 02:30] String Immutability — The Foundation

**[SHOW SLIDE: "Strings Are Immutable — Methods Return New Strings"]**

"Before we touch a single method, we need to lock in one rule that governs everything else: **strings in Python are immutable**. No string method modifies the original string. Every method returns a **new string** and leaves the original unchanged.

**[DEMO]**

```python
s = 'hello'
s.upper()       # returns 'HELLO' — but s is unchanged
print(s)        # hello
```

Output:

```text
hello
```

The call to `s.upper()` happened — it returned `'HELLO'` — but we threw the result away. To keep it, you must assign:

```python
s = s.upper()
print(s)        # HELLO
```

**[PAUSE]**

This is a classic PCAP trap. The exam will show code that calls a string method and then asks the value of the original variable. The answer is always the original, unchanged string — unless the result was explicitly reassigned.

You cannot change a character in a string by indexing:

```python
word = 'cat'
word[0] = 'b'    # TypeError: 'str' object does not support item assignment
```

If you need to change one character, build a new string: `'b' + word[1:]`."

---

## [02:30 – 04:30] Case Methods and String Testing

**[SHOW SLIDE: "Case Conversion and Testing Methods"]**

"**[DEMO — case conversion]**

```python
text = 'Hello, World!'

print(text.upper())       # HELLO, WORLD!
print(text.lower())       # hello, world!
print(text.capitalize())  # Hello, world! — only first char upper
print(text.title())       # Hello, World! — first char of each word upper
print(text.swapcase())    # hELLO, wORLD!
```

**[DEMO — boolean testing methods]**

These return `True` or `False`. Extremely useful for input validation.

```python
print('HELLO'.isupper())     # True
print('hello'.islower())     # True
print('Hello'.isupper())     # False
print('abc123'.isalpha())    # False — not all letters
print('abc'.isalpha())       # True
print('123'.isdigit())       # True
print('abc123'.isalnum())    # True — all alphanumeric
print('   '.isspace())       # True
print('Hello'.startswith('He'))   # True
print('Hello'.endswith('lo'))     # True
print('Hello'.endswith('LO'))     # False — case-sensitive
```

[PAUSE]

`.startswith()` and `.endswith()` accept tuples to test multiple options at once:

```python
filename = 'report.pdf'
print(filename.endswith(('.pdf', '.docx', '.txt')))    # True
```"

---

## [04:30 – 06:30] Searching — find(), index(), count()

**[SHOW SLIDE: "Searching in Strings"]**

"**[DEMO — find() and index()]**

```python
s = 'Python programming'

print(s.find('gram'))      # 10 — index where 'gram' starts
print(s.find('java'))      # -1 — not found, NO exception
print(s.index('gram'))     # 10 — same result when found
print(s.index('java'))     # ValueError: substring not found
```

[PAUSE]

This is one of the most tested distinctions on the PCAP exam. Both methods search for a substring. The difference: `.find()` returns `-1` if the substring is not found. `.index()` raises `ValueError`. Use `.find()` when the substring might be absent and you want to handle it gracefully. Use `.index()` when you want an error if it is missing.

```python
# Safe pattern using find()
if s.find('gram') >= 0:
    print('Found it')
else:
    print('Not found')
```

**[DEMO — rfind() searches from the right]**

```python
s = 'banana'
print(s.find('a'))     # 1 — first occurrence
print(s.rfind('a'))    # 5 — last occurrence
```

**[DEMO — count()]**

```python
print(s.count('a'))    # 3 — non-overlapping occurrences
print('aaa'.count('aa'))    # 1 — non-overlapping
```"

---

## [06:30 – 08:00] strip(), replace(), and Cleaning Text

**[SHOW SLIDE: "Cleaning Strings — strip() and replace()"]**

"Real-world data is messy. User input has extra spaces. File lines have trailing newlines. CSV values have quotes you need to remove. These methods clean it up.

**[DEMO — strip()]**

```python
messy = '   hello world   '
print(repr(messy.strip()))     # 'hello world'
print(repr(messy.lstrip()))    # 'hello world   '
print(repr(messy.rstrip()))    # '   hello world'
```

I used `repr()` here so you can see the quotes around the string and confirm the spaces are actually gone.

```python
# strip with specific characters
line = '---important---'
print(line.strip('-'))    # important
```

**[DEMO — replace()]**

```python
s = 'I like cats. Cats are great.'
print(s.replace('cats', 'dogs'))      # replaces all occurrences
print(s.replace('Cats', 'dogs'))      # case-sensitive — only second 'Cats'
print(s.replace('a', 'X', 2))         # third argument limits replacements
```

Output:

```text
I like dogs. Cats are great.
I like cats. dogs are great.
I like cXts. CXts are great.
```

[PAUSE]

Remember — `s.replace()` returns a new string. The original `s` is not changed unless you reassign."

---

## [08:00 – 10:00] split() and join()

**[SHOW SLIDE: "split() and join() — Text Parsing and Assembly"]**

"**[DEMO — split()]**

```python
sentence = 'the quick brown fox'
words = sentence.split()        # splits on any whitespace
print(words)                    # ['the', 'quick', 'brown', 'fox']
print(type(words))              # <class 'list'>
```

With no argument, `.split()` splits on any whitespace (spaces, tabs, newlines) and discards empty strings from multiple consecutive spaces.

```python
# split with a separator
csv_line = 'Alice,92,Dallas'
parts = csv_line.split(',')
print(parts)    # ['Alice', '92', 'Dallas']
```

**[DEMO — split() with whitespace edge case — PCAP trap]**

```python
double_space = 'a  b'
print(double_space.split())      # ['a', 'b'] — no empty string
print(double_space.split(' '))   # ['a', '', 'b'] — empty string appears
```

[PAUSE]

This is a tested PCAP distinction. `.split()` with no argument collapses multiple spaces and trims leading/trailing whitespace. `.split(' ')` treats every space as a delimiter — two spaces in a row produce an empty string.

**[DEMO — join()]**

```python
words = ['the', 'quick', 'brown', 'fox']

# join is called on the SEPARATOR
print(' '.join(words))      # the quick brown fox
print('-'.join(words))      # the-quick-brown-fox
print(', '.join(words))     # the, quick, brown, fox
print(''.join(words))       # thequickbrownfox
```

[PAUSE]

The syntax is `separator.join(list)`. This surprises students who expect `list.join(separator)`. The method belongs to the string (the separator), not the list. All elements in the list must be strings, or `TypeError` is raised."

---

## [10:00 – 11:30] Slicing Review and String Operators

**[SHOW SLIDE: "Slicing and String Operators"]**

"You saw slicing in Module 06 for lists. The syntax is identical for strings.

**[DEMO]**

```python
s = 'Python'
print(s[0])       # P — first character
print(s[-1])      # n — last character
print(s[1:4])     # yth — stop index is EXCLUDED
print(s[:3])      # Pyt
print(s[3:])      # hon
print(s[::2])     # Pto — every other character
print(s[::-1])    # nohtyP — reversed string
```

[PAUSE]

`s[::-1]` is the standard Python idiom for reversing a string. It appears on the PCAP exam.

**[DEMO — string operators]**

```python
a = 'hello'
b = ' world'
print(a + b)         # hello world — concatenation
print(a * 3)         # hellohellohello — repetition
print('ell' in a)    # True — substring test
print('xyz' not in a) # True
print(len(a))        # 5
```

**[DEMO — ord() and chr()]**

```python
print(ord('A'))     # 65 — Unicode code point
print(ord('a'))     # 97
print(chr(65))      # A
print(chr(97))      # a
```

`ord()` converts a character to its integer code point. `chr()` goes the other direction. These appear on the PCAP exam in character-comparison and sorting questions."

---

## [11:30 – 13:30] text_cleaner.py — Realistic String Pipeline

**[DEMO — live code]**

```python
# text_cleaner.py
# Demonstrates a realistic string processing pipeline
# Module 11 Lab — CIS-1310


def clean_line(line):
    '''Strip whitespace, convert to lowercase, replace punctuation.'''
    line = line.strip()
    line = line.lower()
    for char in '.,!?;:':
        line = line.replace(char, '')
    return line


def word_stats(text):
    '''Return a dict of word count stats for cleaned text.'''
    words = clean_line(text).split()
    return {
        'word_count': len(words),
        'unique_words': len(set(words)),
        'longest': max(words, key=len) if words else '',
        'contains_python': 'python' in words,
    }


# Test input
sample = '  Python is great. Python is powerful!  '

cleaned = clean_line(sample)
print('Cleaned:', cleaned)

stats = word_stats(sample)
for key, val in stats.items():
    print(f'  {key}: {val}')

# Split / join round-trip
words = cleaned.split()
hyphenated = '-'.join(words)
print('Hyphenated:', hyphenated)
print('Round trip:', ' '.join(hyphenated.split('-')))
```

Output:

```text
Cleaned: python is great python is powerful
  word_count: 6
  unique_words: 4
  longest: powerful
  contains_python: True
Hyphenated: python-is-great-python-is-powerful
Round trip: python is great python is powerful
```

---

## [13:30 – 15:00] PCAP Exam Tips and Wrap-Up

**[SHOW SLIDE: "Module 11 — PCAP Alignment"]**

"Key exam take-aways:

**1.** String methods return new strings — they never modify the original. Calling `s.upper()` without capturing the return value has no lasting effect.

**2.** `.find()` returns `-1` when the substring is absent. `.index()` raises `ValueError`. Know which is which.

**3.** `.split()` with no argument splits on any whitespace and discards empty strings. `.split(' ')` treats every single space as a delimiter and can produce empty strings.

**4.** `.join()` syntax: `separator.join(iterable)` — called on the separator, not the list. All elements must be strings.

**5.** `s[::-1]` reverses a string. `s[start:stop:step]` — stop is excluded.

**6.** `.strip()` removes both ends. `.lstrip()` left only. `.rstrip()` right only. An argument specifies characters to strip, not a substring.

**7.** `.startswith()` and `.endswith()` are case-sensitive and accept tuples for multiple options.

Module 12 covers exception handling — `try`, `except`, `else`, `finally`, and how to raise your own exceptions. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 11 — String Methods and Operations]**

---

## Additional Resources

- [Python for Everybody — Chapter 6](https://www.py4e.com/book) — Strings chapter with parsing examples
- [Official Python Docs — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods) — complete method reference
- [Official Python Docs — Built-in Functions: ord(), chr(), len()](https://docs.python.org/3/library/functions.html)
- [Real Python — Python String Formatting](https://realpython.com/python-string-formatting/) — f-strings, .format(), and % formatting in depth
