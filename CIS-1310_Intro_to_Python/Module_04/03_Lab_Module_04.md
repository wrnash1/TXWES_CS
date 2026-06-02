# Lab Activity: Module 04 — Control Flow: Conditional Statements

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 60–75 minutes

---

## Overview

In this lab you will practice Boolean expressions with all six relational operators, combine conditions with logical operators, observe short-circuit evaluation stopping execution, explore truthiness with every falsy value, and build three complete interactive programs: a grade calculator, a login validator, and a season checker. You will also intentionally write a mis-ordered `elif` chain to observe the silent logic error it produces.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.
- `~/cis1310/module03` directory and its files exist from Module 03.

---

## Setup

```bash
cd ~/cis1310
mkdir module04
cd module04
```

---

## Part 1 — Relational Operators in the REPL

```bash
python3
```

### Step 1.1 — Test All Six Operators

Type each expression and observe the result. Predict the output before pressing Enter.

```python
>>> 10 > 5
True
>>> 10 < 5
False
>>> 10 >= 10
True
>>> 10 <= 9
False
>>> 10 == 10
True
>>> 10 != 10
False
```

### Step 1.2 — The = vs == Distinction

```python
>>> x = 10
>>> x == 10
True
>>> x == 20
False
>>> x == '10'
False
```

Note: `10 == '10'` is `False`. An integer and a string are never equal even if their string representations match.

### Step 1.3 — Comparing Strings

```python
>>> 'apple' == 'apple'
True
>>> 'apple' == 'Apple'
False
>>> 'b' > 'a'
True
>>> 'Z' < 'a'
True
```

String comparisons use Unicode code-point values. Uppercase letters have lower values than lowercase letters — `'Z'` (90) is less than `'a'` (97).

### Step 1.4 — Chained Comparisons

```python
>>> score = 85
>>> 0 <= score <= 100
True
>>> score = -5
>>> 0 <= score <= 100
False
>>> score = 105
>>> 0 <= score <= 100
False
>>> x = 5
>>> 1 < x < 10
True
>>> 1 < x < 4
False
```

Exit the REPL:

```python
>>> exit()
```

---

## Part 2 — Logical Operators and Short-Circuit Evaluation

```bash
python3
```

### Step 2.1 — and, or, not

```python
>>> age = 20
>>> age >= 18 and age < 65
True
>>> age < 18 or age >= 65
False
>>> not (age >= 18)
False
>>> not False
True
>>> True and False
False
>>> True or False
True
>>> False or False
False
```

### Step 2.2 — Compound Conditions

```python
>>> score = 78
>>> score >= 70 and score < 80
True
>>> score < 60 or score >= 90
False
>>> not (score >= 60)
False
```

### Step 2.3 — Short-Circuit Evaluation Demo

This is the key demo. Watch carefully:

```python
>>> x = 0
>>> x != 0 and 10 / x > 1
False
```

Expected behavior: `x != 0` is `False`, so Python short-circuits. It never evaluates `10 / x`. If it did, you would get `ZeroDivisionError`.

Now force evaluation of the right side:

```python
>>> x = 0
>>> 10 / x > 1
```

Expected:

```text
ZeroDivisionError: division by zero
```

Confirm `or` short-circuits too:

```python
>>> x = 5
>>> x > 0 or 10 / 0 > 1
True
```

`x > 0` is `True`, so Python short-circuits and never evaluates `10 / 0`.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the short-circuit evaluation demo from Step 2.3 — both the safe `and` example and the `ZeroDivisionError` from direct evaluation. Save as `lab04_screenshot_01_short_circuit.png`.

---

## Part 3 — Truthiness Exploration

```bash
python3
```

### Step 3.1 — Test Every Falsy Value

```python
>>> bool(False)
False
>>> bool(None)
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool('')
False
>>> bool([])
False
>>> bool({})
False
>>> bool(())
False
```

### Step 3.2 — Truthy Values

```python
>>> bool(True)
True
>>> bool(1)
True
>>> bool(-1)
True
>>> bool(0.001)
True
>>> bool('hello')
True
>>> bool(' ')
True
>>> bool([0])
True
```

Note: `' '` (a string containing a single space) is truthy — it is not empty. `bool([0])` is truthy — the list is not empty, even though its only element is `0`.

### Step 3.3 — Truthiness in Conditions

```python
>>> name = ''
>>> if name:
...     print(f'Hello, {name}')
... else:
...     print('No name entered.')
...
No name entered.

>>> name = 'Alice'
>>> if name:
...     print(f'Hello, {name}')
... else:
...     print('No name entered.')
...
Hello, Alice

>>> items = []
>>> if items:
...     print(f'You have {len(items)} items.')
... else:
...     print('No items.')
...
No items.
```

Exit the REPL:

```python
>>> exit()
```

---

## Part 4 — Write grade_calculator.py

### Step 4.1 — Create the Script

```bash
nano grade_calculator.py
```

