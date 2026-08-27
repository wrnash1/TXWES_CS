# Quiz: Module 12 — Exception Handling

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 12 topics.

---

### Question 1

What is the output of this code?

```python
try:
    print('A')
    x = int('bad')
    print('B')
except ValueError:
    print('C')
print('D')
```

- A) `A B C D`
- B) `A C D`
- C) `A B D`
- D) `C D`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `int('bad')` raises `ValueError` before `print('B')` executes. Code after the raising line inside `try` is skipped immediately.
- *Why B is correct:* `print('A')` runs. Then `int('bad')` raises `ValueError` — `print('B')` is skipped. The `except ValueError:` clause runs → `print('C')`. Execution continues normally → `print('D')`.
- *Why C is incorrect:* `print('B')` is inside the `try` block after the line that raises. Since the exception is raised before reaching it, `B` is never printed.
- *Why D is incorrect:* `print('A')` comes before the raising line and executes normally. `A` is always printed.

---

### Question 2

Which clause in a try-except structure runs **only** when no exception was raised in the `try` block?

- A) `except`
- B) `finally`
- C) `else`
- D) All three run when no exception occurs

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `except` runs only when a matching exception **was** raised. It is skipped entirely when the `try` block succeeds.
- *Why B is incorrect:* `finally` runs unconditionally — whether or not an exception occurred. It is not exclusive to the success case.
- *Why C is correct:* `else` is the success-only clause. It runs after the `try` block if and only if no exception was raised. It is skipped whenever an exception occurs in `try`.
- *Why D is incorrect:* When no exception occurs: `try` runs, `except` is skipped, `else` runs, `finally` runs. Not all three — `except` is skipped on success.

---

### Question 3

What is the output of this code?

```python
def f():
    try:
        return 'try'
    finally:
        print('finally')

print(f())
```

- A) `try`
- B) `finally` then `try`
- C) `try` then `finally`
- D) `finally` only — the return is overridden

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `finally` always executes — even when `return` is present. The function does not skip `finally` and return immediately.
- *Why B is correct:* `finally` executes before the return value is handed to the caller. So `print('finally')` runs first (printing `finally`), then the function returns `'try'`, and `print(f())` prints `try`.
- *Why C is incorrect:* The output order is reversed. `finally` runs during the function call — before the return value reaches `print(f())`.
- *Why D is incorrect:* `finally` does not override the `return` value. The `try` block's return value (`'try'`) is still returned after `finally` completes.

---

### Question 4

What is the output of this code?

```python
try:
    int('abc')
except Exception:
    print('generic')
except ValueError:
    print('specific')
```

- A) `specific`
- B) `generic` then `specific`
- C) `generic`
- D) `ValueError` — unreachable except clause causes error

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `except Exception:` appears before `except ValueError:`. Since `ValueError` is a subclass of `Exception`, the `Exception` clause matches first. The `ValueError` clause is never reached.
- *Why B is incorrect:* Only one `except` clause runs per exception. Once `except Exception:` matches and handles the exception, execution does not continue to `except ValueError:`.
- *Why C is correct:* Python tests `except` clauses top to bottom. `except Exception:` matches `ValueError` (because `ValueError` is a subclass of `Exception`) and runs `print('generic')`. The `except ValueError:` clause below it is unreachable.
- *Why D is incorrect:* Python does not raise an error for unreachable `except` clauses. It silently makes them dead code. (Python 3.12+ issues a `SyntaxWarning` for this pattern, but no exception is raised.)

---

### Question 5

What exception does `[][0]` raise?

- A) `ValueError`
- B) `KeyError`
- C) `IndexError`
- D) `TypeError`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `ValueError` is raised for wrong values of the correct type — for example, `int('abc')` or `math.sqrt(-1)`. Accessing out-of-range list positions is not a value error.
- *Why B is incorrect:* `KeyError` is the dictionary equivalent — raised when a dictionary key is not found. Lists use integer indices, not keys.
- *Why C is correct:* `IndexError` is raised whenever a sequence index is out of range. An empty list `[]` has no elements — accessing index `0` is out of range.
- *Why D is incorrect:* `TypeError` is raised for incompatible types — for example, using a string as a list index. Using an integer index on an empty list is valid syntax with an out-of-range value, which is `IndexError`.

---

### Question 6

What is the output of this code?

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print('zero')
else:
    print('success:', result)
finally:
    print('done')
