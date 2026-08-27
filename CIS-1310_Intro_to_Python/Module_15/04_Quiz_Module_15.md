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

---

### Question 11

What is the output of this code?

```python
class A:
    def method(self):
        return 'A'

class B(A):
    def method(self):
        return super().method() + 'B'

class C(B):
    def method(self):
        return super().method() + 'C'

print(C().method())
```

- A) `C`
- B) `BC`
- C) `ABC`
- D) `CBA`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `C.method()` calls `super().method()` which is `B.method()`. `B.method()` calls `super().method()` which is `A.method()`. The results are composed as each call returns.
- *Why B is incorrect:* The chain goes C → B → A. `A.method()` returns `'A'`. `B.method()` returns `'A' + 'B'` = `'AB'`. `C.method()` returns `'AB' + 'C'` = `'ABC'`.
- *Why C is correct:* Following the call chain: `A.method()` = `'A'`. `B.method()` = `super().method() + 'B'` = `'A' + 'B'` = `'AB'`. `C.method()` = `super().method() + 'C'` = `'AB' + 'C'` = `'ABC'`.
- *Why D is incorrect:* `'CBA'` would result if each level prepended instead of appended. The `+` in each method appends the letter after the parent's result.

---

### Question 12

What is the MRO for this class hierarchy?

```python
class X:
    pass

class Y(X):
    pass

class Z(Y, X):
    pass
```

- A) `Z → Y → X → object`
- B) `Z → X → Y → object`
- C) `X → Y → Z → object`
- D) `Z → Y → X → X → object` (X appears twice since Y inherits from X and Z inherits from X)

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Python's C3 linearization algorithm produces `Z → Y → X → object`. The leftmost base class (`Y`) comes before the rightmost (`X`), and duplicates are eliminated. Each class appears exactly once.
- *Why B is incorrect:* `X` would not come before `Y` — `Y` inherits from `X`, so `Y` must be searched before `X` to preserve the child-before-parent ordering.
- *Why C is incorrect:* Python searches from most specific to least specific — `Z` first, not `X` first.
- *Why D is incorrect:* The MRO never includes the same class twice. C3 linearization explicitly prevents this — `X` appears once in the final MRO.

---

### Question 13

What is the output of this code?

```python
class Base:
    def __init__(self):
        print('Base init')

class Child(Base):
    def __init__(self):
        super().__init__()
        print('Child init')

class GrandChild(Child):
    def __init__(self):
        super().__init__()
        print('GrandChild init')

GrandChild()
```

- A) `GrandChild init` then `Child init` then `Base init`
- B) `Base init` then `Child init` then `GrandChild init`
- C) `GrandChild init` only
- D) `Base init` then `GrandChild init`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `super().__init__()` calls the parent's `__init__` before the current class's print statement. The order is bottom-up in call ordering but top-down in execution because each class calls `super()` first.
- *Why B is correct:* `GrandChild.__init__` calls `super().__init__()` (Child) first. `Child.__init__` calls `super().__init__()` (Base) first. `Base.__init__` prints `'Base init'`, returns to `Child` which prints `'Child init'`, returns to `GrandChild` which prints `'GrandChild init'`.
- *Why C is incorrect:* `super().__init__()` calls are present and cause the parent classes' prints to execute.
- *Why D is incorrect:* `Child.__init__` is also called and prints `'Child init'` between `'Base init'` and `'GrandChild init'`.

---

### Question 14

What does `issubclass(Dog, Animal)` return, and what does `issubclass(Animal, Dog)` return, assuming `class Dog(Animal): pass`?

- A) `True` then `True`
- B) `True` then `False`
- C) `False` then `True`
- D) `False` then `False`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `issubclass(Animal, Dog)` is `False`. `Animal` does not inherit from `Dog` — the relationship is only one-directional.
- *Why B is correct:* `Dog` inherits from `Animal` → `issubclass(Dog, Animal)` is `True`. `Animal` does not inherit from `Dog` → `issubclass(Animal, Dog)` is `False`.
- *Why C is incorrect:* `issubclass(Dog, Animal)` is `True` because `Dog` inherits directly from `Animal`.
- *Why D is incorrect:* `issubclass(Dog, Animal)` is definitely `True` — `Dog` explicitly inherits from `Animal` in the class definition.

---

### Question 15

What is the output of this code?

```python
class Animal:
    sound = 'generic'

    def speak(self):
        return f'I say: {self.sound}'

class Dog(Animal):
    sound = 'Woof'

class Cat(Animal):
    sound = 'Meow'

animals = [Animal(), Dog(), Cat()]
for a in animals:
    print(a.speak())
```

- A) `I say: generic` three times
- B) `I say: generic` then `I say: Woof` then `I say: Meow`
- C) `I say: Woof` then `I say: Woof` then `I say: Woof`
- D) `TypeError` — `speak()` uses `self.sound` which is not defined per-instance

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Dog.sound` and `Cat.sound` are class variables that override `Animal.sound` for those classes. When `self.sound` is accessed on a `Dog` instance, Python finds `Dog.sound = 'Woof'` before `Animal.sound`.
- *Why B is correct:* `speak()` is inherited by all three classes. Inside `speak()`, `self.sound` resolves via the MRO of `self`'s actual type. `Animal` → `'generic'`, `Dog` → `'Woof'`, `Cat` → `'Meow'`.
- *Why C is incorrect:* Class variables are not shared downward. `Animal.sound` is `'generic'`, not `'Woof'`. And `Cat.sound` is `'Meow'`, not `'Woof'`.
- *Why D is incorrect:* `self.sound` resolves correctly via the class hierarchy. Class variables are accessible on instances. No `TypeError` is raised.

---

### Question 16

What is the output of this code?

```python
class Shape:
    def __init__(self, color='white'):
        self.color = color

