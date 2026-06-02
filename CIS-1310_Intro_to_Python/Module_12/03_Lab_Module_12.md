# Lab Activity: Module 12 — Exception Handling

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 75–90 minutes

---

## Overview

In this lab you will trigger common built-in exceptions, wrap code in `try/except` blocks, practice catching multiple exception types, trace the execution order of `try`/`except`/`else`/`finally`, demonstrate that `finally` runs even when `return` is present, use the `raise` statement to signal errors, write a custom exception class, and build a complete input validation program.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module12
cd module12
```

---

## Part 1 — Triggering and Catching Exceptions

```bash
python3
```

### Step 1.1 — Common Exceptions Without Handling

```python
>>> int('hello')
```

```text
ValueError: invalid literal for int() with base 10: 'hello'
```

```python
>>> 10 / 0
```

```text
ZeroDivisionError: division by zero
```

```python
>>> [][0]
```

```text
IndexError: list index out of range
```

```python
>>> {}['missing']
```

```text
KeyError: 'missing'
```

### Step 1.2 — Basic try/except

```python
>>> try:
...     value = int('hello')
... except ValueError:
...     print('Caught: not a valid integer')
...
Caught: not a valid integer
```

### Step 1.3 — Code After the Failing Line Is Skipped

```python
>>> try:
...     print('before')
...     result = 10 / 0
...     print('after')    # SKIPPED when exception raised
... except ZeroDivisionError:
...     print('caught division by zero')
...
before
caught division by zero
```

"after" is never printed because `10 / 0` raises the exception and control jumps immediately to `except`.

### Step 1.4 — Accessing the Exception Message with as

```python
>>> try:
...     int('abc')
... except ValueError as e:
...     print(type(e).__name__)
...     print(str(e))
...
ValueError
invalid literal for int() with base 10: 'abc'
```

### Step 1.5 — Exception Does Not Crash the Program

```python
>>> for item in ['10', 'bad', '20', 'also_bad', '30']:
...     try:
...         print(int(item))
...     except ValueError:
...         print(f'  Skipping: {item!r}')
...
10
  Skipping: 'bad'
20
  Skipping: 'also_bad'
30
```

The loop continues after each caught exception.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the basic try/except from Step 1.2, the "after" line being skipped from Step 1.3, and the exception message access from Step 1.4. Save as `lab12_screenshot_01_basic_except.png`.

---

## Part 2 — Multiple except Clauses and Ordering

```bash
python3
```

### Step 2.1 — Multiple Handlers

```python
>>> def safe_divide(a, b):
...     try:
...         return a / b
...     except ZeroDivisionError:
...         print('  Cannot divide by zero.')
...     except TypeError:
...         print('  Both arguments must be numbers.')
...
>>> safe_divide(10, 2)
5.0
>>> safe_divide(10, 0)
  Cannot divide by zero.
>>> safe_divide(10, 'x')
  Both arguments must be numbers.
```

### Step 2.2 — Catching Multiple Types in One Clause

```python
>>> def parse(s):
...     try:
...         return int(s)
...     except (ValueError, TypeError) as e:
...         print(f'  Parse error: {e}')
...         return None
...
>>> parse('42')
42
>>> parse('abc')
  Parse error: invalid literal for int() with base 10: 'abc'
>>> parse(None)
  Parse error: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
```

### Step 2.3 — The Ordering Bug: Broad Before Specific

```python
>>> try:
...     int('abc')
... except Exception:
...     print('generic handler — Exception matches first')
... except ValueError:
...     print('UNREACHABLE — ValueError is a subclass of Exception')
...
generic handler — Exception matches first
```

The `except ValueError:` clause is never reached because `except Exception:` matched first.

### Step 2.4 — Fixed Ordering: Specific Before General

```python
>>> try:
...     int('abc')
... except ValueError:
...     print('value error — caught specifically')
... except Exception:
...     print('generic fallback')
...
value error — caught specifically
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing the ordering bug from Step 2.3 and the fixed ordering from Step 2.4 side by side. Save as `lab12_screenshot_02_ordering.png`.

---

## Part 3 — else, finally, and Execution Order

```bash
python3
```

### Step 3.1 — All Four Clauses

```python
>>> def read_number(s):
...     try:
...         value = int(s)
...     except ValueError:
...         print('  except: not a valid integer')
...     else:
...         print(f'  else: converted to {value}')
...     finally:
...         print('  finally: always runs')
...
>>> print('--- Valid ---')
--- Valid ---
>>> read_number('42')
  else: converted to 42
  finally: always runs
>>> print('--- Invalid ---')
--- Invalid ---
>>> read_number('abc')
  except: not a valid integer
  finally: always runs
```

Trace carefully: valid input → `else` runs, `except` skipped. Invalid input → `except` runs, `else` skipped. `finally` runs both times.

### Step 3.2 — finally With return

```python
>>> def demo():
...     try:
...         print('  try: about to return')
...         return 'from try'
...     finally:
...         print('  finally: runs BEFORE the return is delivered')
...
>>> result = demo()
  try: about to return
  finally: runs BEFORE the return is delivered
>>> print('result:', result)
result: from try
```

