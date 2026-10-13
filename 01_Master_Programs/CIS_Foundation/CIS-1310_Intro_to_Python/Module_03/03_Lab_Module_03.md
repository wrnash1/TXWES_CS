# Lab Activity: Module 03 — Variables and Basic I/O

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 60–75 minutes

---

## Overview

In this lab you will practice Python variable naming rules, explore dynamic typing, use augmented assignment operators, master `print()` output formatting, work with f-strings, and build two complete interactive programs that use `input()` with type conversion. You will also intentionally trigger `TypeError`, `ValueError`, and `NameError` to understand exactly what Python reports and why.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module03
cd module03
```

---

## Part 1 — Variable Naming Rules in the REPL

Launch the REPL:

```bash
python3
```

### Step 1.1 — Test Valid Variable Names

```python
>>> my_name = 'Alice'
>>> my_name
'Alice'
>>> _hidden = 42
>>> _hidden
42
>>> user_age_2 = 25
>>> user_age_2
25
>>> CONSTANT_PI = 3.14159
>>> CONSTANT_PI
3.14159
```

All of these are valid identifiers. Notice underscores, digits (not as first character), and uppercase all work fine.

### Step 1.2 — Trigger SyntaxError With Invalid Names

```python
>>> 2fast = 10
```

Expected:

```text
  File "<stdin>", line 1
    2fast = 10
        ^
SyntaxError: invalid decimal literal
```

```python
>>> my-var = 5
```

Expected:

```text
SyntaxError: cannot assign to expression here
```

```python
>>> my var = 5
```

Expected:

```text
SyntaxError: invalid syntax
```

### Step 1.3 — Trigger SyntaxError With Reserved Keywords

```python
>>> class = 'CIS-1310'
```

Expected:

```text
SyntaxError: invalid syntax
```

```python
>>> for = 10
```

Expected:

```text
SyntaxError: invalid syntax
```

### Step 1.4 — Demonstrate Case Sensitivity

```python
>>> count = 1
>>> Count = 2
>>> COUNT = 3
>>> print(count, Count, COUNT)
1 2 3
>>> count == Count
False
```

Three different variables — same letters, different capitalization.

### Step 1.5 — Trigger NameError

```python
>>> student_name = 'Bob'
>>> print(studentname)
```

Expected:

```text
NameError: name 'studentname' is not defined
```

The underscore in `student_name` is missing. Python treats `studentname` as a completely different name that has never been assigned.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the `SyntaxError` and `NameError` examples from Steps 1.2–1.5. Save as `lab03_screenshot_01_naming_rules.png`.

---

## Part 2 — Dynamic Typing and Augmented Assignment in the REPL

```bash
python3
```

### Step 2.1 — Dynamic Typing

```python
>>> x = 42
>>> type(x)
<class 'int'>
>>> x = 'hello'
>>> type(x)
<class 'str'>
>>> x = 3.14
>>> type(x)
<class 'float'>
>>> x = True
>>> type(x)
<class 'bool'>
>>> x = None
>>> type(x)
<class 'NoneType'>
```

The same variable `x` holds five different types in sequence. Python never raises an error — it simply updates what `x` points to.

### Step 2.2 — Multiple Assignment

```python
>>> a, b, c = 10, 20, 30
>>> print(a, b, c)
10 20 30
>>> x = y = z = 0
>>> print(x, y, z)
0 0 0
```

Swap two variables without a temporary:

```python
>>> p, q = 100, 200
>>> print(p, q)
100 200
>>> p, q = q, p
>>> print(p, q)
200 100
```

### Step 2.3 — Augmented Assignment Operators

```python
>>> count = 0
>>> count += 1
>>> count
1
>>> count += 9
>>> count
10
>>> count -= 3
>>> count
7
>>> count *= 4
>>> count
28
>>> count //= 3
>>> count
9
>>> count **= 2
>>> count
81
>>> count %= 10
>>> count
1
```

Trace through each operation and verify the result makes sense before checking.

Exit the REPL:

```python
>>> exit()
```

---

## Part 3 — print() Parameters and f-strings

```bash
python3
```

### Step 3.1 — The sep Parameter

```python
>>> print('A', 'B', 'C')
A B C
>>> print('A', 'B', 'C', sep=', ')
A, B, C
>>> print('2026', '06', '01', sep='-')
2026-06-01
>>> print('A', 'B', 'C', sep='')
ABC
>>> print('one', 'two', 'three', sep=' | ')
one | two | three
```

### Step 3.2 — The end Parameter

```python
>>> print('Step 1', end=' -> ')
>>> print('Step 2', end=' -> ')
>>> print('Step 3')
Step 1 -> Step 2 -> Step 3
```

Notice that the three `print()` calls produce output on ONE line because `end` was changed from the default newline.

### Step 3.3 — f-strings

```python
>>> name = 'Alice'
>>> age = 30
>>> gpa = 3.857
>>> print(f'Student: {name}')
Student: Alice
>>> print(f'Age: {age}')
Age: 30
>>> print(f'GPA: {gpa:.2f}')
GPA: 3.86
>>> print(f'{name} is {age} years old and has a {gpa:.1f} GPA.')
Alice is 30 years old and has a 3.9 GPA.
```

Embed expressions directly:

```python
>>> price = 9.99
>>> qty = 5
>>> print(f'Total: ${price * qty:.2f}')
Total: $49.95
>>> print(f'2 ** 10 = {2 ** 10}')
2 ** 10 = 1024
>>> print(f'pi ≈ {3.14159:.4f}')
pi ≈ 3.1416
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot of REPL showing f-string examples from Step 3.3. Save as `lab03_screenshot_02_fstrings.png`.

