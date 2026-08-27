# Quiz: Module 08 — Functions and Parameter Passing

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 08 topics.

---

### Question 1

What does a function return if it has no `return` statement?

- A) `0`
- B) `False`
- C) `None`
- D) `SyntaxError` — all functions must have a `return` statement

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Python functions return `None` by default, not `0`. Only a `return 0` statement would give `0`.
- *Why B is incorrect:* `False` is the boolean false value, not the default return. Although `None` is falsy, they are different objects.
- *Why C is correct:* Any Python function without a `return` statement (or with a bare `return`) implicitly returns `None`. This is a fundamental Python rule.
- *Why D is incorrect:* `return` is optional in Python. A function that only performs side effects (like printing) legitimately has no `return` statement.

---

### Question 2

Which function definition is syntactically correct?

- A) `def f(a=1, b, c=3):`
- B) `def f(a, b=2, c=3):`
- C) `def f(a=1, b=2, c):`
- D) `def f(a=1, b, c):`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `a=1` is a default parameter followed by `b`, which has no default — `SyntaxError: non-default argument follows default argument`.
- *Why B is correct:* `a` has no default, `b` and `c` have defaults. Non-default parameters come before default parameters — this is the required order.
- *Why C is incorrect:* `a=1` and `b=2` have defaults, but `c` does not — `SyntaxError` for the same reason as A.
- *Why D is incorrect:* Same problem — `a=1` has a default, but `b` and `c` that follow it do not.

---

### Question 3

What type is `args` inside a function defined as `def f(*args)`?

- A) `list`
- B) `dict`
- C) `tuple`
- D) `set`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `*args` collects extra positional arguments into a `tuple`, not a `list`. This is a common misconception.
- *Why B is incorrect:* `dict` is the type of `**kwargs`, which collects keyword arguments.
- *Why C is correct:* `*args` creates a `tuple` containing all extra positional arguments passed to the function. You can iterate over it, index it, and pass it to functions like `sum()`.
- *Why D is incorrect:* Sets are not used for argument collection in Python.

---

### Question 4

What does the following code output?

```python
def greet(name, greeting='Hello'):
    return f'{greeting}, {name}!'

print(greet('Alice'))
print(greet('Bob', 'Hi'))
```

- A) `Hello, Alice!` then `Hello, Bob!`
- B) `Hello, Alice!` then `Hi, Bob!`
- C) `Alice` then `Bob`
- D) `TypeError` — `greeting` is required

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The second call overrides the default — `greet('Bob', 'Hi')` passes `'Hi'` as the `greeting` argument.
- *Why B is correct:* The first call uses the default `greeting='Hello'`, producing `Hello, Alice!`. The second call overrides it with `'Hi'`, producing `Hi, Bob!`.
- *Why C is incorrect:* The function returns the full formatted string, not just the name.
- *Why D is incorrect:* `greeting` has a default value, making it optional. No `TypeError` is raised when it is omitted.

---

### Question 5

What does `kwargs` contain inside a function `def f(**kwargs)` when called as `f(x=1, y=2, z=3)`?

- A) `(1, 2, 3)` — a tuple of values
- B) `['x', 'y', 'z']` — a list of keys
- C) `{'x': 1, 'y': 2, 'z': 3}` — a dict of key-value pairs
- D) `(('x', 1), ('y', 2), ('z', 3))` — a tuple of pairs

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The tuple `(1, 2, 3)` contains only values. `**kwargs` includes both the names and the values.
- *Why B is incorrect:* `kwargs` contains both keys and values — not just keys.
- *Why C is correct:* `**kwargs` collects all keyword arguments into a `dict`. Each keyword argument becomes a key-value pair.
- *Why D is incorrect:* `kwargs` is a `dict`, not a tuple of pairs.

---

### Question 6

What is the output of this code?

```python
x = 5

def change():
    x = 100

change()
print(x)
```

- A) `100`
- B) `5`
- C) `None`
- D) `UnboundLocalError`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The `x = 100` inside `change()` creates a new **local** variable named `x`. It does not modify the global `x`.
- *Why B is correct:* The `x` inside `change()` is a local variable — completely separate from the global `x`. The global `x` remains `5`.
- *Why C is incorrect:* `None` would result from printing the return value of `change()`, not from printing the global `x`.
- *Why D is incorrect:* `UnboundLocalError` would occur if the function tried to read `x` before assigning it, combined with a later assignment. Here the assignment is straightforward and does not trigger this error.

