# Lab Activity: Module 02 — Literals, Operators, and Expressions

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 60–75 minutes

---

## Overview

In this lab you will explore all of Python's core data type literals in the REPL, trace and verify operator precedence expressions, witness the float precision issue firsthand, and write two complete Python scripts: a circle calculator and a temperature converter. By the end of this lab you will have hands-on experience with every concept tested in Module 02 of the PCAP exam.

---

## Prerequisites

- Your Ubuntu VM from Module 01 is running.
- Python 3 is installed (`python3 --version` returns 3.10 or higher).
- You have a terminal open and are in your `~/cis1310` directory.

---

## Setup

Open a terminal in your Ubuntu VM and navigate to your course directory:

```bash
cd ~/cis1310
mkdir module02
cd module02
```

---

## Part 1 — Exploring Data Type Literals in the REPL

Launch the REPL:

```bash
python3
```

### Step 1.1 — Integer Literals

Type each line and observe the output:

```python
>>> 42
42
>>> -100
-100
>>> 0
0
>>> type(42)
<class 'int'>
```

Now test the alternate integer bases:

```python
>>> 0b1010
10
>>> 0b11111111
255
>>> 0o17
15
>>> 0o100
64
>>> 0xFF
255
>>> 0x1F
31
>>> type(0xFF)
<class 'int'>
```

All three produce regular Python `int` values — just different notation. Verify they're equal:

```python
>>> 0b11111111 == 0xFF
True
>>> 0xFF == 255
True
```

### Step 1.2 — Float Literals and the Precision Trap

```python
>>> 3.14
3.14
>>> -0.5
-0.5
>>> 1e6
1000000.0
>>> 2.5e-3
0.0025
>>> type(3.14)
<class 'float'>
```

Now run the most important float test in this entire course:

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
```

Read those outputs carefully. `0.1 + 0.2` is not exactly `0.3`. And the equality test returns `False`. This is IEEE 754 binary floating-point arithmetic — not a Python bug. Remember it for the PCAP exam.

Now try a safer comparison:

```python
>>> abs(0.1 + 0.2 - 0.3) < 0.0001
True
```

This tolerance-based comparison returns `True`. Use this pattern whenever you need to compare floats.

### Step 1.3 — String Literals and Escape Sequences

```python
>>> 'Hello'
'Hello'
>>> "World"
'World'
>>> 'It\'s Python'
"It's Python"
>>> "She said \"hi\""
'She said "hi"'
```

Now test escape sequences with `print()` to see their actual effect:

```python
>>> print('Line 1\nLine 2\nLine 3')
Line 1
Line 2
Line 3
>>> print('Name:\tAlice')
Name:	Alice
>>> print('Path: C:\\Users\\student')
Path: C:\Users\student
```

Triple-quoted strings:

```python
>>> msg = """This is
... a multiline
... string"""
>>> print(msg)
This is
a multiline
string
>>> type(msg)
<class 'str'>
```

### Step 1.4 — Boolean Literals and Arithmetic

```python
>>> True
True
>>> False
False
>>> type(True)
<class 'bool'>
>>> True == 1
True
>>> False == 0
True
```

Now the critical bool-as-int behavior:

```python
>>> True + True
2
>>> True + False
1
>>> False + False
0
>>> True * 10
10
>>> int(True)
1
>>> int(False)
0
```

### Step 1.5 — None

```python
>>> None
>>> type(None)
<class 'NoneType'>
>>> None == 0
False
>>> None == False
False
>>> None is None
True
```

Notice that typing `None` by itself in the REPL produces no output — the REPL does not display `None` results automatically (this is the one exception to the REPL auto-print rule).

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Take a screenshot showing your REPL session from Parts 1.1–1.5. Make sure it shows the `0.1 + 0.2` result and the `True + True` result. Save as `lab02_screenshot_01_literals.png`.

---

## Part 2 — Arithmetic Operators and Precedence in the REPL

Launch the REPL again:

```bash
python3
```

### Step 2.1 — All Seven Arithmetic Operators

Work through each operator systematically:

```python
>>> 15 + 4
19
>>> 15 - 4
11
>>> 15 * 4
60
>>> 15 / 4
3.75
>>> 15 // 4
3
>>> 15 % 4
3
>>> 2 ** 10
1024
```

Now test the type return difference between `/` and `//`:

