# Reading Guide: Module 09 — Scopes, Namespaces, and Recursion

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 09 — Scopes, Namespaces, and Recursion**. This module digs into how Python manages variable names, where Python looks when it resolves a name, and how functions can call themselves to solve problems elegantly.

The **LEGB rule** is tested directly on the PCAP exam — not as a fact to memorize but as a skill to apply. You will be shown code with multiple variables sharing the same name at different scope levels and asked to trace the output. You need to know the lookup order cold.

The **nonlocal** keyword and **closures** extend that understanding into nested functions — a pattern used extensively in Python decorators and functional programming.

**Recursion** is one of the most beautiful ideas in programming. A recursive function solves a problem by calling itself with a smaller version of the same problem. Once the call stack model is clear, a whole class of elegant solutions opens up.

---

## 1. High-Yield Glossary

### Scope

The region of a program where a name is visible and accessible. Every variable has a scope — the part of the code where Python will find it when you use the name.

### LEGB Rule

Python's name lookup order. When Python encounters a name, it searches four scopes in order and uses the first match it finds:

| Letter | Scope | Description |
|---|---|---|
| **L** | Local | Inside the currently executing function |
| **E** | Enclosing | Any enclosing (outer) functions, searched from inner to outer |
| **G** | Global | The module-level scope — the top of the current `.py` file |
| **B** | Built-in | Python's built-in names: `len`, `print`, `range`, `True`, `None`, etc. |

If Python searches all four levels and finds nothing, it raises `NameError`.

```python
x = 'global'

def outer():
    x = 'enclosing'

    def inner():
        x = 'local'
        print(x)    # L — finds 'local'

    inner()
    print(x)        # E — inner is done; outer's x is 'enclosing'

outer()
print(x)            # G — outer is done; module-level x is 'global'
```

Output:

```text
local
enclosing
global
```

### Local Variable

A variable assigned inside a function. It exists only for the duration of that function call. When the function returns, the local variable is destroyed. It is completely separate from any global variable with the same name.

```python
x = 5

def change():
    x = 99    # local x — shadow of global x, not a modification
    print(x)  # 99

change()
print(x)      # 5 — global x is unchanged
```

### Global Variable

A variable assigned at module level, outside all functions. It is visible throughout the module. A function can **read** a global variable without any special declaration. To **assign** to a global variable from inside a function, you must declare it with `global`.

### Enclosing Scope

The scope of a function that contains (wraps) another function. Only relevant for nested functions. When an inner function cannot find a name in its own local scope, Python searches the enclosing function's scope next — before reaching the global scope.

### Built-in Scope

The outermost scope — the names Python itself provides: `print`, `len`, `range`, `int`, `str`, `True`, `False`, `None`, all exceptions, and more. You can shadow a built-in name accidentally, which is a common source of hard-to-find bugs.

```python
len = 'oops'     # shadows the built-in len
print(len([1, 2, 3]))    # TypeError: 'str' object is not callable
```

Always avoid using built-in names as variable names.

### global Keyword

Declares that a name inside a function refers to the module-level global, not a new local. Without `global`, assigning to a name creates a local.

```python
count = 0

def increment():
    global count
    count += 1    # modifies the global count

increment()
increment()
print(count)    # 2
```

**PCAP exam rule:** `global` is used when a function needs to **modify** a global variable. Reading a global without `global` is fine — Python finds it through LEGB. It is only assignment that requires `global`.

Using `global` is generally discouraged in professional code. Pass values through parameters and return values through `return` instead. `global` creates hidden dependencies between functions and the module state.

### nonlocal Keyword