```

- A) `zero` then `done`
- B) `success: 5.0` then `done`
- C) `success: 5.0`
- D) `done` only

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `10 / 2 = 5.0` — no `ZeroDivisionError` is raised. `except` is skipped entirely.
- *Why B is correct:* `try` completes without error → `except` is skipped → `else` runs (prints `success: 5.0`) → `finally` always runs (prints `done`).
- *Why C is incorrect:* `finally` always runs regardless of whether an exception occurred. `done` will always be printed.
- *Why D is incorrect:* `finally` runs unconditionally, but so does `else` when no exception occurs. Both `else` and `finally` run here.

---

### Question 7

Which of the following correctly raises a `ValueError` with a descriptive message?

- A) `raise ValueError`
- B) `raise 'ValueError: bad input'`
- C) `raise ValueError('bad input')`
- D) `throw ValueError('bad input')`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `raise ValueError` raises the class object rather than an instance. While it technically works, it is poor practice — there is no message for the caller to inspect. Always instantiate with a message.
- *Why B is incorrect:* `raise 'ValueError: bad input'` raises a string, which Python does not allow. You can only raise instances (or classes) that are subclasses of `BaseException`. This produces `TypeError: exceptions must derive from BaseException`.
- *Why C is correct:* `raise ValueError('bad input')` creates an instance of `ValueError` with the message `'bad input'` and raises it. This is the standard, correct form.
- *Why D is incorrect:* Python uses `raise`, not `throw`. `throw` is the keyword used in Java and JavaScript. Using `throw` in Python raises `NameError: name 'throw' is not defined`.

---

### Question 8

Inside an `except` block, what does a bare `raise` (with no argument) do?

- A) Raises a new generic `Exception` with no message
- B) Re-raises the currently caught exception with its original traceback
- C) Raises `RuntimeError` indicating the exception was not handled
- D) Does nothing — it is a no-op inside an `except` block

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Bare `raise` does not create a new exception. It re-raises the one that was caught — preserving the original exception type, message, and traceback.
- *Why B is correct:* A bare `raise` inside an `except` block re-raises the caught exception exactly as it was originally raised. This is useful for logging an error before propagating it to an outer handler.
- *Why C is incorrect:* Python does not raise a secondary `RuntimeError` — the original exception is simply propagated unchanged.
- *Why D is incorrect:* Bare `raise` is not a no-op. It actively propagates the exception. Using `pass` instead would suppress it.

---

### Question 9

What does `except BaseException:` catch that `except Exception:` does not?

- A) `ValueError` and `TypeError`
- B) `ZeroDivisionError` and `IndexError`
- C) `SystemExit` and `KeyboardInterrupt`
- D) `FileNotFoundError` and `PermissionError`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `ValueError` and `TypeError` are subclasses of `Exception`. They are caught by both `except Exception:` and `except BaseException:`.
- *Why B is incorrect:* `ZeroDivisionError` and `IndexError` are both under `Exception` in the hierarchy — caught by `except Exception:` already.
- *Why C is correct:* `SystemExit` (raised by `sys.exit()`) and `KeyboardInterrupt` (raised by `Ctrl+C`) are direct subclasses of `BaseException` but NOT subclasses of `Exception`. `except Exception:` does not catch them. `except BaseException:` does — which is why bare `except:` and `except BaseException:` are dangerous.
- *Why D is incorrect:* `FileNotFoundError` and `PermissionError` are subclasses of `OSError`, which is a subclass of `Exception`. They are caught by `except Exception:` without needing `BaseException`.

---

### Question 10

What is the output of this code?

```python
def check(n):
    if n < 0:
        raise ValueError(f'negative: {n}')
    return n * 2

try:
    print(check(5))
    print(check(-3))
    print(check(4))
except ValueError as e:
    print(f'Error: {e}')
```

- A) `10` then `Error: negative: -3` then `8`
- B) `10` then `Error: negative: -3`
- C) `Error: negative: -3`
- D) `10` then `-6` then `8`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Once `check(-3)` raises `ValueError`, control immediately jumps to the `except` clause. `print(check(4))` is inside the same `try` block — it is skipped entirely. `8` is never printed.
- *Why B is correct:* `check(5)` succeeds → prints `10`. `check(-3)` raises `ValueError` → the `print` of the result is abandoned, `check(4)` is skipped, and the `except` clause runs → prints `Error: negative: -3`.
- *Why C is incorrect:* `check(5)` is called first and succeeds. `10` is printed before the exception occurs.
- *Why D is incorrect:* `check(-3)` raises `ValueError` — it does not return `-6`. The `raise` statement stops execution of the function and the `try` block.

---

### Question 11

What is the output of this code?

```python
try:
    x = int('5')
except ValueError:
    print('error')
else:
    print('ok:', x)
finally:
    print('done')