Even with a `return` in the `try` block, `finally` runs before the value reaches the caller.

### Step 3.3 — finally With Unhandled Exception

```python
>>> def demo2():
...     try:
...         raise RuntimeError('something went wrong')
...     finally:
...         print('  finally: cleanup before propagating')
...
>>> try:
...     demo2()
... except RuntimeError as e:
...     print(f'  outer except: {e}')
...
  finally: cleanup before propagating
  outer except: something went wrong
```

`finally` ran inside `demo2()` even though the exception was not caught there — it propagated up to the outer `try`.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 3 REQUIRED:** Screenshot showing the four-clause execution trace from Step 3.1 (both valid and invalid inputs) and the `finally` with `return` demo from Step 3.2. Save as `lab12_screenshot_03_else_finally.png`.

---

## Part 4 — raise and Custom Exceptions

```bash
python3
```

### Step 4.1 — raise with a Message

```python
>>> def set_age(age):
...     if age < 0:
...         raise ValueError(f'Age cannot be negative: {age}')
...     if age > 150:
...         raise ValueError(f'Age is unrealistically large: {age}')
...     return age
...
>>> set_age(25)
25
>>> try:
...     set_age(-5)
... except ValueError as e:
...     print(f'Error: {e}')
...
Error: Age cannot be negative: -5
>>> try:
...     set_age(200)
... except ValueError as e:
...     print(f'Error: {e}')
...
Error: Age is unrealistically large: 200
```

### Step 4.2 — Bare raise to Re-raise

```python
>>> def process(data):
...     try:
...         return int(data)
...     except ValueError:
...         print(f'  process(): logging bad data: {data!r}')
...         raise    # re-raise with original traceback
...
>>> try:
...     process('bad_input')
... except ValueError as e:
...     print(f'  outer: caught re-raised ValueError: {e}')
...
  process(): logging bad data: 'bad_input'
  outer: caught re-raised ValueError: invalid literal for int() with base 10: 'bad_input'
```

The bare `raise` propagates the original `ValueError` out of `process()` to the outer `try`.

### Step 4.3 — Custom Exception Class

```python
>>> class NegativeValueError(ValueError):
...     '''Raised when a value is unexpectedly negative.'''
...     pass
...
>>> def square_root(n):
...     if n < 0:
...         raise NegativeValueError(f'Cannot take square root of {n}')
...     return n ** 0.5
...
>>> try:
...     square_root(-9)
... except NegativeValueError as e:
...     print(f'Custom error: {e}')
...
Custom error: Cannot take square root of -9
>>> try:
...     square_root(-9)
... except ValueError as e:
...     print(f'Caught as ValueError too: {e}')
...
Caught as ValueError too: Cannot take square root of -9
```

`NegativeValueError` is a subclass of `ValueError`, so it is caught by either handler.

Exit the REPL:

```python
>>> exit()
```

---

## Part 5 — input_validator.py

```bash
nano input_validator.py
```

```python
# input_validator.py
# Demonstrates exception handling with user input validation
# Module 12 Lab — CIS-1310


class OutOfRangeError(ValueError):
    '''Raised when a number is outside an acceptable range.'''
    pass


def get_integer(prompt, min_val=None, max_val=None):
    '''Prompt until a valid integer in range [min_val, max_val] is entered.

    Args:
        prompt: Text to show the user.
        min_val: Minimum acceptable value (inclusive). None = no minimum.
        max_val: Maximum acceptable value (inclusive). None = no maximum.
    Returns:
        A valid integer.
    '''
    while True:
        try:
            raw = input(prompt).strip()
            value = int(raw)
            if min_val is not None and value < min_val:
                raise OutOfRangeError(
                    f'{value} is below minimum ({min_val})'
                )
            if max_val is not None and value > max_val:
                raise OutOfRangeError(
                    f'{value} is above maximum ({max_val})'
                )
        except ValueError as e:
            print(f'  Invalid input: {e}. Try again.')
        else:
            return value    # only runs if no exception occurred


def safe_calculate(expr):
    '''Safely evaluate a simple "a op b" expression string.

    Returns the result or None on error.
    '''
    try:
        parts = expr.split()
        if len(parts) != 3:
            raise ValueError(f'Expected "a op b", got: {expr!r}')
        a, op, b = parts
        a, b = float(a), float(b)
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError('Division by zero')
            return a / b
        else:
            raise ValueError(f'Unknown operator: {op!r}')
    except (ValueError, ZeroDivisionError) as e:
        print(f'  Calculation error: {e}')
        return None
    finally:
        print(f'  safe_calculate({expr!r}) called')


# --- Non-interactive demos (for screenshot)
print('=== safe_calculate demos ===')
tests = ['10 + 5', '9 / 3', '5 / 0', '2 ** 3', 'bad input']
for test in tests:
    result = safe_calculate(test)
    if result is not None:
        print(f'  Result: {result}')
    print()

# --- Interactive demo (comment out if running non-interactively)
# print('\n=== Interactive Input Validator ===')
# n = get_integer('Enter a number between 1 and 10: ', min_val=1, max_val=10)
# print(f'You entered: {n}')
```

