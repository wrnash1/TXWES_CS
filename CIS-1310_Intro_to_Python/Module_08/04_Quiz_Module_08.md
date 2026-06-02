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
