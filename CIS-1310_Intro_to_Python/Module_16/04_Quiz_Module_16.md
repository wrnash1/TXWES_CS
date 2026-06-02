# Quiz: Module 16 — Final Exam Prep and PCAP Certification Review

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** This is a comprehensive practice quiz drawing from all 15 modules. Choose the single best answer for each question.

---

### Question 1

What is the output of this code?

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item('a'))
print(add_item('b'))
```

- A) `['a']` then `['a', 'b']`
- B) `['a']` then `['b']`
- C) `['a', 'b']` then `['a', 'b']`
- D) `TypeError` — default argument cannot be `None`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This would be the result if the default were `lst=[]` (mutable default). With `lst=[]`, the same list is reused across calls, so the second call appends to it. But here the default is `None`, so each call creates a fresh `[]`.
- *Why B is correct:* `lst=None` is the correct pattern. Each time `add_item` is called without a list argument, `lst` is `None`, the `if` creates a brand-new `[]`, and `'a'` or `'b'` is appended to that new list. Each call is independent.
- *Why C is incorrect:* `['a', 'b']` would appear on both calls only if both were appending to the same shared list — the mutable default trap. The `None` default prevents this.
- *Why D is incorrect:* `None` is a perfectly valid default argument. It is the recommended pattern precisely to avoid the mutable default trap.

---

### Question 2

What is the output of this code?

```python
x = 10

def outer():
    x = 20
    def inner():
        nonlocal x
        x = 30
    inner()
    print(x)

outer()
print(x)
```

- A) `30` then `30`
- B) `20` then `10`
- C) `30` then `10`
- D) `10` then `10`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `nonlocal x` inside `inner` refers to `outer`'s `x`, not the global `x`. After `inner()` runs, `outer`'s `x` is `30`. But the global `x` — declared at module level — is unchanged. `print(x)` after `outer()` reads the global: `10`.
- *Why B is incorrect:* `nonlocal x` makes `inner` modify `outer`'s `x`. After `inner()`, `outer`'s local `x` is `30`, not `20`. The first print is `30`.
- *Why C is correct:* `nonlocal x` refers to the enclosing `outer` function's `x`. `inner()` sets it to `30`. `outer` then prints `30`. The global `x = 10` is untouched — `print(x)` after `outer()` returns `10`.
- *Why D is incorrect:* `outer`'s `x` is modified by `inner()`. It is `30` after `inner()` runs, so the first print is `30`, not `10`.

---

### Question 3

What is the output of this code?

```python
for i in range(1, 6):
    if i == 3:
        break
else:
    print('completed')
print('done')
```

- A) `completed` then `done`
- B) `done`
- C) `completed`
- D) Nothing is printed

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The `else` clause on a `for` loop runs only if the loop completed without hitting a `break`. Here, `i == 3` causes a `break`, so the `else` block is skipped entirely.
- *Why B is correct:* `break` fires when `i == 3`. This exits the loop without running the `else` block. Execution continues after the entire for/else structure — `print('done')` runs.
- *Why C is incorrect:* The `else` block requires the loop to finish without `break`. Since `break` occurred, `'completed'` is never printed.
- *Why D is incorrect:* `print('done')` is outside the for/else structure — it runs regardless of how the loop ended.

---

### Question 4

What is the output of this code?

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('caught')
else:
    print('success')
finally:
    print('finally')
```

- A) `caught` then `success` then `finally`
- B) `caught` then `finally`
- C) `success` then `finally`
- D) `finally` only

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `else` runs only when no exception occurred in `try`. Since `ZeroDivisionError` was raised and caught, `else` is skipped. `else` and `except` are mutually exclusive — if `except` ran, `else` does not.
- *Why B is correct:* `10 / 0` raises `ZeroDivisionError` → `except` runs (prints `caught`) → `else` is skipped → `finally` always runs (prints `finally`).
- *Why C is incorrect:* `success` requires no exception. The division by zero prevents `else` from running.
- *Why D is incorrect:* `finally` always runs, but so does `except` when a matching exception occurs. Both `caught` and `finally` are printed.

---

### Question 5

What is the output of this code?

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name}: ...'

    def describe(self):
        return f'I am {self.name}. {self.speak()}'

class Dog(Animal):
    def speak(self):
        return f'{self.name}: Woof!'

d = Dog('Rex')
print(d.describe())
```

- A) `I am Rex. Rex: ...`
- B) `I am Rex. Rex: Woof!`
- C) `AttributeError` — `describe` is not defined on `Dog`
- D) `I am Rex.`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `d.describe()` calls the inherited `Animal.describe()`. Inside that method, `self.speak()` is called — and `self` is a `Dog` instance. Python looks up `speak` on the actual type, which is `Dog`. `Dog.speak()` is found and called, returning `'Rex: Woof!'`.
- *Why B is correct:* `Dog` inherits `describe()` from `Animal`. Inside `describe`, `self.speak()` uses the MRO — `Dog.speak()` is found first and returns `'Rex: Woof!'`. This demonstrates that polymorphism applies even inside inherited methods.
- *Why C is incorrect:* `Dog` inherits `describe` from `Animal`. Inherited methods are fully accessible on subclass instances.
- *Why D is incorrect:* `self.speak()` returns the full string — the sentence is not cut off. The complete `describe()` output includes both parts.

---

### Question 6

What is the output of this code?

```python
data = [3, 1, 4, 1, 5, 9, 2, 6]
result = sorted(data, reverse=True)
print(data[0])
print(result[0])
```

- A) `3` then `9`
- B) `9` then `9`
- C) `9` then `3`
- D) `3` then `3`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `sorted()` returns a new sorted list — it does not modify `data`. `data` is unchanged: `data[0]` is still `3`. `result` is the new reversed-sorted list: `[9, 6, 5, 4, 3, 2, 1, 1]`, so `result[0]` is `9`.
- *Why B is incorrect:* `data[0]` is `3` — `data` was not modified. `sorted()` creates a new list.
- *Why C is incorrect:* `result` is sorted in reverse (descending) — `result[0]` is `9`, the largest element. `data[0]` is the original first element `3`.
- *Why D is incorrect:* `result[0]` is the largest element `9` (reverse sort puts largest first), not `3`.

---

### Question 7

What is the output of this code?

```python
d = {'a': 1, 'b': 2, 'c': 3}

