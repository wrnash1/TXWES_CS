# Quiz: Module 13 — Modules and Packages

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 13 topics.

---

### Question 1

After executing `import math`, which of the following calls is correct?

- A) `sqrt(16)`
- B) `math.sqrt(16)`
- C) `math::sqrt(16)`
- D) `Math.sqrt(16)`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `import math` puts the name `math` in the namespace, not `sqrt`. Calling `sqrt(16)` raises `NameError: name 'sqrt' is not defined`. You would need `from math import sqrt` to call it without a prefix.
- *Why B is correct:* `import math` makes `math` available as a module object. All of its contents are accessed with the dot notation `math.sqrt`.
- *Why C is incorrect:* Python uses `.` for attribute access, not `::`. The `::` operator does not exist in Python (it is used in C++ and Ruby).
- *Why D is incorrect:* Module names in Python are case-sensitive. The module is named `math` (lowercase), not `Math`. Using the wrong case raises `NameError`.

---

### Question 2

What is the output of this code?

```python
from math import sqrt as sq
print(sq(49))
print(math.sqrt(49))
```

- A) `7.0` then `7.0`
- B) `7.0` then `NameError`
- C) `NameError` then `7.0`
- D) `49` then `49`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `from math import sqrt as sq` imports `sqrt` under the alias `sq` — it does NOT import `math` itself into the namespace. The second line `math.sqrt(49)` raises `NameError`.
- *Why B is correct:* `sq(49)` succeeds because `sq` is the alias for `sqrt`. The second line fails because `math` was never imported — only `sqrt` was, renamed to `sq`.
- *Why C is incorrect:* The first line succeeds — `sq` is a valid alias for `sqrt`. The error occurs on the second line, not the first.
- *Why D is incorrect:* `sq(49)` calls `math.sqrt(49)` which returns `7.0` (a float), not `49`. The square root of 49 is 7.0.

---

### Question 3

What value does `__name__` have inside a module file when that file is **imported** by another script?

- A) `'__main__'`
- B) `None`
- C) The module's filename including `.py`
- D) The module's filename without `.py`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `__name__` equals `'__main__'` only when the file is run directly with `python3 filename.py`. When imported, `__name__` is the module name, not `'__main__'`.
- *Why B is incorrect:* `__name__` is never `None`. It is always a string — either `'__main__'` or the module name.
- *Why C is incorrect:* The module name does not include the `.py` extension. `greetings.py` has `__name__ == 'greetings'` when imported, not `'greetings.py'`.
- *Why D is correct:* When `greetings.py` is imported, `__name__` inside that file equals `'greetings'` — the filename without the `.py` extension. This is how Python identifies modules.

---

### Question 4

What is the output of this code?

```python
# utils.py
def greet(name):
    return f'Hi, {name}!'

print(greet('World'))
```

```python
# main.py
import utils
print(utils.greet('Alice'))
```

Running `python3 main.py` produces:

- A) `Hi, Alice!`
- B) `Hi, World!` then `Hi, Alice!`
- C) `Hi, Alice!` then `Hi, World!`
- D) `Hi, World!`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `utils.py` has a top-level `print(greet('World'))` that is NOT inside a `if __name__ == '__main__':` guard. When `import utils` executes, Python runs the entire `utils.py` file — including that print — before returning control to `main.py`.
- *Why B is correct:* Importing `utils` runs the entire module file. The `print(greet('World'))` runs first during import, printing `Hi, World!`. Then `main.py` calls `utils.greet('Alice')` and prints `Hi, Alice!`.
- *Why C is incorrect:* The import runs first, before `main.py`'s own code. The output order is `Hi, World!` then `Hi, Alice!`, not the reverse.
- *Why D is incorrect:* `print(utils.greet('Alice'))` also runs — the import side effect and the explicit call both execute.

---

### Question 5

What does `random.shuffle(items)` return?

- A) A new shuffled list
- B) The original list, shuffled in place
- C) `None`
- D) The first element of the shuffled list

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `random.shuffle()` does not create a new list. It modifies the existing list in place.
- *Why B is incorrect:* While `shuffle` does modify the list in place, the return value is `None`, not the list. Assigning `result = random.shuffle(items)` gives `result` the value `None`, not the shuffled list.
- *Why C is correct:* `random.shuffle()` is an in-place operation that returns `None`. To get the shuffled list, use the variable you passed in — not the return value.
- *Why D is incorrect:* `shuffle` does not return any element. Its return value is always `None`.

---

### Question 6

Which command installs a third-party package named `requests` using pip?

