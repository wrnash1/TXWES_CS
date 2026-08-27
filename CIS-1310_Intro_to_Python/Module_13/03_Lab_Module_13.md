# Lab Activity: Module 13 — Modules and Packages

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 75–90 minutes

---

## Overview

In this lab you will practice all three import forms and observe their namespace effects, explore the standard library interactively with `dir()` and `help()`, create your own module and import it from a separate script, demonstrate the `__name__ == '__main__'` guard, install a third-party package with pip, create and use a virtual environment, and build a multi-module program that combines everything.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module13
cd module13
```

---

## Part 1 — Import Forms and Namespace Effects

```bash
python3
```

### Step 1.1 — import module (prefix required)

```python
>>> import math
>>> math.sqrt(144)
12.0
>>> math.pi
3.141592653589793
>>> math.factorial(5)
120
>>> sqrt(16)
```

```text
NameError: name 'sqrt' is not defined
```

`import math` puts only the name `math` in your namespace. Everything inside must be accessed with the `math.` prefix.

### Step 1.2 — from module import name (no prefix)

```python
>>> from math import sqrt, pi, factorial
>>> sqrt(25)
5.0
>>> pi
3.141592653589793
>>> factorial(6)
720
>>> math.sqrt(9)
```

```text
NameError: name 'math' is not defined
```

`from math import sqrt` does NOT import `math` itself — only the listed names.

### Step 1.3 — import as alias

```python
>>> import math as m
>>> m.sqrt(36)
6.0
>>> from math import factorial as fact
>>> fact(7)
5040
```

### Step 1.4 — Confirm namespace with dir()

```python
>>> import math as m2
>>> 'math' in dir()
False
>>> 'm2' in dir()
True
```

The alias name lands in namespace, not the original module name.

### Step 1.5 — Star import and namespace pollution

```python
>>> from math import *
>>> sqrt(4)
2.0
>>> ceil(3.1)
4
>>> dir()
```

Note how many names are now in your namespace. This is why star import is avoided — you lose track of where everything came from.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the `NameError` from Step 1.1 (sqrt without prefix), the `NameError` from Step 1.2 (math not imported), and the alias usage from Step 1.3. Save as `lab13_screenshot_01_import_forms.png`.

---

## Part 2 — Exploring Modules with dir() and help()

```bash
python3
```

### Step 2.1 — dir() on a module

```python
>>> import random
>>> dir(random)
```

```text
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
 'SystemRandom', 'TWOPI', '_Sequence', '__all__', '__builtins__', '__cached__',
 '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss',
 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate',
 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate',
 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
```

### Step 2.2 — help() on a function

```python
>>> help(random.randint)
```

```text
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
```

### Step 2.3 — random module demos

```python
>>> random.randint(1, 10)
7
>>> random.random()
0.6394267984578837
>>> random.choice(['red', 'green', 'blue'])
'green'
>>> items = [1, 2, 3, 4, 5]
>>> random.shuffle(items)
>>> items
[3, 1, 5, 2, 4]
>>> result = random.shuffle(items)
>>> print(result)
None
```

`random.shuffle()` modifies the list in place and returns `None`. Assigning the return value is a common mistake.

### Step 2.4 — sys module

```python
>>> import sys
>>> sys.version
'3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]'
>>> sys.platform
'linux'
>>> sys.path[:3]
['', '/usr/lib/python310.zip', '/usr/lib/python3.10']
```

The empty string `''` at the beginning of `sys.path` means the current directory is searched first.

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing `dir(random)` output, `help(random.randint)` output, and the `random.shuffle()` returning `None` demo. Save as `lab13_screenshot_02_dir_help.png`.

---

## Part 3 — Creating a Custom Module

### Step 3.1 — Write the module file

```bash
nano geometry.py
```

```python
# geometry.py
# Geometry utility module
# Module 13 Lab — CIS-1310

import math


def circle_area(radius):
    '''Return the area of a circle with given radius.'''
    if radius < 0:
        raise ValueError(f'Radius cannot be negative: {radius}')
    return math.pi * radius ** 2


def circle_circumference(radius):
    '''Return the circumference of a circle with given radius.'''
    return 2 * math.pi * radius


def rectangle_area(width, height):
    '''Return the area of a rectangle.'''
    return width * height


def rectangle_perimeter(width, height):
    '''Return the perimeter of a rectangle.'''
    return 2 * (width + height)


def triangle_area(base, height):
    '''Return the area of a triangle.'''
    return 0.5 * base * height


