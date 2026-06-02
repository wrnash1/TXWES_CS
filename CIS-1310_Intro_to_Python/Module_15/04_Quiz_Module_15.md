# Quiz: Module 15 — Advanced OOP: Inheritance and Polymorphism

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 15 topics.

---

### Question 1

What is the output of this code?

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} makes a sound.'

class Dog(Animal):
    def speak(self):
        return f'{self.name} says: Woof!'

d = Dog('Rex')
print(d.speak())
print(d.name)
```

- A) `Rex makes a sound.` then `Rex`
- B) `Rex says: Woof!` then `AttributeError`
- C) `Rex says: Woof!` then `Rex`
- D) `AttributeError` — Dog has no `__init__`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Dog` overrides `speak()`. Python calls `Dog.speak()`, not `Animal.speak()`. The override replaces the parent's version.
- *Why B is incorrect:* `Dog` does not define `__init__`, so Python uses `Animal.__init__`. This is automatic inheritance — the parent's `__init__` runs when you create `Dog('Rex')`, setting `self.name = 'Rex'`. No `AttributeError`.
- *Why C is correct:* `Dog.speak()` is called (override). `d.name` exists because `Animal.__init__` ran automatically (inherited). Both work correctly.
- *Why D is incorrect:* When a child class does not define `__init__`, Python automatically uses the parent's `__init__`. `Dog('Rex')` calls `Animal.__init__(d, 'Rex')` — no error.

---

### Question 2

What is the output of this code?

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed

d = Dog('Rex', 'Labrador')
print(d.breed)
print(d.name)
```

- A) `Labrador` then `Rex`
- B) `Labrador` then `AttributeError`
- C) `AttributeError` — Dog cannot override `__init__`
- D) `Rex` then `Labrador`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Dog.__init__` does not call `super().__init__(name)`. `Animal.__init__` never runs, so `self.name` is never created. Accessing `d.name` raises `AttributeError`.
- *Why B is correct:* `Dog.__init__` only sets `self.breed`. Because `super().__init__()` was not called, `self.name` does not exist. `d.breed` succeeds, but `d.name` raises `AttributeError: 'Dog' object has no attribute 'name'`.
- *Why C is incorrect:* Child classes can absolutely override `__init__`. The issue is not overriding — it is forgetting to call `super().__init__()` to initialize parent attributes.
- *Why D is incorrect:* `d.name` would need to exist before printing. Since `super().__init__()` was omitted, it does not.

---

### Question 3

What is the output of this code?

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Shape(), Circle(3), Circle(1)]
for s in shapes:
    print(s.area())
```

- A) `0` then `0` then `0`
- B) `0` then `28.26` then `3.14`
- C) `TypeError` — cannot call area() on mixed types
- D) `28.26` then `3.14` then `0`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Circle` overrides `area()`. Calling `area()` on a `Circle` instance returns the circle's area, not `0`.
- *Why B is correct:* `Shape().area()` returns `0` (parent's version). `Circle(3).area()` returns `3.14 * 9 = 28.26`. `Circle(1).area()` returns `3.14 * 1 = 3.14`. This demonstrates polymorphism — the same `area()` call produces different results based on the actual type.
- *Why C is incorrect:* Python does not enforce type constraints on lists or for-loops. This is polymorphism — calling the same method on objects of different types works fine as long as the method exists.
- *Why D is incorrect:* The loop iterates in order: `Shape`, `Circle(3)`, `Circle(1)`. The first value is `0`, not `28.26`.

---

### Question 4

What is printed by this code?

```python
class Animal:
    def speak(self):
        return 'generic sound'

class Dog(Animal):
    def speak(self):
        base = super().speak()
        return f'Woof! ({base})'

d = Dog()
print(d.speak())
```

- A) `generic sound`
- B) `Woof!`
- C) `Woof! (generic sound)`
- D) `TypeError` — super() requires arguments

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Dog.speak()` is called (it overrides the parent). The parent's `generic sound` is only returned by `super().speak()` — used internally, not as the final return value.
- *Why B is incorrect:* `Dog.speak()` calls `super().speak()` and incorporates its result in the f-string. The final return is the combined string, not just `'Woof!'`.
- *Why C is correct:* `super().speak()` calls `Animal.speak()` which returns `'generic sound'`. `Dog.speak()` then returns `f'Woof! (generic sound)'`. This demonstrates using `super()` to extend a method rather than completely replace it.
- *Why D is incorrect:* In Python 3, `super()` with no arguments works correctly inside a class method. It automatically refers to the enclosing class. No arguments are needed.

---

### Question 5

Given this hierarchy:

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj = C()
```

Which of the following is `True`?

- A) `isinstance(obj, A)` is `False`
- B) `isinstance(obj, B)` is `True` but `isinstance(obj, A)` is `False`
- C) `isinstance(obj, A)`, `isinstance(obj, B)`, and `isinstance(obj, C)` are all `True`
- D) `type(obj) == A` is `True`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `isinstance(obj, A)` is `True` because `C` inherits from `B` which inherits from `A`. `obj` is an indirect instance of `A`.
- *Why B is incorrect:* `isinstance(obj, A)` is also `True`. `isinstance` checks the entire inheritance chain — `C` is a subclass of `B` which is a subclass of `A`.
- *Why C is correct:* `isinstance` returns `True` for the object's class and every class in its inheritance chain. `obj` is a `C`, which is a `B`, which is an `A`. All three checks return `True`.
- *Why D is incorrect:* `type(obj)` is `C`, not `A`. `type(obj) == A` is `False`. `type()` returns the exact runtime class, not any parent class.

