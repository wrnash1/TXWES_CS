# Lab Activity: Module 16 — Final Exam Prep and PCAP Certification Review

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 90–120 minutes

---

## Overview

This is the capstone lab for CIS-1310. You will write a complete multi-module Python program that integrates the major skills from every module: data structures, functions and scope, exception handling, OOP with inheritance, and file-like output formatting. This lab is a final self-assessment — if you can build this program from scratch, you are ready for the PCAP exam.

The second part of this lab covers scheduling your PCAP certification exam.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.
- All previous lab screenshots available for review.

---

## Setup

```bash
cd ~/cis1310
mkdir module16
cd module16
```

---

## Part 1 — Exam Trap Verification (REPL review)

Open the REPL and trace each trap from the reading guide. Write down the output before running each — then verify.

```bash
python3
```

### Step 1.1 — Arithmetic traps

```python
>>> -7 // 2
-4
>>> -2 ** 2
-4
>>> (-2) ** 2
4
>>> 7 % 3
1
>>> -7 % 3
2
```

### Step 1.2 — Truthiness traps

```python
>>> bool('0')
True
>>> bool('')
False
>>> bool([])
False
>>> bool(0)
False
>>> bool('False')
True
```

### Step 1.3 — String method traps

```python
>>> 'a  b  c'.split(' ')
['a', '', 'b', '', 'c']
>>> 'a  b  c'.split()
['a', 'b', 'c']
>>> '-'.join(['a', 'b', 'c'])
'a-b-c'
>>> s = '  hello  '
>>> s.strip()
'hello'
>>> s
'  hello  '
```

`s.strip()` on its own does nothing to `s` — immutability.

### Step 1.4 — List traps

```python
>>> lst = [3, 1, 2]
>>> result = lst.sort()
>>> print(result)
None
>>> lst
[1, 2, 3]
>>> import random
>>> items = [1, 2, 3, 4, 5]
>>> r = random.shuffle(items)
>>> print(r)
None
>>> items
[4, 1, 3, 5, 2]
```

Both `.sort()` and `random.shuffle()` return `None` — they modify in place.

### Step 1.5 — Tuple trap

```python
>>> t1 = (1)
>>> type(t1)
<class 'int'>
>>> t2 = (1,)
>>> type(t2)
<class 'tuple'>
```

### Step 1.6 — Set vs dict trap

```python
>>> d = {}
>>> type(d)
<class 'dict'>
>>> s = set()
>>> type(s)
<class 'set'>
>>> s2 = {1, 2, 3}
>>> type(s2)
<class 'set'>
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the arithmetic traps (Step 1.1), truthiness results (Step 1.2), and the string immutability trap (Step 1.3). Save as `lab16_screenshot_01_traps.png`.

---

## Part 2 — OOP and Inheritance Verification (REPL review)

```bash
python3
```

### Step 2.1 — `super().__init__()` — both with and without

```python
>>> class Animal:
...     def __init__(self, name):
...         self.name = name
...
>>> class GoodDog(Animal):
...     def __init__(self, name, breed):
...         super().__init__(name)
...         self.breed = breed
...
>>> class BadDog(Animal):
...     def __init__(self, name, breed):
...         self.breed = breed   # missing super().__init__()
...
>>> g = GoodDog('Rex', 'Lab')
>>> g.name
'Rex'
>>> b = BadDog('Luna', 'Beagle')
>>> b.breed
'Beagle'
>>> b.name
```

```text
AttributeError: 'BadDog' object has no attribute 'name'
```

### Step 2.2 — isinstance() across hierarchy

```python
>>> isinstance(g, GoodDog)
True
>>> isinstance(g, Animal)
True
>>> isinstance(g, object)
True
>>> type(g) == Animal
False
```

### Step 2.3 — Polymorphism

```python
>>> class Cat(Animal):
...     def speak(self): return f'{self.name}: Meow!'
...
>>> class Dog(Animal):
...     def speak(self): return f'{self.name}: Woof!'
...
>>> animals = [Dog('Rex'), Cat('Whiskers'), Dog('Luna')]
>>> for a in animals:
...     print(a.speak())
...
Rex: Woof!
Whiskers: Meow!
Luna: Woof!
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing the `AttributeError` from missing `super().__init__()` (Step 2.1), `isinstance()` results (Step 2.2), and the polymorphic loop (Step 2.3). Save as `lab16_screenshot_02_oop.png`.

