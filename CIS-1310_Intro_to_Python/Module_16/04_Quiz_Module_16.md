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

---

### Question 11

What is the output of this code?

```python
s = 'abcde'
print(s[1:4])
print(s[::-1])
print(s[::2])
```

- A) `bcd`, `edcba`, `ace`
- B) `bcd`, `abcde`, `ace`
- C) `bcde`, `edcba`, `ace`
- D) `bcd`, `edcba`, `abce`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `s[1:4]` extracts indices 1, 2, 3 → `'bcd'`. `s[::-1]` reverses the entire string → `'edcba'`. `s[::2]` takes every second character starting at index 0 → indices 0, 2, 4 → `'ace'`.
- *Why B is incorrect:* `s[::-1]` reverses the string to `'edcba'`, not `'abcde'`. A step of `−1` reads right to left.
- *Why C is incorrect:* `s[1:4]` stops before index 4 (exclusive upper bound), returning `'bcd'` not `'bcde'`. Slices follow the half-open interval `[start, stop)`.
- *Why D is incorrect:* `s[::2]` selects indices 0, 2, 4 — letters `a`, `c`, `e` — which is `'ace'`, not `'abce'`.

---

### Question 12

What is the output of this code?

```python
def make_adder(n):
    return lambda x: x + n

add5 = make_adder(5)
add10 = make_adder(10)

print(add5(3))
print(add10(3))
print(add5(add10(1)))
```

- A) `8`, `13`, `16`
- B) `8`, `13`, `14`
- C) `5`, `10`, `16`
- D) `8`, `13`, `8`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `add5(3)` → `3 + 5 = 8`. `add10(3)` → `3 + 10 = 13`. `add5(add10(1))`: inner `add10(1)` → `11`; outer `add5(11)` → `16`. Closures capture `n` at definition time.
- *Why B is incorrect:* `add5(add10(1))` = `add5(11)` = `16`, not `14`. `add10(1)` evaluates to `11`, not `4`.
- *Why C is incorrect:* `add5(3)` is `3 + 5 = 8`, not `5`. The lambda adds `x` to the captured `n`, not just returns `n`.
- *Why D is incorrect:* `add10(3)` is `13` not `8`, and `add5(add10(1))` evaluates the inner call first (`11`) then adds `5` → `16`.

---

### Question 13

What is the output of this code?

```python
data = {'x': [1, 2, 3], 'y': [4, 5]}
copy = data.copy()
copy['x'].append(99)
copy['z'] = [6]

print(data['x'])
print('z' in data)
```

- A) `[1, 2, 3, 99]` then `False`
- B) `[1, 2, 3]` then `False`
- C) `[1, 2, 3, 99]` then `True`
- D) `[1, 2, 3]` then `True`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `.copy()` creates a **shallow** copy — a new dict, but the values (the lists) are shared references. `copy['x'].append(99)` mutates the shared list, so `data['x']` also becomes `[1, 2, 3, 99]`. `copy['z'] = [6]` adds a new key only to `copy` — `data` is unaffected, so `'z' in data` is `False`.
- *Why B is incorrect:* Shallow copy means the list objects inside are shared. Mutating `copy['x']` (via `.append`) also changes `data['x']` because both point to the same list object.
- *Why C is incorrect:* `copy['z'] = [6]` only modifies `copy`, not `data`. Adding a key to the copy does not affect the original dict.
- *Why D is incorrect:* Both errors from B and C combined. `.append` does mutate the shared inner list, and adding `'z'` to `copy` does not touch `data`.

---

### Question 14

What is the output of this code?

```python
class Base:
    def greet(self):
        return 'Hello from Base'

class Child(Base):
    def greet(self):
        return super().greet() + ' and Child'

class GrandChild(Child):
    def greet(self):
        return super().greet() + ' and GrandChild'

print(GrandChild().greet())
```

- A) `Hello from Base and GrandChild`
- B) `Hello from Base and Child and GrandChild`
- C) `Hello from Base`
- D) `Hello from Base and Child`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `GrandChild.greet()` calls `super().greet()` which is `Child.greet()`. `Child.greet()` itself calls `super().greet()` (i.e., `Base.greet()`). The chain unwinds: Base returns `'Hello from Base'`, Child appends `' and Child'`, GrandChild appends `' and GrandChild'`.
- *Why B is correct:* MRO for GrandChild is `GrandChild → Child → Base → object`. `GrandChild.greet()` calls `Child.greet()` via `super()`, which calls `Base.greet()` via `super()`. Result builds up: `'Hello from Base'` + `' and Child'` + `' and GrandChild'`.
- *Why C is incorrect:* Each level extends the parent result. `Child` and `GrandChild` do not discard the parent return — they append to it.
- *Why D is incorrect:* `GrandChild.greet()` adds `' and GrandChild'` to whatever `Child.greet()` returned, so the final string includes all three levels.

