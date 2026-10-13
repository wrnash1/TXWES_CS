# Reading Guide: Module 15 — Advanced OOP: Inheritance and Polymorphism

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

Welcome to **Module 15 — Advanced OOP: Inheritance and Polymorphism**. Module 14 gave you classes and instances. This module gives you the two most powerful OOP mechanisms: **inheritance** (child classes reuse and extend parent classes) and **polymorphism** (different classes respond to the same method call in their own way). These concepts explain how Python's own built-in types work — `list`, `dict`, `str`, and `int` are all classes in a hierarchy — and they are essential PCAP exam content. After this module you will understand why professional Python code is organized into class hierarchies and how `super()`, method overriding, and the Method Resolution Order fit together.

---

## 1. High-Yield Glossary

### Inheritance

A mechanism where a child class automatically acquires all the attributes and methods of its parent class, and can extend or override them.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} makes a sound.'

class Dog(Animal):                 # Dog inherits from Animal
    def speak(self):               # overrides Animal.speak
        return f'{self.name} says: Woof!'
```

The child class `Dog` inherits `__init__` and `name` from `Animal` automatically. It only needs to define what is different.

### Parent Class (Superclass / Base Class)

The class being inherited from. Named in parentheses after the child class name. All of its public and protected attributes and methods are available in the child class.

### Child Class (Subclass / Derived Class)

The class that inherits. Defined as `class Child(Parent):`. Can:

1. **Inherit** — use a parent method unchanged.
2. **Override** — redefine a parent method with a new implementation.
3. **Extend** — call the parent's method via `super()` and add to it.

### Inheritance Syntax

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f'{self.year} {self.make} {self.model}'

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)    # initialize parent attributes
        self.doors = doors                     # add child-specific attribute

    def describe(self):
        return f'{super().describe()} ({self.doors}-door)'

class ElectricCar(Car):
    def __init__(self, make, model, year, doors, range_km):
        super().__init__(make, model, year, doors)
        self.range_km = range_km

    def describe(self):
        return f'{super().describe()}, range={self.range_km}km'
```

```python
v = Vehicle('Toyota', 'Corolla', 2020)
c = Car('Honda', 'Civic', 2022, 4)
e = ElectricCar('Tesla', 'Model 3', 2023, 4, 560)

print(v.describe())    # 2020 Toyota Corolla
print(c.describe())    # 2022 Honda Civic (4-door)
print(e.describe())    # 2023 Tesla Model 3 (4-door), range=560km
```

### super()

A built-in function that returns a proxy object representing the parent class (the next class in the MRO). Used to call parent class methods from within a child class.

**Most common usage — calling the parent's `__init__`:**

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # runs Animal.__init__(self, name)
        self.breed = breed
```

**Calling super() in an overridden method:**

```python
class Dog(Animal):
    def speak(self):
        parent_result = super().speak()    # Animal.speak(self)
        return f'{parent_result} (and wags tail)'
```

**Critical rule:** Never hardcode the parent class name (`Animal.__init__(self, name)`) when `super()` is available. `super()` respects the MRO and works correctly in multiple inheritance scenarios.

### Method Overriding

When a child class defines a method with the same name as the parent class. Python calls the child's version, not the parent's.

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):            # overrides Shape.area
        import math
        return math.pi * self.radius ** 2
```

```python
s = Shape()
c = Circle(5)
print(s.area())    # 0 — Shape's version
print(c.area())    # 78.539... — Circle's version
```

The child's method completely replaces the parent's unless you explicitly call `super()`.

### Polymorphism

The ability of different objects to respond to the same method call with their own specific behavior. Objects of different types are treated uniformly through a shared interface.

```python
animals = [Dog('Rex'), Cat('Whiskers'), Duck('Donald')]

for a in animals:
    print(a.speak())    # each calls its own speak()
```

```text
Rex says: Woof!
Whiskers says: Meow!
Donald says: Quack!
```

The loop does not check the type of each object. It simply calls `.speak()` and lets Python route the call to the correct implementation.

### Duck Typing

Python's approach to polymorphism: if an object has the method being called, it works — regardless of its type. "If it walks like a duck and quacks like a duck, it is a duck."

```python
def make_sound(thing):
    print(thing.speak())

make_sound(Dog('Rex'))       # works — Dog has speak()
make_sound(Cat('Whiskers'))  # works — Cat has speak()
make_sound(42)               # AttributeError — int has no speak()
```

You do not need a formal inheritance relationship for polymorphism in Python. Any object with the required method works.

### Method Resolution Order (MRO)

The ordered list of classes Python searches when looking up a method or attribute. For single inheritance, the order is always: child → parent → grandparent → ... → `object`.

