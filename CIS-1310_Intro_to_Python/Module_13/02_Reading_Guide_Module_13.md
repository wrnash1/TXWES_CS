# Reading Guide: Module 13 — Modules and Packages

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 13 — Modules and Packages**. Every large Python program is split across multiple files. The module system is how Python lets you organize code, reuse it across projects, and pull in the enormous ecosystem of third-party libraries. The PCAP exam tests the exact syntax of all three import forms, what each puts in your namespace, the `__name__ == '__main__'` guard, and the relationship between packages and directories. Understanding modules is also the foundation for every topic that follows — file handling, OOP, and real-world library use all rely on imports.

---

## 1. High-Yield Glossary

### Module

A single `.py` file. Any Python file is automatically a module — it can be imported by other files. The module's name is the filename without the `.py` extension.

```python
# mymodule.py
PI = 3.14159

def area(radius):
    return PI * radius ** 2
```

```python
# main.py
import mymodule
print(mymodule.area(5))    # 78.53975
```

### Package

A directory that contains Python modules and an `__init__.py` file. The presence of `__init__.py` tells Python this directory is a package, not just a folder.

```text
mypackage/
    __init__.py
    geometry.py
    statistics.py
```

```python
import mypackage.geometry
from mypackage import statistics
```

### import Statement — Three Forms

| Form | Syntax | What lands in namespace | How you call it |
|---|---|---|---|
| Module import | `import math` | `math` | `math.sqrt(4)` |
| Name import | `from math import sqrt` | `sqrt` | `sqrt(4)` |
| Alias import | `import math as m` | `m` | `m.sqrt(4)` |
| Name + alias | `from math import sqrt as sq` | `sq` | `sq(4)` |
| Star import | `from math import *` | All public names | `sqrt(4)` — avoid |

**Key rule:** `import math` does not put `sqrt` in your namespace. You must write `math.sqrt`. `from math import sqrt` puts `sqrt` directly in your namespace so you can call it without a prefix.

```python
import math
sqrt(4)        # NameError — sqrt is not in namespace
math.sqrt(4)   # 4.0 — correct

from math import sqrt
sqrt(4)        # 4.0 — now it is in namespace
```

### Namespace (import context)

When you import a module, its names live inside the module's namespace. `import math` makes `math` a name in your namespace; everything inside `math` is accessed through that name.

`from math import sqrt` copies `sqrt` out of `math`'s namespace into your current namespace. After this, changing `math.sqrt` would not affect the local `sqrt` — they are separate references.

### Standard Library

The collection of modules that ships with every Python installation. No installation required — they are always available.

| Module | Key Contents |
|---|---|
| `math` | `sqrt`, `floor`, `ceil`, `log`, `pi`, `e`, `factorial` |
| `random` | `randint`, `random`, `choice`, `shuffle`, `sample` |
| `os` | `getcwd`, `listdir`, `path.exists`, `path.join`, `makedirs` |
| `sys` | `argv`, `path`, `version`, `exit`, `platform` |
| `datetime` | `datetime.now()`, `date.today()`, `timedelta`, `strftime` |
| `collections` | `Counter`, `defaultdict`, `namedtuple`, `deque` |
| `json` | `json.dumps`, `json.loads`, `json.dump`, `json.load` |
| `re` | Regular expressions — `re.search`, `re.findall`, `re.sub` |
| `string` | `string.ascii_letters`, `string.digits`, `string.punctuation` |

### sys.path

The list of directories Python searches when you write `import something`. Python checks each directory left to right and stops at the first match.

```python
import sys
print(sys.path)
# ['', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', ...]
```

The empty string `''` at the front means the current working directory is searched first. This is why `import greetings` works when `greetings.py` is in the same directory as your script.

### `__name__` and the Module Guard

Every Python file has a built-in `__name__` variable. Its value is:

- `'__main__'` when the file is **run directly** (`python3 myfile.py`)
- The module name (e.g., `'myfile'`) when the file is **imported** by another file

This enables the module guard pattern:

```python
# greetings.py

def hello(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    # Only runs when you execute: python3 greetings.py
    # Does NOT run when another file does: import greetings
    print(hello('Test'))
```

Without this guard, every `import greetings` would execute the test print — running side effects at import time. The guard separates reusable library code from startup/test code.

**This is one of the most commonly tested PCAP patterns.**

### `__init__.py`

The file that marks a directory as a package. It can be empty or contain initialization code that runs when the package is first imported.

```text
shapes/
    __init__.py      ← makes 'shapes' a package
    circle.py
    rectangle.py
```

```python
from shapes import circle
from shapes.rectangle import area
```

### pip — Package Installer for Python

The command-line tool for installing third-party packages from PyPI (Python Package Index).

```bash
pip3 install requests          # install latest version
pip3 install requests==2.28.0  # install specific version
pip3 uninstall requests        # remove a package
pip3 list                      # show all installed packages
pip3 show requests             # show info about one package
pip3 freeze                    # list installed packages in requirements format
```