---

### Question 7

What is the output of this code?

```python
def add(a, b):
    total = a + b

result = add(3, 4)
print(result)
```

- A) `7`
- B) `None`
- C) `0`
- D) `TypeError` — `add` does not return a value

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The function computes `7` but never returns it — `total` is a local variable that is discarded when the function ends.
- *Why B is correct:* `add()` has no `return` statement. Python returns `None` implicitly. `result` is assigned `None`, and `print(result)` prints `None`.
- *Why C is incorrect:* There is no default numeric return value. The implicit return is `None`.
- *Why D is incorrect:* The function call itself succeeds — there is no `TypeError`. The only issue is that the programmer forgot to `return total`.

---

### Question 8

Which call correctly passes `b` as a keyword argument and `a` as a positional argument to `def f(a, b)`?

- A) `f(b=2, 1)` — keyword before positional
- B) `f(1, b=2)` — positional first, then keyword
- C) `f(a=1, 2)` — keyword before positional
- D) `f(b=2, a=1)` is the only valid keyword syntax

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `f(b=2, 1)` places a positional argument after a keyword argument — `SyntaxError: positional argument follows keyword argument`.
- *Why B is correct:* `f(1, b=2)` passes `1` positionally to `a`, then `b=2` as a keyword. Positional arguments must come before keyword arguments — this is valid.
- *Why C is incorrect:* Same problem as A — positional `2` follows keyword `a=1` — `SyntaxError`.
- *Why D is incorrect:* `f(b=2, a=1)` is also valid. You can pass all arguments as keywords in any order.

---

### Question 9

What happens on the second call of the following code?

```python
def append_item(item, lst=[]):
    lst.append(item)
    return lst

print(append_item('x'))
print(append_item('y'))
```

- A) `['x']` then `['y']`
- B) `['x']` then `['x', 'y']`
- C) `['x']` then `['y']`  — same as A but for a different reason
- D) `TypeError` — lists cannot be default argument values

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The default list `[]` is created **once** at function definition time and shared across all calls. The second call reuses the same list, which already contains `'x'` from the first call.
- *Why B is correct:* This is the mutable default argument trap. The default `lst=[]` is one shared object. First call appends `'x'` → `['x']`. Second call appends `'y'` to the same list → `['x', 'y']`.
- *Why C is incorrect:* The reason matters — C describes the same output as A but for a different reason. Neither A nor C describes the actual output.
- *Why D is incorrect:* Python allows mutable objects (lists, dicts) as default values — it is syntactically valid. The bug is behavioral, not a TypeError.

---

### Question 10

What is the correct way to call `def describe(name, age, city='Unknown')` using keyword arguments with `city` and `age` provided but `name` positional?

- A) `describe(name, age=25, city='Dallas')`
- B) `describe('Alice', age=25, city='Dallas')`
- C) `describe(age=25, 'Alice', city='Dallas')`
- D) `describe('Alice', city='Dallas', 25)`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `name` in the call would be treated as a variable name, not the string `'Alice'`. The call would fail with `NameError` unless a variable named `name` is defined. The intent is `describe('Alice', ...)`.
- *Why B is correct:* `'Alice'` is passed positionally to `name`, then `age=25` and `city='Dallas'` are keyword arguments. Positional comes first — valid Python.
- *Why C is incorrect:* `age=25` is a keyword argument followed by `'Alice'`, which is positional — `SyntaxError: positional argument follows keyword argument`.
- *Why D is incorrect:* `city='Dallas'` is a keyword argument followed by `25`, which is positional — same `SyntaxError`.

---

### Question 11

What does the following code output?

```python
def mystery(a, b, c=10):
    return a + b + c

print(mystery(1, 2))
print(mystery(1, 2, 3))
print(mystery(c=5, a=2, b=3))
```

- A) `13` then `6` then `10`
- B) `13` then `13` then `10`
- C) `13` then `6` then `13`
- D) `TypeError` — keyword arguments cannot be passed out of order

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* First call: `1 + 2 + 10 = 13` (c uses its default). Second call: `1 + 2 + 3 = 6` (c overridden to 3). Third call: `a=2, b=3, c=5` → `2 + 3 + 5 = 10`. Keyword arguments match by name regardless of order.
- *Why B is incorrect:* The second call passes `c=3`, not the default `c=10`. `1 + 2 + 3 = 6`, not `13`.
- *Why C is incorrect:* The third call uses `c=5`, not the default `c=10`. `2 + 3 + 5 = 10`, not `13`.
- *Why D is incorrect:* Python fully supports out-of-order keyword arguments. `mystery(c=5, a=2, b=3)` is valid — each parameter is matched by name.