---

## Part 3 — capstone.py (Full Integration Program)

This program integrates: a class hierarchy, exception handling, dictionary accumulation, list operations, and formatted output.

```bash
nano capstone.py
```

```python
# capstone.py
# Capstone program for CIS-1310 — integrates all major topics
# Module 16 Lab

import math
import random


# ── OOP Hierarchy ──────────────────────────────────────────────

class Shape:
    '''Abstract base for shapes.'''

    def __init__(self, color='black'):
        self.color = color

    def area(self):
        raise NotImplementedError(
            f'{type(self).__name__} must implement area()'
        )

    def describe(self):
        return (f'{type(self).__name__}(color={self.color!r}, '
                f'area={self.area():.4f})')

    def __str__(self):
        return self.describe()


class Circle(Shape):
    def __init__(self, radius, color='black'):
        super().__init__(color)
        if radius <= 0:
            raise ValueError(f'Radius must be positive, got {radius}')
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height, color='black'):
        super().__init__(color)
        if width <= 0 or height <= 0:
            raise ValueError('Dimensions must be positive')
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side, color='black'):
        super().__init__(side, side, color)
        self.side = side

    def describe(self):
        return (f'Square(side={self.side}, color={self.color!r}, '
                f'area={self.area():.4f})')


# ── Functions ──────────────────────────────────────────────────

def total_area(shapes):
    '''Return sum of areas.'''
    return sum(s.area() for s in shapes)


def classify_shapes(shapes):
    '''Return a dict mapping class name to count.'''
    counts = {}
    for s in shapes:
        key = type(s).__name__
        counts[key] = counts.get(key, 0) + 1
    return counts


def largest_and_smallest(shapes):
    '''Return (largest, smallest) by area. Raises ValueError if empty.'''
    if not shapes:
        raise ValueError('Cannot find extremes of empty list')
    largest = max(shapes, key=lambda s: s.area())
    smallest = min(shapes, key=lambda s: s.area())
    return largest, smallest


def safe_create_circle(radius, color='black'):
    '''Create a Circle, catching ValueError for invalid radius.'''
    try:
        return Circle(radius, color)
    except ValueError as e:
        print(f'  [Warning] Could not create circle: {e}')
        return None


# ── Main ───────────────────────────────────────────────────────

if __name__ == '__main__':
    random.seed(7)

    # Build a collection of shapes
    raw = [
        Circle(5, 'red'),
        Rectangle(4, 6, 'blue'),
        Square(3, 'green'),
        Circle(2, 'yellow'),
        Rectangle(10, 2, 'purple'),
        Square(7),
        safe_create_circle(-1),     # invalid — returns None
        safe_create_circle(1.5, 'orange'),
    ]

    # Filter out None results from failed creations
    shapes = [s for s in raw if s is not None]

    print('=== All Shapes ===')
    for s in shapes:
        print(f'  {s}')
    print()

    print('=== isinstance() checks ===')
    sq = Square(4)
    print(f'Square is Rectangle: {isinstance(sq, Rectangle)}')
    print(f'Square is Shape:     {isinstance(sq, Shape)}')
    print(f'Square is Circle:    {isinstance(sq, Circle)}')
    print()

    print('=== Classification ===')
    counts = classify_shapes(shapes)
    for name, count in sorted(counts.items()):
        print(f'  {name}: {count}')
    print()

    print(f'=== Total area: {total_area(shapes):.4f} ===')
    big, small = largest_and_smallest(shapes)
    print(f'Largest:  {big}')
    print(f'Smallest: {small}')
    print()

    print('=== Exception handling ===')
    try:
        largest_and_smallest([])
    except ValueError as e:
        print(f'  Caught: {e}')

    try:
        s = Shape()
        s.area()
    except NotImplementedError as e:
        print(f'  Caught: {e}')
    print()

    print('=== Standard library demos ===')
    print(f'  math.pi  = {math.pi:.6f}')
    print(f'  math.e   = {math.e:.6f}')
    radii = [random.uniform(1, 10) for _ in range(5)]
    areas = [math.pi * r ** 2 for r in radii]
    print(f'  5 random radii: {[round(r, 2) for r in radii]}')
    print(f'  their areas:    {[round(a, 2) for a in areas]}')
    print()

    print('=== MRO for Square ===')
    for cls in Square.__mro__:
        print(f'  {cls.__name__}')
```