- A) `python3 install requests`
- B) `import requests`
- C) `pip3 install requests`
- D) `python3 -m install requests`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `python3 install` is not a valid command. Python's interpreter does not have an `install` subcommand. You use the `pip3` tool, not the `python3` interpreter directly for installation.
- *Why B is incorrect:* `import requests` imports a package that is already installed. It does not install anything. Running this before installation raises `ModuleNotFoundError`.
- *Why C is correct:* `pip3 install requests` is the correct command to download `requests` from PyPI and install it for your Python 3 environment.
- *Why D is incorrect:* The correct pip invocation through the Python interpreter is `python3 -m pip install requests` (using `-m pip`, not `-m install`). Option D is not valid syntax.

---

### Question 7

What is the purpose of `if __name__ == '__main__':` at the bottom of a module file?

- A) To define the main function that Python always calls first
- B) To prevent the code inside from running when the file is imported
- C) To mark the file as the entry point for the entire program
- D) To import the module into itself

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python does not have a mandatory `main()` function like Java or C. Python files execute top to bottom from line 1. There is no automatic call to any `main` function.
- *Why B is correct:* The block inside `if __name__ == '__main__':` only runs when the file is executed directly. When the file is imported, `__name__` is the module's name (not `'__main__'`), so the condition is `False` and the block is skipped. This separates reusable library code from startup/test code.
- *Why C is incorrect:* There is no formal "entry point" designation in Python's module system. Any `.py` file can be run directly. The guard does not mark a file as special to the interpreter — it just conditionally executes code.
- *Why D is incorrect:* A module importing itself would create a circular import. `if __name__ == '__main__':` does not perform any import.

---

### Question 8

What is the output of this code?

```python
import random
random.seed(0)
print(random.randint(1, 6))
print(random.randint(1, 6))
```

- A) `1` then `1` (seed makes all values identical)
- B) Two unpredictable values that change on every run
- C) Two specific values that are the same every run because seed is fixed
- D) `0` then `0` (seed value is returned)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `random.seed(0)` initializes the random number generator to a fixed starting state. Subsequent calls produce a deterministic sequence — but each call produces a different value in that sequence. They are not all the same.
- *Why B is incorrect:* With `random.seed(0)`, the sequence is fully deterministic. Running this code a thousand times always produces the same two values.
- *Why C is correct:* `random.seed(0)` makes the random sequence reproducible. With seed 0, `random.randint(1, 6)` produces the same specific sequence every run. The values are not the same as each other, but the sequence is identical across runs.
- *Why D is incorrect:* `random.seed()` returns `None`. It does not return the seed value, and the subsequent `randint` calls return values in the range 1–6, not 0.

---

### Question 9

Which of the following correctly creates a virtual environment named `myenv` and activates it on Linux?

- A) `python3 venv myenv` then `activate myenv`
- B) `python3 -m venv myenv` then `source myenv/bin/activate`
- C) `pip3 venv myenv` then `source myenv/activate`
- D) `virtualenv myenv` then `myenv/activate`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `python3 venv myenv` is missing the `-m` flag. The correct command runs the `venv` module with `-m`. Also, `activate myenv` is not the correct activation syntax — you `source` the activate script.
- *Why B is correct:* `python3 -m venv myenv` creates the virtual environment directory. `source myenv/bin/activate` runs the activation script in the current shell, modifying the `PATH` so `python3` and `pip3` point to the environment's copies.
- *Why C is incorrect:* `pip3 venv myenv` is not a valid pip subcommand. Also, the activate script is at `myenv/bin/activate`, not `myenv/activate`.
- *Why D is incorrect:* `virtualenv` is a third-party tool that is not part of the standard library. The standard built-in tool is `python3 -m venv`. Also, you `source` the activate script — you do not run it directly as a path.

---

### Question 10

What is the output of this code?

```python
import math

print(math.ceil(4.0))
print(math.ceil(4.1))
print(math.floor(4.9))
print(math.floor(-4.1))
```

- A) `4` then `4` then `4` then `-4`
- B) `4` then `5` then `4` then `-5`
- C) `5` then `5` then `5` then `-4`
- D) `4.0` then `5.0` then `4.0` then `-5.0`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `math.ceil(4.1)` rounds **up** to the nearest integer, giving `5`, not `4`. Ceiling always rounds toward positive infinity.
- *Why B is correct:* `ceil(4.0)` → `4` (already integer). `ceil(4.1)` → `5` (round up). `floor(4.9)` → `4` (round down). `floor(-4.1)` → `-5` (round toward negative infinity — `-4.1` rounded down is `-5`, not `-4`).
- *Why C is incorrect:* `math.ceil(4.0)` is `4`, not `5`. An exact integer has no fractional part, so ceiling and floor both return the integer itself.
- *Why D is incorrect:* `math.ceil` and `math.floor` return Python `int`, not `float`. The results are `4`, `5`, `4`, `-5` — not `4.0`, `5.0`, etc.

