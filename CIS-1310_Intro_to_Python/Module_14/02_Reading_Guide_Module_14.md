# Reading Guide: Module 14 — Object-Oriented Programming: Basics

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

Welcome to **Module 14 — Object-Oriented Programming: Basics**. Every value in Python — integers, strings, lists, dictionaries — is already an object, an instance of a class. Now you will define your own classes and create your own types with custom data and behavior. This module covers the class definition syntax, the `__init__` constructor, `self`, instance variables, instance methods, the `__str__` dunder method, class variables, and the `isinstance()` / `type()` built-ins. These concepts are among the most heavily tested on the PCAP exam and form the foundation for Module 15 (inheritance and polymorphism).

---

## 1. High-Yield Glossary

### Class

A user-defined blueprint for creating objects. A class defines the attributes (data) and methods (behaviors) that every instance of that class will have.

```python
class Dog:
    pass    # minimal valid class definition
```

Class names use **PascalCase** by convention — `Dog`, `BankAccount`, `StudentGrade`. This distinguishes them from variables and functions (which use snake_case).

### Object / Instance

An individual object built from a class blueprint. Creating an object is called **instantiation**. Each instance has its own copy of instance variables.

```python
d1 = Dog()    # d1 is an instance of Dog
d2 = Dog()    # d2 is a separate instance of Dog
```

`d1` and `d2` are different objects in memory even though they were created from the same class.

### `__init__` — The Constructor

A special method that Python calls automatically when you create a new instance. Its purpose is to initialize the instance's attributes.

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
```

```python
d = Dog('Rex', 'German Shepherd', 4)
# Python automatically calls: Dog.__init__(d, 'Rex', 'German Shepherd', 4)
```

**`__init__` must not contain a `return` statement with a value.** It implicitly returns `None`. Returning anything else raises `TypeError: __init__() should return None`.

### self

The first parameter of every instance method. It is a reference to the specific instance on which the method was called. Python passes it automatically — you never supply `self` when calling a method.

```python
class Dog:
    def __init__(self, name):
        self.name = name       # self refers to the new instance

    def bark(self):
        return f'{self.name} says: Woof!'

d = Dog('Rex')
d.bark()    # Python translates this to: Dog.bark(d)
            # self = d inside the method
```

`self` is a convention, not a keyword. You could name it anything, but you must always name it `self` — any other name will confuse every Python programmer reading your code and will fail the PCAP exam.

### Instance Variable

A variable that belongs to a specific instance. Defined by assigning to `self.variable_name` inside a method. Each instance has its own independent copy.

```python
d1 = Dog('Rex', 'German Shepherd', 4)
d2 = Dog('Luna', 'Labrador', 2)

d1.name = 'Max'    # changes only d1's name
print(d1.name)     # Max
print(d2.name)     # Luna — unchanged
```

### Class Variable

A variable defined directly on the class body (not inside any method). Shared by all instances. Accessed as `ClassName.variable` or `instance.variable`.

```python
class Dog:
    species = 'Canis lupus familiaris'    # class variable

    def __init__(self, name):
        self.name = name                  # instance variable
```

```python
d1 = Dog('Rex')
d2 = Dog('Luna')
print(d1.species)    # Canis lupus familiaris
print(d2.species)    # Canis lupus familiaris
print(Dog.species)   # Canis lupus familiaris
```

**Critical distinction — instance assignment shadows class variable:**

```python
d1.species = 'Override'     # creates a NEW instance variable on d1
print(d1.species)           # Override — reads d1's own instance variable
print(d2.species)           # Canis lupus familiaris — d2 still reads class variable
print(Dog.species)          # Canis lupus familiaris — class variable unchanged
```

Assigning through an instance does not modify the class variable. It creates a new instance variable that shadows the class variable for that instance only.

### Instance Method

A function defined inside a class that operates on an instance. Always takes `self` as the first parameter.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):                    # instance method
        return f'{self.name}: Woof!'

    def birthday(self):                # method that modifies state
        self.age += 1
        return self.age

    def describe(self):
        return f'{self.name}, age {self.age}'
```

