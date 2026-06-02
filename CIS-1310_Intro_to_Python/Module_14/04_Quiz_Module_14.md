# Quiz: Module 14 — Object-Oriented Programming: Basics

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 14 topics.

---

### Question 1

What is the output of this code?

```python
class Dog:
    def __init__(self, name):
        self.name = name

d1 = Dog('Rex')
d2 = Dog('Luna')
d1.name = 'Max'
print(d1.name)
print(d2.name)
```

- A) `Max` then `Max`
- B) `Rex` then `Luna`
- C) `Max` then `Luna`
- D) `TypeError` — you cannot modify attributes after creation

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `d1.name` and `d2.name` are separate instance variables. Modifying one instance's attribute does not affect any other instance.
- *Why B is incorrect:* `d1.name = 'Max'` does modify `d1`'s name. The question shows an explicit assignment after creation, so `d1.name` is `'Max'`, not the original `'Rex'`.
- *Why C is correct:* `d1.name = 'Max'` changes only `d1`'s instance variable. `d2.name` remains `'Luna'` because each instance has its own independent copy of instance variables.
- *Why D is incorrect:* Python instances are mutable by default. You can add, change, or delete instance attributes at any time after creation.

---

### Question 2

What is the output of this code?

```python
class Dog:
    def bark():
        return 'Woof!'

d = Dog()
d.bark()
```

- A) `'Woof!'`
- B) `TypeError: bark() takes 0 positional arguments but 1 was given`
- C) `AttributeError: 'Dog' object has no attribute 'bark'`
- D) `None`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `bark()` is missing `self` as its first parameter. When you call `d.bark()`, Python automatically passes the instance `d` as the first argument. Since `bark()` accepts no parameters, Python cannot place `d` anywhere — hence the error.
- *Why B is correct:* Python's method call mechanism always passes the instance as the first argument. `bark()` declares zero parameters but receives one (the instance), causing the `TypeError`.
- *Why C is incorrect:* `bark` is defined in the class and is accessible as an attribute. `AttributeError` would occur if `bark` did not exist at all.
- *Why D is incorrect:* The call raises an exception before any return value can be produced.

---

### Question 3

What is the output of this code?

```python
class Counter:
    count = 0

c1 = Counter()
c2 = Counter()
c1.count = 99
print(Counter.count)
print(c2.count)
```

- A) `99` then `99`
- B) `0` then `0`
- C) `99` then `0`
- D) `0` then `99`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `c1.count = 99` does not modify the class variable. It creates a new instance variable `count` on `c1` that shadows the class variable for `c1` only.
- *Why B is correct:* `Counter.count` is the class variable — it remains `0` because `c1.count = 99` only created a new instance variable on `c1`. `c2.count` has no instance variable, so it reads the class variable `Counter.count`, which is still `0`.
- *Why C is incorrect:* `Counter.count` is unchanged by the instance assignment. It is still `0`, not `99`.
- *Why D is incorrect:* `Counter.count` is `0` (not changed) and `c2.count` is also `0` (reads class variable). The order of values is reversed from what this option says.

---

### Question 4

Which of the following correctly defines `__str__` for this class?

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

- A) `def __str__(self): return self.x, self.y`
- B) `def __str__(self): return f'Point({self.x}, {self.y})'`
- C) `def __str__(self): print(f'Point({self.x}, {self.y})')`
- D) `def __str__(x, y): return f'Point({x}, {y})'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `return self.x, self.y` returns a tuple, not a string. `__str__` must return a string — returning anything else raises `TypeError: __str__ returned non-string`.
- *Why B is correct:* Returns a properly formatted string using an f-string. This is the correct `__str__` implementation — it takes `self` as the first parameter and returns a string.
- *Why C is incorrect:* This uses `print()` inside the method, which prints a side effect but returns `None`. `print(obj)` calls `__str__` and uses its return value — if `__str__` returns `None`, it would print `None`.
- *Why D is incorrect:* Instance methods must take `self` as the first parameter. `def __str__(x, y)` treats `x` as `self` (the instance) and `y` as the second positional argument. Calling `str(p)` would pass only the instance — there is no value for `y`, causing `TypeError`.

---

### Question 5

What is the output of this code?

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, age {self.age}'

d = Dog('Rex', 4)
d.age = 5
print(d)
```

- A) `Rex, age 4`
- B) `Rex, age 5`
- C) `<__main__.Dog object at 0x...>`
- D) `TypeError` — cannot modify age after construction

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `d.age = 5` modifies `d.age` to `5` before the `print()` call. `__str__` reads `self.age` at the time it is called, so it returns the updated value `5`.
- *Why B is correct:* `d.age = 5` updates the instance variable. When `print(d)` calls `__str__`, `self.age` is `5`, so the output is `Rex, age 5`.
- *Why C is incorrect:* `__str__` is defined, so `print(d)` uses it instead of the default memory address representation.
- *Why D is incorrect:* Python instances are mutable. Instance variable attributes can be modified at any time.

---

### Question 6

What does `isinstance(d, object)` return for any Python object `d`?

