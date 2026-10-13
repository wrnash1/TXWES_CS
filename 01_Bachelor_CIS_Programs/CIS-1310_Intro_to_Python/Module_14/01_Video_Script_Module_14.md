# Video Script: CIS-1310 — Introduction to Python

## Module 14 — Object-Oriented Programming: Basics

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - Draw a class-to-object diagram on the whiteboard: the class is a blueprint, instances are the houses built from it.
> - Demonstrate the `self` TypeError live — call an instance method and forget `self` — students need to see this error.
> - Show instance variable vs class variable sharing live: modify a class variable through one instance and show it affects all instances.
> - Run `__str__` before and after adding it so students see the default `<__main__.Dog object at 0x...>` output transform into something readable.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 14 | OOP Basics | CIS-1310"]**

"Welcome back. Every object you have used in this course — strings, lists, dictionaries, integers — is an instance of a class. When you call `'hello'.upper()`, you are calling a method on a `str` object. When you call `[1,2,3].append(4)`, you are calling a method on a `list` object.

Object-oriented programming lets you define your own types with their own data and behaviors. A class is a blueprint. An object is an instance built from that blueprint. This module covers defining classes, the `__init__` constructor, `self`, instance variables, instance methods, and the special `__str__` method. OOP is one of the most heavily tested areas on the PCAP exam, and it is the foundational skill for all modern Python development."

---

## [00:45 – 03:00] Defining a Class — Blueprint and Instances

**[SHOW SLIDE: "class — The Blueprint"]**

"Let us start with the simplest possible class.

**[DEMO — minimal class]**

```python
class Dog:
    pass
```

That's it. `class Dog:` defines a new type called `Dog`. The `pass` means no body yet.

**[DEMO — creating instances]**

```python
d1 = Dog()
d2 = Dog()
print(type(d1))    # <class '__main__.Dog'>
print(d1)          # <__main__.Dog object at 0x7f...>
print(d1 is d2)    # False — two separate objects
```

`Dog()` calls the class to create an instance — this is called **instantiation**. `d1` and `d2` are two separate objects in memory. `is` checks identity — whether two variables point to the same object in memory. `d1` and `d2` are different objects so `is` returns `False`.

[PAUSE]

The default string representation — `<__main__.Dog object at 0x7f...>` — is not useful. We will fix that shortly."

---

## [03:00 – 06:30] `__init__` and `self` — Initializing Instances

**[SHOW SLIDE: "`__init__` — The Constructor"]**

"The `__init__` method is Python's constructor. It runs automatically every time you create a new instance, and it is where you initialize the instance's data.

**[DEMO — `__init__` with attributes]**

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
```

`self` is a reference to the instance being created. Every instance method's first parameter must be `self`. Python passes it automatically — you never supply it yourself when calling the method.

`self.name = name` creates an **instance variable** called `name` on this specific object and assigns it the value of the parameter `name`.

**[DEMO — creating instances]**

```python
d1 = Dog('Rex', 'German Shepherd', 4)
d2 = Dog('Luna', 'Labrador', 2)

print(d1.name)    # Rex
print(d2.name)    # Luna
print(d1.breed)   # German Shepherd
print(d2.age)     # 2
```

Each instance has its own copy of `name`, `breed`, and `age`. Changing `d1.name` does not affect `d2.name`.

[PAUSE]

**What happens if you forget `self`?**

```python
class Dog:
    def __init__(name, breed):    # WRONG — missing self
        name.name = name          # this makes no sense
```

If you forget `self`, Python passes the instance as the first argument — which you named `name`. So `name.name = name` is trying to set an attribute on the string passed as the first positional argument. You will get a confusing `AttributeError` or `TypeError`. Always make `self` the first parameter.

**The PCAP exam frequently tests this. `self` must be the first parameter of every instance method.**"

---

## [06:30 – 09:00] Instance Methods

**[SHOW SLIDE: "Instance Methods — Behaviors"]**

"Instance methods are functions defined inside a class. They always take `self` as their first parameter, which gives them access to the instance's data.

**[DEMO — adding methods]**

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f'{self.name} says: Woof!'

    def birthday(self):
        self.age += 1
        return f'{self.name} is now {self.age} years old.'

    def describe(self):
        return f'{self.name} is a {self.age}-year-old {self.breed}.'
```

**[DEMO — calling methods]**

```python
d1 = Dog('Rex', 'German Shepherd', 4)

print(d1.bark())        # Rex says: Woof!
print(d1.describe())    # Rex is a 4-year-old German Shepherd.
print(d1.birthday())    # Rex is now 5 years old.
print(d1.age)           # 5 — the attribute was actually modified
```

`d1.bark()` — Python automatically passes `d1` as the `self` argument. You write `d1.bark()` with no arguments, but the method receives `self=d1` behind the scenes.

[PAUSE]

