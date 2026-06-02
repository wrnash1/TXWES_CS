# Video Script: CIS-1310 — Introduction to Python

## Module 12 — Exception Handling

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - Draw the try→except→else→finally execution flow on a whiteboard before the code demos.
> - Show the "broad before specific" ordering bug live — let it fail silently, then fix it.
> - Run the finally-with-return demo — students are always surprised that finally still executes.
> - Run `input_validator.py` interactively so students see the loop behavior with bad input.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 12 | Exception Handling | CIS-1310"]**

"Welcome back. Every program you write will eventually encounter unexpected input, missing files, or invalid operations. The question is not whether errors will happen — it is whether your program handles them gracefully or crashes with a traceback the user does not understand.

Python's exception handling system — `try`, `except`, `else`, and `finally` — gives you complete control over what happens when things go wrong. The PCAP exam tests the exact execution order of these clauses, how to catch multiple exception types, and how to raise exceptions yourself.

This module is the difference between code that works only in ideal conditions and code that works in the real world."

---

## [00:45 – 03:00] try and except — The Basic Pattern

**[SHOW SLIDE: "try / except — Catching Exceptions"]**

"Without exception handling, a bad conversion crashes the program immediately:

**[DEMO — unhandled exception]**

```python
value = int('hello')    # ValueError: invalid literal for int() with base 10: 'hello'
```

With exception handling:

**[DEMO — basic try/except]**

```python
try:
    value = int('hello')
    print('Converted:', value)
except ValueError:
    print('That is not a valid number.')

print('Program continues...')
```

Output:

```text
That is not a valid number.
Program continues...
```

[PAUSE]

Here is exactly what Python does: it executes the `try` block line by line. When `int('hello')` raises `ValueError`, Python immediately stops executing the `try` block — the `print('Converted:', value)` line is **skipped** — and jumps to the matching `except ValueError:` clause. After the `except` block finishes, execution continues normally after the entire try-except structure.

**[DEMO — accessing the exception message with `as`]**

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f'Error caught: {e}')
```

Output:

```text
Error caught: division by zero
```

The `as e` syntax binds the exception object to the name `e`. `str(e)` gives you the message."

---

## [03:00 – 05:00] Multiple except Clauses — Order Matters

**[SHOW SLIDE: "Multiple except Clauses — Specific Before General"]**

"A single `try` block can have multiple `except` clauses, each catching a different exception type. Python checks them top to bottom and executes the **first** matching one.

**[DEMO — multiple handlers]**

```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    except TypeError:
        print('Both arguments must be numbers.')

print(safe_divide(10, 2))    # 5.0
safe_divide(10, 0)            # Cannot divide by zero.
safe_divide(10, 'x')          # Both arguments must be numbers.
```

**[DEMO — catching multiple types in one clause]**

```python
try:
    value = int(input('Enter a number: '))
except (ValueError, TypeError) as e:
    print(f'Input error: {e}')
```

**[DEMO — the ordering bug: broad before specific]**

```python
try:
    x = int('abc')
except Exception:          # TOO BROAD — catches everything
    print('Generic error')
except ValueError:         # UNREACHABLE — Exception matches first
    print('Value error')
```

Output:

```text
Generic error
```

[PAUSE]

`ValueError` is a subclass of `Exception`. When Python checks the `except Exception:` clause first, it matches — and the `except ValueError:` clause below it is never reached. Always put **specific** exceptions before **general** ones.

The correct order:

```python
try:
    x = int('abc')
except ValueError:      # specific first
    print('Value error')
except Exception:       # general catches anything else
    print('Generic error')
```

Output:

```text
Value error
```"

---

## [05:00 – 07:30] else and finally — Execution Flow

**[SHOW SLIDE: "else and finally — The Full try-except Structure"]**

"The complete try-except structure has four clauses:

```python
try:
    # code that might raise an exception
except SomeError:
    # runs ONLY if SomeError was raised in try
else:
    # runs ONLY if NO exception was raised in try
finally:
    # ALWAYS runs — exception or not
```

**[DEMO — all four clauses]**

```python
def read_number(s):
    try:
        value = int(s)
    except ValueError:
        print('except: not a valid integer')
    else:
        print(f'else: successfully converted to {value}')
    finally:
        print('finally: always runs')
    print('after the block')

print('--- Valid input ---')
read_number('42')
print()
print('--- Invalid input ---')
read_number('abc')
```

Output:

```text
--- Valid input ---
else: successfully converted to 42
finally: always runs
after the block

--- Invalid input ---
except: not a valid integer
finally: always runs
after the block
```

[PAUSE]

Read this output carefully. For valid input: `try` succeeds, `except` is skipped, `else` runs, `finally` runs. For invalid input: `try` raises ValueError, `except` runs, `else` is **skipped**, `finally` runs. The `else` clause is the success-only path. `finally` is unconditional.

**[DEMO — finally with return — the PCAP trap]**

```python
def demo():
    try:
        return 'from try'
    finally:
        print('finally runs before the return!')

