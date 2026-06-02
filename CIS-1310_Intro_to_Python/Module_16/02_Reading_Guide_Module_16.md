# Reading Guide: Module 16 — Final Exam Prep and PCAP Certification Review

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 16 — Final Exam Prep**. This reading guide is your consolidated review of all 15 modules. It is organized by topic area, focuses on the specific patterns the PCAP exam tests most heavily, and ends with exam-day strategy. There is no new material here — everything below is a precise summary of what you have already learned, distilled into the most testable form.

Work through this guide actively: cover the answers and try to recall each concept before reading the explanation. The patterns you struggle to recall are the ones to prioritize in your final study sessions.

---

## 1. Variables, Types, and Operators (Modules 1–3)

### Key Facts

- Python is **dynamically typed** — variables hold references to objects; the type belongs to the object, not the variable.
- `type(x)` returns the type object. `type(x).__name__` returns the string name.
- Integer types: `int` (unlimited precision), `float` (64-bit IEEE 754), `complex` (`3+4j`).
- `bool` is a subclass of `int`. `True == 1` and `False == 0`.

### Arithmetic Operator Traps

| Expression | Result | Why |
|---|---|---|
| `7 // 2` | `3` | Floor division truncates toward −∞ |
| `−7 // 2` | `−4` | Floor toward −∞: −3.5 floors to −4 |
| `7 % 3` | `1` | Result sign matches divisor |
| `−7 % 3` | `2` | (−7) = 3×(−3) + 2 |
| `−2 ** 2` | `−4` | `**` binds tighter than unary minus |
| `(−2) ** 2` | `4` | Parentheses override |
| `10 / 3` | `3.333...` | True division always returns float |
| `10 // 3` | `3` | Floor division returns int (if both operands int) |

### Truthiness

| Value | Falsy? |
|---|---|
| `0`, `0.0`, `0j` | Yes |
| `''`, `[]`, `()`, `{}`, `set()` | Yes |
| `None` | Yes |
| `'0'`, `[0]`, `(False,)` | No — non-empty container / non-empty string |

**`bool('0')` is `True`** — the string `'0'` is a non-empty string.

### Type Conversion

```python
int('42')         # 42
int('3.5')        # ValueError — int() cannot parse decimal strings
int(float('3.5')) # 3
float('3.14')     # 3.14
str(42)           # '42'
bool(x)           # False for zero/empty/None, True otherwise
```

---

## 2. Strings (Modules 3 and 11)

### Immutability

Every string method returns a new string. The original is unchanged.

```python
s = '  hello  '
s.strip()          # returns '  hello  ' discarded — s unchanged
s = s.strip()      # correct — reassign
```

### Key Method Traps

| Pattern | Trap | Correct |
|---|---|---|
| `.split(' ')` | Returns `['a', '', 'b']` for `'a  b'` | `.split()` collapses all whitespace |
| `.join()` | `lst.join('-')` → `AttributeError` | `'-'.join(lst)` — separator is the caller |
| `.find('x')` | `if s.find('x'):` is `False` when found at 0 | `if s.find('x') != -1:` |
| `.index('x')` | Raises `ValueError` if not found | Use `.find()` if you want −1 |
| `.sort()` | Returns `None` — modifies in place | `sorted(lst)` returns a new list |

### Slicing

```python
s = 'Python'
s[0]       # 'P'
s[-1]      # 'n'
s[1:4]     # 'yth' — stop is exclusive
s[::-1]    # 'nohtyP' — reverse
s[::2]     # 'Pto' — every other character
```

---

## 3. Control Flow (Modules 4–5)

### if / elif / else

Python uses indentation, not braces. `elif` (not `else if`). Conditions do not require parentheses.

### Loops

```python
for i in range(5):         # 0, 1, 2, 3, 4
for i in range(1, 6):      # 1, 2, 3, 4, 5
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
```

`range(stop)`, `range(start, stop)`, `range(start, stop, step)` — stop is always exclusive.

**`for/else`:** the `else` block runs only if the loop completed without a `break`.

```python
for item in lst:
    if condition(item):
        break
else:
    print('no break occurred')    # runs if break never hit
```