```python
# grade_calculator.py
# Grade calculator using if-elif-else with guardian pattern
# Module 04 Lab — CIS-1310

print('=== Grade Calculator ===')
print()

score = float(input('Enter your numeric score (0-100): '))

# Guardian — validate input before proceeding
if score < 0 or score > 100:
    print(f'Error: {score} is not a valid score.')
    print('Please enter a number between 0 and 100.')
else:
    # Assign letter grade — conditions ordered high-to-low
    if score >= 90:
        grade = 'A'
        message = 'Excellent work!'
    elif score >= 80:
        grade = 'B'
        message = 'Good work.'
    elif score >= 70:
        grade = 'C'
        message = 'Satisfactory.'
    elif score >= 60:
        grade = 'D'
        message = 'Needs improvement.'
    else:
        grade = 'F'
        message = 'Please see your instructor.'

    # Ternary for pass/fail
    passed = 'Yes' if score >= 60 else 'No'

    print()
    print(f'  Score:   {score:.1f}')
    print(f'  Grade:   {grade}')
    print(f'  Passed:  {passed}')
    print(f'  Note:    {message}')
```

Save and run:

```bash
python3 grade_calculator.py
```

Test run 1 — valid score:

```text
=== Grade Calculator ===

Enter your numeric score (0-100): 88

  Score:   88.0
  Grade:   B
  Passed:  Yes
  Note:    Good work.
```

Test run 2 — boundary (exactly 90):

```text
Enter your numeric score (0-100): 90

  Score:   90.0
  Grade:   A
  Passed:  Yes
  Note:    Excellent work!
```

Test run 3 — failing score:

```text
Enter your numeric score (0-100): 55

  Score:   55.0
  Grade:   F
  Passed:  No
  Note:    Please see your instructor.
```

Test run 4 — invalid input (guardian fires):

```text
Enter your numeric score (0-100): -10

Error: -10.0 is not a valid score.
Please enter a number between 0 and 100.
```

### Step 4.2 — Demonstrate the elif Ordering Bug

Open a new file to show what happens when `elif` conditions are ordered wrong:

```bash
nano grade_bug.py
```

```python
# grade_bug.py
# INTENTIONAL BUG — wrong elif order to observe the problem
# Module 04 Lab — CIS-1310

score = float(input('Enter score: '))

# BUG: conditions ordered smallest first — every score >= 60 gets 'D'
if score >= 60:
    grade = 'D'
elif score >= 70:
    grade = 'C'
elif score >= 80:
    grade = 'B'
elif score >= 90:
    grade = 'A'
else:
    grade = 'F'

print(f'Grade: {grade}')
```

Run it and enter `95`:

```text
Enter score: 95
Grade: D
```

A score of 95 gets 'D' because `95 >= 60` is True — it hits the first branch and stops. This is a **silent logic error** — Python does not raise an error or warning. The program runs and produces wrong output without any complaint.

> **SCREENSHOT 2 REQUIRED:** Screenshot showing `grade_calculator.py` running with at least two different inputs (one passing, one failing OR one invalid). Save as `lab04_screenshot_02_grade_calculator.png`.

---

## Part 5 — Write login_validator.py

This program demonstrates the guardian pattern with multiple validation conditions.

### Step 5.1 — Create the Script

```bash
nano login_validator.py
```

```python
# login_validator.py
# Demonstrates guardian pattern with multiple validation checks
# Module 04 Lab — CIS-1310

print('=== Login Validator ===')
print()

username = input('Enter username: ')
password = input('Enter password: ')

# Guardian — validate username
if len(username) < 3:
    print('Error: Username must be at least 3 characters.')
elif len(username) > 20:
    print('Error: Username must not exceed 20 characters.')
# Guardian — validate password
elif len(password) < 8:
    print('Error: Password must be at least 8 characters.')
elif ' ' in password:
    print('Error: Password must not contain spaces.')
else:
    # Only reach here if all validations pass
    print()
    print(f'  Username: {username}')
    print(f'  Password: {"*" * len(password)}')
    print()
    print('  Input accepted. Credentials valid format.')
```

Save and run:

```bash
python3 login_validator.py
```

Test run 1 — valid credentials:

```text
=== Login Validator ===

Enter username: jsmith
Enter password: securePass1

  Username: jsmith
  Password: ***********

  Input accepted. Credentials valid format.
```

Test run 2 — username too short:

```text
Enter username: ab
Enter password: securePass1
Error: Username must be at least 3 characters.
```

Test run 3 — password too short:

```text
Enter username: jsmith
Enter password: pass
Error: Password must be at least 8 characters.
```

Test run 4 — password with space:

```text
Enter username: jsmith
Enter password: my password
Error: Password must not contain spaces.
```

Notice: `' ' in password` uses the `in` operator to check whether a space character exists anywhere inside the password string. `in` returns `True` or `False` — making it a valid Boolean expression for an `if` condition.

