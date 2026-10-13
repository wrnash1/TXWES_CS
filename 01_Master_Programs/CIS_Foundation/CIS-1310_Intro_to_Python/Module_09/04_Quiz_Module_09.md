# Quiz: Module 09 — Scopes, Namespaces, and Recursion

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 09 topics.

---

### Question 1

In what order does Python search scopes when resolving a variable name?

- A) Global → Local → Enclosing → Built-in
- B) Built-in → Global → Enclosing → Local
- C) Local → Enclosing → Global → Built-in
- D) Local → Global → Enclosing → Built-in

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Global is not searched first. Python always searches the innermost scope first — starting with Local.
- *Why B is incorrect:* Built-in is the last resort, not the first. Searching Built-in first would mean Python ignores all user-defined variables.
- *Why C is correct:* LEGB stands for Local → Enclosing → Global → Built-in. Python searches these scopes in this exact order and uses the first match found.
- *Why D is incorrect:* Enclosing scope (the outer function's scope) is searched before Global. This order matters in nested functions.

---

### Question 2

What is the output of this code?

```python
x = 'global'

def outer():
    x = 'enclosing'
    def inner():
        print(x)
    inner()

outer()
print(x)
```

- A) `global` then `global`
- B) `enclosing` then `global`
- C) `enclosing` then `enclosing`
- D) `global` then `enclosing`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* When `inner()` runs, it has no local `x`, so Python searches Enclosing — and finds `x = 'enclosing'` in `outer()`. It does not skip to Global.
- *Why B is correct:* `inner()` has no local `x`, so LEGB finds `x = 'enclosing'` in the Enclosing scope. After `outer()` returns, the module-level `print(x)` uses the Global `x = 'global'`.
- *Why C is incorrect:* The second `print(x)` is at module level — there is no `outer()` in scope. The module-level `x` is `'global'`.
- *Why D is incorrect:* `inner()` has no local `x`, so it searches Enclosing first (not Global). It finds `'enclosing'`, not `'global'`.

---

### Question 3

What keyword allows an inner function to modify a variable in the directly enclosing function's scope?

- A) `global`
- B) `enclosing`
- C) `outer`
- D) `nonlocal`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `global` reaches the module-level namespace, not the enclosing function's scope. Using `global x` inside a nested function when there is no module-level `x` creates a new global rather than modifying the enclosing `x`.
- *Why B is incorrect:* `enclosing` is not a Python keyword. It is part of the LEGB description, not actual syntax.
- *Why C is incorrect:* `outer` is not a Python keyword. It is a conventional function name in examples.
- *Why D is correct:* `nonlocal x` declares that `x` inside the inner function refers to the nearest enclosing function that has a variable named `x`. This is the only way to assign to an enclosing scope variable without creating a new local.

---

### Question 4