```python
>>> type(15 / 4)
<class 'float'>
>>> type(15 // 4)
<class 'int'>
>>> 4 / 2
2.0
>>> 4 // 2
2
>>> type(4 / 2)
<class 'float'>
```

Important: `4 / 2` returns `2.0` — a `float`. The `/` operator in Python 3 **always** returns `float`.

### Step 2.2 — Floor Division and Modulo With Negative Numbers

This is a PCAP exam topic. Work through these carefully:

```python
>>> -7 // 2
-4
>>> 7 // -2
-4
>>> -7 // -2
3
```

Why is `-7 // 2` = `-4` and not `-3`?
`-7 / 2 = -3.5`. Floor of `-3.5` is `-4` (the next integer below, toward negative infinity).

```python
>>> -7 % 2
1
>>> 7 % -2
-1
```

Modulo in Python follows the sign of the **divisor** (second number). `-7 % 2` is positive `1` because the divisor `2` is positive. Verify the relationship: `dividend == (dividend // divisor) * divisor + remainder`

```python
>>> (-7 // 2) * 2 + (-7 % 2)
-7
```

The math checks out.

### Step 2.3 — Operator Precedence

**Before running each expression, predict the answer on paper. Then verify in the REPL.**

```python
>>> 2 + 3 * 4
```

Expected: `14` (multiply first: `3 * 4 = 12`, then `2 + 12`)

```python
>>> 10 - 2 ** 3
```

Expected: `2` (exponent first: `2 ** 3 = 8`, then `10 - 8`)

```python
>>> -2 ** 2
```

Expected: `-4` (exponent before unary minus: `2 ** 2 = 4`, then `-(4)`)

```python
>>> (-2) ** 2
```

Expected: `4` (parentheses override: `(-2) ** 2 = 4`)

```python
>>> 2 ** 3 ** 2
```

Expected: `512` (right-associative: `3 ** 2 = 9` first, then `2 ** 9 = 512`)

```python
>>> (2 ** 3) ** 2
```

Expected: `64` (parentheses override: `8 ** 2 = 64`)

```python
>>> 10 % 3 ** 2
```

Expected: `1` (exponent first: `3 ** 2 = 9`, then `10 % 9 = 1`)

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Take a screenshot of your REPL showing the precedence expressions from Step 2.3. Save as `lab02_screenshot_02_precedence.png`.

---

## Part 3 — Write the Circle Calculator Script

### Step 3.1 — Create circle.py

Make sure you are in `~/cis1310/module02/`:

```bash
nano circle.py
```

Type the following:

```python
# circle.py
# Computes area and circumference of a circle
# Demonstrates: operator precedence, math module, float operations
# Module 02 Lab — CIS-1310

import math

# Define the radius
radius = 7

# Calculate area: A = pi * r^2
# Note: ** evaluates before *, so math.pi * radius ** 2 is correct
area = math.pi * radius ** 2

# Calculate circumference: C = 2 * pi * r
circumference = 2 * math.pi * radius

# Display results
print('Circle Calculator')
print('=================')
print('Radius:', radius)
print('Area:', area)
print('Circumference:', circumference)

# Round to 2 decimal places for readability
print('')
print('Rounded Results:')
print('Area:', round(area, 2))
print('Circumference:', round(circumference, 2))
```

Save (Ctrl+O, Enter, Ctrl+X) and run:

```bash
python3 circle.py
```

Expected output:

```text
Circle Calculator
=================
Radius: 7
Area: 153.93804002589985
Circumference: 43.982297150257104

Rounded Results:
Area: 153.94
Circumference: 43.98
```

Notice that `math.pi * radius ** 2` works correctly because `**` evaluates before `*` — Python computes `radius ** 2 = 49` first, then `math.pi * 49`. If you wrote `(math.pi * radius) ** 2`, the result would be completely wrong — that would square the entire product, not just the radius.

