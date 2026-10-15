# Video Script: CIS-1310 — Introduction to Python

## Module 08 — Functions and Parameter Passing

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / Python Institute &bull; Python Programming Full Course &bull; Module 08</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=rfscVS0vtbw" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/rfscVS0vtbw" title="freeCodeCamp / Python Institute &bull; Python Programming Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp / Python Institute &bull; Python Programming Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Opening

Welcome back. We are now at one of the most important modules in the course — functions.

Everything we have built so far works, but every program has been one long linear script. Functions change that. Functions are reusable named blocks of code that you can call from anywhere in your program, any number of times, with different data each time.

A good programmer does not write the same logic twice. They put it in a function and call it. That is the foundation of every professional codebase. The PCAP exam tests function definitions, parameters, default arguments, keyword arguments, return values, and the `*args`/`**kwargs` mechanisms in significant depth. This module covers all of it.

---

## Defining and Calling Functions

A function is defined with the `def` keyword, a name, a parameter list in parentheses, and a colon. The body is indented.

```python
def function_name(parameters):
    body
    return value    # optional
```

```python
def greet():
    print('Hello, World!')

greet()
```

Output:

```text
Hello, World!
```

`greet()` is the **function call** — it executes the body. `def greet():` is the **function definition** — it tells Python what to do when `greet()` is called.

```python
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')
greet('Bob')
```

Output:

```text
Hello, Alice!
Hello, Bob!
```

`name` is a **parameter** — a variable that holds the value passed to the function. `'Alice'` and `'Bob'` are **arguments** — the actual values passed in each call.

Functions can be called as many times as needed with different arguments. The body runs each time.

---

## Return Values

A function that uses `print()` displays output but produces no value. A function that uses `return` sends a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

Output:

```text
8
```

`result = add(3, 5)` calls the function and assigns its **return value** to `result`.

**Multiple return values:**

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([88, 72, 95, 61, 83])
print(f'Low: {low}, High: {high}')
```

Output:

```text
Low: 61, High: 95
```

Returning multiple values works because Python packs them into a tuple — `return min, max` is equivalent to `return (min, max)`. The caller unpacks with `low, high = min_max(...)`.

**Functions that do not return — return None:**

```python
def display(x):
    print(x)

result = display(42)
print(result)
```

Output:

```text
42
None
```

If a function has no `return` statement, or a bare `return` with no value, it returns `None`.

---

## Default Parameters and Keyword Arguments

### Default Parameter Values

You can give a parameter a default value that is used if the caller does not provide one.

```python
def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')
```

```python
>>> greet('Alice')            # uses default greeting
Hello, Alice!
>>> greet('Bob', 'Hi')        # overrides default
Hi, Bob!
>>> greet('Carol', greeting='Good morning')    # keyword argument
Good morning, Carol!
```

**PCAP exam rule:** Default parameters must come after non-default parameters. `def f(a=1, b)` is a `SyntaxError`. `def f(a, b=1)` is valid.

### Keyword Arguments

You can pass arguments by name, in any order:

```python
def describe(name, age, city):
    print(f'{name}, age {age}, from {city}')

describe(age=30, city='Dallas', name='Alice')
```

Output:

```text
Alice, age 30, from Dallas
```

Keyword arguments improve readability, especially for functions with many parameters. You can mix positional and keyword arguments — but positional arguments must come before keyword arguments.

---

## *args and **kwargs

### *args — Collect Extra Positional Arguments

`*args` lets a function accept any number of positional arguments. Inside the function, `args` is a tuple.

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3))
print(total(10, 20, 30, 40))
print(total())
```

Output:

```text
6
100
0
```

The `*` before `args` is the syntax — the name `args` is a convention, not a keyword. You could write `*numbers` — but `*args` is what everyone expects to see.

### **kwargs — Collect Extra Keyword Arguments

`**kwargs` lets a function accept any number of keyword arguments. Inside the function, `kwargs` is a dictionary.

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f'  {key}: {value}')

show_info(name='Alice', age=30, city='Dallas')
```

Output:

```text
  name: Alice
  age: 30
  city: Dallas
```

You can combine positional parameters, `*args`, keyword parameters, and `**kwargs` in one function — but they must appear in that specific order:

```python
def full_example(a, b, *args, x=0, **kwargs):
    ...