---

## Part 4 — Understanding input() Behavior

### Step 4.1 — Create input_demo.py

```bash
nano input_demo.py
```

```python
# input_demo.py
# Demonstrates input() behavior and type conversion
# Module 03 Lab — CIS-1310

# Part A: input() always returns str
raw = input('Type anything: ')
print(f'You typed: {raw}')
print(f'Type of raw: {type(raw)}')
print(f'Length of raw: {len(raw)}')
```

Save and run:

```bash
python3 input_demo.py
```

Enter `hello` when prompted:

```text
Type anything: hello
You typed: hello
Type of raw: <class 'str'>
Length of raw: 5
```

Now run again and enter `42`:

```text
Type anything: 42
You typed: 42
Type of raw: <class 'str'>
Length of raw: 2
```

Even `42` comes back as `str`. The length is `2` — two characters, not a two-digit number.

---

## Part 5 — Intentional Error Triggering

Understanding errors by causing them on purpose builds debugging intuition.

### Step 5.1 — Trigger TypeError

```bash
nano error_demo.py
```

```python
# error_demo.py
# Intentionally demonstrates TypeError from input() + arithmetic
# Module 03 Lab — CIS-1310

age = input('Enter your age: ')
# This will crash — age is a str, not int
result = age + 1
print(result)
```

Save and run:

```bash
python3 error_demo.py
```

Enter `25` when prompted:

```text
Enter your age: 25
Traceback (most recent call last):
  File "error_demo.py", line 6, in <module>
    result = age + 1
TypeError: can only concatenate str (not "int") to str
```

Read the traceback:

- `File "error_demo.py", line 6` — the exact line number
- `result = age + 1` — the exact line of code
- `TypeError: can only concatenate str (not "int") to str` — the error type and message

Now fix the file. Open it again in nano and change line 6:

```python
age = int(input('Enter your age: '))
result = age + 1
print(f'Next year you will be {result}.')
```

Run again:

```text
Enter your age: 25
Next year you will be 26.
```

### Step 5.2 — Trigger ValueError

Open nano and add to `error_demo.py` (or create a new file):

```bash
nano value_error_demo.py
```