### Step 3.2 — Try Different Radius Values

Edit `circle.py` and change the radius value at line 8. Try:

- `radius = 1` — verify area is approximately `3.14`
- `radius = 10` — verify area is approximately `314.16`
- `radius = 0` — verify area is `0.0`

> **SCREENSHOT 3 REQUIRED:** Screenshot of `circle.py` running with your final radius value and correct output. Save as `lab02_screenshot_03_circle.png`.

---

## Part 4 — Write the Temperature Converter Script

### Step 4.1 — Create temp_converter.py

```bash
nano temp_converter.py
```

Type the following:

```python
# temp_converter.py
# Converts temperatures between Fahrenheit, Celsius, and Kelvin
# Demonstrates: arithmetic expressions, operator precedence, round()
# Module 02 Lab — CIS-1310

# Starting temperature in Fahrenheit
fahrenheit = 98.6

# Convert Fahrenheit to Celsius: C = (F - 32) * 5 / 9
# Parentheses are required here — (F - 32) must happen before multiplying
celsius = (fahrenheit - 32) * 5 / 9

# Convert Celsius to Kelvin: K = C + 273.15
kelvin = celsius + 273.15

# Display results
print('Temperature Converter')
print('=====================')
print('Fahrenheit:', fahrenheit)
print('Celsius:', round(celsius, 2))
print('Kelvin:', round(kelvin, 2))

print('')

# Test a few standard temperatures
temps_f = [32, 212, 98.6, -40]

for f in temps_f:
    c = (f - 32) * 5 / 9
    print(f'{f}°F = {round(c, 2)}°C')
```

Save and run:

```bash
python3 temp_converter.py
```

Expected output:

```text
Temperature Converter
=====================
Fahrenheit: 98.6
Celsius: 37.0
Kelvin: 310.15

32°F = 0.0°C
212°F = 100.0°C
98.6°F = 37.0°C
-40°F = -40.0°C
```

Verify the results manually:

- 32°F = 0°C (water freezes) — correct
- 212°F = 100°C (water boils) — correct
- -40°F = -40°C (where the scales meet) — correct

Notice the f-string syntax `f'{f}°F = {round(c, 2)}°C'` — curly braces `{}` insert variable values directly into the string. We cover f-strings in detail in Module 03.

> **SCREENSHOT 4 REQUIRED:** Screenshot of `temp_converter.py` running with the correct output. Save as `lab02_screenshot_04_temp_converter.png`.

---

## Part 5 — Type Conversion Exercises

### Step 5.1 — Create type_conversion.py

```bash
nano type_conversion.py
```

Type the following:

```python
# type_conversion.py
# Demonstrates Python's built-in type conversion functions
# Module 02 Lab — CIS-1310

print('=== int() Conversions ===')
print(int(3.9))          # 3 — truncates, does NOT round
print(int(3.1))          # 3 — truncates
print(int(-3.9))         # -3 — truncates toward zero
print(int('42'))         # 42 — converts digit string
print(int('0b1010', 2))  # 10 — binary string to int

print('')
print('=== float() Conversions ===')
print(float(5))          # 5.0
print(float('3.14'))     # 3.14
print(float('1e3'))      # 1000.0

print('')
print('=== str() Conversions ===')
print(str(42))           # '42'
print(str(3.14))         # '3.14'
print(str(True))         # 'True'
print(str(None))         # 'None'

print('')
print('=== bool() Conversions — Truthiness ===')
print(bool(0))           # False — zero is falsy
print(bool(1))           # True
print(bool(-5))          # True — any non-zero number is truthy
print(bool(''))          # False — empty string is falsy
print(bool('hello'))     # True — non-empty string is truthy
print(bool(None))        # False — None is falsy
```

Save and run:

```bash
python3 type_conversion.py
```

Expected output:

```text
=== int() Conversions ===
3
3
-3
42
10

=== float() Conversions ===
5.0
3.14
1000.0

=== str() Conversions ===
42
3.14
True
None

=== bool() Conversions — Truthiness ===
False
True
True
False
True
False
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `type_conversion.py` running with correct output. Save as `lab02_screenshot_05_type_conversion.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 02 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab02_screenshot_01_literals.png` | REPL showing `0.1 + 0.2` and `True + True` results |
| 2 | `lab02_screenshot_02_precedence.png` | REPL showing all precedence expressions from Step 2.3 |
| 3 | `lab02_screenshot_03_circle.png` | `circle.py` running with correct output |
| 4 | `lab02_screenshot_04_temp_converter.png` | `temp_converter.py` running with correct output |
| 5 | `lab02_screenshot_05_type_conversion.png` | `type_conversion.py` running with correct output |

---

## Part 9 — Challenge Exercise

These steps are optional and ungraded. They explore operator behavior at a deeper level suitable for PCAP exam preparation.

### Challenge 9.1 — Build a Comprehensive Operator Truth Table

Create a script that systematically demonstrates every edge case of Python's arithmetic operators with both positive and negative operands:

```bash
nano ~/cis1310/module02/operator_deep_dive.py
```

Write a script that prints the result of every combination below in a formatted table:

- `7 // 3`, `7 // -3`, `-7 // 3`, `-7 // -3`
- `7 % 3`, `7 % -3`, `-7 % 3`, `-7 % -3`
- For each result, verify the invariant: `(a // b) * b + (a % b) == a`

Your output should display each expression, its result, and a `PASS`/`FAIL` indicator for the invariant check. This pattern of systematic operator verification is directly tested on PCAP scenario questions.

---

### Challenge 9.2 — Implement a Precision-Safe Floating-Point Comparator

The standard advice is "never use `==` for floats — use a tolerance." Write a function `float_eq(a, b, tolerance=1e-9)` that returns `True` if two floats are within `tolerance` of each other, and a test script that demonstrates:

1. `float_eq(0.1 + 0.2, 0.3)` returns `True`
2. `float_eq(0.1 + 0.2, 0.3, tolerance=0)` returns `False` (exact comparison)
3. `float_eq(1.0, 1.0000000001)` returns `True` with default tolerance
4. `float_eq(1.0, 1.001)` returns `False` with default tolerance

Save as `~/cis1310/module02/float_comparator.py`. This pattern is used in production code (e.g., `math.isclose()`, which is the standard library implementation of this exact idea — compare your implementation to `math.isclose(a, b)` and verify they agree).

---

### Challenge 9.3 — Number Base Converter

Write a script `~/cis1310/module02/base_converter.py` that accepts an integer and prints its representation in all four number systems Python supports:

```python
def show_bases(n):
    print(f'Decimal:     {n}')
    print(f'Binary:      {bin(n)}')
    print(f'Octal:       {oct(n)}')
    print(f'Hexadecimal: {hex(n)}')
```

Call `show_bases()` for the values: `0`, `10`, `15`, `16`, `255`, `256`, and `65535`. Study the output and explain in a comment why `255` is significant in both binary (`0b11111111`) and hexadecimal (`0xFF`) contexts (hint: it is the maximum value of a single byte — the foundation of color values in RGB, IP address octets, and memory addressing).

---

## Troubleshooting Guide

**`import math` causes `ModuleNotFoundError`.**
`math` is a Python standard library module — it should always be available. If you see this error, verify you are running `python3`, not `python` (Python 2 also has `math`, but this would indicate an environment issue).

**`int('3.14')` raises `ValueError`.**
This is expected behavior — `int()` cannot directly convert a float-format string. Use `int(float('3.14'))` for a two-step conversion.

**f-strings cause `SyntaxError`.**
f-strings require Python 3.6+. Verify your version with `python3 --version`. If you are below 3.6, use `str.format()` instead: `'{:.2f}'.format(celsius)`.

**nano does not open.**
Run `sudo apt install nano -y` to install it.

**Results don't match expected output.**
Common cause: wrong parentheses placement in the formula. For temperature conversion, `(fahrenheit - 32) * 5 / 9` — the subtraction MUST be inside parentheses. Without them, `fahrenheit - 32 * 5 / 9` computes `32 * 5 / 9` first, giving the wrong result entirely.