Save and run:

```bash
python3 capstone.py
```

Expected output (random values will match due to seed):

```text
  [Warning] Could not create circle: Radius must be positive, got -1

=== All Shapes ===
  Circle(color='red', area=78.5398)
  Rectangle(color='blue', area=24.0000)
  Square(side=3, color='green', area=9.0000)
  Circle(color='yellow', area=12.5664)
  Rectangle(color='purple', area=20.0000)
  Square(side=7, color='black', area=49.0000)
  Circle(color='orange', area=7.0686)

=== isinstance() checks ===
Square is Rectangle: True
Square is Shape:     True
Square is Circle:    False

=== Classification ===
  Circle: 3
  Rectangle: 2
  Square: 2

=== Total area: 200.2748 ===
Largest:  Circle(color='red', area=78.5398)
Smallest: Circle(color='orange', area=7.0686)

=== Exception handling ===
  Caught: Cannot find extremes of empty list
  Caught: Shape must implement area()

=== Standard library demos ===
  math.pi  = 3.141593
  math.e   = 2.718282
  5 random radii: [...]
  their areas:    [...]

=== MRO for Square ===
  Square
  Rectangle
  Shape
  object
```

> **SCREENSHOT 3 REQUIRED:** Screenshot of `capstone.py` running and showing the complete output. Save as `lab16_screenshot_03_capstone.png`.

---

## Part 4 — review_quiz.py (Self-Test)

This program quizzes you interactively on PCAP exam traps.

```bash
nano review_quiz.py
```

```python
# review_quiz.py
# Interactive self-quiz on PCAP exam traps
# Module 16 Lab — CIS-1310

QUESTIONS = [
    {
        'q': 'What is the result of -7 // 2?',
        'a': '-4',
        'hint': 'Floor division rounds toward negative infinity.'
    },
    {
        'q': 'What is the result of -2 ** 2?',
        'a': '-4',
        'hint': '** binds tighter than unary minus. Use (-2)**2 for 4.'
    },
    {
        'q': 'What does bool("0") return?',
        'a': 'True',
        'hint': 'Non-empty strings are truthy. Only "" is falsy.'
    },
    {
        'q': 'What does list.sort() return?',
        'a': 'None',
        'hint': '.sort() modifies in place and returns None. Use sorted() for a new list.'
    },
    {
        'q': 'What type does (1) produce?',
        'a': 'int',
        'hint': 'A single-element tuple requires a trailing comma: (1,)'
    },
    {
        'q': 'What does {} create — dict or set?',
        'a': 'dict',
        'hint': 'Use set() for an empty set. {1,2,3} is a set, {} is a dict.'
    },
    {
        'q': 'Which clause runs ONLY when no exception occurred in try?',
        'a': 'else',
        'hint': 'else runs on success. finally runs always. except runs on error.'
    },
    {
        'q': 'What does bare raise do inside an except block?',
        'a': 're-raises',
        'hint': 'Bare raise re-raises the current exception with original traceback.'
    },
]


def run_quiz(questions):
    score = 0
    wrong = []

    print('=== PCAP Self-Quiz ===')
    print('Type your answer and press Enter. Type "hint" for a clue.\n')

    for i, q in enumerate(questions, 1):
        print(f'Q{i}: {q["q"]}')
        while True:
            answer = input('  Your answer: ').strip().lower()
            if answer == 'hint':
                print(f'  Hint: {q["hint"]}')
                continue
            break

        correct = q['a'].lower()
        if answer == correct or answer in correct or correct in answer:
            print('  Correct!\n')
            score += 1
        else:
            print(f'  Incorrect. Answer: {q["a"]}')
            print(f'  Hint: {q["hint"]}\n')
            wrong.append(q)

    print(f'=== Result: {score}/{len(questions)} ===')
    if wrong:
        print('\nReview these topics:')
        for q in wrong:
            print(f'  - {q["q"]}')
            print(f'    {q["hint"]}')


if __name__ == '__main__':
    run_quiz(QUESTIONS)
```

