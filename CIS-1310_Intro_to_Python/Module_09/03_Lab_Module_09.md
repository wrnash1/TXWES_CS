# Lab Activity: Module 09 — Scopes, Namespaces, and Recursion

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 75–90 minutes

---

## Overview

In this lab you will trace Python's LEGB name lookup order in nested functions, use `nonlocal` to modify enclosing scope variables, build closure factories, write and trace recursive functions, trigger and observe `RecursionError`, inspect namespaces with `locals()` and `globals()`, and build a combined demonstration program.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module09
cd module09
```

---

## Part 1 — LEGB Scope Lookup

```bash
python3
```

### Step 1.1 — Three-Level Nested Functions

```python
>>> x = 'global'
...
>>> def outer():
...     x = 'enclosing'
...     def inner():
...         x = 'local'
...         print('inner sees:', x)
...     inner()
...     print('outer sees:', x)
...
>>> outer()
inner sees: local
outer sees: enclosing
>>> print('module sees:', x)
module sees: global
```

Each scope has its own `x`. The assignments in `inner` and `outer` do not affect the global `x`.

### Step 1.2 — Reading a Global Without global

```python
>>> name = 'Alice'
...
>>> def greet():
...     print('Hello,', name)    # no local 'name' → walks up to global
...
>>> greet()
Hello, Alice
```

Reading a global variable requires no declaration. Python finds it through LEGB automatically.

### Step 1.3 — UnboundLocalError Trap

```python
>>> value = 100
...
>>> def broken():
...     print(value)    # Python sees assignment below — treats value as local everywhere
...     value = 200
...
>>> broken()
```

Expected:

```text
UnboundLocalError: local variable 'value' referenced before assignment
```

Once Python sees `value = 200` inside the function, it marks `value` as local throughout the entire function — even for the `print` above the assignment. The fix is either to rename the local variable or to use `global value`.

### Step 1.4 — Accidentally Shadowing a Built-in

```python
>>> len([1, 2, 3])
3
>>> len = 'I overwrote len'
>>> len([1, 2, 3])
```

Expected:

```text
TypeError: 'str' object is not callable
```

Restore the built-in:

```python
>>> del len
>>> len([1, 2, 3])
3
```

Never name variables `len`, `list`, `dict`, `str`, `int`, `print`, `type`, or any other built-in name.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the three-level LEGB output from Step 1.1 and the UnboundLocalError from Step 1.3. Save as `lab09_screenshot_01_legb_scope.png`.

---

## Part 2 — nonlocal Keyword and Closures

```bash
python3
```

### Step 2.1 — Make a Counter Closure

```python
>>> def make_counter(start=0, step=1):
...     count = start
...     def increment():
...         nonlocal count
...         count += step
...         return count
...     return increment
...
>>> counter = make_counter()
>>> counter()
1
>>> counter()
2
>>> counter()
3
```

`nonlocal count` tells `increment()` that `count` lives in `make_counter()`'s scope, not in `increment()`'s local scope. Without `nonlocal`, `count += step` would raise `UnboundLocalError` because `count` would be treated as a new, uninitialized local.

### Step 2.2 — Independent Closures Share Nothing

```python
>>> c1 = make_counter(start=0, step=10)
>>> c2 = make_counter(start=100, step=5)
>>> c1()
10
>>> c1()
20
>>> c2()
105
>>> c2()
110
>>> c1()
30
```

`c1` and `c2` each have their own captured `count` — they are completely independent. Calling one does not affect the other.

### Step 2.3 — Closure With Reset

```python
>>> def make_counter_with_reset(start=0, step=1):
...     count = start
...     def increment():
...         nonlocal count
...         count += step
...         return count
...     def reset():
...         nonlocal count
...         count = start
...     return increment, reset
...
>>> inc, rst = make_counter_with_reset(step=5)
>>> inc()
5
>>> inc()
10
>>> inc()
15
>>> rst()
>>> inc()
5
```

Both `increment` and `reset` share access to the same `count` in the enclosing scope. `reset()` sets it back to `start`.

### Step 2.4 — Multiplier Factory Closure

```python
>>> def make_multiplier(factor):
...     def multiply(n):
...         return n * factor
...     return multiply
...
>>> double = make_multiplier(2)
>>> triple = make_multiplier(3)
>>> square = make_multiplier.__class__    # just to confirm type
>>> double(7)
14
>>> triple(7)
21
>>> double(10)
20
>>> triple(10)
30
```

Each call to `make_multiplier()` captures its own `factor`. `double` has `factor=2` locked in. `triple` has `factor=3` locked in. The `make_multiplier` function is a **factory** — it produces customized functions.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing the make_counter output from Steps 2.1–2.2 (demonstrating independent closures) and the multiplier factory from Step 2.4. Save as `lab09_screenshot_02_closures.png`.

---

## Part 3 — Recursion Basics

```bash
python3
```

### Step 3.1 — Factorial

```python
>>> def factorial(n):
...     if n == 0:
...         return 1
...     return n * factorial(n - 1)
...
>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(4)
24
>>> factorial(5)
120
>>> factorial(10)
3628800
```

Trace `factorial(4)` manually:

```text
factorial(4) → 4 * factorial(3)
    factorial(3) → 3 * factorial(2)
        factorial(2) → 2 * factorial(1)
            factorial(1) → 1 * factorial(0)
                factorial(0) → 1   (base case)
            → 1 * 1 = 1
        → 2 * 1 = 2
    → 3 * 2 = 6