```python
print(Dog.__mro__)
# (<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)

print(Dog.mro())
# [<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>]
```

Python checks each class in this order and uses the first definition it finds. This explains why an overriding method in the child is found before the parent's version.

### Single vs Multiple Inheritance

**Single inheritance:** A class has one parent.

```python
class Dog(Animal):     # single parent
    pass
```

**Multiple inheritance:** A class has multiple parents.

```python
class FlyingFish(Fish, Bird):    # two parents
    pass
```

The PCAP exam primarily tests single inheritance. Multiple inheritance is introduced but not heavily tested. The MRO becomes more complex with multiple inheritance — Python uses the C3 linearization algorithm to determine a consistent order.

### `isinstance()` with Inheritance

`isinstance(obj, cls)` returns `True` if `obj` is an instance of `cls` **or any subclass of `cls`**.

```python
d = Dog('Rex')

isinstance(d, Dog)      # True — d is directly a Dog
isinstance(d, Animal)   # True — Dog is a subclass of Animal
isinstance(d, object)   # True — all Python objects inherit from object
isinstance(d, Cat)      # False — Dog is not a Cat
```

This is why `isinstance()` is preferred over `type(obj) == cls`. A `Dog` object should be recognized as an `Animal` — and `isinstance` handles this correctly while `type(d) == Animal` does not.

### Abstract Behavior — The Interface Contract

A parent class often defines a method that child classes are expected to override. The parent's version may be empty, raise `NotImplementedError`, or provide a default:

```python
class Shape:
    def area(self):
        raise NotImplementedError('Subclasses must implement area()')

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
```

This establishes a contract: any `Shape` subclass must implement `area()`. Python's formal mechanism for this is Abstract Base Classes (`abc` module), but the `NotImplementedError` pattern achieves the same intent.

---

## 2. Inheritance vs Composition — When to Use Each

| Approach | Relationship | Use when |
|---|---|---|
| Inheritance | "is-a" | A `Dog` IS-A `Animal` — the child is a more specific version of the parent |
| Composition | "has-a" | A `Car` HAS-A `Engine` — the object contains another object as an attribute |

```python
# Inheritance — correct: a Dog IS an Animal
class Dog(Animal):
    pass

# Composition — correct: a Car HAS an Engine
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine    # Car HAS-A Engine
```

Overusing inheritance for "has-a" relationships is a common design mistake. If you cannot naturally say "a Child is a Parent," prefer composition.

---

## 3. Common Error Patterns to Memorize

**Pattern 1 — Forgetting `super().__init__()` causes AttributeError:**

```python
class Dog(Animal):
    def __init__(self, name, breed):
        # super().__init__(name) MISSING
        self.breed = breed

d = Dog('Rex', 'Lab')
print(d.name)    # AttributeError: 'Dog' object has no attribute 'name'
```

The parent's `__init__` never ran, so `self.name` was never created.

**Pattern 2 — Calling parent method with hardcoded class name:**

```python
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)    # works but brittle — use super() instead
        self.breed = breed
```

Hardcoding `Animal.__init__(self, name)` breaks if you later rename the parent class or use multiple inheritance.

**Pattern 3 — Method override accidentally calls wrong class:**

```python
class Dog(Animal):
    def speak(self):
        Animal.speak(self)    # calls parent's speak, not Dog's — use super()
        return 'Woof!'
```

If you want to call the parent and add behavior, use `super().speak()`.

**Pattern 4 — `isinstance` vs `type ==` with subclasses:**

```python
d = Dog('Rex')
print(type(d) == Animal)     # False — even though Dog inherits from Animal
print(isinstance(d, Animal)) # True — correct check for is-a relationship
```

**Pattern 5 — Child class without `__str__` falls back to parent:**

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    # no __str__ defined