What is the output of this code?

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = make_counter()
print(c())
print(c())
print(c())
```

- A) `1` then `1` then `1`
- B) `0` then `1` then `2`
- C) `1` then `2` then `3`
- D) `NameError` — `count` is not defined inside `increment`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Each call does not reset `count`. `nonlocal count` means `count` persists in `make_counter`'s scope between calls to `increment()`.
- *Why B is incorrect:* The first call increments `count` from 0 to 1 and returns 1, not 0. The increment happens before the return.
- *Why C is correct:* `count` starts at 0 in `make_counter()`. Each call to `c()` runs `increment()`, which uses `nonlocal count` to increment the shared `count`. Calls return 1, 2, 3.
- *Why D is incorrect:* `nonlocal count` successfully links `increment()`'s `count` to `make_counter()`'s `count`. No `NameError` occurs.

---

### Question 5

Which of the following is a correct recursive function for computing `n!` (n factorial)?

- A) `def factorial(n): return n * factorial(n)`
- B) `def factorial(n): if n == 0: return 0; return n * factorial(n - 1)`
- C) `def factorial(n): if n == 0: return 1; return n * factorial(n - 1)`
- D) `def factorial(n): return factorial(n - 1) * n if n > 0`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* There is no base case. `factorial(n)` calls `factorial(n)` endlessly — infinite recursion → `RecursionError`.
- *Why B is incorrect:* The base case returns `0` instead of `1`. `0! = 1` by mathematical definition. Returning `0` would make every factorial equal to `0` because any number multiplied by `0` is `0`.
- *Why C is correct:* Base case `n == 0` returns `1` (correct — `0! = 1`). Recursive case `n * factorial(n - 1)` moves toward the base case by decrementing `n`. This is the standard correct implementation.
- *Why D is incorrect:* This is a syntax error — `return ... if condition` without an `else` is invalid Python. A ternary expression requires both `if` and `else`.

---

### Question 6

What is the value returned by `factorial(4)` where `factorial` is the correct recursive implementation?

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

- A) `10`
- B) `16`
- C) `24`
- D) `120`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `10` would be `1+2+3+4` — this is a sum, not a factorial. Factorial multiplies, it does not add.
- *Why B is incorrect:* `16` would be `4**2` — this is exponentiation, not factorial.
- *Why C is correct:* `4! = 4 × 3 × 2 × 1 × 1 = 24`. The call trace: `4 * factorial(3)` → `4 * 3 * factorial(2)` → `4 * 3 * 2 * factorial(1)` → `4 * 3 * 2 * 1 * factorial(0)` → `4 * 3 * 2 * 1 * 1 = 24`.
- *Why D is incorrect:* `120` is `5!`, not `4!`. This is an off-by-one error — a common trap when tracing recursion.

---

### Question 7

What exception does Python raise when a recursive function has no base case and calls itself until the call stack is full?

- A) `StackOverflowError`
- B) `MemoryError`
- C) `RuntimeError`
- D) `RecursionError`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `StackOverflowError` is the Java and C++ equivalent. Python has its own specific exception name.
- *Why B is incorrect:* `MemoryError` is raised when Python cannot allocate memory for an object — a different kind of resource exhaustion.
- *Why C is incorrect:* `RuntimeError` is a generic runtime exception. While `RecursionError` is technically a subclass of `RuntimeError`, the PCAP exam expects the specific class name `RecursionError`.
- *Why D is correct:* Python raises `RecursionError: maximum recursion depth exceeded` when the call stack reaches the recursion limit (default: 1,000 frames). This is the Python-specific exception for infinite recursion.

---

### Question 8

What does `globals()` return when called inside a Python function?

- A) A dictionary of the function's local variables
- B) A dictionary of the module-level (global) namespace
- C) A list of all variable names visible from the current scope
- D) A tuple of all built-in names

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `locals()` returns the function's local variables. `globals()` always returns the module-level namespace regardless of where it is called.
- *Why B is correct:* `globals()` returns the global (module-level) namespace as a live dictionary. You can read and even modify module-level variables through it: `globals()['x']` is the same object as the module-level `x`.
- *Why C is incorrect:* Neither `globals()` nor `locals()` returns a combined list of everything visible. They each return one specific namespace. LEGB lookup is done automatically by the interpreter, not through these functions.
- *Why D is incorrect:* Built-in names are in the `builtins` module, accessible via `import builtins; dir(builtins)`. `globals()` does not include built-ins.

---

### Question 9

What is the output of this code?

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
```

- A) `10` then `10`
- B) `10` then `15`
- C) `15` then `15`
- D) `TypeError` — `factor` is not defined inside `multiply`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `triple` captures `factor=3`, not `factor=2`. The two closures are independent — each call to `make_multiplier()` creates a separate captured `factor`.
- *Why B is correct:* `double` captures `factor=2` → `double(5) = 5 * 2 = 10`. `triple` captures `factor=3` → `triple(5) = 5 * 3 = 15`. Each closure has its own independent copy of `factor`.
- *Why C is incorrect:* `double` captures `factor=2`, not `factor=3`. `double(5) = 10`, not `15`.
- *Why D is incorrect:* `factor` is captured from the enclosing `make_multiplier()` scope. Python's closure mechanism makes it available inside `multiply` without any error.

---

### Question 10

What does this code print?

```python
x = 'module'

def outer():
    x = 'outer'
    def inner():
        global x
        x = 'changed by inner'
    inner()
    print(x)

outer()
print(x)
```

