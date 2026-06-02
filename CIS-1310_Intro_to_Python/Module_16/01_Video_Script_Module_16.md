# Video Script: CIS-1310 — Introduction to Python

## Module 16 — Final Exam Prep and PCAP Certification Review

**Estimated Duration:** 18–22 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run quick code snippets to reinforce each trap.
> - [PAUSE] = hold 2 seconds of silence.
> - This script is longer than typical modules — it is a full course review. Consider recording in two parts: Part 1 (00:00–10:00) covering language fundamentals, Part 2 (10:00–end) covering OOP and exam strategy.
> - Emphasize the "trap" patterns — these are the questions students miss most on PCAP.
> - End with actionable exam-day advice: schedule, question strategy, time management.

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 16 | Final Exam Prep | CIS-1310"]**

"Welcome to Module 16 — the final module of CIS-1310. You have covered the full core Python language. Today we do not introduce new material. Instead, we consolidate everything you have learned across fifteen modules into a systematic review, with focused attention on the exam traps that the PCAP tests most heavily.

By the end of this module you will have a clear map of every major topic, a list of the patterns that trick students, and a strategy for approaching the exam itself. Let us make sure every one of you walks in prepared."

---

## [01:00 – 04:00] Part 1 — Language Foundations (Modules 1–5)

**[SHOW SLIDE: "Modules 1–5: Foundations"]**

"**Variables, Types, and Operators (Modules 1–3)**

Python is dynamically typed — variables have no declared type. The type belongs to the value. `type(x)` returns the actual type at runtime.

Integer division: `//` truncates toward negative infinity. `7 // 2` is `3`. `-7 // 2` is `-4` — not `-3`.

Modulo: `7 % 3` is `1`. The sign of the result matches the divisor in Python.

`**` is exponentiation. Operator precedence: `**` before unary minus — `-2**2` is `-4`, not `4`. Parenthesize: `(-2)**2` for `4`.

String multiplication: `'ab' * 3` is `'ababab'`. String concatenation with `+` requires both sides to be strings — mixing with int raises `TypeError`.

**[DEMO — type conversion traps]**

```python
int('3.5')       # ValueError — int() cannot parse a decimal string
int(float('3.5'))  # 3 — convert to float first, then int
bool(0)          # False
bool('')         # False
bool([])         # False
bool(0.0)        # False
bool('0')        # True — non-empty string is truthy
```

[PAUSE]

**Input and Comparison (Modules 3–4)**

`input()` always returns a string. `int(input())` is required to get a number.

`==` compares value. `is` compares identity (same object in memory). Never use `is` to compare strings or numbers in general — use `==`.

`and`, `or`, `not` — short-circuit evaluation. `False and anything` is `False` without evaluating `anything`. `True or anything` is `True` without evaluating `anything`.

**Strings are immutable.** Every string method returns a new string — it does not modify the original. `s.strip()` on a line by itself discards the result."

---

## [04:00 – 07:00] Part 2 — Control Flow and Collections (Modules 4–8)

**[SHOW SLIDE: "Modules 4–8: Control Flow and Data Structures"]**

"**Loops (Module 5)**

`for item in sequence` — iterates items. `for i in range(n)` — produces integers 0 through n-1.

`range(start, stop, step)` — stop is exclusive. `range(1, 10, 2)` produces `1, 3, 5, 7, 9` — not `10`.

`break` exits the loop entirely. `continue` skips to the next iteration. `else` on a loop runs only if the loop completed without a `break`.

**[DEMO — loop/else trap]**

```python
for n in [2, 4, 6]:
    if n % 2 != 0:
        break
else:
    print('all even')    # prints — no break occurred
```

**Lists (Module 6)**

Lists are mutable sequences. Methods that modify in place return `None`: `.sort()`, `.append()`, `.reverse()`. Methods that return a new value: `sorted()`, `s + t`, `s[:]`.

Negative indexing: `lst[-1]` is the last element. Slicing: `lst[1:4]` — indexes 1, 2, 3 (stop is exclusive).