Declares that a name inside an inner function refers to the enclosing function's scope, not a new local. `nonlocal` is the `global`-equivalent for the **E** in LEGB.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count    # refers to make_counter's count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())    # 1
print(counter())    # 2
print(counter())    # 3
```

`nonlocal` vs `global` comparison:

| Keyword | Reaches | When to use |
|---|---|---|
| `global x` | Module-level `x` | Modify a variable defined at the top of the file |
| `nonlocal x` | Nearest enclosing function's `x` | Modify a variable in the directly enclosing function |

Neither keyword can reach a scope that does not already have that variable. If the variable does not exist in that scope, Python raises `SyntaxError`.

### Closure

A function that **captures** variables from its enclosing scope and retains access to them even after the enclosing function has returned. The captured variables are stored with the closure and live as long as the closure exists.

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor    # captures 'factor' from make_multiplier's scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))    # 10 — factor=2 was captured
print(triple(5))    # 15 — factor=3 was captured independently
```

Each call to `make_multiplier()` creates a separate closure with its own captured `factor`. `double` and `triple` are completely independent.

Why closures matter:

- They are the foundation of Python **decorators**
- They allow functions to carry state without using global variables or classes
- They replace many patterns that would require classes in other languages

### Recursion

A technique where a function calls itself to solve a smaller version of the same problem.

Every recursive function requires:

1. **Base case** — a condition that stops the recursion and returns a value directly
2. **Recursive case** — the function calling itself with a simpler or smaller argument, moving toward the base case

```python
def factorial(n):
    if n == 0:           # base case
        return 1
    return n * factorial(n - 1)    # recursive case
```

### Base Case

The condition in a recursive function that stops the recursion. Without a base case, the function calls itself forever until Python hits the recursion limit and raises `RecursionError`.

The base case must be:

- **Reachable** — every sequence of recursive calls must eventually reach it
- **Correct** — it must return the right value for the simplest input

### Recursive Case

The part of a recursive function that calls itself with a **reduced** argument. Each recursive call must move closer to the base case. Common reductions: `n - 1`, `lst[1:]`, `n // 2`.

### Call Stack

A data structure Python uses to track active function calls. Each time a function is called, Python pushes a **stack frame** onto the call stack. Each frame stores the function's local variables and the return address (where execution should resume after the function returns). When a function returns, its frame is popped.

For `factorial(4)`:

```text
Push: factorial(4) — waits for factorial(3)
Push: factorial(3) — waits for factorial(2)
Push: factorial(2) — waits for factorial(1)
Push: factorial(1) — waits for factorial(0)
Push: factorial(0) — returns 1

Pop: factorial(0) → 1
Pop: factorial(1) → 1*1 = 1
Pop: factorial(2) → 2*1 = 2
Pop: factorial(3) → 3*2 = 6
Pop: factorial(4) → 4*6 = 24
```

### Stack Frame

A record on the call stack representing a single function call. Contains the function's local variables and a pointer to the calling code. Each recursive call creates a new, independent frame — which is why each call gets its own copy of `n`.

### RecursionError

The exception raised when Python's call stack grows beyond its limit. Default limit: **1,000 frames**.

```python
def bad(n):
    return bad(n - 1)    # no base case

bad(1)    # RecursionError: maximum recursion depth exceeded
```

Check the current limit: `import sys; sys.getrecursionlimit()`

`RecursionError` is Python-specific. Other languages call the equivalent condition a "stack overflow."

### Namespace

A mapping from names to objects — essentially a dictionary. When you write `x = 5`, Python adds `'x': 5` to the current namespace.

Python maintains several namespaces simultaneously:

| Namespace | Lifetime | Contents |
|---|---|---|
| Local | Duration of one function call | Function's local variables |
| Enclosing | Duration of the enclosing function call | Enclosing function's variables |
| Global | Duration of the module | Module-level variables and imported names |
| Built-in | Duration of the interpreter session | All Python built-ins |

Namespaces are why two functions can both have a local variable named `x` without conflict — each function call has its own local namespace dictionary.

### locals() and globals()

Built-in functions that return the current namespace as a dictionary.

```python
x = 10
y = 20

def demo():
    z = 30
    print(locals())     # {'z': 30}

demo()
print('x' in globals())    # True
print(globals()['x'])      # 10
```