```

The PCAP exam tests this ordering rule.

---

## Scope — Where Variables Live

Every variable in Python has a **scope** — the region of the program where it is visible.

Variables created inside a function are **local** — they exist only while the function is running and are destroyed when it returns.

Variables created at the top level of a module (outside any function) are **global** — they are visible throughout the module.

```python
x = 10    # global

def change():
    x = 99    # local — does NOT change the global x
    print(f'Inside: x = {x}')

change()
print(f'Outside: x = {x}')
```

Output:

```text
Inside: x = 99
Outside: x = 10
```

The `x` inside `change()` is a completely new local variable — it shadows the global `x` but does not modify it.

To actually modify a global variable from inside a function, use the `global` keyword:

```python
def change_global():
    global x
    x = 99

change_global()
print(x)    # 99
```

Using `global` is generally discouraged — it makes programs harder to reason about. Pass values through parameters instead.

---

## Docstrings

A **docstring** is a string literal on the first line of a function body that documents what the function does. Use triple quotes.

```python
def add(a, b):
    '''Return the sum of a and b.'''
    return a + b
```

Access a docstring with `help()` or the `__doc__` attribute:

```python
>>> def celsius_to_fahrenheit(c):
...     '''Convert Celsius to Fahrenheit.
...
...     Args:
...         c: Temperature in Celsius.
...     Returns:
...         Temperature in Fahrenheit as a float.
...     '''
...     return c * 9 / 5 + 32
...
>>> help(celsius_to_fahrenheit)
```

Output shows the docstring formatted as help text.

Docstrings are part of professional Python — every public function should have one. They are also how tools like IDEs and documentation generators work.

---

## Type Hints (Optional but Professional)

Python 3 supports **type hints** — annotations that tell developers what types a function expects and returns. They are not enforced at runtime but improve readability and enable IDE tooling.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> None:
    print(f'Hello, {name}!')

def min_max(numbers: list) -> tuple:
    return min(numbers), max(numbers)
```

The `->` before the colon indicates the return type. Type hints do not change how the function works — they are documentation for humans and static analysis tools.

```python
>>> add(3, 4)
7
>>> add('hello', ' world')    # no error — hints are not enforced
'hello world'
```

Use type hints in any code that others will read. They make function signatures self-documenting.

---

## Putting It Together — Calculator Module

Let me build a calculator using well-structured functions:

```python
# calculator.py
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
    '''Return a / b. Raises ValueError if b is zero.'''
    if b == 0:
        raise ValueError('Division by zero is undefined.')
    return a / b

def calculate(a: float, op: str, b: float) -> float:
    '''Dispatch to the appropriate operation function.'''
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    if op not in operations:
        raise ValueError(f'Unknown operator: {op}')
    return operations[op](a, b)

# Main program
print('=== Calculator ===')
while True:
    expr = input('Enter expression (e.g., 5 + 3) or q to quit: ')
    if expr.lower() == 'q':
        break
    try:
        parts = expr.split()
        a, op, b = float(parts[0]), parts[1], float(parts[2])
        result = calculate(a, op, b)
        print(f'  = {result}')
    except (ValueError, IndexError) as e:
        print(f'  Error: {e}')
```

This uses docstrings, type hints, a dispatch dictionary, exception handling (preview of Module 12), and clean function design.

---

## PCAP Exam Tips and Wrap-Up

Key exam take-aways:

**1.** `def` defines a function. A function is not executed until it is called.

**2.** Parameters with defaults must come after parameters without defaults.

**3.** Keyword arguments can be passed in any order — but positional arguments must precede keyword arguments in a call.

**4.** A function with no `return` statement returns `None`.

**5.** `*args` collects extra positional arguments as a tuple. `**kwargs` collects extra keyword arguments as a dict.

**6.** Local variables are local — they do not affect global variables of the same name.

**7.** `global x` inside a function allows modification of the global `x` — use sparingly.

Module 09 covers scopes and namespaces in depth, and introduces recursion — functions that call themselves. See you there.

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 08 — Functions and Parameter Passing]**

---

## Additional Resources

- [Python for Everybody — Chapter 4](https://www.py4e.com/book) — Functions
- [Official Python Docs — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Official Python Docs — Type Hints (PEP 484)](https://docs.python.org/3/library/typing.html)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [Python for Everybody Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Episodes 4 (Functions)
