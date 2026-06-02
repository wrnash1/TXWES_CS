# Lab Activity: Module 14 — Object-Oriented Programming: Basics

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 75–90 minutes

---

## Overview

In this lab you will define classes with `__init__` and instance methods, trigger the `self` omission TypeError and read its message, demonstrate the class variable vs instance variable distinction and the shadowing behavior, add `__str__` and observe its effect on `print()`, practice `isinstance()` and `type()`, and build a complete `BankAccount` class that demonstrates encapsulation with a protected attribute.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module14
cd module14
```

---

## Part 1 — Defining Classes and Creating Instances

```bash
python3
```

### Step 1.1 — Minimal class

```python
>>> class Dog:
...     pass
...
>>> d1 = Dog()
>>> d2 = Dog()
>>> type(d1)
<class '__main__.Dog'>
>>> d1 is d2
False
>>> d1 == d2
False
```

`d1` and `d2` are separate objects. `is` checks identity (same object in memory). `==` without a custom `__eq__` also defaults to identity.

### Step 1.2 — Adding `__init__`

```python
>>> class Dog:
...     def __init__(self, name, breed, age):
...         self.name = name
...         self.breed = breed
...         self.age = age
...
>>> d1 = Dog('Rex', 'German Shepherd', 4)
>>> d2 = Dog('Luna', 'Labrador', 2)
>>> d1.name
'Rex'
>>> d2.name
'Luna'
>>> d1.age
4
```

Each instance has its own independent attribute values.

### Step 1.3 — Modify one instance, other is unchanged

```python
>>> d1.name = 'Max'
>>> d1.name
'Max'
>>> d2.name
'Luna'
```

### Step 1.4 — Default string representation (before `__str__`)

```python
>>> print(d1)
<__main__.Dog object at 0x7f...>
```

The memory address output is not useful. We will fix this shortly.

### Step 1.5 — The self TypeError

```python
>>> class BadDog:
...     def bark():    # missing self
...         return 'Woof'
...
>>> b = BadDog()
>>> b.bark()
```

```text
TypeError: BadDog.bark() takes 0 positional arguments but 1 was given
```

Python automatically passes the instance (`b`) as the first argument. Since `bark()` has no parameters, there is nowhere for it to go. Always include `self` as the first parameter.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the instance creation from Step 1.2, the independent modification from Step 1.3, and the TypeError from Step 1.5. Save as `lab14_screenshot_01_init_self.png`.

---

## Part 2 — Instance Methods and `__str__`

```bash
python3
```

### Step 2.1 — Class with instance methods

```python
>>> class Dog:
...     def __init__(self, name, breed, age):
...         self.name = name
...         self.breed = breed
...         self.age = age
...     def bark(self):
...         return f'{self.name} says: Woof!'
...     def birthday(self):
...         self.age += 1
...         return f'{self.name} is now {self.age} years old.'
...     def describe(self):
...         return f'{self.name} is a {self.age}-year-old {self.breed}.'
...
>>> d = Dog('Rex', 'German Shepherd', 4)
>>> d.bark()
'Rex says: Woof!'
>>> d.describe()
'Rex is a 4-year-old German Shepherd.'
>>> d.birthday()
'Rex is now 5 years old.'
>>> d.age
5
```

`birthday()` modifies `self.age` in place. The change persists on the object.

### Step 2.2 — Adding `__str__`

```python
>>> class Dog:
...     def __init__(self, name, breed, age):
...         self.name = name
...         self.breed = breed
...         self.age = age
...     def __str__(self):
...         return f'Dog({self.name!r}, {self.breed!r}, age={self.age})'
...     def bark(self):
...         return f'{self.name} says: Woof!'
...
>>> d = Dog('Rex', 'German Shepherd', 4)
>>> print(d)
Dog('Rex', 'German Shepherd', age=4)
>>> str(d)
"Dog('Rex', 'German Shepherd', age=4)"
```

`print()` calls `__str__` automatically.

### Step 2.3 — `__str__` must return a string

```python
>>> class BadStr:
...     def __init__(self, value):
...         self.value = value
...     def __str__(self):
...         return self.value    # value is an int, not a string
...
>>> b = BadStr(42)
>>> print(b)
```

```text
TypeError: __str__ returned non-string (type int)
```

Always return a string from `__str__`.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing the instance methods from Step 2.1 (bark, describe, birthday), the `__str__` output from Step 2.2, and the TypeError from Step 2.3. Save as `lab14_screenshot_02_methods_str.png`.

---

## Part 3 — Class Variables vs Instance Variables

```bash
python3
```

### Step 3.1 — Define a class variable

```python
>>> class Dog:
...     species = 'Canis lupus familiaris'
...     def __init__(self, name):
...         self.name = name
...
>>> d1 = Dog('Rex')
>>> d2 = Dog('Luna')
>>> d1.species
'Canis lupus familiaris'
>>> d2.species
'Canis lupus familiaris'
>>> Dog.species
'Canis lupus familiaris'
```

All three access the same class variable.

### Step 3.2 — Modify the class variable through the class

```python
>>> Dog.species = 'Changed via class'
>>> d1.species
'Changed via class'
>>> d2.species
'Changed via class'
```

Modifying through the class affects all instances.

### Step 3.3 — The shadowing trap

```python
>>> d1.species = 'Instance override'
>>> d1.species
'Instance override'
>>> d2.species
'Changed via class'
>>> Dog.species
'Changed via class'
```

Assigning `d1.species = ...` creates a new **instance variable** on `d1`. It does not modify the class variable. `d2` and `Dog` still use the class variable.

### Step 3.4 — Instance variable with no class variable

```python
>>> Dog.name
```

```text
AttributeError: type object 'Dog' has no attribute 'name'
```

`name` is an instance variable — it only exists on instances, not on the class itself.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 3 REQUIRED:** Screenshot showing the class variable access (Step 3.1), class-level modification affecting all instances (Step 3.2), and the shadowing trap where `d1.species` and `d2.species` diverge (Step 3.3). Save as `lab14_screenshot_03_class_var.png`.

---

## Part 4 — isinstance(), type(), hasattr(), getattr()

```bash
python3
```

### Step 4.1 — isinstance() vs type()

```python
>>> class Animal:
...     pass
...
>>> class Dog(Animal):
...     pass
...
>>> d = Dog()
>>> isinstance(d, Dog)
True
>>> isinstance(d, Animal)
True
>>> isinstance(d, object)
True
>>> type(d) == Dog
True
>>> type(d) == Animal
False
```

`isinstance()` returns `True` for the object's class and all parent classes. `type() ==` is a strict check — it only returns `True` for the exact class, not parent classes.

### Step 4.2 — isinstance() with a tuple of types

```python
>>> isinstance(42, (int, float))
True
>>> isinstance('hello', (int, float))
False
>>> isinstance(3.14, (int, float))
True
```

You can pass a tuple of types to check against any of them.

### Step 4.3 — hasattr() and getattr()

```python
>>> class Dog:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...
>>> d = Dog('Rex', 4)
>>> hasattr(d, 'name')
True
>>> hasattr(d, 'weight')
False
>>> getattr(d, 'name')
'Rex'
>>> getattr(d, 'weight', 0)
0
>>> getattr(d, 'weight')
```

```text
AttributeError: 'Dog' object has no attribute 'weight'
```

`getattr(obj, name, default)` with a default is safe. Without a default, it raises `AttributeError` for missing attributes.

### Step 4.4 — setattr()

```python
>>> setattr(d, 'weight', 32.5)
>>> d.weight
32.5
>>> hasattr(d, 'weight')
True
```

Exit the REPL:

```python
>>> exit()
```

---

## Part 5 — bank_account.py (Complete Class with Encapsulation)

```bash
nano bank_account.py
```

```python
# bank_account.py
# Demonstrates a complete class with encapsulation
# Module 14 Lab — CIS-1310


