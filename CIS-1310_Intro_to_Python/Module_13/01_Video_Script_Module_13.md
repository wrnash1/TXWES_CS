# Video Script: CIS-1310 — Introduction to Python

## Module 13 — Modules and Packages

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - Show the `import math` vs `from math import sqrt` namespace difference live — this is an exam question.
> - Demonstrate the `__name__ == '__main__'` guard by running a file directly and then importing it.
> - Create a two-file custom module example so students see how splitting code across files works.
> - Run `pip install requests` and show the virtual environment workflow — students will encounter pip immediately in any real project.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 13 | Modules and Packages | CIS-1310"]**

"Welcome back. So far every program you have written has been a single file. As programs grow, a single file becomes unmanageable — thousands of lines of code, no organization, nothing reusable across projects.

Python solves this with modules and packages. A module is simply a `.py` file. A package is a directory of modules. Python ships with hundreds of ready-to-use modules in the standard library, and the pip package manager gives you access to hundreds of thousands more.

This module covers how to import and use modules, how to create your own, and how to install third-party packages with pip. These are everyday professional skills — and the import system is tested on the PCAP exam."

---

## [00:45 – 03:30] import — Three Ways to Import

**[SHOW SLIDE: "Three Forms of import"]**

"There are three forms of the import statement. Each one controls what names land in your namespace.

### Form 1: import module

**[DEMO — import module]**

```python
import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.141592653589793
print(math.floor(3.7))  # 3
```

This imports the `math` module and makes it available under the name `math`. Every name you use must be prefixed: `math.sqrt`, `math.pi`. This keeps your namespace clean — there is no risk of a name in `math` colliding with a name you defined yourself.

[PAUSE]

### Form 2: from module import name

**[DEMO — from module import name]**

```python
from math import sqrt, pi

print(sqrt(25))    # 5.0
print(pi)          # 3.141592653589793
```

This imports specific names directly into your current namespace. No prefix needed. But now `sqrt` and `pi` are local names — if you later define a variable called `sqrt`, you would shadow the imported function.

### Form 3: import as alias

**[DEMO — import as alias]**

```python
import math as m

print(m.sqrt(9))    # 3.0
```

```python
from math import factorial as fact

print(fact(5))    # 120
```

The `as` keyword creates an alias — a shorter name. You see this constantly in professional code: `import numpy as np`, `import pandas as pd`. The PCAP exam tests all three forms, including aliases.

[PAUSE]

**What about `from math import *`?**

```python
from math import *

print(sqrt(4))    # works
print(pi)         # works
```

This imports everything from the module — every public name — directly into your namespace. This is considered bad practice because you cannot tell where any name came from. If two modules both define a function called `log`, the second import silently overwrites the first. Avoid `import *` in production code."

---

## [03:30 – 05:30] Standard Library — Commonly Used Modules

**[SHOW SLIDE: "Python Standard Library — No Installation Needed"]**

"The standard library is built into Python. These modules are always available.

**[DEMO — math module]**

```python
import math

print(math.sqrt(144))       # 12.0
print(math.ceil(4.2))       # 5
print(math.floor(4.8))      # 4
print(math.log(100, 10))    # 2.0
print(math.pi)              # 3.141592653589793
print(math.e)               # 2.718281828459045
```

**[DEMO — random module]**

```python
import random

print(random.randint(1, 10))        # random int 1–10 inclusive
print(random.random())              # float in [0.0, 1.0)
print(random.choice(['a', 'b', 'c']))  # random element
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)                        # shuffled in place
```

**[DEMO — os module]**

```python
import os

print(os.getcwd())               # current working directory
print(os.path.exists('file.txt'))  # True or False
print(os.path.join('folder', 'file.txt'))  # 'folder/file.txt'
files = os.listdir('.')
print(files)                     # list of files in current directory
```

`os.path.join` is the right way to build file paths — it automatically uses the correct separator for the operating system.

**[DEMO — sys module]**

