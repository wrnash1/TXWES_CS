# Lab Activity: Module 15 — Advanced OOP: Inheritance and Polymorphism

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 75–90 minutes

---

## Overview

In this lab you will define a parent class and multiple child classes that inherit from it, demonstrate what happens when `super().__init__()` is omitted, practice method overriding and calling `super()` from overridden methods, demonstrate polymorphism with a list of mixed objects, inspect the Method Resolution Order, use `isinstance()` across the inheritance hierarchy, and build a complete multi-class shape hierarchy with area calculations.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module15
cd module15
```

---

## Part 1 — Basic Inheritance

```bash
python3
```

### Step 1.1 — Parent class

```python
>>> class Animal:
...     def __init__(self, name, species):
...         self.name = name
...         self.species = species
...     def speak(self):
...         return f'{self.name} makes a sound.'
...     def __str__(self):
...         return f'{self.species}({self.name!r})'
...
```

### Step 1.2 — Child class with super()

```python
>>> class Dog(Animal):
...     def __init__(self, name, breed):
...         super().__init__(name, 'Canis lupus familiaris')
...         self.breed = breed
...     def speak(self):
...         return f'{self.name} says: Woof!'
...     def fetch(self):
...         return f'{self.name} fetches the ball!'
...
>>> d = Dog('Rex', 'German Shepherd')
>>> d.name
'Rex'
>>> d.species
'Canis lupus familiaris'
>>> d.breed
'German Shepherd'
>>> d.speak()
'Rex says: Woof!'
>>> d.fetch()
'Rex fetches the ball!'
>>> print(d)
Canis lupus familiaris('Rex')
```

`d` has both parent attributes (`name`, `species`) and its own (`breed`). It inherits `__str__` from `Animal` but overrides `speak()`.

### Step 1.3 — What happens without `super().__init__()`

```python
>>> class BadDog(Animal):
...     def __init__(self, name, breed):
...         # super().__init__() NOT CALLED
...         self.breed = breed
...
>>> b = BadDog('Luna', 'Labrador')
>>> b.breed
'Labrador'
>>> b.name
```

```text
AttributeError: 'BadDog' object has no attribute 'name'
```

`Animal.__init__` never ran, so `self.name` and `self.species` were never created.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the `Dog` instance with both inherited and own attributes (Step 1.2) and the `AttributeError` from the missing `super().__init__()` (Step 1.3). Save as `lab15_screenshot_01_inheritance.png`.

---

## Part 2 — Method Overriding and super() in Methods

```bash
python3
```

### Step 2.1 — Multiple subclasses overriding the same method

```python
>>> class Animal:
...     def __init__(self, name):
...         self.name = name
...     def speak(self):
...         return f'{self.name} makes a generic sound.'
...
>>> class Dog(Animal):
...     def speak(self):
...         return f'{self.name} says: Woof!'
...
>>> class Cat(Animal):
...     def speak(self):
...         return f'{self.name} says: Meow!'
...
>>> class Duck(Animal):
...     def speak(self):
...         return f'{self.name} says: Quack!'
...
>>> a = Animal('Generic')
>>> d = Dog('Rex')
>>> c = Cat('Whiskers')
>>> k = Duck('Donald')
>>> a.speak()
'Generic makes a generic sound.'
>>> d.speak()
'Rex says: Woof!'
>>> c.speak()
'Whiskers says: Meow!'
>>> k.speak()
'Donald says: Quack!'
```

### Step 2.2 — super() to extend a method (not replace it)

```python
>>> class LoudDog(Dog):
...     def speak(self):
...         quiet = super().speak()
...         return quiet.upper() + '!!'
...
>>> ld = LoudDog('Thunder')
>>> ld.speak()
"THUNDER SAYS: WOOF!!!"
```

`super().speak()` calls `Dog.speak()`. `LoudDog` extends it instead of replacing it entirely.

### Step 2.3 — MRO inspection

```python
>>> LoudDog.__mro__
(<class '__main__.LoudDog'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)
```

Python searches in this order: `LoudDog` → `Dog` → `Animal` → `object`. The first match wins.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing the four `speak()` calls from Step 2.1, the `LoudDog.speak()` result using `super()` (Step 2.2), and the MRO output (Step 2.3). Save as `lab15_screenshot_02_override_super.png`.

---

## Part 3 — Polymorphism

```bash
python3
```

### Step 3.1 — List of mixed types, uniform interface

Redefine the classes from Part 2 (copy the same definitions), then:

```python
>>> animals = [
...     Dog('Rex'),
...     Cat('Whiskers'),
...     Duck('Donald'),
...     Animal('Unknown'),
... ]
...
>>> for a in animals:
...     print(a.speak())
...
Rex says: Woof!
Whiskers says: Meow!
Donald says: Quack!
Unknown makes a generic sound.
```

The loop does not check the type of each element — it just calls `.speak()`.

### Step 3.2 — Polymorphic function

```python
>>> def describe_animal(a):
...     print(f'{type(a).__name__}: {a.speak()}')
...
>>> for a in animals:
...     describe_animal(a)
...
Dog: Rex says: Woof!
Cat: Whiskers says: Meow!
Duck: Donald says: Quack!
Animal: Unknown makes a generic sound.
```

### Step 3.3 — isinstance() across the hierarchy

```python
>>> d = Dog('Rex')
>>> isinstance(d, Dog)
True
>>> isinstance(d, Animal)
True
>>> isinstance(d, object)
True
>>> isinstance(d, Cat)
False
>>> type(d) == Animal
False
>>> type(d) == Dog
True
```

`isinstance(d, Animal)` is `True` because `Dog` is a subclass of `Animal`. `type(d) == Animal` is `False` — strict type equality does not account for inheritance.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 3 REQUIRED:** Screenshot showing the polymorphic for-loop output (Step 3.1), the `describe_animal()` output (Step 3.2), and the `isinstance()` results (Step 3.3). Save as `lab15_screenshot_03_polymorphism.png`.

---

## Part 4 — shapes.py (Shape Hierarchy)

```bash
nano shapes.py
```

```python
# shapes.py
# Demonstrates inheritance and polymorphism with a Shape hierarchy
# Module 15 Lab — CIS-1310