class BankAccount:
    '''A simple bank account with deposit, withdraw, and balance inquiry.'''

    bank_name = 'Python National Bank'    # class variable — shared by all

    def __init__(self, owner, balance=0.0):
        '''Create account for owner with optional starting balance.'''
        self.owner = owner
        self._balance = float(balance)    # protected — use methods to access
        self._transactions = []

    def deposit(self, amount):
        '''Add amount to balance. Raises ValueError for non-positive amount.'''
        if amount <= 0:
            raise ValueError(f'Deposit must be positive, got {amount}')
        self._balance += amount
        self._transactions.append(f'+{amount:.2f}')
        return self._balance

    def withdraw(self, amount):
        '''Subtract amount from balance. Raises ValueError if insufficient.'''
        if amount <= 0:
            raise ValueError(f'Withdrawal must be positive, got {amount}')
        if amount > self._balance:
            raise ValueError(
                f'Insufficient funds: balance={self._balance:.2f}, '
                f'requested={amount:.2f}'
            )
        self._balance -= amount
        self._transactions.append(f'-{amount:.2f}')
        return self._balance

    def get_balance(self):
        '''Return current balance.'''
        return self._balance

    def transaction_count(self):
        '''Return the number of transactions made.'''
        return len(self._transactions)

    def statement(self):
        '''Return a string showing all transactions.'''
        if not self._transactions:
            return f'  {self.owner}: no transactions yet.'
        lines = [f'  Statement for {self.owner}:']
        for t in self._transactions:
            lines.append(f'    {t}')
        lines.append(f'  Current balance: ${self._balance:.2f}')
        return '\n'.join(lines)

    def __str__(self):
        return (f'BankAccount(owner={self.owner!r}, '
                f'balance=${self._balance:.2f})')

    def __repr__(self):
        return (f'BankAccount(owner={self.owner!r}, '
                f'balance={self._balance!r})')