Save and run:

```bash
python3 review_quiz.py
```

Work through all 8 questions. Use the `hint` command if needed. Aim for 8/8 before moving on.

> **SCREENSHOT 4 REQUIRED:** Screenshot of `review_quiz.py` running and showing at least 5 questions answered (including your score). Save as `lab16_screenshot_04_quiz.png`.

---

## Part 5 — PCAP Exam Scheduling

The PCAP exam (Certified Associate in Python Programming) is administered by the Python Institute.

### Step 5.1 — Verify eligibility

You have completed all 16 modules of CIS-1310 and are ready to schedule. Review the PCAP exam page at [pythoninstitute.org/pcap](https://pythoninstitute.org/pcap) for current pricing and scheduling options.

### Step 5.2 — Exam format

- **Length:** 40 questions, 65 minutes
- **Passing score:** 70% (28 of 40 questions)
- **Question types:** single-choice, multiple-choice, gap-fill, code output
- **Topics:** All content from Modules 1–15 of this course

### Step 5.3 — Schedule your exam

Follow the Python Institute's current scheduling process to register. The exam is available online with a remote proctor or at a testing center.

> **SCREENSHOT 5 REQUIRED:** Screenshot of your PCAP exam confirmation email or exam results page showing your name and score. Submit to the Canvas Module 16 Lab Assignment. Save as `lab16_screenshot_05_pcap_result.png`.

If your exam is scheduled but not yet completed, submit a screenshot of your registration confirmation as a placeholder. Your final grade for this assignment will be updated when your results are submitted.

---

## Deliverables

Upload all 5 screenshots (or 4 screenshots + exam confirmation) to Canvas.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab16_screenshot_01_traps.png` | Arithmetic, truthiness, and string immutability traps |
| 2 | `lab16_screenshot_02_oop.png` | AttributeError from missing `super().__init__()`, isinstance(), polymorphism |
| 3 | `lab16_screenshot_03_capstone.png` | capstone.py complete output |
| 4 | `lab16_screenshot_04_quiz.png` | review_quiz.py session showing score |
| 5 | `lab16_screenshot_05_pcap_result.png` | PCAP exam result or registration confirmation |

---

## Troubleshooting Guide

**`capstone.py` fails with `NotImplementedError`.**
Make sure you have all three concrete classes defined (`Circle`, `Rectangle`, `Square`). The `Shape` base class intentionally raises `NotImplementedError` — only instantiate the concrete subclasses.

**`review_quiz.py` answer matching seems loose.**
The quiz uses `in` for matching, so partial answers are accepted. For the actual PCAP exam, exact answers are required — use this quiz for recall practice, not as a measure of exam readiness.

**PCAP exam registration issues.**
Contact the Python Institute directly at their official website. Texas Wesleyan University may have a voucher program — check with Professor Nash for current student pricing before registering at full price.