### `__str__` — String Representation

A dunder method (double-underscore on each side) called by `print()` and `str()` to get a human-readable string representation of an object.

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return f'Dog({self.name!r}, {self.breed!r}, age={self.age})'
```

```python
d = Dog('Rex', 'German Shepherd', 4)
print(d)         # Dog('Rex', 'German Shepherd', age=4)
print(str(d))    # Dog('Rex', 'German Shepherd', age=4)
```

Without `__str__`, `print(d)` outputs `<__main__.Dog object at 0x7f4a2b3c1d50>` — the memory address, which is not useful to end users.

`__str__` must return a **string**. If it returns anything else, Python raises `TypeError`.

### `__repr__` — Developer Representation

A dunder method called by `repr()` and used in the REPL when you evaluate an expression. Intended to be an unambiguous developer-facing representation — ideally something that could be passed to `eval()` to recreate the object.

```python
def __repr__(self):
    return f'Dog(name={self.name!r}, breed={self.breed!r}, age={self.age!r})'
```

**`__str__` vs `__repr__` fallback rule:**

| Method defined | `print(obj)` uses | REPL uses |
|---|---|---|
| Both `__str__` and `__repr__` | `__str__` | `__repr__` |
| Only `__repr__` | `__repr__` | `__repr__` |
| Only `__str__` | `__str__` | default memory address |
| Neither | default memory address | default memory address |

### Dunder Methods (Magic Methods)

Methods whose names start and end with double underscores: `__init__`, `__str__`, `__repr__`, `__len__`, `__eq__`, etc. Python calls these automatically in specific situations. You define them to customize how your objects behave with built-in functions and operators.

| Dunder | Called by |
|---|---|
| `__init__(self, ...)` | `ClassName(args)` — construction |
| `__str__(self)` | `print(obj)`, `str(obj)` |
| `__repr__(self)` | `repr(obj)`, REPL display |
| `__len__(self)` | `len(obj)` |
| `__eq__(self, other)` | `obj1 == obj2` |
| `__lt__(self, other)` | `obj1 < obj2` |
| `__add__(self, other)` | `obj1 + obj2` |

### Encapsulation

The practice of bundling data (attributes) and the methods that operate on that data together in a class, and controlling access to the internal state. Python uses naming conventions rather than strict access modifiers:

| Convention | Name format | Meaning |
|---|---|---|
| Public | `name` | Anyone can access |
| Protected | `_name` | "Internal use" — accessible but don't touch from outside |
| Private (name-mangled) | `__name` | Name-mangled to `_ClassName__name` — harder to access accidentally |

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance       # protected — internal use
        self.__pin = '1234'           # name-mangled — private

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance
```

```python
acc = BankAccount(100)
acc._balance        # accessible but discouraged
acc.__pin           # AttributeError — name-mangled to _BankAccount__pin
acc._BankAccount__pin    # accessible if you know the mangled name
```

### isinstance() and type()

```python
d = Dog('Rex', 'German Shepherd', 4)

type(d)                    # <class '__main__.Dog'>
type(d) == Dog             # True — strict type check
isinstance(d, Dog)         # True — preferred check
isinstance(d, object)      # True — all Python objects are instances of object
isinstance(42, (int, float))   # True — checks against tuple of types
```

**Prefer `isinstance()` over `type() ==` in production code.** `isinstance()` returns `True` for subclasses, which is almost always the desired behavior. `type() ==` is a strict identity check that fails for subclasses.

### `hasattr()`, `getattr()`, `setattr()`

Built-in functions for dynamic attribute access.

```python
d = Dog('Rex', 'German Shepherd', 4)

hasattr(d, 'name')           # True
hasattr(d, 'weight')         # False — attribute does not exist

getattr(d, 'name')           # 'Rex'
getattr(d, 'weight', 0)      # 0 — default if attribute missing

setattr(d, 'weight', 32.5)   # creates d.weight = 32.5
print(d.weight)              # 32.5
```

---

## 2. Complete Class Example