---

### Question 6

What is the correct Method Resolution Order for this hierarchy?

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

- A) `object → Animal → Dog`
- B) `Dog → Animal → object`
- C) `Animal → Dog → object`
- D) `Dog → object → Animal`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python searches from most specific to most general — child first, then parent, then `object`. The reverse order (grandparent first) would mean the parent's methods always shadow the child's.
- *Why B is correct:* `Dog.__mro__` is `(Dog, Animal, object)`. Python always searches the most specific class first and works up the chain. This is why `Dog.speak()` is found before `Animal.speak()`.
- *Why C is incorrect:* `Animal` is not the starting point of the search. Python starts at the actual type of the object — `Dog` — and works up.
- *Why D is incorrect:* `object` is not between `Dog` and `Animal`. The MRO always ends with `object` as it is the root of all Python classes.

---

### Question 7

What is the output of this code?

```python
class Vehicle:
    def __init__(self, make):
        self.make = make

    def describe(self):
        return f'Vehicle: {self.make}'

class Car(Vehicle):
    def __init__(self, make, doors):
        super().__init__(make)
        self.doors = doors

    def describe(self):
        return f'{super().describe()} ({self.doors} doors)'

c = Car('Honda', 4)
print(c.describe())
```

- A) `Vehicle: Honda`
- B) `Honda (4 doors)`
- C) `Vehicle: Honda (4 doors)`
- D) `AttributeError` — make is not defined in Car

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Car.describe()` overrides `Vehicle.describe()`. The parent's version alone would only print `Vehicle: Honda`.
- *Why B is incorrect:* `Car.describe()` calls `super().describe()` which returns `'Vehicle: Honda'`, then appends `' (4 doors)'`. The make is included.
- *Why C is correct:* `super().__init__(make)` sets `self.make = 'Honda'`. `Car.describe()` calls `super().describe()` (returns `'Vehicle: Honda'`) and formats it into `'Vehicle: Honda (4 doors)'`.
- *Why D is incorrect:* `super().__init__(make)` in `Car.__init__` calls `Vehicle.__init__`, which sets `self.make`. The attribute exists on `c`.

---

### Question 8

Which statement about polymorphism in Python is correct?

- A) Polymorphism requires that all objects inherit from the same parent class
- B) Python's polymorphism works through duck typing — any object with the required method works
- C) Polymorphism only works with `isinstance()` checks to determine the type before calling the method
- D) Polymorphism requires explicit type declarations for the method parameter

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python uses duck typing. Any object that has the method being called works — there is no requirement for a shared parent class. You can pass a `Duck` object to a function that calls `.speak()` even if `Duck` does not inherit from `Animal`.
- *Why B is correct:* Duck typing means Python does not check the type — it just tries to call the method. If the method exists, it works. Objects of completely unrelated classes can be used interchangeably if they share the same method names.
- *Why C is incorrect:* Polymorphism specifically avoids type-checking. Calling `isinstance()` before every method call defeats the purpose. The loop just calls `.speak()` — no type check needed.
- *Why D is incorrect:* Python is dynamically typed and does not require type declarations. Method parameters accept any object.

---

### Question 9

What is the output of this code?

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Animal({self.name!r})'

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog('Rex', 'Labrador')
print(d)
print(d.name)
print(d.breed)
```

- A) `Animal('Rex')` then `Rex` then `Labrador`
- B) `Dog('Rex', 'Labrador')` then `Rex` then `Labrador`
- C) `<__main__.Dog object at 0x...>` then `Rex` then `Labrador`
- D) `AttributeError` — `__str__` is defined on Animal, not Dog

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `Dog` does not define `__str__`, so Python uses `Animal.__str__` (inherited). `Animal.__str__` returns `f'Animal({self.name!r})'` — it uses `self.name` which exists (set by `super().__init__(name)`). The output is `Animal('Rex')`. `d.name` and `d.breed` both exist.
- *Why B is incorrect:* `Dog` inherits `Animal.__str__` which formats as `Animal(name)`, not `Dog(name, breed)`. To get `Dog('Rex', 'Labrador')` you would need to define `__str__` in `Dog`.
- *Why C is incorrect:* `Animal.__str__` is inherited and works. The default memory address output only appears when no `__str__` or `__repr__` is defined anywhere in the MRO.
- *Why D is incorrect:* Inheritance means `Dog` has access to `Animal.__str__`. Methods defined on a parent class are fully accessible on child instances.

---

### Question 10

What is the output of this code?

```python
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f'Shape with area {self.area()}'

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

s = Square(4)
print(s.describe())
```

- A) `Shape with area 0`
- B) `Shape with area 16`
- C) `AttributeError` — `describe` is defined on Shape, not Square
- D) `TypeError` — `describe` does not know how to call `Square.area`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `s.describe()` calls `Shape.describe()` (inherited), which calls `self.area()`. Because `self` is a `Square` instance, `self.area()` calls `Square.area()` — not `Shape.area()`. This is polymorphism in action: even inside an inherited method, method calls on `self` use the actual runtime type.
- *Why B is correct:* `s.describe()` runs `Shape.describe()`. Inside that method, `self.area()` is called. `self` is a `Square`, so the MRO finds `Square.area()` first — which returns `4 ** 2 = 16`. The output is `Shape with area 16`.
- *Why C is incorrect:* `Square` inherits `describe()` from `Shape`. Inherited methods are fully accessible on instances of the child class.
- *Why D is incorrect:* Python does not check types before calling methods. `self.area()` works regardless of whether `area()` is defined on `Shape` or `Square` — Python finds the right one via the MRO.
