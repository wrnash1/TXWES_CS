# Reading Guide: Module 12 — Exception Handling

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-1310 &BULL; INTRODUCTION TO PYTHON PROGRAMMING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 12 — Exception Handling**. Every program of any size will encounter errors: user input that cannot be converted to a number, a file that does not exist, a division by zero, a network timeout. Without exception handling, these errors crash the program with a raw traceback that the user does not understand. With exception handling, you choose what to do — retry, provide a default value, log the error, clean up resources, or present a friendly message.

Python's exception system is one of the most heavily tested topics on the PCAP exam. You need to know the exact execution order of `try`, `except`, `else`, and `finally`; when each clause runs and when it is skipped; how to catch multiple exception types; how the exception hierarchy determines which `except` clause matches; and how to raise exceptions yourself with the `raise` statement.

---

## 1. High-Yield Glossary

### Exception

A runtime error that disrupts the normal flow of a program. When Python encounters an operation it cannot perform, it **raises** (creates and throws) an exception. If no exception handler is present, Python terminates the program and prints a traceback.

```python
int('hello')    # raises ValueError
10 / 0          # raises ZeroDivisionError
[][0]           # raises IndexError
```

### try Block

The clause that wraps code which might raise an exception. If no exception occurs, the entire `try` block runs normally. If an exception occurs, Python immediately stops executing the `try` block at the line that raised the exception and jumps to the matching `except` clause.

```python
try:
    value = int(input('Enter a number: '))
    print('You entered:', value)     # skipped if int() raises ValueError
except ValueError:
    print('Not a valid number.')
```

### except Clause

Specifies the exception type to catch and the code to run when that exception occurs. Only executes if a matching exception was raised in the `try` block.

```python
except ValueError:          # catches only ValueError
except (ValueError, TypeError):  # catches either
except ValueError as e:    # binds exception to name 'e'
except Exception:           # catches most runtime errors
except:                     # bare — catches EVERYTHING (avoid)
```

### Specific vs General — Ordering Rule

Python tests `except` clauses **top to bottom** and executes the first one that matches. Because specific exceptions are subclasses of general ones, placing a general handler before a specific one makes the specific handler **unreachable**.

```python
# WRONG — ValueError is a subclass of Exception;
# except Exception: matches first, except ValueError: is unreachable
try:
    int('abc')
except Exception:
    print('generic')
except ValueError:
    print('value error')    # NEVER reached

# CORRECT — specific before general
try:
    int('abc')
except ValueError:
    print('value error')    # matches
except Exception:
    print('generic')        # fallback for anything else
```

### as Keyword (Exception Object)

Binds the caught exception to a variable name. Allows you to access the exception's message and type.

```python
try:
    int('abc')
except ValueError as e:
    print(type(e).__name__)    # ValueError
    print(str(e))              # invalid literal for int() with base 10: 'abc'
    print(e.args)              # ("invalid literal for int() with base 10: 'abc'",)
```

### else Clause

Runs only if the `try` block completed **without raising any exception**. Skipped entirely if any exception occurred (even a handled one).

Use `else` for code that should only run when the operation succeeded — separating the "success path" from the `try` block itself.

```python
try:
    value = int(user_input)
except ValueError:
    print('Invalid input.')
else:
    print(f'Converted successfully: {value}')    # only if no exception
```

### finally Clause

Always runs — whether or not an exception occurred, whether or not it was caught. Runs even if the `try` block contains a `return`, `break`, or `continue` statement.

`finally` is the right place for **cleanup code** — closing files, releasing locks, closing database connections.

```python
def load_file(path):
    f = None
    try:
        f = open(path)
        return f.read()
    except FileNotFoundError:
        return ''
    finally:
        if f:
            f.close()    # ALWAYS closes, even if an exception occurs
```

**`finally` with `return` — PCAP exam trap:**

```python
def demo():
    try:
        return 'from try'
    finally:
        print('finally runs first!')    # prints before return is delivered

result = demo()
print(result)
```

Output:

```text
finally runs first!
from try
```

`finally` executes **before** the return value is handed to the caller.

### Full Execution Order

```text
try block runs.
    └─ Exception raised?
        ├─ YES: matching except clause runs → finally runs → continue
        │       else is SKIPPED
        └─ NO: else clause runs → finally runs → continue
```