```python
# value_error_demo.py
# Demonstrates ValueError from int() on non-numeric strings
# Module 03 Lab — CIS-1310

# This will crash
age = int(input('Enter your age: '))
print(f'Your age is {age}')
```

Run and type `twenty-five` when prompted:

```text
Enter your age: twenty-five
Traceback (most recent call last):
  File "value_error_demo.py", line 5, in <module>
    age = int(input('Enter your age: '))
ValueError: invalid literal for int() with base 10: 'twenty-five'
```

Also test what happens with `int('3.14')` in the REPL:

```bash
python3
```

```python
>>> int('3.14')
```

Expected:

```text
ValueError: invalid literal for int() with base 10: '3.14'
```

Fix: chain `float()` and `int()`:

```python
>>> int(float('3.14'))
3
```

Exit: `exit()`

> **SCREENSHOT 3 REQUIRED:** Screenshot showing the `TypeError` traceback and the `ValueError` traceback. Save as `lab03_screenshot_03_errors.png`.

---

## Part 6 — Write greeting.py

### Step 6.1 — Create the Script

```bash
nano greeting.py
```

```python
# greeting.py
# Interactive greeting program with formatted output
# Module 03 Lab — CIS-1310

print('=== Student Greeter ===')
print()

# Collect user information
name = input('Enter your first name: ')
age = int(input('Enter your age: '))
major = input('Enter your major: ')

# Compute derived values
birth_year = 2026 - age
years_to_graduation = max(0, 22 - age)

# Display formatted output
print()
print('=' * 35)
print(f'  Welcome, {name}!')
print('=' * 35)
print(f'  Name:          {name}')
print(f'  Age:           {age}')
print(f'  Major:         {major}')
print(f'  Birth year:    {birth_year}')
print(f'  Est. grad:     {2026 + years_to_graduation}')
print('=' * 35)
print(f'  Go Rams, {name}!')
print('=' * 35)
```

Save and run:

```bash
python3 greeting.py
```

Sample interaction:

```text
=== Student Greeter ===

Enter your first name: Marcus
Enter your age: 20
Enter your major: Computer Science

===================================
  Welcome, Marcus!
===================================
  Name:          Marcus
  Age:           20
  Major:         Computer Science
  Birth year:    2006
  Est. grad:     2028
===================================
  Go Rams, Marcus!
===================================
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `greeting.py` running with your own inputs. Save as `lab03_screenshot_04_greeting.png`.

---

## Part 7 — Write unit_converter.py

### Step 7.1 — Create the Script

```bash
nano unit_converter.py
```

```python
# unit_converter.py
# Converts miles to multiple units
# Demonstrates: input(), float conversion, f-strings with format specs
# Module 03 Lab — CIS-1310

print('=== Distance Unit Converter ===')
print()

miles = float(input('Enter distance in miles: '))

# Conversion factors
km = miles * 1.60934
meters = km * 1000
feet = miles * 5280
inches = feet * 12
nautical_miles = miles * 0.868976

# Display results
print()
print(f'  {miles} miles =')
print(f'  {km:.4f} kilometers')
print(f'  {meters:.2f} meters')
print(f'  {feet:,.2f} feet')
print(f'  {inches:,.0f} inches')
print(f'  {nautical_miles:.4f} nautical miles')
```

Save and run:

```bash
python3 unit_converter.py
```

Sample interaction:

```text
=== Distance Unit Converter ===

Enter distance in miles: 26.2

  26.2 miles =
  42.1648 kilometers
  42164.81 meters
  138,336.00 feet
  1,660,032 inches
  22.7652 nautical miles