if __name__ == '__main__':
    print(f'=== {BankAccount.bank_name} ===')
    print()

    alice = BankAccount('Alice', 1000.0)
    bob = BankAccount('Bob', 500.0)

    print(f'Created: {alice}')
    print(f'Created: {bob}')
    print()

    alice.deposit(250.0)
    alice.deposit(100.0)
    alice.withdraw(75.0)

    bob.deposit(200.0)
    bob.withdraw(600.0)

    print(alice.statement())
    print()
    print(bob.statement())
    print()

    print(f'Alice transactions: {alice.transaction_count()}')
    print(f'Bob transactions:   {bob.transaction_count()}')
    print()

    # Demonstrate class variable
    print(f'All accounts at: {BankAccount.bank_name}')
    print(f'alice.bank_name:  {alice.bank_name}')
    print(f'bob.bank_name:    {bob.bank_name}')
    print()

    # Demonstrate isinstance
    print(f'isinstance(alice, BankAccount): {isinstance(alice, BankAccount)}')
    print(f'isinstance(alice, object):      {isinstance(alice, object)}')
    print(f'type(alice).__name__:           {type(alice).__name__}')
    print()

    # Demonstrate exception handling
    print('=== Exception handling ===')
    try:
        alice.withdraw(9999.0)
    except ValueError as e:
        print(f'  Caught: {e}')

    try:
        bob.deposit(-50)
    except ValueError as e:
        print(f'  Caught: {e}')
```

Save and run:

```bash
python3 bank_account.py
```

Expected output:

```text
=== Python National Bank ===

Created: BankAccount(owner='Alice', balance=$1000.00)
Created: BankAccount(owner='Bob', balance=$500.00)

  Statement for Alice:
    +250.00
    +100.00
    -75.00
  Current balance: $1275.00

  Statement for Bob:
    +200.00
    -600.00
  Current balance: $100.00

Alice transactions: 3
Bob transactions:   2

All accounts at: Python National Bank
alice.bank_name:  Python National Bank
bob.bank_name:    Python National Bank

isinstance(alice, BankAccount): True
isinstance(alice, object):      True
type(alice).__name__:           BankAccount

=== Exception handling ===
  Caught: Insufficient funds: balance=1275.00, requested=9999.00
  Caught: Deposit must be positive, got -50
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `bank_account.py` running and showing the complete output. Save as `lab14_screenshot_04_bank_account.png`.

---

## Part 6 — student.py (Design-Your-Own Class)

```bash
nano student.py
```