SHAPE_NAMES = ['circle', 'rectangle', 'triangle']


if __name__ == '__main__':
    print('Testing geometry module:')
    print(f'  Circle area (r=5): {circle_area(5):.4f}')
    print(f'  Rectangle area (4x6): {rectangle_area(4, 6)}')
    print(f'  Triangle area (base=10, h=3): {triangle_area(10, 3)}')
```

Save (`Ctrl+O`, `Enter`, `Ctrl+X`).

### Step 3.2 — Test the module guard

Run the file directly — the test block should execute:

```bash
python3 geometry.py
```

```text
Testing geometry module:
  Circle area (r=5): 78.5398
  Rectangle area (4x6): 24
  Triangle area (base=10, h=3): 15.0
```

### Step 3.3 — Import the module from the REPL

```bash
python3
```

```python
>>> import geometry
```

No test output — the `if __name__ == '__main__':` block does not run during import.

```python
>>> geometry.circle_area(7)
153.93804002589985
>>> geometry.rectangle_perimeter(3, 4)
14
>>> geometry.SHAPE_NAMES
['circle', 'rectangle', 'triangle']
>>> from geometry import triangle_area
>>> triangle_area(8, 5)
20.0
>>> help(geometry.circle_area)
```

```text
Help on function circle_area in module geometry:

circle_area(radius)
    Return the area of a circle with given radius.
```

```python
>>> exit()
```

> **SCREENSHOT 3 REQUIRED:** Screenshot showing `python3 geometry.py` running the test block, then the REPL import session showing `geometry.circle_area(7)` and `help(geometry.circle_area)`. Save as `lab13_screenshot_03_custom_module.png`.

---

## Part 4 — pip and Virtual Environments

### Step 4.1 — Check pip

```bash
pip3 --version
pip3 list
```

### Step 4.2 — Install a package

```bash
pip3 install colorama
```

`colorama` is a small library that makes terminal text colorful. Verify it installed:

```bash
pip3 show colorama
```

```text
Name: colorama
Version: 0.4.6
Summary: Cross-platform colored terminal text.
...
```

Test it:

```bash
python3
```

```python
>>> from colorama import Fore, Style
>>> print(Fore.RED + 'This is red text' + Style.RESET_ALL)
This is red text
>>> print(Fore.GREEN + 'This is green text' + Style.RESET_ALL)
This is green text
>>> exit()
```

### Step 4.3 — Create and activate a virtual environment

```bash
python3 -m venv labenv
source labenv/bin/activate
```

Your prompt changes to show `(labenv)` — you are now inside the isolated environment.

```bash
pip3 list
```

The list is nearly empty — only `pip` and `setuptools` are pre-installed. The system packages (including `colorama`) are not visible here.

### Step 4.4 — Install into the virtual environment

```bash
pip3 install colorama
pip3 list
```

Now `colorama` is installed in `labenv` only.

### Step 4.5 — Generate requirements.txt

```bash
pip3 freeze > requirements.txt
cat requirements.txt
```

```text
colorama==0.4.6
```

This file captures the exact package versions for reproducibility.

### Step 4.6 — Deactivate

```bash
deactivate
```

Your prompt returns to normal. The `colorama` installed in `labenv` is no longer on the Python path.

> **SCREENSHOT 4 REQUIRED:** Screenshot showing the `pip3 install colorama` command, the colorama color demo in the REPL, the virtual environment activation, and `pip3 freeze` output. Save as `lab13_screenshot_04_pip_venv.png`.

---

## Part 5 — module_demo.py (Standard Library Showcase)

```bash
nano module_demo.py
```

```python
# module_demo.py
# Demonstrates standard library modules: math, random, os, sys, datetime
# Module 13 Lab — CIS-1310

import math
import random
import os
import sys
from datetime import datetime, date, timedelta


def math_demos():
    print('=== math module ===')
    print(f'  math.sqrt(2)       = {math.sqrt(2):.6f}')
    print(f'  math.ceil(4.1)     = {math.ceil(4.1)}')
    print(f'  math.floor(4.9)    = {math.floor(4.9)}')
    print(f'  math.factorial(8)  = {math.factorial(8)}')
    print(f'  math.log(100, 10)  = {math.log(100, 10):.1f}')
    print(f'  math.pi            = {math.pi:.10f}')
    print()