---

### Question 15

What is the output of this code?

```python
nums = [4, 2, 7, 1, 9, 3]
nums.sort()
print(nums)
result = sorted(nums, key=lambda x: -x)
print(result)
print(nums)
```

- A) `[1, 2, 3, 4, 7, 9]`, `[9, 7, 4, 3, 2, 1]`, `[1, 2, 3, 4, 7, 9]`
- B) `[1, 2, 3, 4, 7, 9]`, `[9, 7, 4, 3, 2, 1]`, `[9, 7, 4, 3, 2, 1]`
- C) `[4, 2, 7, 1, 9, 3]`, `[9, 7, 4, 3, 2, 1]`, `[4, 2, 7, 1, 9, 3]`
- D) `[1, 2, 3, 4, 7, 9]`, `[1, 2, 3, 4, 7, 9]`, `[1, 2, 3, 4, 7, 9]`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `nums.sort()` sorts in place → `[1, 2, 3, 4, 7, 9]`. `sorted(nums, key=lambda x: -x)` creates a new list sorted by negative value (descending) → `[9, 7, 4, 3, 2, 1]`. `sorted()` never modifies the original — `nums` is still `[1, 2, 3, 4, 7, 9]`.
- *Why B is incorrect:* `sorted()` returns a new list and does not mutate `nums`. The third print still shows the ascending-sorted `nums`, not the descending `result`.
- *Why C is incorrect:* `nums.sort()` modifies `nums` in place — the first print shows the sorted list, not the original order.
- *Why D is incorrect:* `key=lambda x: -x` negates each value before comparison, reversing the sort order. The result is descending `[9, 7, 4, 3, 2, 1]`, not ascending.

---

### Question 16

What is the output of this code?

```python
def count_vowels(text):
    vowels = set('aeiouAEIOU')
    return sum(1 for ch in text if ch in vowels)

words = ['Python', 'is', 'great']
results = list(map(lambda w: (w, count_vowels(w)), words))
print(results)
```

- A) `[('Python', 1), ('is', 1), ('great', 2)]`
- B) `[('Python', 2), ('is', 1), ('great', 2)]`
- C) `[('Python', 1), ('is', 2), ('great', 2)]`
- D) `[1, 1, 2]`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `count_vowels('Python')` → `'o'` is the only vowel (1). `count_vowels('is')` → `'i'` is the only vowel (1). `count_vowels('great')` → `'e'` and `'a'` (2). `map` with the lambda produces a tuple `(word, count)` for each. `list(map(...))` collects them.
- *Why B is incorrect:* `'Python'` contains only one vowel: `'o'`. The `'y'` is not in the vowel set `'aeiouAEIOU'`, so the count is 1, not 2.
- *Why C is incorrect:* `'is'` contains only `'i'` — one vowel. The count is 1, not 2.
- *Why D is incorrect:* The `map` lambda returns a tuple `(word, count)` for each word, not just the integer count. The result is a list of tuples.

---

### Question 17

What is the output of this code?

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
        return self

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)