d = Dog('Rex', 'Lab')
print(d)    # Uses Animal's __str__ — may not show breed
```

If you need the child's output to include child-specific attributes, define `__str__` in the child.

---

## 4. Certification Exam Tips

**Tip 1 — Inheritance syntax is `class Child(Parent):`.**
The parent class name goes in parentheses. Multiple parents are separated by commas: `class Child(Parent1, Parent2):`.

**Tip 2 — Always call `super().__init__(...)` in the child's `__init__`.**
This initializes the parent's attributes. The exam will show code that omits this and ask what error occurs — `AttributeError` when you try to access the missing parent attribute.

**Tip 3 — Method override: child's version is called first.**
Python checks the child class before the parent. If the child defines `speak()`, that version runs — the parent's is hidden unless you explicitly call `super().speak()`.

**Tip 4 — `super()` calls the next class in the MRO.**
In single inheritance, that is always the parent. `super().__init__()` runs the parent's `__init__` with `self` automatically passed.

**Tip 5 — Polymorphism: any object with the required method works.**
Python does not enforce type constraints. A function that calls `.speak()` works on any object that has a `speak()` method, regardless of class hierarchy.

**Tip 6 — `isinstance(child_obj, ParentClass)` returns True.**
A `Dog` instance passes `isinstance(d, Animal)`. Use `isinstance()` when you need to check "is this an Animal (or any subclass of Animal)?"

**Tip 7 — `__mro__` shows the method lookup order.**
`Dog.__mro__` returns a tuple: `(Dog, Animal, object)`. Python searches left to right. The exam may show a multi-level hierarchy and ask which method is called.

---

## 5. Beyond the Exam — Real-World Context

**Abstract Base Classes (ABC).**
Python's `abc` module provides `ABC` and `@abstractmethod` to formally require that subclasses implement certain methods:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    # subclasses must implement this

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2

s = Shape()    # TypeError: Can't instantiate abstract class Shape
c = Circle(5)  # OK — area() is implemented
```

**Mixin classes.**
A mixin is a class that provides methods intended to be inherited but not instantiated directly:

```python
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Dog(Animal, JsonMixin):    # inherits to_json from mixin
    pass

d = Dog('Rex')
print(d.to_json())    # '{"name": "Rex"}'
```

**Python's built-in hierarchy.**
`int`, `float`, `bool`, `str`, `list`, `dict` are all classes. `bool` inherits from `int` (`True` and `False` are `1` and `0`). `IOBase → RawIOBase → FileIO` is the file handling hierarchy. Understanding inheritance explains why `isinstance(True, int)` returns `True`.

---

## 6. Required Readings and Videos

**Required Reading — Chapter 14:**
Read Chapter 14 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). This chapter covers OOP with inheritance examples.

**Required Reading — Official Python Docs:**
Read [Classes](https://docs.python.org/3/tutorial/classes.html) in the official Python 3 tutorial, specifically the sections on inheritance and multiple inheritance.

**Supplemental Video:**
Watch the OOP episodes of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) and the relevant segment from Professor Messer's supplemental materials if available for your certification track.

---

## 7. Supplemental Resources

**1. Official Python 3 Docs — Inheritance**
[https://docs.python.org/3/tutorial/classes.html#inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
The authoritative tutorial section on inheritance and multiple inheritance, including the Method Resolution Order (MRO), `super()`, and the `isinstance()` / `issubclass()` built-ins. This section is the primary source for PCAP exam questions on OOP inheritance.

**2. Official Python 3 Docs — abc — Abstract Base Classes**
[https://docs.python.org/3/library/abc.html](https://docs.python.org/3/library/abc.html)
Documents the `ABC` base class and `@abstractmethod` decorator. Understanding abstract base classes explains how Python enforces interface contracts and why `isinstance()` returns `True` for built-in abstract base classes like `Sequence` and `Mapping`.

**3. Python for Everybody — Chapter 14: Object-Oriented Programming**
[https://www.py4e.com/html3/14-objects](https://www.py4e.com/html3/14-objects)
Free textbook chapter with inheritance examples showing parent and child classes. Covers method overriding and using parent class methods from child classes.

**4. Real Python — Inheritance and Composition: A Python OOP Guide**
[https://realpython.com/inheritance-composition-python/](https://realpython.com/inheritance-composition-python/)
A comprehensive free article comparing inheritance and composition with real-world design examples. Covers `super()`, MRO, multiple inheritance, mixins, and abstract base classes. The section on when to use inheritance versus composition is highly practical.

**5. Real Python — Python's super() Considered Super!**
[https://realpython.com/python-super/](https://realpython.com/python-super/)
A focused deep-dive into Python's `super()` function — how it uses the MRO, how it handles multiple inheritance via cooperative multiple inheritance, and common mistakes. Essential reading for understanding why `super()` does what it does.

---

## 8. Study Checklist

- [ ] Watch the Module 15 video lecture by Professor Nash.
- [ ] Draw the Animal → Dog/Cat/Duck hierarchy on paper and trace method calls for each.
- [ ] Write a three-level hierarchy from scratch: one grandparent, two parents, one child of each parent.
- [ ] Deliberately omit `super().__init__()` and observe the `AttributeError` — understand the message.
- [ ] Demonstrate polymorphism with a list of mixed objects calling a common method.
- [ ] Print `ClassName.__mro__` for your hierarchy and trace it.
- [ ] Practice `isinstance()` across the hierarchy: child object passed as parent type.
- [ ] Review all 7 Certification Exam Tips in Section 4.
- [ ] Proceed to the Module 15 Lab Activity.