def random_demos():
    random.seed(42)    # fixed seed for reproducible output
    print('=== random module (seed=42) ===')
    print(f'  randint(1, 100)    = {random.randint(1, 100)}')
    print(f'  random()           = {random.random():.6f}')
    print(f'  choice(colors)     = {random.choice(["red","green","blue"])}')
    sample = random.sample(range(1, 50), 6)
    print(f'  sample(1-49, 6)    = {sample}')
    lst = list(range(1, 6))
    random.shuffle(lst)
    print(f'  shuffle([1-5])     = {lst}')
    print()


def os_demos():
    print('=== os module ===')
    print(f'  getcwd()           = {os.getcwd()}')
    files = os.listdir('.')
    print(f'  listdir (count)    = {len(files)} files/dirs')
    print(f'  path.exists(.)     = {os.path.exists(".")}')
    print(f'  path.join          = {os.path.join("data", "output", "results.csv")}')
    name = 'module_demo.py'
    stem, ext = os.path.splitext(name)
    print(f'  splitext           = stem={stem!r}, ext={ext!r}')
    print()


def datetime_demos():
    print('=== datetime module ===')
    today = date.today()
    print(f'  date.today()       = {today}')
    now = datetime.now()
    print(f'  datetime.now()     = {now.strftime("%Y-%m-%d %H:%M:%S")}')
    next_week = today + timedelta(days=7)
    print(f'  today + 7 days     = {next_week}')
    birthday = datetime(1990, 6, 15)
    age_days = (datetime.now() - birthday).days
    print(f'  days since 1990-06-15 = {age_days}')
    print()


def sys_demos():
    print('=== sys module ===')
    print(f'  sys.version        = {sys.version.split()[0]}')
    print(f'  sys.platform       = {sys.platform}')
    print(f'  sys.path[0]        = {sys.path[0]!r}')
    print(f'  sys.path entries   = {len(sys.path)}')
    print()


if __name__ == '__main__':
    math_demos()
    random_demos()
    os_demos()
    datetime_demos()
    sys_demos()
```

Save and run:

```bash
python3 module_demo.py
```

Expected output:

```text
=== math module ===
  math.sqrt(2)       = 1.414214
  math.ceil(4.1)     = 5
  math.floor(4.9)    = 4
  math.factorial(8)  = 40320
  math.log(100, 10)  = 2.0
  math.pi            = 3.1415926536

=== random module (seed=42) ===
  randint(1, 100)    = 52
  random()           = 0.639427
  choice(colors)     = blue
  sample(1-49, 6)    = [38, 27, 43, 3, 9, 49]
  shuffle([1-5])     = [4, 1, 3, 5, 2]

=== os module ===
  getcwd()           = /home/student/cis1310/module13
  listdir (count)    = 5 files/dirs
  path.exists(.)     = True
  path.join          = data/output/results.csv
  splitext           = stem='module_demo', ext='.py'

=== datetime module ===
  date.today()       = 2025-03-15
  datetime.now()     = 2025-03-15 14:22:07
  today + 7 days     = 2025-03-22
  days since 1990-06-15 = 12692

=== sys module ===
  sys.version        = 3.10.12
  sys.platform       = linux
  sys.path[0]        = ''
  sys.path entries   = 8
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `module_demo.py` running and showing the complete output. Save as `lab13_screenshot_05_module_demo.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 13 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab13_screenshot_01_import_forms.png` | NameError without prefix, NameError when module not imported, alias usage |
| 2 | `lab13_screenshot_02_dir_help.png` | dir(random), help(random.randint), shuffle returning None |
| 3 | `lab13_screenshot_03_custom_module.png` | geometry.py direct run, REPL import session |
| 4 | `lab13_screenshot_04_pip_venv.png` | pip install, colorama demo, virtual environment workflow |
| 5 | `lab13_screenshot_05_module_demo.png` | module_demo.py complete output |

---

## Part 9 — Challenge Exercise

These steps are optional and ungraded. They extend module concepts to real packaging and introspection patterns.

### Step 9.1 — Introspect a Standard Library Module

Use Python's built-in introspection tools (`dir()`, `help()`, `inspect`, and `sys.modules`) to explore a module's contents, understand what was loaded, and locate source files.

```bash
python3
```

```python
>>> import math
>>> import inspect
>>> import sys

# What is math's source?
>>> print(math.__file__)

# List all public names
>>> public = [name for name in dir(math) if not name.startswith('_')]
>>> print(len(public), 'public names:', public[:8], '...')

# Find all callables (functions)
>>> funcs = [name for name in public if callable(getattr(math, name))]
>>> print('Functions:', funcs)

# Get signature of a function
>>> print(inspect.signature(math.log))

# Confirm the module is cached
>>> print('math in sys.modules:', 'math' in sys.modules)
>>> print('Same object:', sys.modules['math'] is math)
```