result = demo()
print(result)
```

Output:

```text
finally runs before the return!
from try
```

Even with a `return` statement inside `try`, `finally` executes first — before the return value is handed back to the caller. This is a classic PCAP exam question. `finally` **always** runs."

---

## [07:30 – 09:30] raise and Re-raise

**[SHOW SLIDE: "raise — Triggering Exceptions Intentionally"]**

"Sometimes you need to signal that something is wrong yourself — user passed a negative age, a required field is empty, a value is out of range. The `raise` statement lets you create and throw any exception.

**[DEMO — raise with a message]**

```python
def set_age(age):
    if age < 0:
        raise ValueError(f'Age cannot be negative: {age}')
    if age > 150:
        raise ValueError(f'Age is unrealistically large: {age}')
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f'Invalid age: {e}')
```

Output:

```text
Invalid age: Age cannot be negative: -5
```

**[DEMO — re-raise with bare raise]**

```python
def process(data):
    try:
        result = int(data)
    except ValueError:
        print('Logging: bad data received')
        raise    # re-raises the original ValueError with original traceback

try:
    process('bad')
except ValueError as e:
    print(f'Outer handler: {e}')
```

Output:

```text
Logging: bad data received
Outer handler: invalid literal for int() with base 10: 'bad'
```

A bare `raise` with no argument re-raises the most recently caught exception, preserving its original type, message, and traceback. This is useful when you want to log or note an error but still propagate it up the call stack."

---

## [09:30 – 11:00] The Exception Hierarchy

**[SHOW SLIDE: "Python Exception Hierarchy"]**

"Python exceptions form a class hierarchy. Here are the most important ones:

```text
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── NameError
    ├── AttributeError
    ├── OSError
    │   └── FileNotFoundError
    └── RuntimeError
        └── RecursionError
```

The `except` clause matches the specified exception **or any of its subclasses**. `except Exception:` catches everything in the `Exception` branch — which includes nearly all runtime errors. `except BaseException:` would also catch `SystemExit` and `KeyboardInterrupt` — almost never what you want.

**[DEMO — bare except vs except Exception]**

```python
# bare except — catches EVERYTHING including Ctrl+C
try:
    pass
except:
    pass    # traps KeyboardInterrupt — very bad practice

# except Exception — catches errors, leaves Ctrl+C to the OS
try:
    pass
except Exception:
    pass    # KeyboardInterrupt can still exit the program
```

Always use `except SomeSpecificError:` in production code. Use `except Exception:` as a last-resort fallback only, and never use bare `except:` unless you have a very specific reason."

---

## [11:00 – 13:30] input_validator.py — Complete Exception Handling Program

**[DEMO — live code]**

```python
# input_validator.py
# Demonstrates try-except-else-finally with user input
# Module 12 Lab — CIS-1310


def get_positive_integer(prompt):
    '''Prompt until a positive integer is entered. Return the integer.'''
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError(f'Must be positive, got {value}')
        except ValueError as e:
            print(f'  Invalid input: {e}. Try again.')
        else:
            return value    # else runs only if no exception — safe to return
        finally:
            print('  (attempt complete)')


def divide_safely(a, b):
    '''Divide a by b with full exception handling.'''
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except TypeError as e:
        raise TypeError(f'Arguments must be numbers: {e}')
    else:
        return result
    finally:
        print(f'  divide_safely({a}, {b}) — cleanup')


# Demo the input validator (interactive)
print('=== Positive Integer Input Validator ===')
# For demo purposes, comment out the interactive call
# n = get_positive_integer('Enter a positive integer: ')
# print(f'You entered: {n}')

# Demo divide_safely
print('\n=== Safe Division ===')
for a, b in [(10, 2), (10, 0), (9, 3)]:
    result = divide_safely(a, b)
    if result is None:
        print(f'{a} / {b} = undefined (division by zero)')
    else:
        print(f'{a} / {b} = {result}')
```

Output (non-interactive portion):

```text
=== Safe Division ===
  divide_safely(10, 2) — cleanup
10 / 2 = 5.0
  divide_safely(10, 0) — cleanup
10 / 0 = undefined (division by zero)
  divide_safely(9, 3) — cleanup
9 / 3 = 3.0
```

---

## [13:30 – 15:00] PCAP Exam Tips and Wrap-Up

**[SHOW SLIDE: "Module 12 — PCAP Alignment"]**

"Key exam take-aways:

**1.** Execution order: `try` runs first. If exception → `except`. If no exception → `else`. `finally` always runs regardless.

**2.** `else` is skipped whenever any exception is raised in `try` — even if the exception is caught by `except`.

**3.** `finally` runs even when `try` contains a `return`, `break`, or `continue`. It runs before the value is returned.

**4.** Put specific exception types before general ones. `except Exception:` before `except ValueError:` makes `except ValueError:` unreachable.

**5.** `raise ExceptionType('message')` creates and throws an exception. Bare `raise` re-raises the current exception.

**6.** `except BaseException:` and bare `except:` catch `SystemExit` and `KeyboardInterrupt` — almost always a mistake.

**7.** `except ValueError as e:` binds the exception object to `e`. `str(e)` gives the error message.

Module 13 covers modules and packages — how to organize Python code across files, use the standard library, and install third-party packages with pip. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 12 — Exception Handling]**

---

## Additional Resources

- [Python for Everybody — Chapter 7](https://www.py4e.com/book) — Exceptions chapter with file I/O examples
- [Official Python Docs — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) — authoritative exception tutorial
- [Official Python Docs — Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) — complete exception hierarchy
- [Real Python — Python Exceptions](https://realpython.com/python-exceptions/) — practical guide with examples