Save and run:

```bash
python3 input_validator.py
```

Expected output:

```text
=== safe_calculate demos ===
  safe_calculate('10 + 5') called
  Result: 15.0

  safe_calculate('9 / 3') called
  Result: 3.0

  safe_calculate('5 / 0') called
  Calculation error: Division by zero

  safe_calculate('2 ** 3') called
  Calculation error: Unknown operator: '**'

  safe_calculate('bad input') called
  Calculation error: Expected "a op b", got: 'bad input'
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `input_validator.py` running and showing the complete output. Save as `lab12_screenshot_04_input_validator.png`.

---

## Part 6 — exception_demo.py (Exception Hierarchy)

```bash
nano exception_demo.py
```

```python
# exception_demo.py
# Demonstrates the exception hierarchy and catching at different levels
# Module 12 Lab — CIS-1310


def trigger(exception_type):
    '''Trigger a specific exception type by name.'''
    if exception_type == 'ValueError':
        int('abc')
    elif exception_type == 'ZeroDivisionError':
        1 / 0
    elif exception_type == 'IndexError':
        [][0]
    elif exception_type == 'KeyError':
        {}['missing']
    elif exception_type == 'TypeError':
        'a' + 1
    elif exception_type == 'AttributeError':
        (42).nonexistent_method()


# Demonstrate hierarchy: ValueError is caught by except Exception
print('=== Catching ValueError with except Exception ===')
try:
    trigger('ValueError')
except Exception as e:
    print(f'Caught by Exception: {type(e).__name__}: {e}')

# Demonstrate all exceptions one by one
exceptions = [
    'ValueError', 'ZeroDivisionError', 'IndexError',
    'KeyError', 'TypeError', 'AttributeError',
]

print('\n=== Catch each by specific type ===')
for name in exceptions:
    try:
        trigger(name)
    except ValueError as e:
        print(f'ValueError   : {e}')
    except ZeroDivisionError as e:
        print(f'ZeroDivision : {e}')
    except IndexError as e:
        print(f'IndexError   : {e}')
    except KeyError as e:
        print(f'KeyError     : {e}')
    except TypeError as e:
        print(f'TypeError    : {e}')
    except AttributeError as e:
        print(f'AttributeError: {e}')

# Demonstrate finally + return interaction
print('\n=== finally with return ===')


def finally_return():
    try:
        return 'try value'
    finally:
        print('  finally executed before return')


result = finally_return()
print(f'  caller received: {result!r}')
```

Save and run:

```bash
python3 exception_demo.py
```

Expected output:

```text
=== Catching ValueError with except Exception ===
Caught by Exception: ValueError: invalid literal for int() with base 10: 'abc'

=== Catch each by specific type ===
ValueError   : invalid literal for int() with base 10: 'abc'
ZeroDivision : division by zero
IndexError   : list index out of range
KeyError     : 'missing'
TypeError    : can only concatenate str (not "int") to str
AttributeError: 'int' object has no attribute 'nonexistent_method'

=== finally with return ===
  finally executed before return
  caller received: 'try value'
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `exception_demo.py` running and showing the complete output. Save as `lab12_screenshot_05_exception_demo.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 12 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab12_screenshot_01_basic_except.png` | Basic try/except, skipped code, exception message access |
| 2 | `lab12_screenshot_02_ordering.png` | Broad-before-specific bug and corrected ordering |
| 3 | `lab12_screenshot_03_else_finally.png` | Four-clause execution trace and finally-with-return |
| 4 | `lab12_screenshot_04_input_validator.png` | input_validator.py full output |
| 5 | `lab12_screenshot_05_exception_demo.png` | exception_demo.py full output |

---

## Troubleshooting Guide

**`except` clause not catching the exception you expect.**
Check that the exception type in the `except` clause matches exactly. `except ValueError:` will not catch `TypeError`. Use `type(e).__name__` to print the actual exception class name and verify what Python is raising.

**`else` block not running when you expect it to.**
`else` only runs when the `try` block completes without any exception. If an exception was raised and caught by `except`, `else` is skipped. Add a print inside `try` before the risky line to confirm whether it raises at all.

**`finally` block printing unexpectedly during debugging.**
`finally` is designed to always run — this is correct behavior, not a bug. If you do not want cleanup code to run during testing, use a flag variable or temporarily comment it out.

**`raise ValueError` vs `raise ValueError('message')`.**
`raise ValueError` raises the class object itself, which technically works but is poor practice. Always use `raise ValueError('descriptive message')` so the caller has useful context when debugging.

**Custom exception not being caught by parent `except` clause.**
Confirm your custom exception inherits from the right parent. `class MyError(Exception):` is caught by `except Exception:`. `class MyError(ValueError):` is caught by both `except ValueError:` and `except Exception:`.
