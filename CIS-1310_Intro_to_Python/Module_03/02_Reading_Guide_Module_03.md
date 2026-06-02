# Reading Guide: Module 03 — Variables and Basic I/O

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 03 — Variables and Basic I/O**. This module connects the literal values and operators from Module 02 to real, interactive programs. Variables let you store and reuse data. The `input()` function lets your programs talk to users. f-strings let you produce clean, readable output. Together, these skills make every program from this point forward possible.

The PCAP exam tests variable naming rules, the behavior of `input()`, type conversion patterns, and f-string syntax extensively. Work through every glossary entry and trace through every example before starting the lab.

---

## 1. High-Yield Glossary

### Variable

A named label that references a value stored in memory. Created with an assignment statement: `name = value`. Variables can be reassigned at any time to new values of any type.

### Assignment Operator (`=`)

The single `=` symbol assigns the value on the right to the name on the left. It is NOT equality comparison — that is `==`. Writing `x = 5` stores `5` under the name `x`. Writing `x == 5` tests whether `x` equals `5` and returns `True` or `False`.

### Identifier

The technical term for a variable name (also applies to function names, class names, etc.). Python has strict rules for valid identifiers — see the naming rules section below.

### Python Naming Rules (PCAP exam critical)

A valid Python identifier must:

1. Start with a letter (`a`–`z`, `A`–`Z`) or an underscore (`_`)
2. Contain only letters, digits (`0`–`9`), and underscores after the first character
3. Not be a Python reserved keyword

Invalid examples and why:

| Name | Problem |
|---|---|
| `2fast` | Starts with a digit |
| `user-name` | Hyphen is not allowed |
| `my var` | Space is not allowed |
| `class` | Reserved keyword |
| `for` | Reserved keyword |

Valid examples: `name`, `_private`, `user_age`, `firstName`, `MAX_SIZE`, `x2`

### Python Reserved Keywords

The 35 words Python reserves for its own syntax — cannot be used as variable names:

```text
False    None     True     and      as       assert
async    await    break    class    continue def
del      elif     else     except   finally  for
from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise
return   try      while    with     yield
```

### Case Sensitivity

Python variable names are case-sensitive. `age`, `Age`, and `AGE` are three distinct variables. A common bug is referring to a variable with the wrong capitalization — Python raises `NameError: name 'X' is not defined`.

### PEP 8 Naming Conventions

| Use | Convention | Example |
|---|---|---|
| Variables and functions | `snake_case` | `user_age`, `total_price` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_SIZE`, `PI` |
| Classes | `PascalCase` | `StudentRecord`, `BankAccount` |

These are conventions, not rules — Python won't error on `userName`, but `user_name` is the professional standard.

### Dynamic Typing

Python determines a variable's type at runtime based on the assigned value. No type declaration is needed or allowed. The same variable can hold different types at different times. Contrast with **static typing** (Java, C) where the type is declared at compile time and cannot change.

### Multiple Assignment

Assigning multiple variables in a single statement:

```python
a, b, c = 1, 2, 3          # tuple unpacking
x = y = z = 0              # assign same value to multiple names
a, b = b, a                # swap two variables
```

### Augmented Assignment Operators

Shorthand operators that combine arithmetic with assignment:

| Operator | Equivalent | Example |
|---|---|---|
| `+=` | `x = x + n` | `count += 1` |
| `-=` | `x = x - n` | `score -= 5` |
| `*=` | `x = x * n` | `total *= 2` |
| `/=` | `x = x / n` | `avg /= count` |
| `//=` | `x = x // n` | `pages //= 2` |
| `%=` | `x = x % n` | `n %= 10` |
| `**=` | `x = x ** n` | `area **= 2` |

### print() Function

Outputs values to the terminal. Key parameters:

- `sep` — separator between multiple arguments (default: `' '` a space)
- `end` — appended after the last argument (default: `'\n'` newline)

Examples:

```python
print('A', 'B', 'C')              # A B C
print('A', 'B', 'C', sep='-')     # A-B-C
print('Loading', end='...')       # Loading... (no newline)
```

### f-string (Formatted String Literal)

A string prefixed with `f` that allows embedding expressions directly inside `{}` placeholders. Available since Python 3.6.

```python
name = 'Alice'
age = 30
print(f'Hello, {name}! You are {age} years old.')
# Hello, Alice! You are 30 years old.
```

Expressions inside `{}` are evaluated at runtime. You can use format specs after a colon:

- `:.2f` — float with 2 decimal places
- `:d` — integer
- `:>10` — right-align in 10-character field
- `:.0f` — float rounded to 0 decimal places

### input() Function

Pauses program execution, displays an optional prompt to the user, reads one line of text from the keyboard, and returns it as a `str`.

**Critical rule: `input()` ALWAYS returns `str` — no exceptions.**

```python
name = input('Enter your name: ')   # always str
age = input('Enter your age: ')     # '25' — a string, not int 25
```

To use the result for arithmetic, convert immediately:

```python
age = int(input('Enter your age: '))
```

### TypeError

Error raised when an operation is applied to a value of an incompatible type. Classic cause in this module: trying to add an `int` to the `str` returned by `input()`.

```python
age = input('Enter age: ')   # returns str
print(age + 1)               # TypeError: can only concatenate str (not "int") to str
```

### ValueError

Error raised when a function receives an argument of the right type but an inappropriate value. Classic cause: passing a non-numeric string to `int()` or `float()`.

```python
int('hello')     # ValueError: invalid literal for int() with base 10: 'hello'
int('3.14')      # ValueError: invalid literal for int() with base 10: '3.14'
```

To convert a float-formatted string to int, chain the calls:

```python
int(float('3.14'))   # 3 — float() first, then int()
```