import math


class Shape:
    '''Base class for all shapes.'''

    def __init__(self, color='black'):
        self.color = color

    def area(self):
        raise NotImplementedError(
            f'{type(self).__name__} must implement area()'
        )

    def perimeter(self):
        raise NotImplementedError(
            f'{type(self).__name__} must implement perimeter()'
        )

    def describe(self):
        return (f'{type(self).__name__} | color={self.color} | '
                f'area={self.area():.4f} | perimeter={self.perimeter():.4f}')

    def __str__(self):
        return f'{type(self).__name__}(color={self.color!r})'


class Circle(Shape):
    '''A circle defined by radius.'''

    def __init__(self, radius, color='black'):
        super().__init__(color)
        if radius <= 0:
            raise ValueError(f'Radius must be positive, got {radius}')
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Circle(radius={self.radius}, color={self.color!r})'


class Rectangle(Shape):
    '''A rectangle defined by width and height.'''

    def __init__(self, width, height, color='black'):
        super().__init__(color)
        if width <= 0 or height <= 0:
            raise ValueError('Width and height must be positive')
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return (f'Rectangle(width={self.width}, height={self.height}, '
                f'color={self.color!r})')


class Square(Rectangle):
    '''A square — a rectangle with equal sides.'''

    def __init__(self, side, color='black'):
        super().__init__(side, side, color)    # width == height == side
        self.side = side

    def __str__(self):
        return f'Square(side={self.side}, color={self.color!r})'


class Triangle(Shape):
    '''A right triangle defined by base and height.'''

    def __init__(self, base, height, color='black'):
        super().__init__(color)
        if base <= 0 or height <= 0:
            raise ValueError('Base and height must be positive')
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        hypotenuse = math.sqrt(self.base ** 2 + self.height ** 2)
        return self.base + self.height + hypotenuse

    def __str__(self):
        return (f'Triangle(base={self.base}, height={self.height}, '
                f'color={self.color!r})')


def total_area(shapes):
    '''Return the sum of areas for a list of shapes.'''
    return sum(s.area() for s in shapes)


def largest_shape(shapes):
    '''Return the shape with the greatest area.'''
    return max(shapes, key=lambda s: s.area())