```python
class BankAccount:
    '''A simple bank account with deposit, withdraw, and balance inquiry.'''

    bank_name = 'Python National Bank'    # class variable

    def __init__(self, owner, balance=0.0):
        '''Create a new account for owner with optional initial balance.'''
        self.owner = owner
        self._balance = float(balance)    # protected — use methods to access
        self._transactions = []

    def deposit(self, amount):
        '''Add amount to balance. Raises ValueError for non-positive amount.'''
        if amount <= 0:
            raise ValueError(f'Deposit amount must be positive: {amount}')
        self._balance += amount
        self._transactions.append(f'+{amount:.2f}')
        return self._balance

    def withdraw(self, amount):
        '''Subtract amount from balance. Raises ValueError if insufficient.'''
        if amount <= 0:
            raise ValueError(f'Withdrawal amount must be positive: {amount}')
        if amount > self._balance:
            raise ValueError(f'Insufficient funds: balance is {self._balance:.2f}')
        self._balance -= amount
        self._transactions.append(f'-{amount:.2f}')
        return self._balance

    def get_balance(self):
        return self._balance

    def transaction_count(self):
        return len(self._transactions)

    def __str__(self):
        return f'BankAccount({self.owner!r}, balance={self._balance:.2f})'

    def __repr__(self):
        return f'BankAccount(owner={self.owner!r}, balance={self._balance!r})'
```

---

## 3. Common Error Patterns to Memorize

**Pattern 1 — Forgetting `self` as first parameter raises TypeError:**

```python
class Dog:
    def bark():     # WRONG — missing self
        return 'Woof'

d = Dog()
d.bark()    # TypeError: bark() takes 0 positional arguments but 1 was given
```

When you call `d.bark()`, Python passes `d` as the first argument. If the method has no parameters, there is nowhere for `d` to go — hence the error.

**Pattern 2 — Returning a value from `__init__`:**

```python
class Dog:
    def __init__(self, name):
        self.name = name
        return self    # TypeError: __init__() should return None (not 'Dog')
```

`__init__` must not return anything other than `None`.

**Pattern 3 — Accessing instance variable as class variable:**

```python
class Dog:
    def __init__(self, name):
        self.name = name

Dog.name    # AttributeError — name is an instance variable, not a class variable
```

`Dog.name` does not exist. You must access instance variables through an instance: `d.name`.

**Pattern 4 — Class variable mutation through instance:**

```python
class Counter:
    count = 0

c1 = Counter()
c2 = Counter()
c1.count = 99     # creates instance variable on c1 — does NOT change Counter.count
print(Counter.count)    # 0 — class variable unchanged
print(c2.count)         # 0 — c2 still reads class variable
```

**Pattern 5 — `__str__` returning a non-string:**

```python
class Dog:
    def __str__(self):
        return self.age    # TypeError: __str__ returned non-string (type int)
```

`__str__` must return a string. Use `str(self.age)` or an f-string.

---

## 4. Certification Exam Tips

**Tip 1 — `self` must be the first parameter of every instance method.**
The PCAP exam frequently shows a class definition where `self` is missing or in the wrong position. Missing `self` raises `TypeError` when the method is called — Python passes the instance automatically, but there is no parameter to receive it.

**Tip 2 — `__init__` does not return a value.**
`__init__` initializes the object. It must not have a `return` statement with a value. Returning `None` explicitly is allowed but unnecessary.

**Tip 3 — Instance variable assignment in `__init__` uses `self.name = value`.**
Without `self.`, you are creating a local variable inside `__init__` that disappears when `__init__` returns. The attribute will not exist on the object.

**Tip 4 — Assigning to `instance.class_var` does not modify the class variable.**
It creates a new instance variable that shadows the class variable for that instance only. The class variable and all other instances are unchanged.

**Tip 5 — `__str__` is called by `print()`. It must return a string.**
If `__str__` is missing, Python falls back to `__repr__`. If neither is defined, you get the unhelpful memory address output.

**Tip 6 — `isinstance(obj, cls)` is True for subclasses.**
`isinstance` handles inheritance correctly. `type(obj) == cls` does not — it fails for subclass instances.

