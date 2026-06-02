# Reading Guide: Module 08 — Functions and Parameter Passing

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 08 — Functions and Parameter Passing**. Functions are the foundation of reusable, organized code. Every significant Python program is built from functions. The PCAP exam tests function definitions, all parameter types (positional, default, keyword, `*args`, `**kwargs`), return values, scope rules, and docstrings. This is one of the most heavily tested topic areas on the exam.

---

## 1. High-Yield Glossary

### Function

A named, reusable block of code that performs a specific task. Defined with `def` and executed by calling it.

```python
def function_name(parameters):
    body
    return value    # optional
```

A function definition does not execute the body — it just defines what to do when called. The body runs each time the function is called.

### Parameter

A variable in a function definition that receives a value when the function is called. Parameters are local to the function.

```python
def greet(name):    # name is a parameter
    print(f'Hello, {name}!')
```

### Argument

The actual value passed to a function when it is called.

```python
greet('Alice')    # 'Alice' is the argument
```

### return Statement

Sends a value back to the caller and ends the function. A function can have multiple `return` statements (e.g., in different branches), but only one executes per call.

```python
def abs_val(x):
    if x >= 0:
        return x
    else:
        return -x
```

**Returning multiple values:** Wrap them in a tuple (implicit or explicit).

```python
def min_max(lst):
    return min(lst), max(lst)    # returns a tuple

low, high = min_max([5, 2, 8])
```

**Function with no return:** Returns `None` implicitly.

```python
def display(x):
    print(x)
    # no return statement — returns None

result = display(42)    # result is None
```

### None Return

Any function without a `return` statement, or with a bare `return`, returns `None`. This is a common source of bugs when developers accidentally use the return value of a function that modifies state (like `list.sort()`).

### Positional Parameter

A standard parameter that receives its value based on its position in the call.

```python
def subtract(a, b):    # a and b are positional
    return a - b

subtract(10, 3)    # a=10, b=3 → 7
subtract(3, 10)    # a=3, b=10 → -7
```

### Default Parameter

A parameter with a predefined value used when the caller does not provide one.

```python
def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

greet('Alice')              # greeting defaults to 'Hello'
greet('Bob', 'Hi')          # greeting overridden to 'Hi'
```

**PCAP exam rule:** Default parameters must appear after non-default parameters.

```python
def f(a, b=1):    # valid
def f(a=1, b):    # SyntaxError — non-default follows default
```

### Keyword Argument

An argument passed by name rather than by position. Allows passing arguments in any order.

```python
def describe(name, age, city):
    print(f'{name}, {age}, {city}')

describe(age=30, city='Dallas', name='Alice')    # keyword args, any order
```

**Mixing positional and keyword:** Positional arguments must come before keyword arguments in a call.

```python
describe('Alice', city='Dallas', age=30)    # valid — positional first
describe(age=30, 'Alice', city='Dallas')    # SyntaxError — positional after keyword
```

### *args (Arbitrary Positional Arguments)

Allows a function to accept any number of positional arguments. Collected into a **tuple** inside the function.

```python
def total(*args):
    return sum(args)

total(1, 2, 3)        # args = (1, 2, 3)
total(10, 20, 30, 40) # args = (10, 20, 30, 40)
total()               # args = ()
```

The `*` is the syntax — `args` is the conventional name but any name works.

### **kwargs (Arbitrary Keyword Arguments)

Allows a function to accept any number of keyword arguments. Collected into a **dict** inside the function.

```python
def show(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

show(name='Alice', age=30)    # kwargs = {'name': 'Alice', 'age': 30}
```

The `**` is the syntax — `kwargs` is the conventional name.

### Parameter Order Rule

When combining parameter types, they must appear in this order:

1. Regular positional parameters
2. `*args`
3. Keyword-only parameters (after `*args`, must use keyword syntax)
4. `**kwargs`

```python
def f(a, b, *args, x=0, **kwargs):
    pass
```

### Scope

The region of a program where a variable is visible. Python uses the **LEGB** rule: Local → Enclosing → Global → Built-in.

```python
x = 10          # global scope

def func():
    x = 99      # local scope — new variable, does NOT change global
    print(x)    # 99

func()
print(x)        # 10
```

### Local Variable

A variable created inside a function. Exists only for the duration of the function call. Cannot be accessed from outside the function.

### Global Variable

A variable created outside all functions. Visible everywhere in the module. Can be read inside a function, but assigning to it inside a function creates a new local unless `global` is declared.

### global Keyword

Declares that a variable name inside a function refers to the global scope, not a new local.

```python
count = 0

def increment():
    global count
    count += 1
```

Using `global` is discouraged in professional code — pass values through parameters and return values instead.

### Docstring

A string literal on the first line of a function (or class, module) body that documents its purpose. Accessed via `help()` or `.__doc__`.

```python
def area(radius):
    '''Calculate the area of a circle.

    Args:
        radius: The radius of the circle (float or int).
    Returns:
        The area as a float.
    '''
    import math
    return math.pi * radius ** 2
```

### Type Hint

An annotation that documents the expected type of parameters and return values. Not enforced at runtime.

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## 2. Parameter Passing — Call by Object Reference

Python does not pass by value (copying) or by reference (C-style pointer). It passes by **object reference** — the function receives a reference to the same object the caller has.

**Immutable objects (int, str, float, tuple):** Function cannot modify the caller's variable — any "modification" inside the function creates a new local object.