```

- A) `ok: 5` then `done`
- B) `error` then `done`
- C) `ok: 5`
- D) `done` only

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `int('5')` succeeds — no exception. `except` is skipped. `else` runs (no exception occurred) → `ok: 5`. `finally` always runs → `done`.
- *Why B is incorrect:* `'5'` is a valid integer string. No `ValueError` is raised. `except` and its print are skipped entirely.
- *Why C is incorrect:* `finally` always runs, even when the `try` block succeeds. `done` will always print.
- *Why D is incorrect:* Both `else` and `finally` run when no exception occurs. Only `except` is skipped on success.

---

### Question 12

What is the output of this code?

```python
try:
    raise ValueError('first')
except ValueError:
    raise ValueError('second')
except Exception:
    print('caught')
```

- A) `caught`
- B) `ValueError: second` is propagated — program terminates
- C) `ValueError: first` then `ValueError: second`
- D) The two exceptions cancel out and nothing happens

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The second `raise ValueError('second')` occurs inside an `except` block, not inside the `try` block. The `except Exception:` clause only catches exceptions from the `try` block — not exceptions raised inside another `except` block.
- *Why B is correct:* `raise ValueError('first')` is caught by `except ValueError:`. Inside that handler, `raise ValueError('second')` raises a new exception. Since this new raise is not inside a `try` block, it propagates uncaught and terminates the program with a traceback showing `ValueError: second`.
- *Why C is incorrect:* When `ValueError('second')` is raised, execution does not continue to print both messages. The new exception propagates immediately.
- *Why D is incorrect:* Python exceptions do not cancel each other out. The second raise propagates normally.

---

### Question 13

Which statement about exception handling performance is correct?

- A) `try` blocks are significantly slower than `if` statements even when no exception occurs
- B) `try` blocks have near-zero overhead when no exception is raised
- C) `except` clauses run even when no exception occurs, adding overhead
- D) `finally` blocks execute before `try`, adding startup cost

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* In CPython, the overhead of a `try` block itself (with no exception) is minimal — typically a few nanoseconds. The EAFP (Easier to Ask Forgiveness than Permission) pattern is considered Pythonic partly because `try` is cheap when exceptions are rare.
- *Why B is correct:* When no exception occurs, `try` blocks have near-zero overhead compared to `if` checks. The cost is only incurred when an exception is actually raised and the handler executes. This makes `try/except` efficient for the happy path.
- *Why C is incorrect:* `except` clauses are only entered when an exception matches. They do not execute on every `try` block entry.
- *Why D is incorrect:* `finally` blocks execute after `try` (and `except`/`else` if present). They never run before `try`.

---

### Question 14

What is the output of this code?

```python
def risky():
    try:
        return 1
    except Exception:
        return 2
    finally:
        return 3

print(risky())
```

- A) `1`
- B) `2`
- C) `3`
- D) `1` then `3`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The `finally` block contains `return 3`, which overrides the `return 1` in the `try` block. When `finally` returns a value, that value replaces any pending return from `try` or `except`.
- *Why B is incorrect:* No exception is raised, so `except` is never entered. The `return 2` is never reached.
- *Why C is correct:* The `try` block prepares `return 1`, but `finally` always runs — and its `return 3` overrides the pending return. The caller receives `3`. This is a well-known Python gotcha: a `return` in `finally` silently discards the `try` block's return value.
- *Why D is incorrect:* Only one value is returned. The `return 3` in `finally` replaces, not appends to, the return from `try`.

---

### Question 15

What is the output of this code?

```python
class AppError(Exception):
    pass

class DatabaseError(AppError):
    pass

try:
    raise DatabaseError('connection failed')
except AppError as e:
    print(f'App error: {e}')
except DatabaseError as e:
    print(f'DB error: {e}')