| Clause | Runs when |
|---|---|
| `try` | Always (it's the code block) |
| `except` | Only when a matching exception occurred in `try` |
| `else` | Only when NO exception occurred in `try` |
| `finally` | ALWAYS — exception or not, caught or not |

### raise Statement

Creates and raises an exception intentionally. Used to signal that a precondition or postcondition has been violated.

```python
raise ValueError('Age must be positive')
raise TypeError(f'Expected int, got {type(x).__name__}')
raise                  # bare raise — re-raises the current exception
```

`raise ExceptionType('message')` creates a new exception instance and raises it. The message is available via `str(e)` in the `except` clause.

### Bare raise

Re-raises the currently active exception without modification. Used inside `except` blocks when you want to perform some action (logging, cleanup) but still propagate the error.

```python
try:
    risky_operation()
except Exception as e:
    log_error(e)    # log it
    raise           # then re-raise — caller still sees the exception
```

### Exception Hierarchy

Python exceptions form a class tree. A `except` clause catches the named class **and all its subclasses**.

```text
BaseException
├── SystemExit          ← raised by sys.exit()
├── KeyboardInterrupt   ← raised by Ctrl+C
└── Exception           ← parent of most runtime errors
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── NameError
    │   └── UnboundLocalError
    ├── AttributeError
    ├── OSError
    │   ├── FileNotFoundError
    │   └── PermissionError
    └── RuntimeError
        └── RecursionError
```

**Important distinctions:**

| Clause | What it catches |
|---|---|
| `except ValueError:` | Only `ValueError` and its subclasses |
| `except Exception:` | All exceptions under `Exception` (most runtime errors) |
| `except BaseException:` | Everything — including `SystemExit` and `KeyboardInterrupt` |
| bare `except:` | Everything — identical to `except BaseException:` |

Avoid bare `except:` and `except BaseException:` — they trap `Ctrl+C` and `sys.exit()`, making the program impossible to stop.

### Custom Exceptions

You can define your own exception types by subclassing `Exception`. Custom exceptions make error handling more specific and self-documenting.

```python
class NegativeAgeError(ValueError):
    '''Raised when an age value is negative.'''
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError(f'Age cannot be negative: {age}')
    return age

try:
    set_age(-5)
except NegativeAgeError as e:
    print(f'Custom error: {e}')
```

Output:

```text
Custom error: Age cannot be negative: -5
```

Because `NegativeAgeError` is a subclass of `ValueError`, it can also be caught by `except ValueError:`.

---

## 2. Common Built-in Exceptions Reference

| Exception | Raised when |
|---|---|
| `ValueError` | Right type, wrong value (`int('abc')`) |
| `TypeError` | Wrong type for operation (`'a' + 1`) |
| `ZeroDivisionError` | Division by zero (`10 / 0`) |
| `IndexError` | List/tuple index out of range (`[][0]`) |
| `KeyError` | Dictionary key not found (`d['missing']`) |
| `NameError` | Variable not defined (`print(undefined_var)`) |
| `AttributeError` | Object has no such attribute (`'str'.nonexistent()`) |
| `FileNotFoundError` | File does not exist (`open('missing.txt')`) |
| `PermissionError` | File access denied |
| `RecursionError` | Recursion limit exceeded |
| `OverflowError` | Numeric result too large |
| `StopIteration` | Iterator exhausted |
| `OSError` | System-level error (parent of FileNotFoundError, PermissionError) |

---

## 3. Common Error Patterns to Memorize

**Pattern 1 — Broad except before specific makes specific unreachable:**

```python
try:
    int('abc')
except Exception:     # catches ValueError — specific handler below never runs
    print('generic')
except ValueError:    # UNREACHABLE
    print('value')
```

Fix: Always put specific exceptions first.

**Pattern 2 — Swallowing exceptions silently with pass:**

```python
try:
    risky()
except Exception:
    pass    # hides all errors — bugs become invisible
```

Fix: At minimum, log the error. Never silently swallow exceptions in production code.

**Pattern 3 — Forgetting that else is skipped when except runs:**

```python
try:
    value = int('abc')
except ValueError:
    print('caught error')
else:
    print('this will NOT print — exception occurred')
```

`else` only runs when the `try` block completes without any exception.

**Pattern 4 — Expecting finally not to run after return:**

```python
def f():
    try:
        return 1
    finally:
        print('this prints!')    # students expect this is skipped

f()    # prints 'this prints!' — finally ALWAYS runs
```

**Pattern 5 — Raising wrong type or forgetting parentheses:**

```python
raise ValueError        # WRONG — raises the class, not an instance
raise ValueError()      # OK — raises instance with no message
raise ValueError('message')   # BEST — raises instance with informative message
```

---

## 4. Certification Exam Tips

**Tip 1 — Know the exact execution order.**
`try` runs → exception? `except` runs → no exception? `else` runs → either way `finally` runs. The PCAP exam will show a try-except-else-finally block and ask which print statements execute.

**Tip 2 — `else` is skipped whenever any exception is raised.**
Even if the exception is caught by an `except` clause, `else` is still skipped. `else` means "the try block succeeded completely."

**Tip 3 — `finally` runs before a `return` value is delivered.**
`try: return 42` with a `finally: print('x')` — the print happens before the caller receives 42. This is one of the most commonly tested PCAP exam questions.

**Tip 4 — Specific except clauses must come before general ones.**
`except Exception:` before `except ValueError:` makes `ValueError` unreachable. Python will warn you with a `SyntaxWarning` in 3.12+, but in earlier versions it silently becomes dead code.

**Tip 5 — Bare `raise` re-raises the current exception unchanged.**
Inside an `except` block, bare `raise` with no argument re-raises the caught exception with its original type, message, and traceback intact.

**Tip 6 — Bare `except:` catches KeyboardInterrupt and SystemExit.**
This is almost always a mistake. Use `except Exception:` for general error handling and let `KeyboardInterrupt`/`SystemExit` propagate normally so the user can Ctrl+C out.

**Tip 7 — `raise ExceptionType('message')` requires parentheses.**
`raise ValueError` raises the class itself (unusual). `raise ValueError('message')` raises an instance with a message. Always use the instance form.

---

## 5. Beyond the Exam — Real-World Context

**Exception handling is not about hiding errors.**
The most common mistake beginners make is `except Exception: pass` — swallowing every error silently. This makes debugging nightmarish because the program keeps running in a broken state. Good exception handling means catching specific errors you know how to recover from, and letting everything else propagate.

**Context managers and `finally`.**
Python's `with` statement (covered in Module 13 file handling) automates the `finally` cleanup pattern. `with open('file.txt') as f:` guarantees the file is closed even if an exception occurs — equivalent to a `try/finally` block but cleaner. Understanding `finally` is the foundation for understanding `with`.

**Custom exceptions in production code.**
Professional Python projects define their own exception hierarchies. A web framework might have `AppError > AuthError > PermissionDeniedError`. This allows callers to catch at the right level of specificity — catch `PermissionDeniedError` to handle auth failures, catch `AppError` as a general application error fallback, and let unexpected exceptions (bugs) propagate to the top-level error handler.

---

## 6. Required Readings and Videos

**Required Reading — Chapter 7:**
Read Chapter 7 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). This chapter covers exception handling for file I/O — the most common real-world application.