if __name__ == '__main__':
    shapes = [
        Circle(5, 'red'),
        Rectangle(4, 6, 'blue'),
        Square(3, 'green'),
        Triangle(6, 8, 'yellow'),
        Circle(2),
    ]

    print('=== Shape Descriptions ===')
    for s in shapes:
        print(f'  {s.describe()}')
    print()

    print('=== Polymorphism: str() output ===')
    for s in shapes:
        print(f'  {s}')
    print()

    print('=== isinstance() checks ===')
    sq = Square(4)
    print(f'isinstance(sq, Square):    {isinstance(sq, Square)}')
    print(f'isinstance(sq, Rectangle): {isinstance(sq, Rectangle)}')
    print(f'isinstance(sq, Shape):     {isinstance(sq, Shape)}')
    print(f'isinstance(sq, Circle):    {isinstance(sq, Circle)}')
    print()

    print('=== MRO for Square ===')
    for cls in Square.__mro__:
        print(f'  {cls}')
    print()

    print(f'Total area: {total_area(shapes):.4f}')
    big = largest_shape(shapes)
    print(f'Largest shape: {big} (area={big.area():.4f})')
    print()

    print('=== Exception handling ===')
    try:
        bad = Circle(-3)
    except ValueError as e:
        print(f'  Caught: {e}')

    try:
        s = Shape()
        s.area()
    except NotImplementedError as e:
        print(f'  Caught: {e}')
```

Save and run:

```bash
python3 shapes.py
```

Expected output:

```text
=== Shape Descriptions ===
  Circle | color='red' | area=78.5398 | perimeter=31.4159
  Rectangle | color='blue' | area=24.0000 | perimeter=20.0000
  Square | color='green' | area=9.0000 | perimeter=12.0000
  Triangle | color='yellow' | area=24.0000 | perimeter=24.0000
  Circle | color='black' | area=12.5664 | perimeter=12.5664

=== Polymorphism: str() output ===
  Circle(radius=5, color='red')
  Rectangle(width=4, height=6, color='blue')
  Square(side=3, color='green')
  Triangle(base=6, height=8, color='yellow')
  Circle(radius=2, color='black')

=== isinstance() checks ===
isinstance(sq, Square):    True
isinstance(sq, Rectangle): True
isinstance(sq, Shape):     True
isinstance(sq, Circle):    False

=== MRO for Square ===
  <class '__main__.Square'>
  <class '__main__.Rectangle'>
  <class '__main__.Shape'>
  <class 'object'>

Total area: 148.6062
Largest shape: Circle(radius=5, color='red') (area=78.5398)

=== Exception handling ===
  Caught: Radius must be positive, got -3
  Caught: Shape must implement area()
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `shapes.py` running and showing the complete output. Save as `lab15_screenshot_04_shapes.png`.

---

## Part 5 — vehicles.py (Three-Level Hierarchy)

```bash
nano vehicles.py
```

```python
# vehicles.py
# Demonstrates a three-level inheritance hierarchy
# Module 15 Lab — CIS-1310


class Vehicle:
    '''Base class for all vehicles.'''

    def __init__(self, make, model, year, speed_kmh=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed_kmh = speed_kmh

    def accelerate(self, amount):
        self.speed_kmh += amount
        return self.speed_kmh

    def brake(self, amount):
        self.speed_kmh = max(0, self.speed_kmh - amount)
        return self.speed_kmh

    def describe(self):
        return f'{self.year} {self.make} {self.model}'

    def __str__(self):
        return f'{self.describe()} @ {self.speed_kmh} km/h'


class Car(Vehicle):
    '''A car with a number of doors.'''

    def __init__(self, make, model, year, doors=4):
        super().__init__(make, model, year)
        self.doors = doors

    def describe(self):
        return f'{super().describe()} ({self.doors}-door)'

    def honk(self):
        return f'{self.make} {self.model}: Beep beep!'


class ElectricCar(Car):
    '''An electric car with a battery range.'''

    def __init__(self, make, model, year, doors=4, range_km=400):
        super().__init__(make, model, year, doors)
        self.range_km = range_km
        self._charge_pct = 100

    def charge(self, pct):
        self._charge_pct = min(100, self._charge_pct + pct)
        return self._charge_pct

    def describe(self):
        return f'{super().describe()}, {self.range_km}km range'

    def __str__(self):
        return (f'{self.describe()} | charge={self._charge_pct}% | '
                f'speed={self.speed_kmh} km/h')


if __name__ == '__main__':
    v = Vehicle('Generic', 'Transport', 2010)
    c = Car('Honda', 'Civic', 2022, 4)
    e = ElectricCar('Tesla', 'Model 3', 2023, 4, 560)

    print('=== Descriptions ===')
    print(v.describe())
    print(c.describe())
    print(e.describe())
    print()

    print('=== str() output ===')
    print(v)
    print(c)
    print(e)
    print()

    c.accelerate(60)
    c.accelerate(30)
    c.brake(20)
    print(f'Car after driving: {c}')
    print(c.honk())
    print()

    e.accelerate(100)
    e._charge_pct = 80    # simulate partial charge
    e.charge(15)
    print(f'Electric car: {e}')
    print()

    print('=== isinstance() across hierarchy ===')
    print(f'isinstance(e, ElectricCar): {isinstance(e, ElectricCar)}')
    print(f'isinstance(e, Car):         {isinstance(e, Car)}')
    print(f'isinstance(e, Vehicle):     {isinstance(e, Vehicle)}')
    print()

    print('=== MRO for ElectricCar ===')
    for cls in ElectricCar.__mro__:
        print(f'  {cls.__name__}')
    print()

    print('=== Polymorphism ===')
    fleet = [v, c, e]
    for vehicle in fleet:
        print(f'  {type(vehicle).__name__}: {vehicle.describe()}')
```