`break` exits the loop. `continue` skips to next iteration. Both affect only the innermost loop.

---

## 4. Lists, Tuples, and Sets (Modules 6–7)

### Lists — Mutable

```python
lst = [1, 2, 3]
lst.append(4)         # modifies in place, returns None
lst.sort()            # modifies in place, returns None
new = sorted(lst)     # returns new sorted list
lst.pop()             # removes and returns last element
lst.pop(0)            # removes and returns element at index 0
lst.remove(2)         # removes first occurrence of value 2
len(lst)              # length
lst[1:3]              # slice — stop exclusive
```

### Tuples — Immutable

```python
t = (1, 2, 3)
t = 1, 2, 3        # parentheses optional
t = (1,)           # single-element tuple — trailing comma required
t = (1)            # NOT a tuple — just the integer 1
```

Tuples can be used as dictionary keys (they are hashable). Lists cannot.

### Sets — Unordered, Unique

```python
s = {1, 2, 3}         # set literal
s = set()             # empty set — NOT {}
s.add(4)
s.remove(4)           # KeyError if not found
s.discard(4)          # no error if not found
s1 | s2               # union
s1 & s2               # intersection
s1 - s2               # difference
```

`{}` creates an empty dict, not an empty set.

---

## 5. Dictionaries (Module 10)

```python
d = {'a': 1, 'b': 2}
d['a']                # 1
d['c']                # KeyError
d.get('c')            # None
d.get('c', 0)         # 0 — safe with default
d['c'] = 3            # add or update
del d['a']            # remove key
d.pop('b')            # remove and return value

for k in d:           # iterates keys
for v in d.values():  # iterates values
for k, v in d.items():  # iterates key-value pairs

'a' in d              # True — tests keys, not values
```

Word frequency counter pattern:

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

---

## 6. Functions (Module 8)

```python
def greet(name, greeting='Hello'):    # default parameter
    return f'{greeting}, {name}!'

greet('Alice')              # Hello, Alice!
greet('Bob', 'Hi')          # Hi, Bob!
greet(greeting='Hey', name='Carol')  # keyword arguments
```

### Mutable Default Trap

```python
def bad(lst=[]):    # lst is created ONCE at definition time
    lst.append(1)
    return lst

bad()    # [1]
bad()    # [1, 1] — same list reused!
```

Fix: `def good(lst=None): if lst is None: lst = []`

### `*args` and `**kwargs`

```python
def f(*args):         # args is a tuple of extra positional arguments
    print(args)

def g(**kwargs):      # kwargs is a dict of extra keyword arguments
    print(kwargs)
```

### Lambda

```python
double = lambda x: x * 2
sorted(pairs, key=lambda p: p[1])    # sort by second element
```

---

## 7. Scope — LEGB (Module 9)

Order of lookup: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

**`UnboundLocalError` trap:** assigning to a name anywhere in a function makes it local throughout the entire function — even lines before the assignment.

```python
x = 10
def f():
    print(x)    # UnboundLocalError — x is local because of the assignment below
    x = 20
```

**`global`:** declares the name refers to the module-level variable.
**`nonlocal`:** declares the name refers to the enclosing function's variable.

**Closures:** a nested function that captures variables from its enclosing scope. Captured variables persist after the enclosing function returns.

**Recursion:** always requires a base case. Default limit 1000 — exceeded raises `RecursionError`.

---

## 8. Exception Handling (Module 12)

### Execution Order

```text
try → exception? → except → finally
try → no exception? → else → finally
```

| Clause | Runs when |
|---|---|
| `try` | Always |
| `except` | Only when matching exception occurred in try |
| `else` | Only when NO exception occurred in try |
| `finally` | ALWAYS — even with return/break/continue |

**Critical traps:**

- `except Exception:` before `except ValueError:` — `ValueError` unreachable.
- `finally` runs before a `return` value is delivered to the caller.
- Bare `raise` re-raises current exception with original traceback.
- `except BaseException:` catches `SystemExit` and `KeyboardInterrupt` — almost always wrong.

---

## 9. Modules (Module 13)