**Tip 7 — `type(obj)` returns the class object, not a string.**
`type(d)` returns `<class '__main__.Dog'>`, not the string `'Dog'`. To get the name as a string, use `type(d).__name__`.

---

## 5. Beyond the Exam — Real-World Context

**Properties — controlled attribute access.**
The `@property` decorator lets you define getter, setter, and deleter methods that look like attribute access. This is the Pythonic way to validate data when setting an attribute:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age    # calls the setter below

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('Age cannot be negative')
        self._age = value
```

```python
d = Dog('Rex', 4)
d.age = -1    # ValueError: Age cannot be negative
```

**Dataclasses — less boilerplate.**
Python 3.7+ includes `@dataclass` which auto-generates `__init__`, `__repr__`, and `__eq__` from class-level type annotations:

```python
from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    breed: str
    age: int
```

This is equivalent to writing `__init__`, `__repr__`, and `__eq__` by hand.

**Everything is an object.**
In Python, functions, classes, modules, and even `None` are all objects — instances of `function`, `type`, `module`, and `NoneType` respectively. `type(print)` is `<class 'builtin_function_or_method'>`. This is why functions can be passed as arguments and stored in variables.

---

## 6. Required Readings and Videos

**Required Reading — Chapter 14:**
Read Chapter 14 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). This chapter introduces object-oriented programming with real-world examples.

**Required Reading — Official Python Docs:**
Read [Classes](https://docs.python.org/3/tutorial/classes.html) in the official Python 3 tutorial — the authoritative source for class syntax and the data model tested on the PCAP exam.

**Supplemental Video:**
Watch Episode 14 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance covers OOP concepts with worked examples.

---

## 7. Supplemental Resources

**1. Official Python 3 Docs — Classes**
[https://docs.python.org/3/tutorial/classes.html](https://docs.python.org/3/tutorial/classes.html)
The authoritative tutorial chapter on Python classes — covers class definitions, `__init__`, `self`, instance variables, class variables, method objects, inheritance, and the data model. This is the primary reference for PCAP exam questions on OOP basics.

**2. Official Python 3 Docs — Data Model**
[https://docs.python.org/3/reference/datamodel.html](https://docs.python.org/3/reference/datamodel.html)
The complete reference for Python's special methods (`__init__`, `__str__`, `__repr__`, `__eq__`, `__lt__`, etc.) and how they interact with Python's operators and built-in functions. Essential for understanding how dunder methods work.

**3. Python for Everybody — Chapter 14: Object-Oriented Programming**
[https://www.py4e.com/html3/14-objects](https://www.py4e.com/html3/14-objects)
Free textbook chapter introducing OOP concepts with real-world analogies. Covers class definitions, `__init__`, instance methods, and the `self` parameter with step-by-step examples appropriate for beginners.

**4. Real Python — Object-Oriented Programming in Python 3**
[https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/)
A comprehensive free article covering class definitions, `__init__`, instance vs. class variables, `__str__` and `__repr__`, inheritance, and encapsulation. The section on class vs. instance variables and the shadowing behavior is directly relevant to PCAP exam questions.

**5. Real Python — Python's property(): Add Managed Attributes to Your Classes**
[https://realpython.com/python-property/](https://realpython.com/python-property/)
A thorough free article on the `@property` decorator — Python's idiomatic way to add validation and computed attributes to classes. Understanding properties is the natural next step after mastering `__init__` and instance variables.

---

## 8. Study Checklist

- [ ] Watch the Module 14 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially the instance variable vs class variable distinction.
- [ ] Draw the class/instance diagram: class = blueprint, instance = individual object with its own data.
- [ ] Write a `Dog` class from scratch with `__init__`, three instance methods, and `__str__`. Test it in the REPL.
- [ ] Deliberately make the TypeError error: define a method without `self` and call it — read the error message.
- [ ] Demonstrate the class variable shadowing behavior: modify through an instance, confirm the class variable is unchanged.
- [ ] Practice `isinstance()` and `type()` on built-in types and your own class.
- [ ] Review all 7 Certification Exam Tips in Section 4.
- [ ] Proceed to the Module 14 Lab Activity.