Save and run:

```bash
python3 vehicles.py
```

Expected output:

```text
=== Descriptions ===
2010 Generic Transport
2022 Honda Civic (4-door)
2023 Tesla Model 3 (4-door), 560km range

=== str() output ===
2010 Generic Transport @ 0 km/h
2022 Honda Civic @ 0 km/h
2023 Tesla Model 3 (4-door), 560km range | charge=100% | speed=0 km/h

Car after driving: 2022 Honda Civic @ 70 km/h
Honda Civic: Beep beep!

Electric car: 2023 Tesla Model 3 (4-door), 560km range | charge=95% | speed=100 km/h

=== isinstance() across hierarchy ===
isinstance(e, ElectricCar): True
isinstance(e, Car):         True
isinstance(e, Vehicle):     True

=== MRO for ElectricCar ===
  ElectricCar
  Car
  Vehicle
  object

=== Polymorphism ===
  Vehicle: 2010 Generic Transport
  Car: 2022 Honda Civic (4-door)
  ElectricCar: 2023 Tesla Model 3 (4-door), 560km range
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `vehicles.py` running and showing the complete output. Save as `lab15_screenshot_05_vehicles.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 15 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab15_screenshot_01_inheritance.png` | Dog with inherited + own attributes, AttributeError from missing `super().__init__()` |
| 2 | `lab15_screenshot_02_override_super.png` | Four speak() overrides, LoudDog super() extension, MRO output |
| 3 | `lab15_screenshot_03_polymorphism.png` | Polymorphic loop, describe_animal(), isinstance() results |
| 4 | `lab15_screenshot_04_shapes.png` | shapes.py complete output |
| 5 | `lab15_screenshot_05_vehicles.png` | vehicles.py complete output |

---

## Troubleshooting Guide

**`AttributeError: 'ChildClass' object has no attribute 'parent_attr'`**
You forgot to call `super().__init__(...)` in the child's `__init__`. The parent's initialization never ran, so attributes set by the parent's `__init__` do not exist. Always call `super().__init__()` as the first line of the child's `__init__`.

**Child's method not being called — parent's version runs instead.**
Verify the method name matches exactly. Python is case-sensitive: `Speak` is not the same as `speak`. Also confirm the child class correctly inherits from the parent (the parent name must appear in parentheses in the class definition).

**`super()` works in class but raises `TypeError` in standalone function.**
`super()` only works inside a class definition. It uses a special cell reference to the class it is defined in. Calling `super()` outside a class or after copying a method out of a class will fail.

**`isinstance(child_obj, ChildClass)` is True but `isinstance(child_obj, ParentClass)` is False.**
This would mean the class hierarchy is wrong. Check the class definitions: `class Child(Parent):` must list the parent. If the child inherits from `object` (all classes do by default) and not from `Parent`, the relationship is broken.

**`NotImplementedError` when calling a base class method.**
The base class intentionally raises `NotImplementedError` to signal that subclasses must override this method. You need to define the method in your subclass. Check the base class definition for which methods require overriding.