`locals()` inside a function returns only that function's local variables. `globals()` always returns the module-level namespace.

---

## 2. LEGB Lookup — Reference Table

| Situation | Which scope is checked and when |
|---|---|
| Name assigned inside a function | **L** — local namespace of that function |
| Name in a nested (inner) function, not in inner's locals | **E** — each enclosing function searched inner to outer |
| Name at the top of the `.py` file | **G** — global (module) namespace |
| Built-in like `len`, `print`, `True` | **B** — Python's built-in namespace |
| Name not found anywhere | **NameError** is raised |

### What triggers a NameError vs a read from a higher scope?

If a name is **not assigned** inside a function at all, Python walks up LEGB normally:

```python
message = 'Hello from global'

def show():
    print(message)    # no local 'message' → searches E (none) → finds G

show()    # Hello from global
```

If a name **is assigned** anywhere inside a function, Python marks it as **local throughout the entire function** — even for reads before the assignment:

```python
x = 10

def broken():
    print(x)    # UnboundLocalError — Python sees x=99 below and marks x as local
    x = 99

broken()
```

This `UnboundLocalError` surprises many programmers. The fix: either rename the local variable, or use `global x` if you intend to modify the global.

---

## 3. Recursion Trace Practice

Trace `factorial(3)` step by step:

```text
factorial(3)
  → 3 == 0? No → return 3 * factorial(2)
      factorial(2)
        → 2 == 0? No → return 2 * factorial(1)
            factorial(1)
              → 1 == 0? No → return 1 * factorial(0)
                  factorial(0)
                    → 0 == 0? Yes → return 1
              → returns 1 * 1 = 1
        → returns 2 * 1 = 2
  → returns 3 * 2 = 6

factorial(3) = 6
```

Trace `list_sum([1, 2, 3])`:

```text
list_sum([1, 2, 3])
  → not [] ? True → return 1 + list_sum([2, 3])
      list_sum([2, 3])
        → not [] ? True → return 2 + list_sum([3])
            list_sum([3])
              → not [] ? True → return 3 + list_sum([])
                  list_sum([])
                    → not [] ? False → return 0
              → returns 3 + 0 = 3
        → returns 2 + 3 = 5
  → returns 1 + 5 = 6
```

---

## 4. Common Error Patterns to Memorize

**Pattern 1 — UnboundLocalError from assignment in function:**

```python
x = 10

def demo():
    print(x)    # UnboundLocalError — Python sees 'x = ...' below
    x = 99

demo()
```

Fix: Use `global x` if you intend to modify the global, or rename the local variable.

**Pattern 2 — Shadowing a built-in:**

```python
list = [1, 2, 3]      # shadows the built-in list() function
x = list([4, 5, 6])   # TypeError: 'list' object is not callable
```

Fix: Never name variables `list`, `dict`, `set`, `str`, `int`, `len`, `print`, `type`, `id`, or any other built-in.

**Pattern 3 — Missing base case causes RecursionError:**

```python
def count_down(n):
    print(n)
    count_down(n - 1)    # no base case — runs until RecursionError

count_down(5)
```

Fix: Always add a base case: `if n <= 0: return`.

**Pattern 4 — Wrong: using global to read (not needed):**

```python
name = 'Alice'

def show():
    global name         # unnecessary — reading a global needs no declaration
    print(name)
```

`global` is only needed when you **assign** to the name inside the function. Reading it works automatically through LEGB.

**Pattern 5 — Confusing nonlocal and global:**

```python
def outer():
    x = 10

    def inner():
        global x        # WRONG — there is no global x, creates a new global
        x += 1

    inner()
    print(x)    # still 10 — inner modified a different x

outer()
```

Fix: Use `nonlocal x` to modify the enclosing function's `x`.

---

## 5. Certification Exam Tips

**Tip 1 — LEGB order is tested with multi-scope code.**
You will see a program with variables named `x` at two or three scope levels. Trace which `x` each `print(x)` resolves to. The answer follows L→E→G→B strictly.

