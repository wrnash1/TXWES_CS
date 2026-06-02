# Video Script: CIS-1310 — Introduction to Python

## Module 09 — Scopes, Namespaces, and Recursion

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - Draw the LEGB stack diagram before running the nested function demo.
> - Trace the factorial recursion on a slide (n=4 → n=3 → n=2 → n=1 → n=0) before coding it.
> - Demonstrate the RecursionError with a deliberately non-terminating recursive function.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 09 | Scopes, Namespaces, and Recursion | CIS-1310"]**

"Welcome back. Module 08 introduced functions and touched on scope. This module goes deeper — into how Python actually tracks variables, what LEGB means, how closures work, and the concept of recursion.

Recursion is one of those topics that causes confusion the first time and then becomes one of the most elegant tools in your toolkit. A recursive function calls itself — and once you understand how Python's call stack makes that safe and predictable, a whole class of problems becomes easy to express.

Scopes and namespaces are also tested directly on the PCAP exam — specifically LEGB lookup order and the `nonlocal` keyword. Let's cover it all."

---

## [00:45 – 03:00] LEGB Scope Rules

**[SHOW SLIDE: "LEGB — Python's Name Lookup Order"]**

"When Python encounters a variable name, it looks for it in four scopes, in order. This is called the **LEGB rule**:

- **L — Local:** The innermost scope — inside the current function
- **E — Enclosing:** Any enclosing functions (for nested functions)
- **G — Global:** The module-level scope (top of the file)
- **B — Built-in:** Python's built-in names like `len`, `print`, `range`

Python searches these scopes in order and uses the first match it finds.

**[DEMO]**

```python
x = 'global'

def outer():
    x = 'enclosing'

    def inner():
        x = 'local'
        print(x)    # Local — finds 'local' first

    inner()
    print(x)    # Enclosing — inner is done, we're in outer's scope

outer()
print(x)    # Global — outer is done
```

Output:

```text
local
enclosing
global
```

Each level of scope has its own `x`. The inner function sees only its own local `x`. The outer function sees its own `x`. The module-level code sees the global `x`.

**[DEMO — when no local variable exists]**

```python
name = 'Global Name'

def show():
    print(name)    # No local 'name' — Python goes to enclosing, then global

show()
```

Output:

```text
Global Name
```

Python walks up the LEGB chain until it finds the name. If it reaches Built-in scope without finding it, it raises `NameError`."

---

## [03:00 – 04:30] The nonlocal Keyword

**[SHOW SLIDE: "nonlocal — Modify Enclosing Scope Variables"]**

"Module 08 introduced `global` — which allows a nested function to modify a module-level variable. `nonlocal` is the equivalent for the enclosing function's scope — it allows an inner function to modify a variable defined in the enclosing function.

**[DEMO]**

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())    # 1
print(counter())    # 2
print(counter())    # 3
```

Output:

```text
1
2
3
```

`nonlocal count` tells Python that `count` inside `increment()` refers to the `count` in `make_counter()`'s scope — not a new local. This is the foundation of **closures** — a function that captures and remembers variables from its enclosing scope."

---

## [04:30 – 06:00] Closures

**[SHOW SLIDE: "Closures — Functions That Remember Their Environment"]**

"A **closure** is a function that carries its enclosing scope's variables with it, even after the enclosing function has returned.

In the `make_counter()` example, `counter` is a closure. After `make_counter()` returns, its local `count` variable is no longer in a live call stack — but `counter` still has access to it, because the closure captured it.

**[DEMO — practical closure: multiplier factory]**

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor    # captures 'factor' from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))    # 10
print(triple(5))    # 15
print(double(7))    # 14
```

Each call to `make_multiplier()` creates a separate closure with its own `factor`. `double` captured `factor=2`. `triple` captured `factor=3`. They are completely independent.

Closures are one of the most powerful patterns in Python — used extensively in decorators, callbacks, and functional programming."

---

## [06:00 – 09:00] Recursion — Functions That Call Themselves

**[SHOW SLIDE: "Recursion — Breaking a Problem into Smaller Copies"]**

"A **recursive** function is one that calls itself. Every recursive function needs two things:

1. A **base case** — a condition that stops the recursion
2. A **recursive case** — the function calling itself with a smaller or simpler argument

**[DEMO — factorial]**

```python
def factorial(n):
    if n == 0:
        return 1        # base case
    return n * factorial(n - 1)    # recursive case

print(factorial(5))
```

Output:

```text
120
```

Trace it: `factorial(5)` → `5 * factorial(4)` → `5 * 4 * factorial(3)` → ... → `5 * 4 * 3 * 2 * 1 * factorial(0)` → `5 * 4 * 3 * 2 * 1 * 1` = `120`.

The base case `n == 0` stops the recursion. Without it, the function calls itself forever.

### Call Stack

Every function call pushes a **stack frame** onto the call stack — a record of the local variables and the return address. When a function returns, its frame is popped.

For `factorial(5)`, the call stack looks like:

```text
factorial(5) → factorial(4) → factorial(3) → factorial(2) → factorial(1) → factorial(0)
```