- A) `outer` then `outer`
- B) `changed by inner` then `changed by inner`
- C) `outer` then `changed by inner`
- D) `changed by inner` then `outer`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `global x` inside `inner()` makes `inner()` reach the module-level `x`, not `outer()`'s `x`. So `inner()` modifies the module-level `x` to `'changed by inner'`. But `outer()`'s `print(x)` still sees `outer()`'s own local `x = 'outer'` — `outer()`'s variable is unaffected.
- *Why B is incorrect:* `outer()`'s local `x` is not the global `x`. `global x` in `inner()` bypasses the Enclosing scope entirely and goes directly to the Global level. `outer()`'s `x` remains `'outer'`.
- *Why C is correct:* `inner()` uses `global x`, which modifies the module-level `x` from `'module'` to `'changed by inner'`. `outer()`'s `print(x)` uses `outer()`'s local `x = 'outer'` (Enclosing → Local lookup from outer's perspective). The final `print(x)` at module level sees the now-changed global `x = 'changed by inner'`.
- *Why D is incorrect:* This reverses the output order. `outer()`'s `print(x)` runs first (inside the `outer()` call) and prints `'outer'`. The module-level `print(x)` runs second and prints `'changed by inner'`.

---

### Question 11

What is the output of this code?

```python
x = 1

def outer():
    x = 2
    def inner():
        x = 3
        print(x)
    inner()
    print(x)

outer()
print(x)
```

- A) `3` then `2` then `1`
- B) `1` then `2` then `3`
- C) `3` then `3` then `3`
- D) `3` then `2` then `3`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `inner()` has its own local `x = 3`, printed first. `outer()` has its own local `x = 2`, printed second. The module-level `x = 1` is printed last. Each scope is independent — no `global` or `nonlocal` statement connects them.
- *Why B is incorrect:* This is the reverse order. `inner()` runs before `outer()`'s `print(x)`, and the module-level print runs last, not first.
- *Why C is incorrect:* Each function's `x` is a separate local variable. Assignment inside a function does not propagate outward without `nonlocal` or `global`.
- *Why D is incorrect:* The module-level `x` is `1`, not `3`. `inner()`'s local `x = 3` is discarded when `inner()` returns.

---

### Question 12

A function has an `UnboundLocalError` when trying to increment a variable from an enclosing function. Which keyword fixes this?

- A) `global`
- B) `nonlocal`
- C) `outer`
- D) `enclosing`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `global` reaches the module-level scope, not the immediately enclosing function's scope. Using `global` would bind the name to the module level, which is a different variable.
- *Why B is correct:* `nonlocal` declares that a name refers to the nearest enclosing function's scope (not the module level). It is the correct keyword for modifying a variable defined in an outer function from an inner function.
- *Why C is incorrect:* `outer` is not a Python keyword. There is no such built-in declaration for accessing enclosing scopes.
- *Why D is incorrect:* `enclosing` is not a Python keyword. LEGB's E (Enclosing) is a concept, not a keyword you write in code.

---

### Question 13

Which of the following best defines a base case in a recursive function?

- A) The first call made to the function
- B) The condition under which the function calls itself
- C) The condition under which the function returns without making a recursive call
- D) The deepest level of recursion the function reaches

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The first call to the function is just the initial invocation. The base case is a logical condition, not a call sequence concept.
- *Why B is incorrect:* This describes the recursive case, not the base case. The recursive case is the branch where the function calls itself with a simpler input.
- *Why C is correct:* The base case is the terminating condition — the branch where the function returns a direct result without a recursive call. Without it, the function recurs indefinitely and raises `RecursionError`.
- *Why D is incorrect:* The deepest level of recursion is the call where the base case is hit, but that is a consequence of the base case, not its definition.

---

### Question 14

What value does this function return when called as `mystery(4)`?

```python
def mystery(n):
    if n == 0:
        return 0
    return n + mystery(n - 1)
```

- A) `4`
- B) `6`
- C) `10`
- D) `24`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `mystery(4)` does not simply return `n`. It returns `n + mystery(n-1)`, which accumulates values at each level.
- *Why B is incorrect:* `6` is `mystery(3)` — the sum of `3 + 2 + 1 + 0`. Tracing `mystery(4)` gives `4 + 3 + 2 + 1 + 0 = 10`.
- *Why C is correct:* Tracing: `mystery(4) = 4 + mystery(3) = 4 + 3 + mystery(2) = 4 + 3 + 2 + mystery(1) = 4 + 3 + 2 + 1 + mystery(0) = 4 + 3 + 2 + 1 + 0 = 10`.
- *Why D is incorrect:* `24` is `4!` (factorial of 4). This function computes the triangular sum `n*(n+1)/2`, not the factorial.

---

### Question 15

What does `locals()` return when called inside a function?

- A) A list of all global variable names
- B) A dictionary mapping the current function's local variable names to their values
- C) A tuple of the function's parameter names only
- D) The same object as `globals()`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `globals()` returns global variables; `locals()` returns the current function's local namespace, which is distinct from the global namespace.
- *Why B is correct:* `locals()` returns a dictionary of the current local symbol table. Inside a function, this includes parameters and any local variables defined up to the point of the call.
- *Why C is incorrect:* `locals()` returns all local variables (parameters plus locally defined names), not parameters only. It also returns a dict, not a tuple.
- *Why D is incorrect:* `locals()` and `globals()` return different objects. `globals()` is the module-level namespace; `locals()` inside a function is the function's local namespace.