**Tip 2 — `global` is only required for assignment, not reading.**
`global x` is needed only when you assign `x = ...` or do `x += ...` inside a function. Simply reading `x` inside a function does not require `global`.

**Tip 3 — `nonlocal` applies to the nearest enclosing scope that has the variable.**
If you have triple-nested functions, `nonlocal x` in the innermost function modifies the nearest enclosing function's `x`, not the outermost.

**Tip 4 — A recursive function without a base case always raises RecursionError.**
The exam will show functions with no base case or with a base case that is never reached (e.g., `if n == 0` when n starts at 3 and decrements by 2). Both cause `RecursionError`.

**Tip 5 — A closure captures the variable, not the value at the time of capture.**
If a closure captures a variable that changes after the closure is created, the closure sees the updated value. This is a common exam trap with loops creating closures.

**Tip 6 — `locals()` returns the local namespace dictionary; `globals()` returns the global namespace dictionary.**
Both are accessible at any point. `locals()` inside a function shows only that function's local variables. `globals()` always returns module-level names.

**Tip 7 — RecursionError is Python's specific exception for call stack overflow.**
The exam may ask what exception is raised by infinite recursion. The answer is `RecursionError`, not `StackOverflowError` (Java/C++) or `RuntimeError` (though `RecursionError` is technically a subclass of `RuntimeError`).

---

## 6. Beyond the Exam — Real-World Context

**Why closures matter in production code.**
Python's `@decorator` syntax is built entirely on closures. When you write `@cache` or `@functools.lru_cache`, you are calling a function that returns a closure wrapping your original function. Flask route handlers, `unittest.mock.patch`, and Django middleware all use closures. Understanding closures is essential for reading and writing Python frameworks.

**When to use recursion.**
Recursion is natural when the data structure itself is recursive — trees, graphs, nested directories, JSON documents, HTML/XML. File system traversal (`os.walk` uses recursion internally), JSON parsing, and AST (Abstract Syntax Tree) walking are all natural fits. For counting loops, use `for` — it is faster and clearer. For divide-and-conquer (merge sort, binary search, quicksort), recursion makes the algorithm structure visible and verifiable.

**Memoization and dynamic programming.**
The naive recursive Fibonacci is exponential in time — `fibonacci(40)` makes billions of calls. Adding a cache (memoization) converts it to linear time. Python's `functools.lru_cache` decorator does this in one line: `@lru_cache(maxsize=None)`. This technique — caching recursive results — is called dynamic programming and is one of the most powerful algorithmic techniques in computer science.

---

## 7. Required Readings and Videos

**Required Reading — Chapter 4:**
Read Chapter 4 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). The chapter covers function basics and scope. Pay special attention to the scope examples.

**Required Reading — Official Python Docs:**
Read [Python Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces) in the official Python 3 tutorial — this is the authoritative description of LEGB used directly in PCAP exam construction.

**Required Reading — Official Python Docs:**
Read [sys.getrecursionlimit()](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit) to understand how the recursion limit is controlled.

**Supplemental Video:**
Watch Episode 4 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance covers function scope and variable lifetime.

**Supplemental Reference:**
[Real Python — Understanding Scope](https://realpython.com/python-scope-legb-rule/) — a thorough written walkthrough of LEGB with diagrams.

---

## 8. Study Checklist

- [ ] Watch the Module 09 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially LEGB, nonlocal, closures, recursion, and RecursionError.
- [ ] Trace the factorial(3) and list_sum([1,2,3]) examples by hand on paper.
- [ ] Work through the Common Error Patterns in Section 4 — run each one in the REPL and observe the error.
- [ ] Read the Python Scopes and Namespaces page in the official Python 3 docs.
- [ ] Read Chapter 4 of *Python for Everybody* at py4e.com.
- [ ] Review all 7 Certification Exam Tips in Section 5.
- [ ] Proceed to the Module 09 Lab Activity.