class Circle(Shape):
    def __init__(self, radius, color='white'):
        super().__init__(color)
        self.radius = radius

c = Circle(5, 'red')
print(c.color)
print(c.radius)
print(isinstance(c, Shape))
```

- A) `white` then `5` then `True`
- B) `red` then `5` then `False`
- C) `red` then `5` then `True`
- D) `red` then `white` then `True`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Circle(5, 'red')` passes `color='red'` to both `Circle.__init__` and `super().__init__(color)`. `self.color` is set to `'red'`, not the default `'white'`.
- *Why B is incorrect:* `isinstance(c, Shape)` returns `True` because `Circle` inherits from `Shape`.
- *Why C is correct:* `super().__init__('red')` calls `Shape.__init__` with `color='red'`, setting `self.color = 'red'`. `self.radius = 5`. `isinstance(c, Shape)` is `True`.
- *Why D is incorrect:* `c.radius` is `5` (set in `Circle.__init__`), not `'white'`. The `color` default `'white'` is never used here because `'red'` was explicitly passed.

---

### Question 17

What is the purpose of `abc.abstractmethod` and abstract base classes?

- A) To make a class faster by preventing unnecessary inheritance
- B) To document that a method should be overridden, without enforcing it
- C) To declare a method that subclasses MUST override — instantiating the abstract class raises `TypeError`
- D) To create classes that cannot be used as parent classes

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Abstract base classes do not affect performance. They exist purely as a design enforcement mechanism.
- *Why B is incorrect:* Unlike docstrings or conventions, `@abstractmethod` is enforced at runtime. Attempting to instantiate a class with unimplemented abstract methods raises `TypeError`.
- *Why C is correct:* When a class inherits from `ABC` and uses `@abstractmethod`, Python prevents direct instantiation of the abstract class. Subclasses that do not implement all abstract methods also cannot be instantiated — until they do.
- *Why D is incorrect:* Abstract classes are specifically designed to be parent classes. Their purpose is to define a contract that child classes must fulfill.

---

### Question 18

What is the output of this code?

```python
class Vehicle:
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        return self

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        return self

    def __str__(self):
        return f'speed={self.speed}'

v = Vehicle()
print(v.accelerate(30).accelerate(20).brake(10))
```

- A) `speed=0`
- B) `speed=40`
- C) `speed=50`
- D) `TypeError` — cannot chain method calls that return `self`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The speed changes through the method chain. Starting at 0: `+30 = 30`, `+20 = 50`, `-10 = 40`.
- *Why B is correct:* Each method returns `self`. `v.accelerate(30)` → speed=30, returns `v`. `.accelerate(20)` → speed=50, returns `v`. `.brake(10)` → speed=40, returns `v`. `print(v)` calls `__str__` → `speed=40`.
- *Why C is incorrect:* The final `.brake(10)` reduces speed by 10: `50 - 10 = 40`.
- *Why D is incorrect:* Returning `self` from methods enables method chaining — a common pattern in Python (the builder pattern and fluent interface). This is valid Python.

---

### Question 19

What does `super().__init__()` call in this multiple-inheritance scenario?

```python
class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        super().__init__()
        print('B')

class C(A):
    def __init__(self):
        super().__init__()
        print('C')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D')

D()
```

- A) `A` then `B` then `D`
- B) `A` then `B` then `C` then `D`
- C) `A` then `C` then `B` then `D`
- D) `B` then `C` then `A` then `D`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The MRO for `D` is `D → B → C → A → object`. `super().__init__()` in `B` does not call `A.__init__()` directly — it calls the next class in the MRO, which is `C`. `C.__init__` then calls `A.__init__`.
- *Why B is incorrect:* `B` and `C` cannot both print in MRO order without `C` coming before `B`. Because each method calls `super()` first, the base class `A` prints first, then the call stack unwinds through `C` then `B` then `D`.
- *Why C is correct:* MRO: `D → B → C → A`. `D.__init__` calls `super()` → `B.__init__`. `B.__init__` calls `super()` → `C.__init__`. `C.__init__` calls `super()` → `A.__init__`. `A` prints `'A'` (no further super). Unwinding: `C` prints `'C'`, `B` prints `'B'`, `D` prints `'D'`. Output: `A C B D`.
- *Why D is incorrect:* `A` always prints first because it is at the bottom of the `super()` chain — the deepest call returns first. `B` does not print before `A`.

---

### Question 20

What is the output of this code?

```python
class Logger:
    def log(self, message):
        return f'[LOG] {message}'

class Saver:
    def save(self, data):
        return f'[SAVE] {data}'

class Service(Logger, Saver):
    def process(self, data):
        logged = self.log(data)
        saved = self.save(data)
        return f'{logged} | {saved}'

s = Service()
print(s.process('test'))
print(isinstance(s, Logger))
print(isinstance(s, Saver))
```

- A) `[LOG] test | [SAVE] test` then `True` then `False`
- B) `[LOG] test | [SAVE] test` then `True` then `True`
- C) `TypeError` — multiple inheritance is not allowed in Python
- D) `[LOG] test` then `True` then `False`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Service` inherits from both `Logger` and `Saver`. `isinstance(s, Saver)` is `True` — `Service` is a subclass of `Saver`.
- *Why B is correct:* `Service` inherits `log()` from `Logger` and `save()` from `Saver`. `s.process('test')` calls both, producing `'[LOG] test | [SAVE] test'`. `isinstance(s, Logger)` and `isinstance(s, Saver)` are both `True`.
- *Why C is incorrect:* Python explicitly supports multiple inheritance. `class Service(Logger, Saver):` is valid syntax and the MRO handles method resolution.
- *Why D is incorrect:* `process()` returns the combined string including both the log and save results. The full string is printed, not just the log portion.