**Instance variables belong to the instance.** Every `Dog` has its own `name`, `breed`, and `age`. Methods access and modify those through `self`."

---

## [09:00 – 11:00] `__str__` — Human-Readable Representation

**[SHOW SLIDE: "`__str__` — Controlling print() Output"]**

"Remember that default string `<__main__.Dog object at 0x7f...>`? We can replace it by defining `__str__`.

`__str__` is a special method (called a dunder method — double underscore on each side) that Python calls when you pass an object to `print()` or `str()`.

**[DEMO — before `__str__`]**

```python
d1 = Dog('Rex', 'German Shepherd', 4)
print(d1)    # <__main__.Dog object at 0x7f...> — not helpful
```

**[DEMO — adding `__str__`]**

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return f'Dog({self.name!r}, {self.breed!r}, age={self.age})'

    def bark(self):
        return f'{self.name} says: Woof!'
```

```python
d1 = Dog('Rex', 'German Shepherd', 4)
print(d1)          # Dog('Rex', 'German Shepherd', age=4)
print(str(d1))     # Dog('Rex', 'German Shepherd', age=4)
```

`__str__` must return a string. Python calls it automatically whenever you print an object.

[PAUSE]

There is also `__repr__` — the developer-facing representation. It is called in the REPL when you type an expression without `print()`. `__str__` is for end users, `__repr__` is for developers. When only `__repr__` is defined and not `__str__`, Python falls back to `__repr__` for `print()` as well."

---

## [11:00 – 13:00] Instance Variables vs Class Variables

**[SHOW SLIDE: "Instance Variables vs Class Variables"]**

"Every variable we have put on `self` is an instance variable — it belongs to one specific object. Python also supports class variables — defined on the class itself, shared by all instances.

**[DEMO — class variable]**

```python
class Dog:
    species = 'Canis lupus familiaris'    # class variable

    def __init__(self, name, breed, age):
        self.name = name      # instance variable
        self.breed = breed    # instance variable
        self.age = age        # instance variable
```

```python
d1 = Dog('Rex', 'German Shepherd', 4)
d2 = Dog('Luna', 'Labrador', 2)

print(d1.species)           # Canis lupus familiaris
print(d2.species)           # Canis lupus familiaris
print(Dog.species)          # Canis lupus familiaris — accessible on class too

Dog.species = 'Changed'
print(d1.species)           # Changed
print(d2.species)           # Changed — both instances see the change
```

[PAUSE]

**The danger: assigning through an instance creates a new instance variable.**

```python
d1.species = 'Individual override'
print(d1.species)    # Individual override — d1 has its own copy now
print(d2.species)    # Changed — d2 still reads the class variable
```

Once you assign `d1.species`, Python creates a new instance variable on `d1` that shadows the class variable. `d2` never got its own copy, so it still reads from the class.

This is a classic PCAP exam trap. Understand the difference: class variables are shared, instance variables are per-object."

---

## [13:00 – 15:00] isinstance() and PCAP Exam Tips

**[SHOW SLIDE: "isinstance() and type()"]**

"Two built-in functions for working with objects.

**[DEMO — type() and isinstance()]**

```python
d1 = Dog('Rex', 'German Shepherd', 4)

print(type(d1))                  # <class '__main__.Dog'>
print(type(d1) == Dog)           # True
print(isinstance(d1, Dog))       # True
print(isinstance(d1, object))    # True — everything in Python is an object
print(isinstance(42, int))       # True
print(isinstance('hi', (str, bytes)))  # True — tuple of types
```

`isinstance(obj, cls)` returns `True` if `obj` is an instance of `cls` or any subclass of `cls`. This is the preferred check in production code — it handles inheritance correctly. `type(obj) == cls` is a strict check that does not account for subclasses.

**Key exam take-aways:**

**1.** `__init__` initializes the instance. It does not return anything — no `return` statement. Python calls it automatically when you write `ClassName(args)`.

**2.** `self` must be the first parameter of every instance method. Python passes it automatically; you never supply it when calling.

**3.** Instance variables live on each object. Class variables live on the class and are shared by all instances. Assigning to `instance.class_var` creates a new instance variable, it does not modify the class variable.

**4.** `__str__` is called by `print()` and `str()`. Always return a string. If missing, Python falls back to `__repr__`. If neither is defined, you get the unhelpful memory address output.

**5.** `isinstance()` is preferred over `type() ==` because `isinstance` returns `True` for subclasses.

Module 15 covers inheritance, `super()`, polymorphism, and method overriding — everything you need to build class hierarchies. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 14 — OOP Basics]**

---

## Additional Resources

- [Python for Everybody — Dr. Charles Severance](https://www.py4e.com/book) — Chapter 14 covers Object-Oriented Programming
- [Official Python Docs — Classes](https://docs.python.org/3/tutorial/classes.html) — authoritative tutorial on Python classes
- [Real Python — Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/) — practical guide with examples