```python
import sys

print(sys.version)     # Python version string
print(sys.platform)    # 'linux', 'win32', 'darwin'
print(sys.path)        # list of directories Python searches for modules
sys.exit(0)            # terminate the program (status code 0 = success)
```

`sys.path` is the list of directories Python searches when you write `import something`. Python checks them left to right — the first match wins.

**[DEMO — datetime module]**

```python
from datetime import datetime, date

today = date.today()
print(today)                          # 2025-03-15

now = datetime.now()
print(now)                            # 2025-03-15 14:22:07.123456
print(now.strftime('%Y-%m-%d %H:%M'))  # formatted: '2025-03-15 14:22'
```"

---

## [05:30 – 08:00] Creating Your Own Modules

**[SHOW SLIDE: "Any .py file is a module"]**

"Any `.py` file you write is already a module. Other files can import from it.

**[DEMO — create two files]**

Create `greetings.py`:

```python
# greetings.py

def hello(name):
    return f'Hello, {name}!'

def goodbye(name):
    return f'Goodbye, {name}!'

GREETING_VERSION = '1.0'
```

Now create `main.py` in the same directory:

```python
# main.py

import greetings

print(greetings.hello('Alice'))
print(greetings.goodbye('Bob'))
print(greetings.GREETING_VERSION)
```

Run `main.py`:

```text
Hello, Alice!
Goodbye, Bob!
1.0
```

[PAUSE]

When you `import greetings`, Python executes the entire `greetings.py` file. Any function definitions, class definitions, and variable assignments at the top level of `greetings.py` run at import time, and the names become available under `greetings.name_here`.

**[DEMO — from greetings import hello]**

```python
from greetings import hello, GREETING_VERSION

print(hello('Carlos'))
print(GREETING_VERSION)
```

You can also import specific names. Only those two names land in your namespace.

**[DEMO — the .pyc cache]**

After running `main.py`, look in the directory:

```bash
ls __pycache__/
```

Python automatically compiles your module to bytecode (`.pyc` files) and caches them in `__pycache__/`. On subsequent imports, Python loads the bytecode cache instead of re-parsing the source file — this makes imports faster."

---

## [08:00 – 10:00] `__name__ == '__main__'` — The Module Guard

**[SHOW SLIDE: "`__name__` — Running vs Importing"]**

"Here is one of the most important Python patterns you will ever learn.

Every Python file has a special variable called `__name__`. Its value depends on how the file is being run:

- When you run the file directly: `__name__` equals `'__main__'`
- When the file is imported by another file: `__name__` equals the module's name (e.g., `'greetings'`)

This lets you write code that only runs when you execute the file directly — not when someone imports it.

**[DEMO — add the guard to greetings.py]**

```python
# greetings.py

def hello(name):
    return f'Hello, {name}!'

def goodbye(name):
    return f'Goodbye, {name}!'

GREETING_VERSION = '1.0'

if __name__ == '__main__':
    # This only runs when you do: python3 greetings.py
    # It does NOT run when main.py does: import greetings
    print('Testing greetings module:')
    print(hello('Test User'))
    print(goodbye('Test User'))
```

**[DEMO — run greetings.py directly]**

```bash
python3 greetings.py
```

```text
Testing greetings module:
Hello, Test User!
Goodbye, Test User!
```

**[DEMO — now import it from main.py]**

```python
import greetings    # the test block does NOT run
print(greetings.hello('Alice'))
```

```text
Hello, Alice!
```

[PAUSE]

The test block is invisible to importers. This is the standard professional pattern: functions and classes at the top level, test or demo code inside `if __name__ == '__main__':`. Every Python module you will ever read in the real world uses this pattern."

---

## [10:00 – 12:30] pip — Installing Third-Party Packages

**[SHOW SLIDE: "pip — Python's Package Installer"]**

"The Python standard library is powerful, but the real ecosystem is on PyPI — the Python Package Index. PyPI has over 500,000 packages. You install them with `pip`.