**Required Reading — Official Python Docs:**
Read [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) in the official Python 3 tutorial — the authoritative source for exception syntax tested on the PCAP exam. Also read [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) for the complete exception hierarchy.

**Supplemental Video:**
Watch Episode 7 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance covers exception handling with file operations.

---

## 7. Supplemental Resources

**1. Official Python 3 Docs — Errors and Exceptions**
[https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html)
The authoritative tutorial chapter on exception handling — covers syntax errors, `try`/`except`/`else`/`finally`, raising exceptions, user-defined exceptions, and exception chaining. This is the primary source for PCAP exam questions on exception handling.

**2. Official Python 3 Docs — Built-in Exceptions**
[https://docs.python.org/3/library/exceptions.html](https://docs.python.org/3/library/exceptions.html)
The complete exception hierarchy with descriptions of every built-in exception class. Shows the full inheritance tree from `BaseException` through `Exception` to specific exception types. Essential for understanding which `except` clause catches which exception.

**3. Python for Everybody — Chapter 7: Files**
[https://www.py4e.com/html3/07-files](https://www.py4e.com/html3/07-files)
Free textbook chapter demonstrating exception handling in the context of file I/O — the most common real-world use of `try/except`. Includes `try/except` with `open()`, `IOError`, and the guard pattern for safe file access.

**4. Real Python — Python Exceptions: An Introduction**
[https://realpython.com/python-exceptions/](https://realpython.com/python-exceptions/)
A comprehensive free article covering the exception hierarchy, `try/except/else/finally`, raising and re-raising, and custom exception classes with practical examples. The section on exception chaining (`raise ... from ...`) provides useful context beyond the PCAP exam scope.

**5. Real Python — Python's assert: Debug and Test Your Code**
[https://realpython.com/python-assert-statement/](https://realpython.com/python-assert-statement/)
A focused article on Python's `assert` statement — when to use it, `AssertionError`, and how it relates to testing. Includes important warnings about relying on `assert` for input validation in production code (assert statements are disabled when Python runs with optimization flags).

---

## 8. Study Checklist

- [ ] Watch the Module 12 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially execution order, `else` vs `finally`, and the ordering rule.
- [ ] Draw the try→except→else→finally execution flow diagram on paper.
- [ ] Trace the "finally with return" example by hand to confirm you understand the order.
- [ ] Work through all 5 Common Error Patterns in the REPL.
- [ ] Memorize the Common Built-in Exceptions reference table — know which operation raises which exception.
- [ ] Read Chapter 7 of *Python for Everybody* at py4e.com.
- [ ] Read the Errors and Exceptions page in the official Python 3 docs.
- [ ] Review all 7 Certification Exam Tips in Section 4.
- [ ] Proceed to the Module 12 Lab Activity.
