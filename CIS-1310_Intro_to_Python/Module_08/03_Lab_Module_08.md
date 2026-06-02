# Lab Activity: Module 08 — Functions and Parameter Passing

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 70–85 minutes

---

## Overview

In this lab you will define and call functions with positional and keyword parameters, use default argument values, write functions that return single and multiple values, demonstrate that functions without `return` return `None`, use `*args` and `**kwargs`, explore local vs. global scope, observe the mutable default argument trap, add docstrings, and build a complete calculator program.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module08
cd module08
```

---

## Part 1 — Basic Function Definitions

```bash
python3
```

### Step 1.1 — Function With No Parameters

```python
>>> def greet():
...     print('Hello, World!')
...
>>> greet()
Hello, World!
>>> greet()
Hello, World!
```

The function runs each time it is called.

### Step 1.2 — Function With a Parameter

```python
>>> def greet(name):
...     print(f'Hello, {name}!')
...
>>> greet('Alice')
Hello, Alice!
>>> greet('Bob')
Hello, Bob!
```

### Step 1.3 — Return Values

```python
>>> def square(n):
...     return n ** 2
...
>>> result = square(5)
>>> result
25
>>> print(square(7))
49
>>> square(3) + square(4)
25
```

### Step 1.4 — Function Returns None Without return

```python
>>> def show(x):
...     print(x)
...
>>> result = show(42)
42
>>> print(result)
None
>>> type(result)
<class 'NoneType'>
```

The function printed `42` (side effect), but it returned `None` because there is no `return` statement.

### Step 1.5 — Multiple Return Values

```python
>>> def min_max(numbers):
...     return min(numbers), max(numbers)
...
>>> low, high = min_max([88, 72, 95, 61, 83])
>>> low
61
>>> high
95
>>> result = min_max([5, 3, 9, 1])
>>> type(result)
<class 'tuple'>
>>> result
(1, 9)
```

Multiple return values are packed into a tuple.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the None return from Step 1.4 and the multiple return values from Step 1.5. Save as `lab08_screenshot_01_functions_return.png`.

---

## Part 2 — Default and Keyword Arguments

```bash
python3
```

### Step 2.1 — Default Parameters

```python
>>> def greet(name, greeting='Hello'):
...     print(f'{greeting}, {name}!')
...
>>> greet('Alice')
Hello, Alice!
>>> greet('Bob', 'Hi')
Hi, Bob!
>>> greet('Carol', greeting='Good morning')
Good morning, Carol!
```

### Step 2.2 — SyntaxError: Default Before Non-Default

```python
>>> def bad(a=1, b):
...     pass
...
```

Expected:

```text
SyntaxError: non-default argument follows default argument
```

Default parameters must come after non-default parameters.

### Step 2.3 — Keyword Arguments in Any Order

```python
>>> def describe(name, age, city):
...     print(f'{name}, age {age}, from {city}')
...
>>> describe('Alice', 30, 'Dallas')
Alice, age 30, from Dallas
>>> describe(age=30, city='Dallas', name='Alice')
Alice, age 30, from Dallas
>>> describe('Bob', city='Austin', age=25)
Bob, age 25, from Austin
```

### Step 2.4 — SyntaxError: Positional After Keyword

```python
>>> describe(name='Alice', 30, 'Dallas')
```

Expected:

```text
SyntaxError: positional argument follows keyword argument
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing the SyntaxError from Step 2.2 (default before non-default) and Step 2.4 (positional after keyword). Save as `lab08_screenshot_02_parameter_errors.png`.

---

## Part 3 — *args and **kwargs

```bash
python3
```

### Step 3.1 — *args

```python
>>> def total(*args):
...     print(f'args = {args}')
...     print(f'type = {type(args)}')
...     return sum(args)
...
>>> total(1, 2, 3)
args = (1, 2, 3)
type = <class 'tuple'>
6
>>> total(10, 20, 30, 40)
args = (10, 20, 30, 40)
type = <class 'tuple'>
100
>>> total()
args = ()
type = <class 'tuple'>
0
```

### Step 3.2 — **kwargs

```python
>>> def show_info(**kwargs):
...     print(f'kwargs = {kwargs}')
...     print(f'type = {type(kwargs)}')
...     for key, value in kwargs.items():
...         print(f'  {key}: {value}')
...
>>> show_info(name='Alice', age=30, city='Dallas')
kwargs = {'name': 'Alice', 'age': 30, 'city': 'Dallas'}
type = <class 'dict'>
  name: Alice
  age: 30
  city: Dallas
```

### Step 3.3 — Combining Parameter Types