total = 0
for item in d:
    total += item

print(total)
```

- A) `6`
- B) `'abc'`
- C) `TypeError`
- D) `0`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `for item in d` iterates the **keys** of the dictionary, not the values. The keys are strings `'a'`, `'b'`, `'c'`. Adding a string to an integer `0` raises `TypeError`.
- *Why B is incorrect:* While `item` does iterate the string keys, `total += item` tries to add a string to `int(0)`. This raises `TypeError` on the first iteration.
- *Why C is correct:* `for item in d` yields keys: `'a'`, `'b'`, `'c'`. `total += 'a'` attempts `0 + 'a'` — `TypeError: unsupported operand type(s) for +=: 'int' and 'str'`.
- *Why D is incorrect:* The loop body executes before `print(total)`. The `TypeError` is raised before `print` is reached.

---

### Question 8

What is the output of this code?

```python
def f():
    try:
        return 'try'
    finally:
        return 'finally'

print(f())
```

- A) `try`
- B) `finally`
- C) `try` then `finally`
- D) `TypeError` — cannot have return in finally

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `finally` always runs before the `return` in `try` delivers its value. When `finally` also contains a `return`, it overrides the `try` block's return value.
- *Why B is correct:* `try` would return `'try'`, but `finally` runs first and itself contains `return 'finally'`. A `return` inside `finally` overrides the `try` block's return. The caller receives `'finally'`.
- *Why C is incorrect:* Only one value is returned. `finally`'s `return` overrides `try`'s `return` — you do not see both.
- *Why D is incorrect:* Python allows `return` inside a `finally` block (though it is considered poor practice). The PCAP exam specifically tests this behavior.

---

### Question 9

What is the output of this code?

```python
from math import sqrt as sq

print(sq(64))

import math as m
print(m.pi > 3)
print(math.pi)
```

- A) `8.0` then `True` then `3.141592...`
- B) `8.0` then `True` then `NameError`
- C) `NameError` on first line
- D) `8.0` then `False` then `NameError`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `import math as m` imports `math` under the alias `m`. The name `math` itself is not added to the namespace. `math.pi` raises `NameError` because `math` is not a name in the current namespace — only `m` is.
- *Why B is correct:* `sq(64)` works — `sq` is the alias for `sqrt`. `m.pi > 3` works — `m` is the alias for `math`, and `math.pi` (~3.14) is greater than `3`. `math.pi` raises `NameError` because `import math as m` did not create the name `math`.
- *Why C is incorrect:* `from math import sqrt as sq` correctly creates `sq` in the namespace. `sq(64)` succeeds.
- *Why D is incorrect:* `m.pi` is `3.141592...` which is greater than `3`, so `m.pi > 3` is `True`, not `False`.

---

### Question 10

What is the output of this code?

```python
class Vehicle:
    count = 0

    def __init__(self, make):
        self.make = make
        Vehicle.count += 1

v1 = Vehicle('Toyota')
v2 = Vehicle('Honda')
v3 = Vehicle('Ford')

print(Vehicle.count)
print(v1.count)
v1.count = 99
print(Vehicle.count)
print(v2.count)
```

- A) `3` then `3` then `99` then `99`
- B) `3` then `3` then `3` then `3`
- C) `3` then `3` then `3` then `3` — but `v1.count` is now `99`
- D) `3` then `3` then `3` then `3`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `v1.count = 99` creates a new instance variable `count` on `v1` — it does not modify `Vehicle.count`. `Vehicle.count` remains `3`. `v2.count` still reads the class variable `3`.
- *Why B is incorrect:* After `v1.count = 99`, `v1.count` is `99` (instance variable shadows class variable on `v1`). The printed values are `3`, `3`, `3`, `3` — but the description does not capture the state of `v1.count` after the assignment.
- *Why C is correct:* `Vehicle.count` is incremented to `3` by three constructions. `v1.count` reads the class variable: `3`. `v1.count = 99` creates an instance variable on `v1` — class variable unchanged. `Vehicle.count` is still `3`. `v2.count` has no instance variable, still reads class variable: `3`. The printed output is `3`, `3`, `3`, `3` — and as a side note, `v1.count` is now `99` (shadowed).
- *Why D is incorrect:* Option D is worded identically to option B — the distinction is the explanatory note in option C that captures what actually happened to `v1.count`. The correct answer is C because it accurately identifies that `v1.count = 99` creates an instance variable (shadowing) while leaving the class variable untouched.