- A) `True` only if `d` is an integer
- B) `True` only if `d` was created from a user-defined class
- C) `True` for any Python object — all classes inherit from `object`
- D) `False` — `object` is not a class that objects are instances of

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `isinstance(d, object)` is not specific to integers. All Python objects — strings, lists, custom class instances, functions, even `None` — are instances of `object`.
- *Why B is incorrect:* `object` is the root of Python's class hierarchy. Built-in types like `int`, `str`, and `list` also inherit from `object`. The result is `True` for built-in types too.
- *Why C is correct:* In Python, all classes implicitly inherit from `object` at the top of the inheritance chain. Therefore `isinstance(anything, object)` is always `True`.
- *Why D is incorrect:* `object` is indeed a class — it is the base class for all Python classes. `isinstance(42, object)` returns `True`.

---

### Question 7

What is the output of this code?

```python
class Dog:
    species = 'Canine'

    def __init__(self, name):
        self.name = name

d1 = Dog('Rex')
d2 = Dog('Luna')
Dog.species = 'Canis familiaris'
print(d1.species)
print(d2.species)
```

- A) `Canine` then `Canine`
- B) `Canis familiaris` then `Canis familiaris`
- C) `Canine` then `Canis familiaris`
- D) `Canis familiaris` then `Canine`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Dog.species = 'Canis familiaris'` modifies the class variable directly through the class. Since neither `d1` nor `d2` have their own instance variable `species`, both read the updated class variable.
- *Why B is correct:* `Dog.species = 'Canis familiaris'` changes the class variable. Neither `d1` nor `d2` have instance-level `species` variables (no instance assignment was made), so both see the new class variable value.
- *Why C is incorrect:* This would be the result if `d1.species` had been set individually to `'Canine'` before the class-level change — but it was not. Both instances read from the class variable.
- *Why D is incorrect:* The class variable was changed before any printing. Both print calls happen after the modification.

---

### Question 8

What is the output of this code?

```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    def deposit(self, amount):
        self._balance += amount
        return self._balance

acc = BankAccount('Alice', 100.0)
result = acc.deposit(50.0)
print(result)
print(acc._balance)
```

- A) `None` then `150.0`
- B) `150.0` then `100.0`
- C) `150.0` then `150.0`
- D) `TypeError` — you cannot access `_balance` from outside the class

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `deposit()` has an explicit `return self._balance` statement. It returns the updated balance, not `None`. `None` would be returned if there was no return statement.
- *Why B is incorrect:* `deposit()` modifies `self._balance` in place (`self._balance += amount`) before returning. Both `result` and `acc._balance` reflect the same updated value.
- *Why C is correct:* `deposit(50.0)` adds 50 to the balance (100 + 50 = 150), then returns `self._balance`. `result` is `150.0`. `acc._balance` was modified in place, so it is also `150.0`.
- *Why D is incorrect:* The single-underscore prefix (`_balance`) is a naming convention that signals "internal use" — it is not enforced by Python. You can access `acc._balance` from outside the class without error, though it is discouraged by convention.

---

### Question 9

What is the output of this code?

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

d = Dog('Rex', 4)
print(hasattr(d, 'name'))
print(hasattr(d, 'weight'))
print(getattr(d, 'age'))
print(getattr(d, 'weight', 0))
```

- A) `True` then `False` then `4` then `AttributeError`
- B) `True` then `True` then `4` then `0`
- C) `True` then `False` then `4` then `0`
- D) `False` then `False` then `4` then `0`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `getattr(d, 'weight', 0)` has a default value of `0`. When the attribute does not exist and a default is provided, `getattr` returns the default instead of raising `AttributeError`.
- *Why B is incorrect:* `hasattr(d, 'weight')` returns `False` because `weight` was never assigned to `d`. Only `name` and `age` were set in `__init__`.
- *Why C is correct:* `hasattr(d, 'name')` is `True` (set in `__init__`). `hasattr(d, 'weight')` is `False` (never set). `getattr(d, 'age')` returns `4`. `getattr(d, 'weight', 0)` returns the default `0` because `weight` does not exist.
- *Why D is incorrect:* `hasattr(d, 'name')` is `True`, not `False`. `name` was assigned in `__init__`.

---

### Question 10

What is the output of this code?

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

d = Dog('Rex', 3)
result = d.birthday()
print(d.age)
print(result)
```

- A) `3` then `None`
- B) `4` then `4`
- C) `4` then `None`
- D) `3` then `4`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `birthday()` modifies `self.age` in place. `self.age += 1` changes `d.age` from `3` to `4`. The printed value of `d.age` is `4`, not `3`.
- *Why B is incorrect:* `birthday()` has no `return` statement. A function with no return statement returns `None`. `result` is `None`, not `4`.
- *Why C is correct:* `birthday()` increments `self.age` to `4` and returns `None` (no return statement). `d.age` is `4`, and `result` is `None`.
- *Why D is incorrect:* `d.age` after calling `birthday()` is `4`, not `3` — the method mutated it. And `result` would be `None`, not `4`.