**[DEMO — check pip version]**

```bash
pip3 --version
```

**[DEMO — install a package]**

```bash
pip3 install requests
```

`requests` is a popular HTTP library — the most downloaded Python package ever. After installation, you can import it like any other module:

```python
import requests

response = requests.get('https://httpbin.org/get')
print(response.status_code)    # 200
print(type(response))          # <class 'requests.models.Response'>
```

**[DEMO — list installed packages]**

```bash
pip3 list
```

**[DEMO — uninstall a package]**

```bash
pip3 uninstall requests
```

**[DEMO — install a specific version]**

```bash
pip3 install requests==2.28.0
```

**Virtual environments — why they matter:**

By default, `pip install` puts packages in your system-wide Python installation. This causes a problem: Project A needs version 1.0 of a library, and Project B needs version 2.0. They conflict.

The solution is a virtual environment — an isolated Python installation per project.

**[DEMO — create and use a virtual environment]**

```bash
python3 -m venv myenv
source myenv/bin/activate
pip3 install requests
pip3 list
deactivate
```

Inside the activated environment, `pip install` only affects that project. When you `deactivate`, you return to the system Python. This is standard practice for all Python development."

---

## [12:30 – 14:30] dir() and help() — Exploring Modules

**[SHOW SLIDE: "dir() and help() — Interactive Documentation"]**

"Python gives you two built-in tools for exploring any module interactively.

**[DEMO — dir()]**

```python
import math

print(dir(math))
```

```text
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos',
 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb',
 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc',
 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan',
 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2',
 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians',
 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```

`dir(module)` returns a sorted list of every name defined in the module. This is how you discover what a module contains without reading the docs.

**[DEMO — help()]**

```python
help(math.sqrt)
```

```text
Help on built-in function sqrt in module math:

sqrt(x, /)
    Return the square root of x.
```

`help(name)` prints the docstring. Use `help(math)` for the full module, `help(math.sqrt)` for a specific function.

**[DEMO — dir() on any object]**

```python
s = 'hello'
print(dir(s))
```

`dir()` works on any Python object — strings, lists, custom classes. You used `dir` when exploring builtins in Module 9 as well."

---

## [14:30 – 15:30] PCAP Exam Tips and Wrap-Up

**[SHOW SLIDE: "Module 13 — PCAP Alignment"]**

"Key exam take-aways:

**1.** Three import forms: `import module`, `from module import name`, `import module as alias`. Know what each puts in your namespace and how you call it.

**2.** `from module import *` imports all public names. Avoid it in production — it pollutes the namespace and hides where names come from.

**3.** `__name__ == '__main__'` is `True` only when the file is run directly. It is `False` when the file is imported. Use this guard to separate reusable code from startup code.

**4.** `sys.path` is the list of directories Python searches for modules. When you create a custom module in the same directory as your script, that directory is on `sys.path` automatically.

**5.** `pip install package-name` installs from PyPI. `pip list` shows installed packages. Virtual environments isolate project dependencies.

**6.** `dir(module)` lists names. `help(name)` shows the docstring. Both work in the REPL and in scripts.

**7.** A package is a directory containing an `__init__.py` file. When you do `import package.module`, Python runs `__init__.py` first, then loads the submodule.

Module 14 covers object-oriented programming — classes, `__init__`, self, and encapsulation. The OOP modules are the most conceptually demanding material in this course, so come in prepared. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 13 — Modules and Packages]**

---

## Additional Resources

- [Python for Everybody — Dr. Charles Severance](https://www.py4e.com/book) — Chapter on reuse and modules
- [Official Python Docs — The import system](https://docs.python.org/3/reference/import.html) — authoritative reference
- [Official Python Docs — The Python Standard Library](https://docs.python.org/3/library/index.html) — complete standard library index
- [PyPI — Python Package Index](https://pypi.org) — search and browse third-party packages
- [Real Python — Python Modules and Packages](https://realpython.com/python-modules-packages/) — practical guide