| Import form | What lands in namespace | Calling syntax |
|---|---|---|
| `import math` | `math` | `math.sqrt(4)` |
| `from math import sqrt` | `sqrt` | `sqrt(4)` |
| `import math as m` | `m` | `m.sqrt(4)` |
| `from math import *` | all public names | `sqrt(4)` — avoid |

`__name__ == '__main__'` is `True` only when run directly. Use as guard for startup code.

`sys.path` — list of directories searched for modules. Current directory is first.

`pip3 install package` installs from PyPI. Virtual environments isolate per-project dependencies.

---

## 10. OOP Basics (Module 14)

```python
class Dog:
    species = 'Canine'           # class variable — shared

    def __init__(self, name, age):
        self.name = name         # instance variable — per object
        self.age = age

    def bark(self):
        return f'{self.name}: Woof!'

    def __str__(self):
        return f'Dog({self.name!r}, age={self.age})'
```

**Critical traps:**

- `self` must be first parameter of every instance method.
- `__init__` must not return a value.
- `instance.class_var = value` creates an instance variable — does not change the class variable.
- `__str__` must return a string.
- `isinstance(obj, cls)` preferred over `type(obj) == cls`.

---

## 11. Inheritance and Polymorphism (Module 15)

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return 'generic sound'

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # REQUIRED — or self.name won't exist
        self.breed = breed
    def speak(self):
        return f'{self.name}: Woof!'
```

**Critical traps:**

- Forgetting `super().__init__()` → `AttributeError` for parent attributes.
- Child's method override is found first in MRO.
- `super()` calls next class in MRO — do not hardcode parent class name.
- `isinstance(child_obj, ParentClass)` is `True`.
- Polymorphism: same method call, different behavior based on actual type.

**MRO:** `ClassName.__mro__` — tuple from most specific to `object`.

---

## 12. PCAP Exam Quick Reference

### Exam Format

- 40 questions, 65 minutes (approximately 97 seconds per question)
- Passing score: 70%
- Question types: single-choice, multiple-choice, code output, fill-in

### The 15 Most-Tested Traps

1. `−7 // 2` = `−4` (not `−3`)
2. `−2**2` = `−4` (not `4`)
3. `input()` always returns string
4. `bool('0')` = `True`
5. Mutable default argument trap — use `None`
6. `.sort()` returns `None` — use `sorted()` for a new list
7. Single-element tuple: `(1,)` not `(1)`
8. `{}` creates dict — use `set()` for empty set
9. `random.shuffle()` returns `None` — in-place
10. `.split(' ')` vs `.split()` — space arg gives empty strings
11. `.join()` on separator: `'-'.join(lst)`
12. `except Exception:` before `except ValueError:` → unreachable handler
13. `finally` runs before `return` is delivered
14. Missing `super().__init__()` → `AttributeError` on parent attributes
15. `isinstance(child, Parent)` = `True`; `type(child) == Parent` = `False`

---

## 13. Exam-Day Strategy

**Before the exam:**

- Get a full night of sleep. Fatigue costs more points than additional cramming.
- Review the 15 traps above one final time.
- Know the exception hierarchy: `BaseException → SystemExit / KeyboardInterrupt / Exception → specific errors`.

**During the exam:**

- Read each question fully before looking at the answers.
- For code output questions: trace by hand on paper, tracking each variable.
- Eliminate obviously wrong answers first — reduce to the best two, then decide.
- Mark difficult questions and return at the end.
- Watch for absolute words: "always," "never," "only" — these are often in the correct answer and can help identify it.

**Common time wasters:**

- Spending more than 2 minutes on any single question — mark and return.
- Second-guessing correct first instincts — change an answer only if you identify a specific reason.

---

## 14. Study Checklist

- [ ] Watch the Module 16 video lecture by Professor Nash.
- [ ] Write out the 15 exam traps from memory — check against the list above.
- [ ] Trace the execution order of try/except/else/finally for both valid and invalid inputs.
- [ ] Write a five-class OOP hierarchy from scratch: base class, two children, one grandchild, demonstrate polymorphism.
- [ ] Complete the Module 16 Lab (comprehensive coding practice).
- [ ] Complete the Module 16 Quiz (final practice exam questions).
- [ ] Schedule your PCAP exam.