→ 4 * 6 = 24
```

### Step 3.2 — Recursive Sum of a List

```python
>>> def list_sum(lst):
...     if not lst:
...         return 0
...     return lst[0] + list_sum(lst[1:])
...
>>> list_sum([])
0
>>> list_sum([5])
5
>>> list_sum([1, 2, 3, 4, 5])
15
```

The base case is an empty list (`not lst` is `True` when `lst == []`). The recursive case takes the first element and adds it to the sum of the rest.

### Step 3.3 — Recursive Countdown

```python
>>> def count_down(n):
...     if n < 0:
...         return
...     print(n, end=' ')
...     count_down(n - 1)
...
>>> count_down(5)
5 4 3 2 1 0
```

### Step 3.4 — Fibonacci

```python
>>> def fibonacci(n):
...     if n <= 1:
...         return n
...     return fibonacci(n - 1) + fibonacci(n - 2)
...
>>> for i in range(8):
...     print(fibonacci(i), end=' ')
...
0 1 1 2 3 5 8 13
```

Two base cases: `fibonacci(0) = 0`, `fibonacci(1) = 1`.

### Step 3.5 — RecursionError Demo

```python
>>> def infinite(n):
...     return infinite(n - 1)
...
>>> infinite(1)
```

Expected (after a moment):

```text
RecursionError: maximum recursion depth exceeded
```

Check Python's default limit:

```python
>>> import sys
>>> sys.getrecursionlimit()
1000
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 3 REQUIRED:** Screenshot showing factorial output from Step 3.1, list_sum from Step 3.2, and the RecursionError from Step 3.5. Save as `lab09_screenshot_03_recursion.png`.

---

## Part 4 — Namespaces

```bash
python3
```

### Step 4.1 — globals() and locals()

```python
>>> x = 10
>>> y = 20
>>> 'x' in globals()
True
>>> globals()['x']
10
>>> def show_locals():
...     a = 100
...     b = 200
...     print(locals())
...
>>> show_locals()
{'a': 100, 'b': 200}
```

`globals()` returns a live dictionary of the module namespace. `locals()` returns the local namespace as a snapshot.

### Step 4.2 — Verifying Scope Separation with id()

```python
>>> x = 'module level'
...
>>> def demo():
...     x = 'function level'
...     print('Inside id:', id(x))
...     print('Inside value:', x)
...
>>> demo()
Inside id: ...    (some address)
Inside value: function level
>>> print('Outside id:', id(x))
Outside id: ...   (a different address)
>>> print('Outside value:', x)
Outside value: module level
```

The two `x` variables have different `id()` values — they are different objects in different namespaces.

### Step 4.3 — Inspect the Built-in Namespace

```python
>>> import builtins
>>> type(builtins.__dict__)
<class 'dict'>
>>> 'print' in dir(builtins)
True
>>> 'len' in dir(builtins)
True
```

Python's built-in namespace is just another dictionary accessible via the `builtins` module.

Exit the REPL:

```python
>>> exit()
```

---

## Part 5 — scope_demo.py (Closures + Recursion Combined)

```bash
nano scope_demo.py
```

```python
# scope_demo.py
# Demonstrates closures and recursion together
# Module 09 Lab — CIS-1310


def make_counter(start=0, step=1):
    '''Create a counter closure with optional reset.'''
    count = start

    def increment():
        nonlocal count
        count += step
        return count

    def reset():
        nonlocal count
        count = start

    return increment, reset


def count_down(n):
    '''Recursively print a countdown from n to 0.'''
    if n < 0:
        return
    print(n, end=' ')
    count_down(n - 1)


def factorial(n):
    '''Return n factorial recursively.'''
    if n == 0:
        return 1
    return n * factorial(n - 1)


# --- Counter closure demo
inc, rst = make_counter(start=0, step=5)
print('Counter by 5s:')
print(inc(), inc(), inc(), inc())

rst()
print('After reset:', inc())

# --- Recursion demo
print('\nCountdown from 8:')
count_down(8)
print()

print('\nFactorials 0 through 7:')
for i in range(8):
    print(f'  {i}! = {factorial(i)}')

# --- Namespace inspection
print('\nGlobal namespace (selected keys):')
for key in ['make_counter', 'count_down', 'factorial']:
    print(f'  {key}: {type(globals()[key]).__name__}')
```