---

### Question 16

What is Python's default maximum recursion depth, and how can you check it?

- A) `500`; check with `sys.max_depth`
- B) `1000`; check with `sys.getrecursionlimit()`
- C) `10000`; check with `sys.recursion_limit`
- D) `unlimited`; Python uses tail-call optimization

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The default limit is `1000`, not `500`. The attribute name `sys.max_depth` does not exist.
- *Why B is correct:* Python's default recursion limit is `1000` (meaning 1000 frames on the call stack). `sys.getrecursionlimit()` returns the current limit; `sys.setrecursionlimit(n)` changes it.
- *Why C is incorrect:* The default is `1000`, not `10000`. `sys.recursion_limit` is not a valid attribute name — it must be called as a function: `sys.getrecursionlimit()`.
- *Why D is incorrect:* CPython does NOT implement tail-call optimization (TCO). Deep recursion always risks `RecursionError`. This is a deliberate design choice in CPython.

---

### Question 17

What is the output of this code?

```python
def f():
    x = 10
    return lambda n: x * n

result = f()(3)
print(result)
```

- A) `30`
- B) `10`
- C) `3`
- D) `NameError: name 'x' is not defined`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `f()` executes, sets `x = 10`, and returns the lambda. The returned lambda is immediately called with `n=3`. The lambda closes over `x = 10` from `f()`'s scope. `10 * 3 = 30`.
- *Why B is incorrect:* `10` is the value of `x`, but the lambda computes `x * n`, not just `x`. With `n=3`, the result is `30`.
- *Why C is incorrect:* `3` is the value of `n`, but the lambda computes `x * n = 30`, not just `n`.
- *Why D is incorrect:* The lambda captures `x` from the enclosing `f()` scope — this is exactly what closures do. `x` is accessible inside the lambda even after `f()` returns.

---

### Question 18

What is a namespace in Python?

- A) A file that contains variable declarations for a module
- B) A mapping from names (identifiers) to objects
- C) The list of all reserved words Python will not allow as variable names
- D) The memory address range where a module's code is stored

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A namespace is not a file. It is a runtime data structure (implemented as a dictionary) that tracks name-to-object mappings.
- *Why B is correct:* Python namespaces are dictionaries. Every scope (local, enclosing, global, built-in) has its own namespace that maps identifier strings to the objects they refer to.
- *Why C is incorrect:* Reserved words (keywords) are part of Python's syntax, not a namespace. Namespaces contain user-defined names and built-ins, not keyword lists.
- *Why D is incorrect:* Namespaces have nothing to do with memory address ranges. Memory layout is handled by CPython's allocator independently of namespace resolution.

---

### Question 19

What does this code print?

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print(funcs[0](), funcs[1](), funcs[2]())
```

- A) `0 1 2`
- B) `0 0 0`
- C) `2 2 2`
- D) `1 2 3`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Each lambda does not capture the value of `i` at creation time. All three lambdas share a reference to the same `i` variable in the enclosing scope.
- *Why B is incorrect:* `i` is not frozen at `0`. After the loop finishes, `i` holds the last value (`2`), and all three lambdas return that value.
- *Why C is correct:* Python closures capture variables by reference, not by value. After the loop, `i = 2`. All three lambdas reference the same `i`, so they all return `2`. The fix is `lambda i=i: i` (default argument captures the value).
- *Why D is incorrect:* The lambdas return the current value of `i`, which is `2` after the loop. No lambda adds `1` to `i`.

---

### Question 20

When is the `global` keyword required inside a function?

- A) Any time you read a global variable inside a function
- B) Any time you use a global variable's name inside a function
- C) Only when you assign to a global variable name inside a function
- D) Only when the global variable is defined after the function definition

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Reading a global variable inside a function requires no special declaration. Python's LEGB rule automatically searches the Global scope if the name is not found locally.
- *Why B is incorrect:* Merely using (reading) a global name inside a function does not require `global`. The keyword is only needed for assignment.
- *Why C is correct:* Without `global x`, assigning `x = value` inside a function creates a new local variable named `x` that shadows the global. `global x` is required to make the assignment target the module-level `x` instead.
- *Why D is incorrect:* The order of definition does not matter. What matters is whether you are assigning (writing) to the name inside the function.