---

### Question 12

What does `*` in `def f(a, *, b)` signify?

- A) `b` is a required positional argument
- B) `f` accepts any number of additional positional arguments between `a` and `b`
- C) `b` must be passed as a keyword argument — it cannot be passed positionally
- D) `SyntaxError` — a bare `*` is not valid in a parameter list

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `b` remains a required argument, but `*` forces it to be keyword-only. Calling `f(1, 2)` raises `TypeError` because `b` must be named.
- *Why B is incorrect:* A bare `*` does not collect extra positional arguments (that is `*args`). It is a separator that marks all following parameters as keyword-only.
- *Why C is correct:* A bare `*` in a parameter list signals that all parameters after it are keyword-only. `def f(a, *, b)` requires calling as `f(1, b=2)` — `f(1, 2)` raises `TypeError`.
- *Why D is incorrect:* A bare `*` is valid Python syntax (introduced in PEP 3102). It is used in many standard library functions to enforce keyword-only arguments.

---

### Question 13

What does calling `f(*[1, 2, 3])` do when `def f(a, b, c)` is defined?

- A) Raises `TypeError` — lists cannot be unpacked with `*`
- B) Passes the list itself as the first argument `a`
- C) Unpacks the list and passes `1` to `a`, `2` to `b`, `3` to `c`
- D) Passes `(1, 2, 3)` as a single tuple to `a`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `*` in a function call unpacks any iterable (lists, tuples, strings) into positional arguments. This is the call-site unpacking operator.
- *Why B is incorrect:* `*[1, 2, 3]` unpacks the list — it does not pass the list object itself. To pass the list as one argument, omit the `*`.
- *Why C is correct:* `*iterable` in a function call unpacks the iterable into separate positional arguments. `f(*[1, 2, 3])` is exactly equivalent to `f(1, 2, 3)`.
- *Why D is incorrect:* The result is three separate positional arguments, not a tuple. Tuple packing only happens with `*args` in the function definition, not at the call site.

---

### Question 14

What is the output of this code?

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(3))
```

- A) `NameError: name 'x' is not defined`
- B) `8`
- C) `5`
- D) `None`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `x` is captured by the `inner` function via closure — it retains access to `x` from the enclosing `outer` function's scope even after `outer` has returned.
- *Why B is correct:* `outer(5)` returns the `inner` function with `x=5` captured in its closure. `add5(3)` calls `inner(3)`, returning `5 + 3 = 8`. This is a basic closure — a concept tested on the PCAP exam.
- *Why C is incorrect:* `5` is just the value of `x`. The result is `x + y = 5 + 3 = 8`.
- *Why D is incorrect:* `inner` has an explicit `return` statement. It returns `x + y`, not `None`.

---

### Question 15

Which of the following correctly uses `**kwargs` to build and return a dictionary?

- A) `def build(**kwargs): return list(kwargs)`
- B) `def build(**kwargs): return kwargs`
- C) `def build(**kwargs): return tuple(kwargs)`
- D) `def build(**kwargs): return kwargs.values()`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `list(kwargs)` returns a list of the **keys only** (not the key-value pairs). The dictionary content is lost.
- *Why B is correct:* Inside the function, `kwargs` is already a `dict`. Returning it directly returns the full dictionary of keyword arguments and their values.
- *Why C is incorrect:* `tuple(kwargs)` returns a tuple of the **keys only**, just like `list(kwargs)`. Values are not included.
- *Why D is incorrect:* `kwargs.values()` returns only the values as a view object, losing the keys. The caller receives values without knowing which parameter name each came from.

---

### Question 16

What is the output of this code?

```python
def greet(name='World'):
    print(f'Hello, {name}!')