**Tuples (Module 7)** — immutable sequences. Can be used as dictionary keys. Parentheses are optional: `t = 1, 2, 3` creates a tuple. A single-element tuple requires a trailing comma: `(1,)` not `(1)`.

**Sets (Module 7)** — unordered, unique elements. `{}` creates a dict, not a set. Use `set()` for an empty set. `{1, 2, 3}` creates a set. `.add()`, `.remove()`, `.discard()`, union `|`, intersection `&`.

**Dictionaries (Module 10)**

`d['key']` raises `KeyError` if key is missing. `d.get('key')` returns `None`. `d.get('key', default)` returns the default.

`for item in d` iterates keys only. Use `.values()`, `.items()` for values and key-value pairs.

`in` tests keys, not values: `'key' in d` checks keys."

---

## [07:00 – 10:00] Part 3 — Functions and Scope (Modules 8–9)

**[SHOW SLIDE: "Modules 8–9: Functions and Scope"]**

"**Functions (Module 8)**

Default parameter values are evaluated once at definition time — not each call. Mutable defaults (like lists) are shared across all calls:

**[DEMO — mutable default trap]**

```python
def append_to(item, lst=[]):    # lst shared across all calls
    lst.append(item)
    return lst

print(append_to(1))    # [1]
print(append_to(2))    # [2, 1] — not [2]!
```

Fix: use `None` as default, create new list inside.

`*args` collects extra positional arguments as a tuple. `**kwargs` collects extra keyword arguments as a dict.

`lambda x: x * 2` — anonymous function. Equivalent to `def f(x): return x * 2`. Useful as a sort key: `sorted(lst, key=lambda x: x[1])`.

**LEGB Rule (Module 9)**

Python looks up names: Local → Enclosing → Global → Built-in. The first match wins.

Assigning to a name anywhere in a function makes it local throughout the whole function — even lines before the assignment. This causes `UnboundLocalError` if you read the name before assigning.

`global x` — declares `x` refers to the module-level variable. `nonlocal x` — declares `x` refers to the nearest enclosing function's variable (not global).

**Recursion (Module 9)** — a function that calls itself. Always needs a base case. Default recursion limit is 1000 — exceeded raises `RecursionError`."

---

## [10:00 – 12:00] Part 4 — Strings and Exception Handling (Modules 11–12)

**[SHOW SLIDE: "Modules 11–12: Strings and Exceptions"]**

"**String Methods (Module 11) — PCAP traps:**

`.split()` with no argument splits on any whitespace and discards empty strings. `.split(' ')` splits on exactly one space — produces empty strings for runs of spaces.

`.join()` is called on the separator, not the list: `', '.join(['a', 'b'])` — not `['a', 'b'].join(', ')`.

`.find()` returns -1 if not found. `.index()` raises `ValueError`. Trap: `if s.find('x'):` — returns False when found at index 0.

String methods return new strings. They never modify in place.

**Exception Handling (Module 12)**

Execution order: `try` runs → exception? `except` runs → no exception? `else` runs → always: `finally` runs.

`else` is skipped whenever any exception occurs — even a caught one.

`finally` runs even with `return` inside `try` — before the value is delivered to the caller.

`except Exception:` before `except ValueError:` makes `ValueError` unreachable — `ValueError` is a subclass of `Exception`.

Bare `raise` inside `except` re-raises the current exception with its original traceback.

`except BaseException:` and bare `except:` catch `SystemExit` and `KeyboardInterrupt` — almost always wrong."

---

## [12:00 – 14:00] Part 5 — Modules and OOP (Modules 13–15)

**[SHOW SLIDE: "Modules 13–15: Modules and OOP"]**

"**Modules (Module 13)**

Three import forms: `import math` → use `math.sqrt`. `from math import sqrt` → use `sqrt`. `import math as m` → use `m.sqrt`.

`from module import *` imports all public names — avoid in production.

`__name__ == '__main__'` is `True` only when the file is run directly. When imported, `__name__` is the module name.

**OOP Basics (Module 14)**