```python
def double(x):
    x *= 2    # creates a new int, does not change caller's x
    print(x)

n = 5
double(n)
print(n)    # still 5
```

**Mutable objects (list, dict, set):** Function can modify the caller's object in place.

```python
def append_zero(lst):
    lst.append(0)    # modifies the caller's list

numbers = [1, 2, 3]
append_zero(numbers)
print(numbers)    # [1, 2, 3, 0]
```

This is one of the most important behaviors to understand for writing correct Python functions.

---

## 3. Common Error Patterns to Memorize

**Pattern 1 — SyntaxError: default after non-default:**

```python
def f(a=1, b):    # SyntaxError
    pass
```

**Pattern 2 — Using the None return value from a mutating method:**

```python
lst = [3, 1, 2]
lst = lst.sort()    # lst is now None
print(lst)          # None
```

**Pattern 3 — Modifying a mutable argument:**

```python
def bad_append(lst, item):
    lst.append(item)
    return lst

original = [1, 2, 3]
result = bad_append(original, 4)
# original is also [1, 2, 3, 4] — the function modified the caller's list
```

**Pattern 4 — Missing return (function returns None):**

```python
def add(a, b):
    result = a + b
    # forgot return result

x = add(3, 5)    # x is None
```

**Pattern 5 — Positional argument after keyword argument:**

```python
describe(name='Alice', 30, 'Dallas')    # SyntaxError
```

---

## 4. Certification Exam Tips

**Tip 1 — Default parameters must follow non-default parameters.**
`def f(a, b=10)` is valid. `def f(a=10, b)` is `SyntaxError`. This is tested with multiple variations.

**Tip 2 — A function with no return statement returns None.**
The exam will show `result = some_function()` and ask for `result` when the function has no `return`. The answer is `None`.

**Tip 3 — `*args` is a tuple, `**kwargs` is a dict.**
Inside the function, `args` is a tuple and `kwargs` is a dict. You can iterate over them, unpack them, and access them with standard sequence/mapping operations.

**Tip 4 — Local variables shadow globals without modifying them.**
`x = 5` inside a function creates a new local `x` that has no connection to a global `x`. The global is unchanged.

**Tip 5 — Mutable default arguments are a known Python gotcha.**
`def f(lst=[]):` — the default list is created once and shared across all calls. This is a well-known bug pattern on the PCAP exam. Use `None` as default and create the list inside:

```python
def f(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst
```

**Tip 6 — Keyword arguments can be in any order.**
`f(b=2, a=1)` is equivalent to `f(a=1, b=2)` — keyword arguments are matched by name, not position.

**Tip 7 — Type hints are not enforced.**
`def add(a: int, b: int) -> int: return a + b` will not raise an error if you call `add('hello', ' world')` — Python ignores type hints at runtime.

---

## 5. Beyond the Exam — Real-World Context

**Why use functions?**
The DRY principle — Don't Repeat Yourself — is the primary motivation. If you write the same logic in five places and find a bug, you have to fix it in five places. Put it in one function and fix it once.

Functions also make code testable. You can write automated tests for a function independently — you know exactly what goes in (parameters) and what comes out (return value). A 500-line script has no natural test boundaries.

**`*args` and `**kwargs` in production code.**
These are used extensively in Python frameworks. Flask and Django route handlers use `**kwargs` to capture URL parameters. Python's `print()` function itself uses `*args` to accept any number of values. Understanding these mechanisms helps you read and extend framework code.

**The mutable default argument bug.**
`def f(lst=[])` is one of Python's most notorious beginner traps. The list is created once at definition time and reused across all calls. After calling `f()` three times, the list has three items. This surprises almost every new Python developer. Always use `None` as the default for mutable arguments.

---

## 6. Required Readings and Videos

**Required Reading — Chapter 4:**
Read Chapter 4 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). The chapter covers function basics with examples.

**Required Reading — Official Python Docs:**
Read [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) and [More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) in the official Python 3 tutorial.

**Required Video:**
Watch Episode 4 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance covers function definitions and usage.

---

## 7. Lab and Command Preview

| Task | What You Will Do |
|---|---|
| Basic function | Define and call a function with and without parameters |
| Return values | Write functions that return single and multiple values |
| Default parameters | Test default and overridden values |
| Keyword arguments | Call functions with keyword args in varying order |
| `*args` | Write a function that accepts variable positional arguments |
| `**kwargs` | Write a function that accepts variable keyword arguments |
| Scope demo | Demonstrate local variable shadowing global |
| Mutable default trap | Observe the shared mutable default bug |
| Docstrings | Add docstrings and access them with `help()` |
| `calculator.py` | Full calculator with dispatch table, error handling, type hints |

---

## 8. Study Checklist

- [ ] Watch the Module 08 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially default parameter rules, `*args`/`**kwargs`, and scope.
- [ ] Work through the Common Error Patterns in Section 3.
- [ ] Read Chapter 4 of *Python for Everybody* at py4e.com.
- [ ] Read the Defining Functions and More on Defining Functions pages in the Official Python 3 Docs.
- [ ] Watch Episode 4 of the Python for Everybody playlist.
- [ ] Review all 7 Certification Exam Tips in Section 4.
- [ ] Preview the lab tasks in Section 7.
- [ ] Proceed to the Module 08 Lab Activity.