```python
>>> def mixed(a, b, *args, x=0, **kwargs):
...     print(f'a={a}, b={b}, args={args}, x={x}, kwargs={kwargs}')
...
>>> mixed(1, 2, 3, 4, 5, x=10, y=20, z=30)
a=1, b=2, args=(3, 4, 5), x=10, kwargs={'y': 20, 'z': 30}
```

Trace: `a=1` (positional), `b=2` (positional), `(3, 4, 5)` → `*args` (extra positional), `x=10` (keyword-only), `y=20, z=30` → `**kwargs`.

Exit the REPL:

```python
>>> exit()
```

---

## Part 4 — Scope

```bash
python3
```

### Step 4.1 — Local vs. Global

```python
>>> x = 10

>>> def change():
...     x = 99    # local — new variable, does not affect global
...     print(f'Inside: x = {x}')
...
>>> change()
Inside: x = 99
>>> print(f'Outside: x = {x}')
Outside: x = 10
```

The `x` inside `change()` is a separate local variable. The global `x` is unchanged.

### Step 4.2 — global Keyword

```python
>>> count = 0
>>> def increment():
...     global count
...     count += 1
...
>>> increment()
>>> increment()
>>> increment()
>>> count
3
```

Without `global count`, the assignment `count += 1` would create a local `count` and raise `UnboundLocalError` (Python sees the assignment and treats `count` as local, then tries to read it before assignment).

### Step 4.3 — Mutable Default Argument Trap

```python
>>> def append_item(item, lst=[]):
...     lst.append(item)
...     return lst
...
>>> append_item('a')
['a']
>>> append_item('b')
['a', 'b']
>>> append_item('c')
['a', 'b', 'c']
```

The default list `[]` is created once at function definition time and shared across all calls. This is a well-known Python gotcha. The fix:

```python
>>> def append_item_safe(item, lst=None):
...     if lst is None:
...         lst = []
...     lst.append(item)
...     return lst
...
>>> append_item_safe('a')
['a']
>>> append_item_safe('b')
['b']
>>> append_item_safe('c')
['c']
```

Now each call with no `lst` argument gets a fresh empty list.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 3 REQUIRED:** Screenshot showing the mutable default argument trap from Step 4.3 — both the buggy version and the fixed version. Save as `lab08_screenshot_03_mutable_default.png`.

---

## Part 5 — Docstrings and Type Hints

```bash
nano documented_functions.py
```

```python
# documented_functions.py
# Demonstrates docstrings and type hints
# Module 08 Lab — CIS-1310

import math


def circle_area(radius: float) -> float:
    '''Calculate the area of a circle.

    Args:
        radius: The radius of the circle (must be non-negative).
    Returns:
        The area as a float.
    Raises:
        ValueError: If radius is negative.
    '''
    if radius < 0:
        raise ValueError(f'Radius cannot be negative: {radius}')
    return math.pi * radius ** 2


def celsius_to_fahrenheit(celsius: float) -> float:
    '''Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.
    Returns:
        Temperature in degrees Fahrenheit.
    '''
    return celsius * 9 / 5 + 32


def describe_person(name: str, age: int, city: str = 'Unknown') -> str:
    '''Build a description string for a person.

    Args:
        name: The person's name.
        age: The person's age in years.
        city: The person's city of residence (default 'Unknown').
    Returns:
        A formatted description string.
    '''
    return f'{name}, age {age}, from {city}'


# --- Test the functions
if __name__ == '__main__':
    print(f'Circle area (r=5): {circle_area(5):.4f}')
    print(f'32°C in Fahrenheit: {celsius_to_fahrenheit(32):.1f}')
    print(describe_person('Alice', 30, 'Dallas'))
    print(describe_person('Bob', 25))

    # Access the docstring
    print()
    print('Docstring for circle_area:')
    print(circle_area.__doc__)
```

Save and run:

```bash
python3 documented_functions.py
```

Expected output:

```text
Circle area (r=5): 78.5398
32°C in Fahrenheit: 89.6
Alice, age 30, from Dallas
Bob, age 25, from Unknown

Docstring for circle_area:
Calculate the area of a circle.

    Args:
        radius: The radius of the circle (must be non-negative).
    Returns:
        The area as a float.
    Raises:
        ValueError: If radius is negative.
```

---

## Part 6 — Write calculator.py

### Step 6.1 — Create the Script

```bash
nano calculator.py
```