greet()
greet('Python')
greet(name='PCAP')
```

- A) `Hello, World!`, `Hello, Python!`, `Hello, PCAP!`
- B) `Hello, !`, `Hello, Python!`, `Hello, PCAP!`
- C) `Hello, name!`, `Hello, name!`, `Hello, name!`
- D) `TypeError: missing required argument`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* First call uses default `'World'`. Second call overrides positionally with `'Python'`. Third call overrides by keyword with `'PCAP'`. All three forms of passing the argument work correctly.
- *Why B is incorrect:* The default is `'World'`, not an empty string. `name='World'` means `name` is `'World'` when not supplied.
- *Why C is incorrect:* F-strings substitute the variable's value, not the variable name. `{name}` becomes whatever `name` holds, not the literal string `'name'`.
- *Why D is incorrect:* `name` has a default value, making it optional. No `TypeError` is raised when it is omitted.

---

### Question 17

What is the correct way to write a function that returns two values and captures both at the call site?

- A) `def f(): return (1, 2)` then `a, b = f()`
- B) `def f(): return 1; return 2` then `a, b = f()`
- C) `def f(): return [1, 2]` — lists cannot be unpacked
- D) Python functions cannot return more than one value

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* A function can return a tuple `(1, 2)`, and the caller can use tuple unpacking `a, b = f()` to assign each element to a separate variable. This is the standard Pythonic pattern for multiple return values.
- *Why B is incorrect:* A function stops executing at the first `return`. The second `return 2` is unreachable dead code — only `1` is ever returned.
- *Why C is incorrect:* Lists can absolutely be unpacked: `a, b = [1, 2]` works the same as tuple unpacking. The claim is false.
- *Why D is incorrect:* Python functions can return any object including tuples, lists, and dicts — which effectively allows returning any number of values via unpacking.

---

### Question 18

What is the purpose of a docstring in a Python function?

- A) It makes the function run faster by caching the result
- B) It is a string placed right after the `def` line that documents the function's purpose, parameters, and return value
- C) It defines the function's type annotations and is enforced at runtime
- D) It is a comment that is stripped by the interpreter and ignored entirely

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Docstrings have no effect on execution speed. Caching is done with `functools.lru_cache`, not docstrings.
- *Why B is correct:* A docstring is a triple-quoted string literal placed immediately after the `def` line (or class definition). Python stores it in the function's `__doc__` attribute. It is displayed by `help()` and IDEs. It is the standard way to document Python code.
- *Why C is incorrect:* Type annotations (e.g., `def f(x: int) -> str`) are separate from docstrings and are not enforced at runtime. Docstrings are plain text documentation.
- *Why D is incorrect:* Docstrings are NOT regular comments. They are string literals that Python retains in the `__doc__` attribute. They are not stripped — they are accessible programmatically.

---

### Question 19

What happens when a function modifies a mutable argument (a list) passed to it?

- A) Python creates a copy of the list before passing it — the original is unchanged
- B) The function can modify the original list because lists are passed by reference to the object
- C) `TypeError` is raised because functions cannot accept mutable arguments
- D) Python freezes the list to prevent modification

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python does NOT copy mutable objects when passing them. The function receives a reference to the same object. This is why the mutable default argument bug exists.
- *Why B is correct:* Python passes object references (sometimes called "pass by object reference" or "pass by assignment"). When you pass a list, the function gets a reference to the same list object. Calling `.append()`, `.pop()`, or any in-place modification on it modifies the original.
- *Why C is incorrect:* Functions can accept any Python object, mutable or immutable. There is no restriction.
- *Why D is incorrect:* Python has no automatic freeze mechanism for passed arguments. `frozenset` is the immutable analogue of `set`, but there is no `frozenlist`.

---

### Question 20

What does the following code output?

```python
def make_adder(n):
    return lambda x: x + n

add10 = make_adder(10)
add20 = make_adder(20)
print(add10(5), add20(5))
```

- A) `15 25`
- B) `15 15`
- C) `5 5`
- D) `NameError: name 'n' is not defined`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `make_adder(10)` returns a lambda that adds `10` to its argument, capturing `n=10`. `make_adder(20)` returns a separate lambda capturing `n=20`. `add10(5) = 15`, `add20(5) = 25`.
- *Why B is incorrect:* Each call to `make_adder()` creates a new closure with its own `n`. `add10` and `add20` capture different values of `n`.
- *Why C is incorrect:* The lambdas add `n` to the argument. `5 + 10 = 15`, not `5`.
- *Why D is incorrect:* `n` is captured in the closure from the enclosing `make_adder` function. It is accessible inside the lambda even after `make_adder` has returned.