> **SCREENSHOT 3 REQUIRED:** Screenshot showing `login_validator.py` running with one valid and one invalid input. Save as `lab04_screenshot_03_login_validator.png`.

---

## Part 6 — Write season_checker.py

This program demonstrates chained comparisons for range testing.

### Step 6.1 — Create the Script

```bash
nano season_checker.py
```

```python
# season_checker.py
# Determines season from month number using chained comparisons
# Module 04 Lab — CIS-1310

print('=== Season Checker ===')
print()

month = int(input('Enter month number (1-12): '))

# Guardian — validate range
if not (1 <= month <= 12):
    print(f'Error: {month} is not a valid month number.')
    print('Enter a number from 1 (January) through 12 (December).')
else:
    # Determine season using chained comparisons
    if month == 12 or 1 <= month <= 2:
        season = 'Winter'
    elif 3 <= month <= 5:
        season = 'Spring'
    elif 6 <= month <= 8:
        season = 'Summer'
    else:
        season = 'Fall'

    # Map month number to name
    month_names = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]
    month_name = month_names[month - 1]

    print(f'  Month:   {month_name} ({month})')
    print(f'  Season:  {season}')
```

Save and run:

```bash
python3 season_checker.py
```

Test run 1 — month 7 (July):

```text
=== Season Checker ===

Enter month number (1-12): 7
  Month:   July (7)
  Season:  Summer
```

Test run 2 — month 12 (December):

```text
Enter month number (1-12): 12
  Month:   December (12)
  Season:  Winter
```

Test run 3 — month 1 (January):

```text
Enter month number (1-12): 1
  Month:   January (1)
  Season:  Winter
```

Test run 4 — invalid:

```text
Enter month number (1-12): 15
Error: 15 is not a valid month number.
Enter a number from 1 (January) through 12 (December).
```

Notice the guardian uses `not (1 <= month <= 12)`. The chained comparison `1 <= month <= 12` checks whether month is in range, and `not` flips it to detect out-of-range.

> **SCREENSHOT 4 REQUIRED:** Screenshot of `season_checker.py` running with at least three different valid months showing different seasons. Save as `lab04_screenshot_04_season_checker.png`.

---

## Part 7 — Ternary Expression Practice

```bash
python3
```

### Step 7.1 — Basic Ternary

```python
>>> score = 75
>>> result = 'pass' if score >= 60 else 'fail'
>>> result
'pass'

>>> score = 45
>>> result = 'pass' if score >= 60 else 'fail'
>>> result
'fail'
```

### Step 7.2 — Ternary in an f-string

```python
>>> age = 17
>>> print(f'Status: {"adult" if age >= 18 else "minor"}')
Status: minor

>>> age = 21
>>> print(f'Status: {"adult" if age >= 18 else "minor"}')
Status: adult
```

### Step 7.3 — Rewrite a Two-Line if-else as a Ternary

Original two-line form:

```python
>>> n = 7
>>> if n % 2 == 0:
...     label = 'even'
... else:
...     label = 'odd'
...
>>> label
'odd'
```

Equivalent ternary form:

```python
>>> label = 'even' if n % 2 == 0 else 'odd'
>>> label
'odd'
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of REPL showing the ternary expression examples from Step 7.2 and 7.3. Save as `lab04_screenshot_05_ternary.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 04 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab04_screenshot_01_short_circuit.png` | Short-circuit demo — safe `and` and `ZeroDivisionError` |
| 2 | `lab04_screenshot_02_grade_calculator.png` | `grade_calculator.py` with two different inputs |
| 3 | `lab04_screenshot_03_login_validator.png` | `login_validator.py` with valid and invalid input |
| 4 | `lab04_screenshot_04_season_checker.png` | `season_checker.py` with three different months |
| 5 | `lab04_screenshot_05_ternary.png` | REPL ternary expression examples |

---

## Troubleshooting Guide

**`SyntaxError: invalid syntax` on an `elif` line.**
Check whether you wrote `else if` (two words) instead of `elif` (one word). Python requires `elif` as a single keyword.

**Grade calculator gives wrong grades for high scores.**
Check your `elif` order. Conditions must go from highest to lowest (`>= 90` first, then `>= 80`, etc.). If you start with `>= 60`, every score above 60 hits the first branch.

**`ZeroDivisionError` even with short-circuit protection.**
Make sure the guard condition is on the left side of `and`. `10 / x > 1 and x != 0` evaluates `10 / x` first — the guard needs to come before the potentially dangerous operation.

**`NameError: name 'grade' is not defined` after if-elif-else.**
This happens when none of your conditions matched and there is no `else` branch — so `grade` was never assigned. Add an `else` clause or trace your conditions carefully.

**`login_validator.py` accepts a short password when it should reject it.**
Check the order of your `elif` conditions. If the username guard matches first, the password check is never reached — this is correct behavior. If both should fail, the first failing condition wins.
