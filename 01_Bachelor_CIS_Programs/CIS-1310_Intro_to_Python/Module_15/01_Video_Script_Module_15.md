# Video Script: CIS-1310 — Introduction to Python

## Module 15 — Advanced OOP: Inheritance and Polymorphism

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / Python Institute &bull; Python Programming Full Course &bull; Module 15</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=rfscVS0vtbw" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/rfscVS0vtbw" title="freeCodeCamp / Python Institute &bull; Python Programming Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp / Python Institute &bull; Python Programming Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 15 | Advanced OOP | CIS-1310"]**

"Welcome back. In Module 14 you learned to define classes, write `__init__`, use `self`, and create instance methods. Now we go further.

Inheritance lets one class reuse and extend another class's code. Polymorphism lets different classes respond to the same method call in their own way. Together, these two concepts are what make object-oriented design powerful — instead of copying and pasting code, you build a hierarchy where child classes inherit everything from their parent and only add or override what is different.

The PCAP exam tests inheritance syntax, `super()`, method overriding, and the Method Resolution Order. These are also the foundations of every Python framework and library you will ever use."

---

## [00:45 – 03:30] Inheritance — Child Classes Extend Parents

**[SHOW SLIDE: "Inheritance — Reuse and Extend"]**

"Inheritance lets a new class acquire all the attributes and methods of an existing class.

**[DEMO — base class]**

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f'{self.name} makes a sound.'

    def __str__(self):
        return f'{self.species}({self.name!r})'
```

**[DEMO — child class]**

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, 'Canis lupus familiaris')
        self.breed = breed

    def speak(self):
        return f'{self.name} says: Woof!'

    def fetch(self):
        return f'{self.name} fetches the ball!'
```

`class Dog(Animal):` — the parentheses mean `Dog` inherits from `Animal`. `Animal` is the **parent class** (also called superclass or base class). `Dog` is the **child class** (also called subclass or derived class).

[PAUSE]

`super().__init__(name, 'Canis lupus familiaris')` calls the parent's `__init__` to initialize the inherited attributes. This is critical — if you forget it, the parent's `__init__` never runs and `self.name` and `self.species` will not exist.

**[DEMO — using the classes]**

```python
a = Animal('Generic', 'Unknown')
d = Dog('Rex', 'German Shepherd')

print(a)            # Unknown('Generic')
print(d)            # Canis lupus familiaris('Rex')
print(d.name)       # Rex — inherited from Animal
print(d.breed)      # German Shepherd — defined in Dog
print(d.speak())    # Rex says: Woof! — overridden in Dog
print(d.fetch())    # Rex fetches the ball! — only on Dog
```

`Dog` inherits `name`, `species`, and `__str__` from `Animal`, adds its own `breed`, and overrides `speak()`."

---

## [03:30 – 06:00] super() — Calling the Parent

**[SHOW SLIDE: "`super()` — Accessing the Parent Class"]**

"`super()` returns a proxy object that lets you call methods from the parent class. The most common use is in `__init__` to run the parent's initialization logic.

**[DEMO — what happens without super()]**

```python
class Dog(Animal):
    def __init__(self, name, breed):
        # forgot super().__init__()
        self.breed = breed

d = Dog('Rex', 'German Shepherd')
print(d.breed)    # German Shepherd — works
print(d.name)     # AttributeError: 'Dog' object has no attribute 'name'
```

Without `super().__init__()`, the parent's `__init__` never runs. `self.name` and `self.species` are never created.

**[DEMO — super() in a method override]**

```python
class Cat(Animal):
    def __init__(self, name, indoor):
        super().__init__(name, 'Felis catus')
        self.indoor = indoor

    def speak(self):
        return f'{self.name} says: Meow!'

    def describe(self):
        location = 'indoor' if self.indoor else 'outdoor'
        return f'{super().__str__()} — {location} cat'
```

```python
c = Cat('Whiskers', True)
print(c.speak())       # Whiskers says: Meow!
print(c.describe())    # Felis catus('Whiskers') — indoor cat
```

`super().__str__()` calls `Animal.__str__` — the parent's version. This lets `describe()` reuse the parent's string format and add to it rather than duplicating it.

[PAUSE]

**`super()` is not limited to `__init__`.** You can call `super().any_method()` anywhere inside a child class to invoke the parent's version of that method."

---

## [06:00 – 08:30] Method Overriding

**[SHOW SLIDE: "Method Overriding — Redefining Behavior"]**

"When a child class defines a method with the same name as the parent, the child's version **overrides** the parent's. Python always calls the most specific (child) version first.

**[DEMO — full hierarchy]**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} makes a generic sound.'

class Dog(Animal):
    def speak(self):
        return f'{self.name} says: Woof!'

class Cat(Animal):
    def speak(self):
        return f'{self.name} says: Meow!'