`__init__` initializes the instance. Must not return a value. `self` must be the first parameter of every instance method — Python passes it automatically.

Instance variables belong to one object. Class variables are shared by all instances. Assigning `instance.class_var = value` creates a new instance variable — does not modify the class variable.

`__str__` is called by `print()` and `str()`. Must return a string.

**Inheritance (Module 15)**

`class Child(Parent):` — child inherits all parent attributes and methods.

Always call `super().__init__()` in the child's `__init__` — or parent attributes will not exist.

Method overriding: child's version is found first in the MRO. `super().method()` calls the parent's version.

`isinstance(child_obj, Parent)` returns `True`. Use `isinstance()` not `type() ==` when inheritance is involved.

Polymorphism: different objects respond to the same method call with their own behavior. The loop just calls the method — Python routes it to the right class."

---

## [14:00 – 17:00] Part 6 — Top Exam Traps

**[SHOW SLIDE: "The 15 Traps That Appear Most on PCAP"]**

"These are the patterns that students most commonly miss. Go through each one.

**1. Integer division direction.** `−7 // 2` is `−4`, not `−3`. Floor toward negative infinity.

**2. `**` precedence over unary minus.** `−2**2` is `−4`. Use `(−2)**2` for `4`.

**3. `input()` always returns string.** `int(input())` required for arithmetic.

**4. `bool('0')` is `True`.** Non-empty strings are truthy — only `''` is falsy.

**5. Mutable default arguments.** Use `None`, not `[]` or `{}` as a default.

**6. `.sort()` returns `None`.** It modifies in place. `sorted()` returns a new list.

**7. Single-element tuple needs trailing comma.** `(1,)` is a tuple. `(1)` is just `1`.

**8. `{}` is a dict, not a set.** Use `set()` for an empty set.

**9. `random.shuffle()` returns `None`.** In-place — use the list variable.

**10. `.split(' ')` vs `.split()`.** Space argument gives empty strings on multiple spaces.

**11. `.join()` is called on the separator.** `'-'.join(lst)` — not `lst.join('-')`.

**12. `except Exception` before `except ValueError` makes `ValueError` unreachable.**

**13. `finally` runs before `return` is delivered.**

**14. Forgetting `super().__init__()` causes `AttributeError` for parent attributes.**

**15. `isinstance(child, Parent)` is `True`. `type(child) == Parent` is `False`.**"

---

## [17:00 – 18:30] Part 7 — Exam Strategy

**[SHOW SLIDE: "PCAP Exam Day Strategy"]**

"Final advice for exam day.

**Read every question twice before answering.** PCAP questions often have two plausible-looking options that differ by a single character or one line of code. Slow down.

**Trace code by hand.** For output questions, write down each variable's value after each line. Do not try to run the code in your head all at once.

**Eliminate clearly wrong answers first.** On four-option questions, you can often eliminate two options immediately — that turns a 25% guess into a 50% chance if you are unsure.

**Mark and return.** If you are stuck, mark the question and move on. Come back with fresh eyes.

**Watch for the trap keywords.** 'only when,' 'always,' 'never' — PCAP loves precision. An answer that says `finally` 'always runs' is correct. An answer that says `else` 'always runs' is wrong.

**Time management.** PCAP gives you 65 minutes for 40 questions — about 97 seconds per question. Do not spend five minutes on one question. Mark it, move on, return at the end.

You have covered every topic that will appear on this exam. Trust your preparation, trace the code carefully, and you will be ready. Good luck — I will see you at certification."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 16 — Final Exam Prep and PCAP Certification Review]**

---

## Additional Resources

- [PCAP Exam Syllabus](https://pythoninstitute.org/pcap) — Python Institute official PCAP exam objectives
- [Python for Everybody — Dr. Charles Severance](https://www.py4e.com/book) — full textbook review
- [Official Python Docs — Tutorial](https://docs.python.org/3/tutorial/index.html) — authoritative Python 3 tutorial
- [Real Python](https://realpython.com) — practical tutorials for every topic covered in this course