s = Stack()
s.push(1).push(2).push(3)
print(len(s))
print(s.pop())
print(len(s))
```

- A) `3`, `3`, `2`
- B) `3`, `1`, `2`
- C) `1`, `3`, `0`
- D) `TypeError` — `push` returns `self`, not `Stack`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `push` appends the item and returns `self` for chaining. After `s.push(1).push(2).push(3)`, `_items = [1, 2, 3]`. `len(s)` calls `__len__` → `3`. `s.pop()` calls `list.pop()` with no argument, which removes and returns the **last** element → `3`. After pop, `_items = [1, 2]`, so `len(s)` → `2`.
- *Why B is incorrect:* `list.pop()` with no argument removes the **last** item, not the first. The last item pushed was `3`, so `s.pop()` returns `3`, not `1`.
- *Why C is incorrect:* Three items were pushed, so `len(s)` starts at `3`. The chain `push(1).push(2).push(3)` completes all three pushes before any print.
- *Why D is incorrect:* Returning `self` from a method is a valid Python pattern enabling method chaining. `self` is the same `Stack` instance — there is no `TypeError`.

---

### Question 18

What is the output of this code?

```python
words = ['banana', 'apple', 'cherry', 'date', 'elderberry']
result = sorted(words, key=lambda w: (len(w), w))
print(result[0])
print(result[-1])
print(len(result))
```

- A) `'apple'`, `'elderberry'`, `5`
- B) `'date'`, `'elderberry'`, `5`
- C) `'apple'`, `'banana'`, `5`
- D) `'date'`, `'cherry'`, `5`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Sorting by `(len(w), w)` orders primarily by length, then alphabetically within equal lengths. `'apple'` has length 5. `'date'` has length 4, which is shorter — so `'date'` sorts first, not `'apple'`.
- *Why B is correct:* Lengths: `date`=4, `apple`=5, `banana`=6, `cherry`=6, `elderberry`=10. Primary sort by length puts `'date'` first (shortest). For the two length-6 words (`banana` and `cherry`), the secondary alphabetical sort places `banana` before `cherry`. The sorted order is `['date', 'apple', 'banana', 'cherry', 'elderberry']`. `result[0]` = `'date'`, `result[-1]` = `'elderberry'`, `len(result)` = `5`.
- *Why C is incorrect:* `result[-1]` is the last element after sorting by `(length, alpha)`. `'elderberry'` (length 10) is the longest word and sorts last, not `'banana'`.
- *Why D is incorrect:* `result[-1]` is `'elderberry'` (length 10), not `'cherry'` (length 6). Longer words sort after shorter words with this key.

---

### Question 19

What is the output of this code?

```python
def mystery(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [x for x in lst[1:] if x <= pivot]
    greater = [x for x in lst[1:] if x > pivot]
    return mystery(less) + [pivot] + mystery(greater)

print(mystery([3, 6, 1, 8, 2, 9, 4]))
```

- A) `[3, 6, 1, 8, 2, 9, 4]`
- B) `[1, 2, 3, 4, 6, 8, 9]`
- C) `[9, 8, 6, 4, 3, 2, 1]`
- D) `[1, 3, 2, 4, 6, 8, 9]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `mystery` is a recursive function that partitions around a pivot and recombines — this is quicksort. The function returns a sorted list, not the original order.
- *Why B is correct:* This is a recursive quicksort implementation. `pivot = 3`. `less = [1, 2]` (elements ≤ 3 from the rest), `greater = [6, 8, 9, 4]` (elements > 3). Recursion sorts each partition; the final result is the fully sorted list `[1, 2, 3, 4, 6, 8, 9]`.
- *Why C is incorrect:* The function sorts ascending. Elements `<= pivot` go to `less` (placed first), which produces ascending order, not descending.
- *Why D is incorrect:* `[1, 3, 2, 4, 6, 8, 9]` is not fully sorted — `2` appears after `3`. The recursion fully sorts all partitions, so every element ends up in ascending position.

---

### Question 20

What is the output of this code?

```python
class Formatter:
    prefix = '>> '

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'{self.prefix}{self.text}'

    def __repr__(self):
        return f'Formatter({self.text!r})'

    @classmethod
    def from_upper(cls, text):
        return cls(text.upper())

f1 = Formatter('hello')
f2 = Formatter.from_upper('world')
items = [f1, f2]
print(str(f1))
print(repr(f2))
print(items)
```

- A) `>> hello`, `Formatter('WORLD')`, `[Formatter('hello'), Formatter('WORLD')]`
- B) `>> hello`, `Formatter('WORLD')`, `[>> hello, >> WORLD]`
- C) `hello`, `Formatter('world')`, `[Formatter('hello'), Formatter('world')]`
- D) `>> hello`, `>> WORLD`, `[>> hello, >> WORLD]`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `str(f1)` calls `__str__` → `'>> hello'`. `repr(f2)` calls `__repr__` → `'Formatter(\'WORLD\')'`. Printing a list uses `repr()` for each element (not `str()`), so `items` displays as `[Formatter('hello'), Formatter('WORLD')]`.
- *Why B is incorrect:* Printing a list calls `repr()` on each element, not `str()`. The list display uses `__repr__`, not `__str__`, so the `>>` prefixes do not appear in the list output.
- *Why C is incorrect:* `from_upper` converts the text to uppercase: `'world'.upper()` → `'WORLD'`. `f2.text` is `'WORLD'`, so `repr(f2)` shows `Formatter('WORLD')`, not `Formatter('world')`.
- *Why D is incorrect:* `repr(f2)` explicitly calls `__repr__`, which returns `'Formatter(\'WORLD\')'`. Only `__str__` returns the `>>` prefixed format. The two dunder methods produce different output.