---

### Question 11

What is the output of this code?

```python
import sys
print(type(sys.argv))
print(sys.argv[0])
```

Run as: `python3 script.py`

- A) `<class 'list'>` then `'script.py'`
- B) `<class 'tuple'>` then `'script.py'`
- C) `<class 'list'>` then `script.py`
- D) `<class 'dict'>` then `0`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `sys.argv` is a `list`, and `print()` outputs the string without surrounding quotes. The printed output is `script.py`, not `'script.py'`.
- *Why B is incorrect:* `sys.argv` is a `list`, not a `tuple`. It is mutable because it represents command-line arguments that could in theory be modified.
- *Why C is correct:* `sys.argv` is a list of strings. `sys.argv[0]` is always the name of the script being run. `print()` outputs it without quotes.
- *Why D is incorrect:* `sys.argv` is not a dict. It is an ordered list where index 0 is the script name and subsequent indices are additional arguments.

---

### Question 12

What is the output of this code?

```python
from os.path import basename, dirname
path = '/home/user/projects/script.py'
print(basename(path))
print(dirname(path))
```

- A) `script.py` then `/home/user/projects`
- B) `/home/user/projects` then `script.py`
- C) `script` then `/home/user/projects/script.py`
- D) `script.py` then `/home/user/projects/script.py`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `basename()` returns the final component of a path — the filename including extension. `dirname()` returns everything before the final component — the directory path.
- *Why B is incorrect:* This reverses the two functions. `basename` → filename, `dirname` → directory. The order here is swapped.
- *Why C is incorrect:* `basename()` returns the full filename with extension (`script.py`), not just the name without extension.
- *Why D is incorrect:* `dirname()` returns the directory part (`/home/user/projects`), not the full original path.

---

### Question 13

What does `import importlib; importlib.reload(mymodule)` accomplish?

- A) Creates a second independent copy of `mymodule` in memory
- B) Re-executes the module's code and updates the existing module object
- C) Deletes `mymodule` from `sys.modules` so it can be freshly imported
- D) `reload()` is not a valid function in Python 3

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `reload()` does not create a second copy. It updates the existing module object in place by re-running its code.
- *Why B is correct:* `importlib.reload(module)` re-executes the module's source code and updates the module's namespace. This is useful in interactive sessions when you have edited a file and want to pick up the changes without restarting Python.
- *Why C is incorrect:* `reload()` does not remove the module from `sys.modules`. It updates it in place.
- *Why D is incorrect:* `reload()` was moved from the built-in `reload()` in Python 2 to `importlib.reload()` in Python 3. It still exists — just in the `importlib` module.

---

### Question 14

What is the purpose of `__all__` in a module?

- A) Lists all functions that are private and cannot be imported
- B) Controls which names are exported when `from module import *` is used
- C) Specifies the module's dependencies for `pip` to install
- D) Defines the order in which functions are executed when the module loads

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `__all__` defines the public API — names that SHOULD be exported. Private names are conventionally prefixed with `_`, not listed in `__all__`.
- *Why B is correct:* When `from module import *` is executed, Python imports only the names listed in `__all__` (if defined). Without `__all__`, all names not starting with `_` are imported. `__all__` lets module authors control the public interface.
- *Why C is incorrect:* Dependencies for pip are specified in `setup.py`, `pyproject.toml`, or `requirements.txt` — not in `__all__`.
- *Why D is incorrect:* `__all__` has no effect on execution order. Code in a module always executes top to bottom.

---

### Question 15

What does `sys.path` contain?

- A) The system's `PATH` environment variable as a list
- B) The list of directory paths Python searches when resolving imports
- C) The path to the Python interpreter executable
- D) The list of all installed package names

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `sys.path` is Python-specific and separate from the OS `PATH` environment variable. The OS `PATH` is accessed via `os.environ['PATH']`.
- *Why B is correct:* `sys.path` is a list of directory strings. When you execute `import mymodule`, Python searches each directory in `sys.path` in order until it finds `mymodule.py` (or a package directory named `mymodule`).
- *Why C is incorrect:* The path to the Python interpreter is `sys.executable`, not `sys.path`.
- *Why D is incorrect:* Installed packages are tracked by `pip` and accessible via `pip3 list` or `importlib.metadata`. `sys.path` is a list of directories, not package names.