class Duck(Animal):
    def speak(self):
        return f'{self.name} says: Quack!'
```

**[DEMO — calling overridden methods]**

```python
a = Animal('Generic')
d = Dog('Rex')
c = Cat('Whiskers')
k = Duck('Donald')

print(a.speak())    # Generic makes a generic sound.
print(d.speak())    # Rex says: Woof!
print(c.speak())    # Whiskers says: Meow!
print(k.speak())    # Donald says: Quack!
```

Each class has its own `speak()`. Python always calls the version defined closest to the actual type of the object."

---

## [08:30 – 11:00] Polymorphism — One Interface, Many Forms

**[SHOW SLIDE: "Polymorphism — Same Call, Different Behavior"]**

"Polymorphism means you can treat objects of different classes uniformly, as long as they share a common interface — in this case, all having a `speak()` method.

**[DEMO — polymorphism with a list]**

```python
animals = [
    Dog('Rex'),
    Cat('Whiskers'),
    Duck('Donald'),
    Animal('Unknown'),
]

for animal in animals:
    print(animal.speak())
```

```text
Rex says: Woof!
Whiskers says: Meow!
Donald says: Quack!
Unknown makes a generic sound.
```

[PAUSE]

Notice that the for-loop does not know or care which specific type each object is. It just calls `.speak()` and Python figures out which version to run based on the actual type. This is polymorphism.

This is tremendously powerful. You can add a new animal type — say `class Parrot(Animal)` — without changing the loop at all. The loop automatically calls the right `speak()` for any object that has one.

**[DEMO — polymorphism with a function]**

```python
def make_noise(animal):
    print(animal.speak())

make_noise(Dog('Rex'))        # Rex says: Woof!
make_noise(Cat('Whiskers'))   # Whiskers says: Meow!
```

`make_noise` does not care about the type — it just calls `.speak()`. Any object with a `speak()` method works. This is called **duck typing** in Python: if it walks like a duck and quacks like a duck, it is a duck."

---

## [11:00 – 13:00] Method Resolution Order (MRO)

**[SHOW SLIDE: "MRO — How Python Finds Methods"]**

"When you call `d.speak()`, Python looks for `speak` in a specific order. This order is called the Method Resolution Order — MRO.

**[DEMO — `__mro__`]**

```python
print(Dog.__mro__)
```

```text
(<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)
```

Python searches `Dog` first, then `Animal`, then `object` (the root of all Python classes). The first match wins.

This is why `d.speak()` calls `Dog.speak()` — it is found first. If `Dog` did not define `speak()`, Python would look in `Animal` and find it there. If neither defined it, Python would look in `object` and find the default behavior.

**[DEMO — `isinstance()` with inheritance]**

```python
d = Dog('Rex')

print(isinstance(d, Dog))       # True — d is a Dog
print(isinstance(d, Animal))    # True — Dog inherits from Animal
print(isinstance(d, object))    # True — everything is an object
```

`isinstance(d, Animal)` returns `True` because `Dog` is a subclass of `Animal`. This is why `isinstance()` is preferred over `type() ==` — it respects the inheritance hierarchy."

---

## [13:00 – 15:00] PCAP Exam Tips and Wrap-Up

**[SHOW SLIDE: "Module 15 — PCAP Alignment"]**

"Key exam take-aways:

**1.** Inheritance syntax: `class Child(Parent):`. The parent class is named in parentheses after the child class name.

**2.** Always call `super().__init__(...)` in the child's `__init__` to initialize inherited attributes. Forgetting it causes `AttributeError` when you access parent attributes.

**3.** Method overriding: when child and parent define the same method name, the child's version is called. Python uses the MRO to find the first matching method.

**4.** `super()` calls the next class in the MRO. In a single-inheritance chain, that is always the parent. `super().method_name()` invokes the parent's version without hardcoding the parent class name.

**5.** Polymorphism: different objects responding to the same method call in their own way. A list of `Animal` subclasses all responding to `.speak()` is the canonical example.

**6.** `isinstance(d, Parent)` returns `True` if `d` is an instance of `Parent` or any subclass of `Parent`. Use `isinstance()`, not `type() ==`, when inheritance is involved.

**7.** `ClassName.__mro__` shows the method resolution order — the search path Python follows when looking up methods and attributes.

Module 16 is the final module — a comprehensive review of all 15 modules and PCAP certification exam strategy. You have covered the full core Python language. See you at the finish line."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 15 — Advanced OOP]**

---

## Additional Resources

- [Python for Everybody — Dr. Charles Severance](https://www.py4e.com/book) — Chapter 14 covers OOP including inheritance
- [Official Python Docs — Classes](https://docs.python.org/3/tutorial/classes.html) — authoritative tutorial on inheritance and MRO
- [Real Python — Inheritance and Composition](https://realpython.com/inheritance-composition-python/) — practical guide with worked examples