```

Notice the `:,.2f` format spec — the comma `,` adds thousands separators (138,336.00 instead of 138336.00). The `:,.0f` spec rounds to zero decimal places with thousands separators.

Test with `1`, `100`, and `0.5` miles to verify the conversions are correct.

> **SCREENSHOT 5 REQUIRED:** Screenshot of `unit_converter.py` running with `26.2` miles. Save as `lab03_screenshot_05_unit_converter.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 03 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab03_screenshot_01_naming_rules.png` | `SyntaxError` and `NameError` from invalid names |
| 2 | `lab03_screenshot_02_fstrings.png` | REPL f-string examples with format specs |
| 3 | `lab03_screenshot_03_errors.png` | `TypeError` and `ValueError` tracebacks |
| 4 | `lab03_screenshot_04_greeting.png` | `greeting.py` running with your inputs |
| 5 | `lab03_screenshot_05_unit_converter.png` | `unit_converter.py` running with 26.2 miles |

---

## Part 9 — Challenge Exercise

These steps are optional and ungraded. They push beyond basic I/O into more sophisticated formatting and input validation patterns.

### Challenge 9.1 — Build a Multi-Field Formatted Receipt

Create `~/cis1310/module03/receipt.py` that prompts the user for three item names and prices, then prints a formatted receipt with:

- A header and footer border made of `=` characters, 40 wide
- Each item left-aligned in a 25-character field with price right-aligned in a 10-character field, formatted to 2 decimal places
- A subtotal, tax (8.25%), and grand total line, each aligned consistently
- All numeric values formatted with the `:>10.2f` format spec

The target output should look like:

```text
========================================
       TEXAS WESLEYAN BOOKSTORE
========================================
Python Textbook              $    49.99
USB Flash Drive              $     8.95
Notebook                     $     3.50
----------------------------------------
Subtotal:                    $    62.44
Tax (8.25%):                 $     5.15
TOTAL:                       $    67.59
========================================
```

Use f-strings exclusively — no old-style `%` formatting or `str.format()`.

---

### Challenge 9.2 — Safe Integer Input Function

Python's `int(input(...))` will crash with `ValueError` if the user types a non-numeric value. Write a script `~/cis1310/module03/safe_input.py` that implements a loop-based safe integer reader:

```python
def get_int(prompt):
    while True:
        raw = input(prompt)
        if raw.lstrip('-').isdigit():
            return int(raw)
        print(f'  Error: "{raw}" is not a valid integer. Try again.')
```

Test it by calling `get_int('Enter a number: ')` and entering invalid inputs (letters, floats, empty string) before finally entering a valid integer. Add a second function `get_float(prompt)` using the same pattern. This pattern previews the exception-handling techniques covered in Module 12.

---

### Challenge 9.3 — Variable Swap Without a Temporary Variable

Python's tuple assignment makes variable swapping elegant. Write a script `~/cis1310/module03/swap_demo.py` that:

1. Demonstrates the traditional three-variable swap (using a `temp` variable) for two integers
2. Demonstrates the Pythonic one-line swap with tuple unpacking
3. Extends the pattern to swap three variables simultaneously: `a, b, c = c, a, b`
4. Prints the values before and after each swap with clear labels

Add a comment explaining why the Pythonic swap works without corruption — specifically that Python evaluates the entire right-hand side as a tuple before performing any assignment, so there is no moment where both names point to the same value unintentionally.

---

## Troubleshooting Guide

**`SyntaxError` when using a keyword as a variable name.**
This is expected and intentional in Part 1. Python cannot parse `class = 'value'` because `class` is reserved syntax.

**`ValueError` when entering non-numeric input to the unit converter.**
This is expected behavior — `float()` cannot convert `'hello'` to a number. We handle this with exception handling in Module 12. For now, always enter valid numeric input.

**`str * int` gives repeated string, not multiplication.**
`'5' * 3` = `'555'`, not `15`. You forgot to convert the `input()` result. Wrap it: `int(input(...))`.

**f-string `SyntaxError`.**
You must put `f` immediately before the opening quote: `f'...'` — not `f '...'` (no space between `f` and the quote). Also ensure curly braces `{}` are balanced — every `{` needs a matching `}`.

**`NameError` in greeting.py.**
Check your variable names for typos and capitalization mismatches. `Name` and `name` are different variables.