```python
# student.py
# A Student class with grade tracking
# Module 14 Lab — CIS-1310


class Student:
    '''Represents a student with a name, ID, and collection of grades.'''

    school_name = 'Texas Wesleyan University'

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self._grades = []    # protected — use methods to manage

    def add_grade(self, grade):
        '''Add a numeric grade (0–100). Raises ValueError for out-of-range.'''
        if not (0 <= grade <= 100):
            raise ValueError(f'Grade must be 0–100, got {grade}')
        self._grades.append(grade)

    def average(self):
        '''Return the average grade, or None if no grades recorded.'''
        if not self._grades:
            return None
        return sum(self._grades) / len(self._grades)

    def letter_grade(self):
        '''Return letter grade based on average.'''
        avg = self.average()
        if avg is None:
            return 'N/A'
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def grade_count(self):
        '''Return the number of grades recorded.'''
        return len(self._grades)

    def __str__(self):
        avg = self.average()
        avg_str = f'{avg:.1f}' if avg is not None else 'no grades'
        return (f'Student({self.name!r}, id={self.student_id}, '
                f'avg={avg_str}, grade={self.letter_grade()})')

    def __repr__(self):
        return f'Student(name={self.name!r}, student_id={self.student_id!r})'


if __name__ == '__main__':
    s1 = Student('Alice Johnson', 'S001')
    s2 = Student('Bob Smith', 'S002')

    for grade in [88, 92, 79, 95, 84]:
        s1.add_grade(grade)

    for grade in [72, 68, 75, 70]:
        s2.add_grade(grade)

    print(s1)
    print(s2)
    print()

    print(f'{s1.name} grade count: {s1.grade_count()}')
    print(f'{s2.name} average: {s2.average():.2f}')
    print(f'{s2.name} letter grade: {s2.letter_grade()}')
    print()

    print(f'School: {Student.school_name}')
    print()

    # Error handling
    try:
        s1.add_grade(105)
    except ValueError as e:
        print(f'Caught: {e}')

    # Student with no grades
    s3 = Student('Charlie', 'S003')
    print(s3)
```

Save and run:

```bash
python3 student.py
```

Expected output:

```text
Student('Alice Johnson', id=S001, avg=87.6, grade=B)
Student('Bob Smith', id=S002, avg=71.2, grade=C)

Alice Johnson grade count: 5
Bob Smith average: 71.25
Bob Smith letter grade: C

School: Texas Wesleyan University

Caught: Grade must be 0–100, got 105
Student('Charlie', id=S003, avg=no grades, grade=N/A)
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `student.py` running and showing the complete output. Save as `lab14_screenshot_05_student.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 14 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab14_screenshot_01_init_self.png` | Instance creation, independent attributes, self TypeError |
| 2 | `lab14_screenshot_02_methods_str.png` | Instance methods, `__str__` output, non-string TypeError |
| 3 | `lab14_screenshot_03_class_var.png` | Class variable shared access, class-level modification, shadowing trap |
| 4 | `lab14_screenshot_04_bank_account.png` | bank_account.py complete output |
| 5 | `lab14_screenshot_05_student.png` | student.py complete output |

---

## Troubleshooting Guide

**`TypeError: method() takes 0 positional arguments but 1 was given`**
You forgot `self` as the first parameter. Every instance method must have `self` as its first parameter. Python automatically passes the instance when you call `obj.method()`.

**`AttributeError: 'ClassName' object has no attribute 'xyz'`**
The attribute was not created with `self.xyz = value` in `__init__` (or another method). Check that your `__init__` assigns the attribute with `self.` prefix, not just as a local variable.

**`__str__` output still shows memory address.**
Python only calls `__str__` if it is defined and returns a string. Check the method name is exactly `__str__` (two underscores on each side) and that it returns a string, not an integer or other type.

**Class variable changed for all instances unexpectedly.**
You modified the class variable through `ClassName.variable = ...`. This changes the shared class variable. If you want to change only one instance, assign to `instance.variable` — but be aware this creates an instance variable that shadows the class variable.

**`__init__` doesn't seem to be running.**
Verify the class is being instantiated with parentheses: `obj = MyClass()`. Just writing `obj = MyClass` without parentheses assigns the class object itself to `obj` — it does not create an instance and does not call `__init__`.