```python
# calculator.py
# Interactive calculator using dispatch table and functions
# Module 08 Lab — CIS-1310


def add(a: float, b: float) -> float:
    '''Return a + b.'''
    return a + b


def subtract(a: float, b: float) -> float:
    '''Return a - b.'''
    return a - b


def multiply(a: float, b: float) -> float:
    '''Return a * b.'''
    return a * b


def divide(a: float, b: float) -> float:
    '''Return a / b. Raises ValueError for division by zero.'''
    if b == 0:
        raise ValueError('Division by zero is undefined.')
    return a / b


def calculate(a: float, op: str, b: float) -> float:
    '''Dispatch an arithmetic operation.

    Args:
        a: Left operand.
        op: Operator string: '+', '-', '*', '/'.
        b: Right operand.
    Returns:
        The result of the operation.
    Raises:
        ValueError: For unknown operator or division by zero.
    '''
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    if op not in operations:
        raise ValueError(f'Unknown operator: "{op}". Use +, -, *, /')
    return operations[op](a, b)


def main():
    '''Run the interactive calculator loop.'''
    print('=== Calculator ===')
    print('Enter an expression like:  5 + 3   or   10.5 * 2')
    print('Type "q" to quit.')
    print()

    while True:
        expr = input('> ').strip()
        if expr.lower() == 'q':
            print('Goodbye.')
            break

        parts = expr.split()
        if len(parts) != 3:
            print('  Error: Enter exactly three items — number operator number')
            continue

        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
            result = calculate(a, op, b)
            print(f'  = {result}')
        except ValueError as e:
            print(f'  Error: {e}')


main()
```

Save and run:

```bash
python3 calculator.py
```

Sample interaction:

```text
=== Calculator ===
Enter an expression like:  5 + 3   or   10.5 * 2
Type "q" to quit.

> 5 + 3
  = 8.0
> 10 * 2.5
  = 25.0
> 9 / 3
  = 3.0
> 5 / 0
  Error: Division by zero is undefined.
> 5 @ 3
  Error: Unknown operator: "@". Use +, -, *, /
> q
Goodbye.
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `calculator.py` running with at least 4 operations including one error. Save as `lab08_screenshot_04_calculator.png`.

---

## Part 7 — *args Statistics Function

```bash
nano stats.py
```

```python
# stats.py
# Demonstrates *args for variable-length input
# Module 08 Lab — CIS-1310


def statistics(*scores: float) -> dict:
    '''Compute basic statistics for any number of scores.

    Args:
        *scores: Any number of numeric scores.
    Returns:
        A dict with count, total, average, minimum, maximum.
    '''
    if not scores:
        return {'count': 0, 'total': 0, 'average': 0.0, 'minimum': None, 'maximum': None}

    total = sum(scores)
    count = len(scores)

    return {
        'count': count,
        'total': total,
        'average': total / count,
        'minimum': min(scores),
        'maximum': max(scores),
    }


# Test with different numbers of arguments
test_cases = [
    (90,),
    (88, 72, 95),
    (88, 72, 95, 61, 83, 90, 77),
    (),
]

for case in test_cases:
    result = statistics(*case)
    print(f'Input: {case}')
    for key, val in result.items():
        if isinstance(val, float):
            print(f'  {key}: {val:.2f}')
        else:
            print(f'  {key}: {val}')
    print()
```

Save and run:

```bash
python3 stats.py
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `stats.py` running showing all four test cases. Save as `lab08_screenshot_05_stats.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 08 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab08_screenshot_01_functions_return.png` | None return and multiple return values |
| 2 | `lab08_screenshot_02_parameter_errors.png` | SyntaxError for bad parameter ordering |
| 3 | `lab08_screenshot_03_mutable_default.png` | Mutable default trap and safe fix |
| 4 | `lab08_screenshot_04_calculator.png` | `calculator.py` with multiple operations including errors |
| 5 | `lab08_screenshot_05_stats.png` | `stats.py` with all four test cases |

---

## Troubleshooting Guide

**`SyntaxError: non-default argument follows default argument`.**
Default parameters must come last. Change `def f(a=1, b)` to `def f(b, a=1)`.

**Function returns None when you expected a value.**
Check that your `return` statement is inside the function body (indented correctly) and is not unreachable. Also check that you are not accidentally calling the function inside `print()` when you meant to assign the return value.

**Mutable default argument accumulates values across calls.**
Use `None` as the default and create the mutable object inside the function: `if lst is None: lst = []`.

**`UnboundLocalError` when using global variable.**
If you assign to a variable inside a function, Python treats it as local throughout the entire function — even for reads before the assignment. Add `global varname` at the top of the function body, or redesign the function to use parameters.

**`calculator.py` expression not parsed.**
The parser splits on whitespace. `5+3` (no spaces) produces a single token, not three. Users must enter spaces around the operator: `5 + 3`.