Six frames deep. When `factorial(0)` returns `1`, each frame unwinds and computes its result.

### RecursionError

If the base case is never reached, Python eventually hits the maximum recursion depth and raises `RecursionError: maximum recursion depth exceeded`.

**[DEMO]**

```python
def bad_recursion(n):
    return bad_recursion(n - 1)    # no base case

bad_recursion(1)
```

Output:

```text
RecursionError: maximum recursion depth exceeded
```

Python's default recursion limit is 1,000 frames. You can check it with `import sys; sys.getrecursionlimit()`."

---

## [09:00 – 11:00] More Recursive Examples

**[SHOW SLIDE: "Classic Recursive Problems"]**

"### Sum of a List

```python
def list_sum(lst):
    if not lst:
        return 0    # base case: empty list
    return lst[0] + list_sum(lst[1:])    # head + sum of tail

print(list_sum([1, 2, 3, 4, 5]))
```

Output: `15`

Trace: `1 + list_sum([2,3,4,5])` → `1 + 2 + list_sum([3,4,5])` → ... → `1+2+3+4+5 + list_sum([])` → `1+2+3+4+5+0` = `15`.

### Fibonacci Sequence

```python
def fibonacci(n):
    if n <= 1:
        return n    # base cases: fibonacci(0)=0, fibonacci(1)=1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=' ')
```

Output: `0 1 1 2 3 5 8 13`

Note: This naive recursive Fibonacci is clear and elegant but very slow for large `n` — it recomputes the same values many times. For production use, you would add memoization (caching results) or use iteration. But as a demonstration of recursion, it is the classic example.

### When to Use Recursion

Recursion shines when the problem is naturally recursive — when it breaks down into identical smaller sub-problems. Tree traversal, file system scanning, parsing nested data, divide-and-conquer algorithms — these are natural fits.

For simple counting or list iteration, a `for` loop is more efficient and easier to read."

---

## [11:00 – 12:15] Namespaces

**[SHOW SLIDE: "Namespaces — Dictionaries of Names"]**

"A **namespace** is a mapping from names to objects — essentially a dictionary. When you write `x = 5`, Python adds `'x': 5` to the current namespace.

Python maintains several namespaces simultaneously:

- **Local namespace:** One per function call. Created when the function is called, destroyed when it returns.
- **Global namespace:** One per module. Lives as long as the module is loaded.
- **Built-in namespace:** One per Python interpreter session. Contains all built-in functions and exceptions.

You can inspect the current global namespace with `globals()` and the local namespace with `locals()`:

**[DEMO]**

```python
>>> x = 10
>>> y = 20
>>> 'x' in globals()
True
>>> globals()['x']
10
```

Namespaces are why Python can have variables with the same name in different scopes without conflict — they live in separate namespace dictionaries."

---

## [12:15 – 13:45] Putting It Together — Counter Closure + Recursive Display

**[DEMO — live code]**

```python
# scope_demo.py
# Demonstrates closures and recursion together
# Module 09 Lab — CIS-1310


def make_counter(start=0, step=1):
    '''Create a counter closure.'''
    count = start

    def increment():
        nonlocal count
        count += step
        return count

    def reset():
        nonlocal count
        count = start

    return increment, reset


def count_down(n):
    '''Recursively print a countdown from n to 0.'''
    if n < 0:
        return
    print(n, end=' ')
    count_down(n - 1)


# Test counter closure
inc, rst = make_counter(start=0, step=5)
print('Counter by 5s:')
print(inc(), inc(), inc(), inc())

rst()
print('After reset:', inc())

# Test recursion
print('\nCountdown from 10:')
count_down(10)
print()
```

Output:

```text
Counter by 5s:
5 10 15 20
After reset: 5

Countdown from 10:
10 9 8 7 6 5 4 3 2 1 0
```

---

## [13:45 – 15:00] PCAP Exam Tips and Wrap-Up

**[SHOW SLIDE: "Module 09 — PCAP Alignment"]**

"Key exam take-aways:

**1.** LEGB: Local → Enclosing → Global → Built-in. Python searches in this order.

**2.** `global x` inside a function references the module-level `x`. `nonlocal x` references the enclosing function's `x`.

**3.** A recursive function must have a base case that stops the recursion.

**4.** No base case → `RecursionError: maximum recursion depth exceeded`.

**5.** A closure is a function that captures variables from its enclosing scope. The captured variables live as long as the closure exists.

**6.** `RecursionError` is the exception for exceeded recursion depth — distinct from `StackOverflowError` in other languages.

**7.** `locals()` and `globals()` return dictionaries of the current local and global namespaces.

Module 10 covers dictionaries — Python's most powerful and flexible mapping type. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 09 — Scopes, Namespaces, and Recursion]**

---

## Additional Resources

- [Python for Everybody — Chapter 4](https://www.py4e.com/book) — Functions (includes scope discussion)
- [Official Python Docs — Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Official Python Docs — sys.getrecursionlimit()](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit)
- [Real Python — Understanding Scope](https://realpython.com/python-scope-legb-rule/)
