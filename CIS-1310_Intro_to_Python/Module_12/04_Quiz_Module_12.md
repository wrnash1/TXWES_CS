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