---

### Question 16

What is the output of this code?

```python
import math
import math as m

print(math is m)
```

- A) `False` — two separate module objects were created
- B) `True` — both names reference the same module object
- C) `TypeError` — `is` cannot compare module objects
- D) `False` — `as` creates a copy of the module

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python caches imported modules in `sys.modules`. The second `import math as m` finds `math` already in `sys.modules` and returns the same object — just bound to a different name.
- *Why B is correct:* Both `math` and `m` refer to the same module object. Python's import system never loads the same module twice. `math is m` confirms they are the identical object.
- *Why C is incorrect:* The `is` operator works with any Python object, including modules. It tests object identity.
- *Why D is incorrect:* `import math as m` is purely a namespace alias. It creates a new name `m` that refers to the same module object — no copying occurs.

---

### Question 17

Which standard library module provides the `Counter` class for frequency counting?

- A) `statistics`
- B) `itertools`
- C) `collections`
- D) `functools`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `statistics` provides statistical functions like `mean()`, `median()`, and `stdev()`. It does not include `Counter`.
- *Why B is incorrect:* `itertools` provides iterator building blocks like `chain()`, `product()`, and `combinations()`. It does not include `Counter`.
- *Why C is correct:* `from collections import Counter` imports the `Counter` class. It is a dict subclass that counts hashable objects. `Counter(words)` builds a frequency dictionary in one call.
- *Why D is incorrect:* `functools` provides higher-order function tools like `lru_cache`, `reduce`, and `partial`. It does not include `Counter`.

---

### Question 18

What is the output of this code?

```python
from math import pi, e
print(round(pi, 4))
print(round(e, 4))
```

- A) `3.1416` then `2.7183`
- B) `3.14159` then `2.71828`
- C) `3` then `3`
- D) `3.1416` then `2.718`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `math.pi ≈ 3.14159265...`. `round(pi, 4)` → `3.1416` (4 decimal places, rounds the 5th digit). `math.e ≈ 2.71828182...`. `round(e, 4)` → `2.7183` (rounds the 5th digit `8` up).
- *Why B is incorrect:* `round(pi, 4)` rounds to 4 decimal places, not 5. The result is `3.1416`, not `3.14159`.
- *Why C is incorrect:* `round(pi, 4)` keeps 4 decimal places. `round(pi, 0)` would give `3.0` and `round(pi)` would give `3` — but 4 decimal places gives `3.1416`.
- *Why D is incorrect:* `round(e, 4)` → `2.7183` (the 5th digit is `8`, which rounds the 4th digit up from `2` to `3`). `2.718` has only 3 decimal places.

---

### Question 19

What is the minimum file needed to make a directory into a Python package?

- A) A `main.py` file in the directory
- B) A `__init__.py` file in the directory
- C) A `setup.py` file in the directory
- D) No file is needed — any directory is automatically a package

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `main.py` is a common convention for the entry-point script but has no special meaning to the import system. It does not make a directory a package.
- *Why B is correct:* `__init__.py` (even if empty) signals to Python that the directory is a package. When Python imports `mypackage.module`, it first runs `mypackage/__init__.py`.
- *Why C is incorrect:* `setup.py` is a packaging/distribution file used with `setuptools` for building installable packages for PyPI. It does not affect the import system directly.
- *Why D is incorrect:* While Python 3.3+ supports "namespace packages" (directories without `__init__.py`), the traditional and PCAP-tested requirement is that `__init__.py` must be present. The exam expects you to know this rule.

---

### Question 20

What is the output of this code?

```python
import random
random.seed(42)
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items[0])
```

- A) An unpredictable value that changes every run
- B) A specific, reproducible value because the seed is fixed
- C) `1` — shuffle never changes the first element
- D) `None` — shuffle returns None, not the list

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `random.seed(42)` makes the random sequence deterministic. The same seed always produces the same shuffle result. The output is reproducible.
- *Why B is correct:* With `random.seed(42)`, `random.shuffle([1, 2, 3, 4, 5])` produces the same permutation every time. `items[0]` will always be the same specific value — it is not unpredictable.
- *Why C is incorrect:* `shuffle` randomizes all positions — including the first element. There is no guarantee the first element stays as `1`.
- *Why D is incorrect:* `random.shuffle(items)` modifies `items` in place and returns `None`, but `print(items[0])` prints from the `items` list — which has been shuffled. The access `items[0]` works correctly.