```

- A) `DB error: connection failed`
- B) `App error: connection failed`
- C) Both clauses run — `App error:` then `DB error:`
- D) `TypeError` — `DatabaseError` is not a valid exception type

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `except AppError:` appears before `except DatabaseError:`. Since `DatabaseError` is a subclass of `AppError`, the first `except` clause matches. The `except DatabaseError:` clause is never reached.
- *Why B is correct:* Python tests `except` clauses top to bottom and uses the first match. `DatabaseError` IS-A `AppError` (by inheritance), so `except AppError:` matches first and handles the exception.
- *Why C is incorrect:* Only one `except` clause runs per exception, always the first match found.
- *Why D is incorrect:* Any class that inherits from `BaseException` is a valid exception type. `DatabaseError` inherits from `AppError`, which inherits from `Exception`, which inherits from `BaseException` — fully valid.

---

### Question 16

What does `except (ValueError, TypeError) as e:` do?

- A) Catches only exceptions that are both `ValueError` and `TypeError` simultaneously
- B) Catches `ValueError` and stores it in `e`; catches `TypeError` separately
- C) Catches either `ValueError` or `TypeError` and binds the caught exception to `e`
- D) `SyntaxError` — you cannot use `as` with a tuple of exception types

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A single exception can only be one type at a time. The tuple syntax means "either of these types" — not "both simultaneously."
- *Why B is incorrect:* The `as e` binding applies to whichever exception was actually caught. There is one `except` clause that handles both types — not two separate clauses.
- *Why C is correct:* `except (ValueError, TypeError) as e:` catches either exception type and binds the caught instance to `e`. This is equivalent to two separate `except` clauses that share the same handler body.
- *Why D is incorrect:* Using `as` with a tuple of exception types is valid syntax. `except (TypeError, ValueError) as e:` is a standard Python pattern.

---

### Question 17

What does `assert x > 0, 'x must be positive'` do when `x = -1`?

- A) Raises `ValueError: x must be positive`
- B) Raises `AssertionError: x must be positive`
- C) Prints `x must be positive` and continues
- D) Raises `RuntimeError: assertion failed`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `assert` raises `AssertionError`, not `ValueError`. The type of exception is always `AssertionError` — the message you provide is passed as the error message.
- *Why B is correct:* `assert condition, message` raises `AssertionError(message)` when `condition` is falsy. `x = -1` makes `x > 0` false, so `AssertionError: x must be positive` is raised.
- *Why C is incorrect:* `assert` does not print a message and continue. It raises an exception when the condition is false.
- *Why D is incorrect:* `RuntimeError` is not raised by `assert`. Python's assert statement specifically raises `AssertionError`.

---

### Question 18

In Python, what is the difference between `raise` and `raise e` inside an `except` block?

- A) No difference — both re-raise the caught exception
- B) `raise` re-raises with the original traceback; `raise e` creates a new traceback starting at the current line
- C) `raise e` is the correct syntax; bare `raise` is a `SyntaxError`
- D) `raise` raises a new `RuntimeError`; `raise e` re-raises the original

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* There is an important difference. Bare `raise` preserves the original traceback completely. `raise e` creates a chained exception — the traceback shows the current `raise` line as the new raise point, with the original exception attached as context.
- *Why B is correct:* Bare `raise` propagates the caught exception unchanged, preserving its original traceback for debugging. `raise e` (raising the bound variable) creates a new exception context, which can complicate tracebacks. For re-raising, bare `raise` is preferred.
- *Why C is incorrect:* Both forms are valid Python syntax. Bare `raise` inside an `except` block is specifically documented as the idiom for re-raising.
- *Why D is incorrect:* Bare `raise` does not create a new `RuntimeError`. It re-raises the same caught exception, preserving its type and message.

---

### Question 19

What exception is raised by `'hello'[10]`?

- A) `ValueError`
- B) `TypeError`
- C) `IndexError`
- D) `KeyError`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `ValueError` is for wrong values of the correct type — for example, `int('abc')`. Accessing an out-of-range index is not a value error.
- *Why B is incorrect:* `TypeError` is for operations on incompatible types — for example, `'hello' + 5`. Indexing a string with an integer is a valid operation; the problem is the out-of-range position.
- *Why C is correct:* `IndexError: string index out of range` is raised for any sequence (string, list, tuple) when the index is out of bounds. `'hello'` has indices 0–4; index 10 is out of range.
- *Why D is incorrect:* `KeyError` is the dictionary equivalent — raised for missing dictionary keys. Strings and lists use indices, not keys.

---

### Question 20

What is the purpose of defining a custom exception class?

- A) To bypass Python's exception hierarchy and raise any object
- B) To provide a specific, named exception type that callers can catch selectively and that carries domain-specific context
- C) To replace the standard exception hierarchy with your own
- D) Custom exceptions are only needed for performance optimization

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Custom exceptions must still inherit from `BaseException`. You cannot raise arbitrary objects as exceptions — `raise "oops"` is a `TypeError`.
- *Why B is correct:* Custom exceptions allow callers to distinguish between your application's specific error conditions. `except DatabaseConnectionError:` is more precise and informative than `except Exception:`. They can also carry extra attributes (port numbers, query text, etc.) as domain context.
- *Why C is incorrect:* Custom exceptions extend the standard hierarchy — they do not replace it. `class MyError(Exception): pass` inherits all of `Exception`'s behavior.
- *Why D is incorrect:* Custom exceptions have nothing to do with performance. They are a design tool for expressing domain-specific error conditions clearly.