Observe that `math.__file__` ends with `.so` or `.pyd` (compiled C extension) on most platforms — meaning `math` is not a pure Python file. Compare with a pure Python module like `random`:

```python
>>> import random
>>> print(random.__file__)
```

Exit the REPL: `exit()`

### Step 9.2 — Build a Multi-Module Package with `__init__.py`

Create a small package named `shapes` with two submodules and a public API defined in `__init__.py`.

```bash
mkdir shapes
```

```bash
nano shapes/__init__.py
```

```python
# shapes/__init__.py
# Public API for the shapes package

from shapes.circle import Circle
from shapes.rectangle import Rectangle

__all__ = ['Circle', 'Rectangle']
__version__ = '1.0.0'
```

```bash
nano shapes/circle.py
```

```python
# shapes/circle.py
import math


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f'Radius must be positive, got {radius}')
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f'Circle(radius={self.radius})'
```

```bash
nano shapes/rectangle.py
```

```python
# shapes/rectangle.py


class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError('Dimensions must be positive')
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
```

```bash
nano test_shapes.py
```

```python
# test_shapes.py
from shapes import Circle, Rectangle, __version__

print(f'shapes package version: {__version__}')

c = Circle(5)
print(f'{c}: area={c.area():.2f}, perimeter={c.perimeter():.2f}')

r = Rectangle(4, 6)
print(f'{r}: area={r.area()}, perimeter={r.perimeter()}, square={r.is_square()}')

sq = Rectangle(5, 5)
print(f'{sq}: square={sq.is_square()}')

# Verify ValueError
try:
    bad = Circle(-1)
except ValueError as e:
    print(f'Caught: {e}')
```

```bash
python3 test_shapes.py
```

### Step 9.3 — Inspect sys.path and Add a Module at Runtime

Understand how Python resolves imports by inspecting and modifying `sys.path` at runtime.

```bash
nano path_demo.py
```

```python
# path_demo.py
import sys
import os

print('Current sys.path:')
for i, p in enumerate(sys.path):
    print(f'  [{i}] {p!r}')

# Create a temporary directory and module at runtime
import tempfile

tmpdir = tempfile.mkdtemp()
module_path = os.path.join(tmpdir, 'greetings.py')

with open(module_path, 'w') as f:
    f.write("def hello(name): return f'Hello from temp dir, {name}!'\n")
    f.write("GREETING = 'Hi!'\n")

print(f'\nCreated temp module at: {module_path}')

# Add tmpdir to sys.path so Python can find 'greetings'
sys.path.insert(0, tmpdir)

import greetings
print(f'Imported: {greetings.__file__}')
print(greetings.hello('Alice'))
print(f'GREETING = {greetings.GREETING!r}')

# Demonstrate that sys.modules caches it
print(f'\ngreetings in sys.modules: {"greetings" in sys.modules}')

# Clean up
import shutil
shutil.rmtree(tmpdir)
print('Temp directory cleaned up.')
```

```bash
python3 path_demo.py
```

Observe that inserting at index 0 of `sys.path` gives the highest priority — it is checked before the standard library. This is how local modules can shadow standard library names (and why you should never name your files `math.py`, `random.py`, etc.).

---

## Troubleshooting Guide

**`ModuleNotFoundError: No module named 'geometry'`**
Your custom module file must be in the same directory as the script that imports it, or in a directory on `sys.path`. Run `ls` to confirm `geometry.py` exists in the current directory, and run `python3` from that same directory.

**`from math import sqrt` then `math.sqrt(4)` raises `NameError`.**
`from math import sqrt` only imports the name `sqrt` — not `math` itself. If you need both forms, use `import math` and `from math import sqrt` together, or just use `import math` consistently.

**`random.shuffle()` returns `None` — list is not shuffled.**
`shuffle` modifies the list in place. The return value is always `None`. Use the list variable itself after calling `shuffle`, not the return value.

**Virtual environment not activating — `source myenv/bin/activate` fails.**
Confirm the virtual environment was created with `python3 -m venv myenv`. If the directory exists, try `ls myenv/bin/` — you should see `activate`. If using Windows (outside the VM), the command is `myenv\Scripts\activate`.

**pip3 not found.**
On Ubuntu, `pip3` is the Python 3 pip. Install it with: `sudo apt install python3-pip`.