Save and run:

```bash
python3 scope_demo.py
```

Expected output:

```text
Counter by 5s:
5 10 15 20
After reset: 5

Countdown from 8:
8 7 6 5 4 3 2 1 0

Factorials 0 through 7:
  0! = 1
  1! = 1
  2! = 2
  3! = 6
  4! = 24
  5! = 120
  6! = 720
  7! = 5040

Global namespace (selected keys):
  make_counter: function
  count_down: function
  factorial: function
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `scope_demo.py` running and showing the complete output. Save as `lab09_screenshot_04_scope_demo.png`.

---

## Part 6 — recursion_demo.py

```bash
nano recursion_demo.py
```

```python
# recursion_demo.py
# Demonstrates multiple recursive patterns
# Module 09 Lab — CIS-1310


def list_sum(lst):
    '''Return the sum of a list using recursion.'''
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])


def fibonacci(n):
    '''Return the nth Fibonacci number using recursion.'''
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def flatten(nested):
    '''Flatten one level of nesting in a list.'''
    if not nested:
        return []
    first = nested[0]
    rest = flatten(nested[1:])
    if isinstance(first, list):
        return first + rest
    return [first] + rest


# --- list_sum
print('list_sum tests:')
print(' ', list_sum([]))
print(' ', list_sum([7]))
print(' ', list_sum([1, 2, 3, 4, 5]))

# --- fibonacci sequence
print('\nFibonacci sequence (n=0 through n=9):')
print(' ', [fibonacci(i) for i in range(10)])

# --- flatten
print('\nFlatten tests:')
print(' ', flatten([1, [2, 3], 4, [5, 6]]))
print(' ', flatten([[10, 20], [30], 40]))

# --- RecursionError demo (safe — caught with try/except)
print('\nRecursionError demo (caught safely):')


def no_base(n):
    return no_base(n - 1)


try:
    no_base(1)
except RecursionError as e:
    print(f'  Caught: {type(e).__name__}')

import sys
print(f'  Default recursion limit: {sys.getrecursionlimit()}')
```

Save and run:

```bash
python3 recursion_demo.py
```

Expected output:

```text
list_sum tests:
  0
  7
  15

Fibonacci sequence (n=0 through n=9):
  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Flatten tests:
  [1, 2, 3, 4, 5, 6]
  [10, 20, 30, 40]

RecursionError demo (caught safely):
  Caught: RecursionError
  Default recursion limit: 1000
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `recursion_demo.py` running and showing the complete output. Save as `lab09_screenshot_05_recursion_demo.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 09 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab09_screenshot_01_legb_scope.png` | Three-level LEGB output and UnboundLocalError |
| 2 | `lab09_screenshot_02_closures.png` | Independent counter closures and multiplier factory |
| 3 | `lab09_screenshot_03_recursion.png` | Factorial, list_sum, and RecursionError |
| 4 | `lab09_screenshot_04_scope_demo.png` | scope_demo.py full output |
| 5 | `lab09_screenshot_05_recursion_demo.png` | recursion_demo.py full output |

---

## Troubleshooting Guide

**UnboundLocalError when reading a global variable inside a function.**
Python marked the variable as local because it sees an assignment to that name somewhere in the function. Either add `global varname` at the top of the function body, or rename the local variable so there is no conflict.

**RecursionError immediately on small inputs.**
Your base case is missing or unreachable. Check the condition: if n starts at 5 and you check `n == 0` but decrement by 2, n will go 5 → 3 → 1 → -1 → -3 ... and never equal 0. Use `n <= 0` for safety.

**nonlocal causes SyntaxError.**
`nonlocal x` requires that `x` already exists in an enclosing function's scope. If the enclosing function does not have a variable named `x`, Python raises `SyntaxError: no binding for nonlocal 'x' found`. Check the spelling and that you defined `x` in the outer function.

**Closure does not remember updated value.**
Make sure you used `nonlocal count` inside the inner function. Without it, `count += 1` creates a new local `count` (and raises `UnboundLocalError`). The `nonlocal` declaration is what links the inner function's `count` to the outer function's `count`.

**fibonacci() takes too long for large n.**
The naive recursive Fibonacci recomputes the same values many times — `fibonacci(40)` makes over a billion calls. Limit your tests to n ≤ 30. For larger values, use iteration or `@functools.lru_cache` (covered in later modules).