Packages installed with `pip3` are available to `import` immediately.

### Virtual Environment

An isolated Python installation for a specific project. Prevents version conflicts between projects.

```bash
python3 -m venv myenv          # create virtual environment
source myenv/bin/activate      # activate (Linux/macOS)
pip3 install flask             # installs into myenv only
deactivate                     # return to system Python
```

While the environment is activated, `pip install` and `import` only see packages in that environment. The environment can be deleted and recreated from a `requirements.txt` file.

### dir() and help()

Built-in functions for exploring any module or object interactively.

```python
import math

dir(math)           # returns sorted list of all names in math
dir('hello')        # returns all string methods and attributes
dir([])             # returns all list methods and attributes

help(math)          # prints full module documentation
help(math.sqrt)     # prints docstring for math.sqrt
help(str.split)     # prints docstring for str.split
```

`dir()` with no arguments lists names in the current namespace.

### `from module import *` — Star Import

Imports all public names from a module directly into the current namespace. "Public" means all names that do not start with an underscore, or all names listed in `__all__` if the module defines it.

```python
from math import *
print(sqrt(16))    # 4.0 — works
print(pi)          # 3.141592653589793 — works
```

**Avoid star imports** in production code. Problems:

1. You cannot tell where any name came from by reading the code.
2. If two star-imported modules both define `log`, the second overwrites the first silently.
3. It pollutes the namespace with dozens of names you may not use.

### `__all__`

A list defined in a module that controls which names are exported when someone does `from module import *`. Names not in `__all__` are still accessible directly but are not exported by star import.

```python
# mymodule.py
__all__ = ['public_func', 'PublicClass']

def public_func():
    pass

def _private_func():    # not exported by import *
    pass
```

### Bytecode Cache (`__pycache__`)

When Python imports a module, it compiles the source to bytecode and stores it in `__pycache__/` as a `.pyc` file. On future imports, Python loads the `.pyc` cache instead of re-parsing the source, making imports faster. You never need to manage the cache manually.

---

## 2. Standard Library Quick Reference

### math Module

```python
import math

math.sqrt(x)          # square root
math.floor(x)         # round down to nearest int
math.ceil(x)          # round up to nearest int
math.log(x)           # natural log
math.log(x, base)     # log with specified base
math.log10(x)         # base-10 log
math.factorial(n)     # n!
math.pow(x, y)        # x**y as float
math.pi               # 3.141592653589793
math.e                # 2.718281828459045
math.inf              # positive infinity
math.isnan(x)         # True if x is NaN
math.isinf(x)         # True if x is +/- infinity
```

### random Module

```python
import random

random.randint(a, b)          # random int, a <= n <= b (both inclusive)
random.random()               # float in [0.0, 1.0)
random.uniform(a, b)          # float in [a, b]
random.choice(seq)            # random element from non-empty sequence
random.choices(seq, k=n)      # k random elements with replacement
random.sample(seq, k)         # k unique elements without replacement
random.shuffle(lst)           # shuffle list in place — returns None
random.seed(n)                # set seed for reproducible results
```

### os and os.path

```python
import os

os.getcwd()                       # current working directory as string
os.listdir(path)                  # list of filenames in directory
os.makedirs(path, exist_ok=True)  # create directory (and parents)
os.remove(path)                   # delete a file
os.rename(src, dst)               # rename file or directory
os.environ.get('HOME', '')        # safe access to environment variable

os.path.exists(path)              # True if path exists
os.path.isfile(path)              # True if path is a file
os.path.isdir(path)               # True if path is a directory
os.path.join(a, b)                # join path components correctly
os.path.basename(path)            # filename portion
os.path.dirname(path)             # directory portion
os.path.splitext(path)            # ('stem', '.ext') tuple
```

### datetime Module

```python
from datetime import datetime, date, timedelta

date.today()                          # date object for today
datetime.now()                        # datetime for current date+time
datetime(2025, 3, 15)                 # construct a specific datetime
dt.year / dt.month / dt.day           # integer attributes
dt.strftime('%Y-%m-%d')               # format to string
datetime.strptime(s, fmt)             # parse string to datetime
date.today() + timedelta(days=7)      # one week from today
```

---

## 3. Common Error Patterns to Memorize

**Pattern 1 — Importing with `import module` then calling without prefix:**

```python
import math
sqrt(16)    # NameError: name 'sqrt' is not defined
```

Fix: `math.sqrt(16)` or `from math import sqrt`.

**Pattern 2 — Forgetting the module guard, causing side effects on import:**

```python
# bad_module.py
def compute():
    return 42

print(compute())    # runs every time this file is imported!
```

Fix: Wrap executable code in `if __name__ == '__main__':`.

**Pattern 3 — Star import name collision:**