### NameError

Error raised when a variable is referenced before it has been assigned a value. Common cause: typo in a variable name, or using a variable outside the scope where it was defined.

```python
print(userage)    # NameError if the variable is actually named user_age
```

---

## 2. The input() Function — Complete Behavior Reference

| Behavior | Detail |
|---|---|
| Return type | Always `str` |
| With no argument | `input()` — shows no prompt, just waits |
| With a prompt | `input('Enter name: ')` — displays the prompt |
| Empty input | Returns empty string `''` if user presses Enter without typing |
| Numeric input | User types `42` → you receive string `'42'` |
| Conversion pattern | `int(input('...'))` or `float(input('...'))` |

---

## 3. Common Error Patterns to Memorize

These patterns appear directly on the PCAP exam:

**Pattern 1 — The `input()` + arithmetic trap:**

```python
x = input('Number: ')
print(x * 2)             # '55' if user entered '5' — string repetition, not multiplication
```

`str * int` does NOT multiply — it repeats the string. `'5' * 2` = `'55'`, not `10`.

**Pattern 2 — The `int()` on a float string:**

```python
int('3.14')    # ValueError — int() cannot parse a decimal point
```

**Pattern 3 — The `NameError` typo:**

```python
user_name = 'Alice'
print(username)    # NameError — underscore missing
```

**Pattern 4 — The keyword as variable name:**

```python
class = 'CIS-1310'    # SyntaxError — class is a reserved keyword
```

---

## 4. Certification Exam Tips

**Tip 1 — `input()` always returns `str`.**
The #1 most tested `input()` fact. If you see code that calls `input()` and immediately uses the result in arithmetic without conversion, that code raises `TypeError`.

**Tip 2 — `str * int` repeats the string, does not multiply.**
`'5' * 2` = `'55'`. If a student forgets to convert `input()` to `int`, their multiplication code won't crash — it'll silently produce wrong results by repeating the string.

**Tip 3 — `int('3.14')` raises `ValueError`.**
`int()` accepts integer-format strings only. A decimal string must go through `float()` first: `int(float('3.14'))` = `3`.

**Tip 4 — Know all identifier rules.**
The PCAP exam shows four options for variable names and asks which are valid. Know that digits cannot start a name, hyphens are never valid, and all 35 keywords are off-limits.

**Tip 5 — f-string syntax.**
The PCAP tests f-string syntax. An f-string must have `f` or `F` before the opening quote. Variables go inside `{}`. Any Python expression is valid inside `{}`.

**Tip 6 — Case sensitivity.**
`Count`, `count`, and `COUNT` are different variables. A `NameError` that seems puzzling on an exam question is often a capitalization mismatch.

---

## 5. Beyond the Exam — Real-World Context

**Why does `input()` always return a string?**
From Python's perspective, it has no way to know what the user will type. The user might type `42`, or `"hello"`, or nothing, or `"3.14"`. Since Python can't predict the type of input at parse time, it always returns the safest, most general type — `str`. You as the programmer know what you expect, so you apply the appropriate conversion.

**Why do professional developers prefer f-strings over string concatenation?**
Compare these two equivalent lines:

```python
# Old style — hard to read, error-prone
print('Hello, ' + name + '! You are ' + str(age) + ' years old.')

# f-string — clean, readable, no type conversion needed
print(f'Hello, {name}! You are {age} years old.')
```

f-strings are more readable, require no manual type conversion to `str`, and are faster at runtime than string concatenation. They have been the preferred style since Python 3.6.

**Why does dynamic typing help in real projects?**
A function that computes something useful doesn't need to be written twice — once for integers and once for floats. In Python, the same function works on both because types are determined at runtime. This is one reason Python is so productive for rapid prototyping and data exploration.

---

## 6. Required Readings & Videos

**Required Reading — Chapters 2–3:**
Read Chapters 2 and 3 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). Chapter 2 covers variables and expressions. Chapter 3 covers conditional execution — but the `input()` examples in Chapter 3 are directly relevant to this module.

**Required Reading — Official Python Docs:**
Read [Built-in Functions: input()](https://docs.python.org/3/library/functions.html#input) and [Formatted String Literals (f-strings)](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) in the official Python 3 documentation.

**Required Video:**
Watch Episodes 5–6 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance walks through building interactive programs that prompt users, convert input, and produce formatted output.

---

## 7. Lab & Command Preview

| Task | What You Will Do |
|---|---|
| Variable naming experiments | Test valid and invalid names in REPL, observe `SyntaxError` and `NameError` |
| Multiple assignment | Practice `a, b = 1, 2` and swap pattern `a, b = b, a` |
| Augmented assignment | Use `+=`, `-=`, `*=` in short accumulator scripts |
| `print()` parameters | Test `sep` and `end` with multiple arguments |
| f-string practice | Write f-strings with variables, expressions, and format specs |
| `greeting.py` | Prompt for name and age, display personalized formatted greeting |
| `unit_converter.py` | Prompt for miles, convert to km, feet, meters |
| Error triggering | Intentionally cause `TypeError`, `ValueError`, `NameError` |

---

## 8. Study Checklist

- [ ] Watch the Module 03 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially the naming rules table and error patterns.
- [ ] Work through the Common Error Patterns in Section 3 — predict each error before reading the explanation.
- [ ] Read Chapters 2–3 of *Python for Everybody* at py4e.com.
- [ ] Read the `input()` and f-string sections of the Official Python 3 Docs.
- [ ] Watch Episodes 5–6 of the Python for Everybody playlist.
- [ ] Review the Certification Exam Tips in Section 4.
- [ ] Preview the lab tasks in Section 7.
- [ ] Proceed to the Module 03 Lab Activity.