```python
from os.path import *
from posixpath import *    # join silently overwrites the previous join
join(...)                  # which join is this? impossible to tell
```

Fix: Use explicit imports — `from os.path import join, exists`.

**Pattern 4 — `from module import name` binds at import time:**

```python
from math import pi
pi = 3.0        # reassigns local name — does not affect math.pi
import math
print(math.pi)  # still 3.141592... — original unchanged
```

The `from` import copies a reference at import time. Reassigning the local name does not mutate the module.

**Pattern 5 — `random.shuffle()` returns None:**

```python
shuffled = random.shuffle([3, 1, 2])
print(shuffled)    # None — shuffle modifies the list in place
```

Fix: `random.shuffle(lst)` then use `lst`.

---

## 4. Certification Exam Tips

**Tip 1 — Know all three import syntaxes and their namespace effects.**
`import math` → access as `math.sqrt`. `from math import sqrt` → access as `sqrt`. `import math as m` → access as `m.sqrt`. `from math import sqrt as sq` → access as `sq`. The exam will show each form and ask what the calling syntax is.

**Tip 2 — `__name__ == '__main__'` is True only for the directly executed file.**
If `a.py` imports `b.py`, then inside `b.py`, `__name__` is `'b'` not `'__main__'`. The guard prevents `b.py`'s startup code from running when it is imported.

**Tip 3 — Star import uses `__all__` if defined, otherwise all non-underscore names.**
If a module defines `__all__ = ['f1', 'f2']`, then `from module import *` imports only `f1` and `f2`. Other names are excluded even if they have no underscore prefix.

**Tip 4 — `random.shuffle()` modifies in place and returns None.**
`shuffled = random.shuffle(lst)` — `shuffled` is `None`. The shuffled list is `lst` itself.

**Tip 5 — `random.randint(a, b)` is inclusive on both ends.**
`random.randint(1, 6)` can return 1, 2, 3, 4, 5, or 6. This differs from `range(1, 6)` which excludes 6.

**Tip 6 — `sys.path[0]` is the script's directory (or `''` for the REPL).**
Custom modules in the same directory as your script are found automatically without modifying `sys.path`.

**Tip 7 — A package requires `__init__.py` in the traditional sense.**
Without `__init__.py`, Python 2 does not recognize the directory as a package. Python 3.3+ supports namespace packages without it, but the PCAP exam expects you to know the traditional `__init__.py` requirement.

---

## 5. Beyond the Exam — Real-World Context

**requirements.txt — Reproducible environments.**
`pip3 freeze > requirements.txt` writes all installed packages and exact versions to a file. Anyone can recreate the environment with `pip3 install -r requirements.txt`. Every professional Python project has a `requirements.txt` or `pyproject.toml`.

**`collections.Counter` — the frequency counter built-in.**
In Module 10 you built a word frequency counter manually with a dictionary. `collections.Counter` does it in one line:

```python
from collections import Counter
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counts = Counter(words)
print(counts.most_common(2))    # [('apple', 3), ('banana', 2)]
```

**`pathlib` — Modern path handling.**
`os.path` works, but `pathlib.Path` is more readable and object-oriented:

```python
from pathlib import Path
p = Path('data') / 'results.csv'    # builds path correctly on any OS
print(p.exists())
print(p.suffix)    # '.csv'
text = p.read_text()
```

**`json` — Reading and writing structured data.**
JSON is the universal format for data exchange. The `json` module converts between Python dicts/lists and JSON strings.

```python
import json

data = {'name': 'Alice', 'scores': [95, 87, 92]}
text = json.dumps(data, indent=2)    # Python → JSON string
obj  = json.loads(text)              # JSON string → Python
```

---

## 6. Required Readings and Videos

**Required Reading — Official Python Docs:**
Read [The import system](https://docs.python.org/3/reference/import.html) in the official Python 3 reference — authoritative source for import mechanics tested on the PCAP exam. Also read [The Python Standard Library](https://docs.python.org/3/library/index.html) overview.

**Required Reading — Chapter on Functions and Reuse:**
Read Chapter 4 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) which covers functions and introduces the concept of code reuse that modules extend.

**Supplemental Video:**
Watch the relevant episode of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) covering modules and standard library use.

---

## 7. Study Checklist

- [ ] Watch the Module 13 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially the import forms table and namespace effects.
- [ ] Practice all three import forms in the REPL: confirm what names land in namespace with `dir()`.
- [ ] Trace `__name__` behavior by running a file directly and then importing it.
- [ ] Create a two-file program: a module and a script that imports it.
- [ ] Run `pip3 install` and `pip3 list` to confirm pip works in your VM.
- [ ] Create and activate a virtual environment; install a package inside it.
- [ ] Use `dir()` and `help()` to explore `math`, `random`, and `os`.
- [ ] Review all 7 Certification Exam Tips in Section 4.
- [ ] Proceed to the Module 13 Lab Activity.
