# Quiz: Module 03 — Variables and Basic I/O

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 03 topics.

---

### Question 1

What is the return type of Python's `input()` function regardless of what the user types?

- A) `int`
- B) `float`
- C) `str`
- D) The type depends on what the user types — numbers return `int`, text returns `str`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `input()` never returns an `int`, even if the user types a whole number. Python has no way to know what type the user intends — it always returns `str`.
- *Why B is incorrect:* `input()` never returns a `float`, even if the user types `3.14`. All input comes back as `str`.
- *Why C is correct:* `input()` always returns `str` — unconditionally. If you need a number, you must explicitly convert with `int()` or `float()`.
- *Why D is incorrect:* Python does not inspect what the user typed to decide on a return type. `input()` returns `str` every time, no matter what.

---

### Question 2

Which of the following best describes **type casting** in Python?

- A) The automatic conversion Python performs when a value of one type is assigned to a variable that previously held a different type
- B) The explicit conversion of a value from one data type to another using a built-in function such as `int()`, `float()`, or `str()`
- C) A compiler optimization that replaces dynamic type checks with faster static inferences at runtime
- D) The process of verifying that a variable name follows Python's identifier rules before binding it to a value

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python does not perform automatic type coercion on assignment. Reassigning a variable to a different type just updates what the variable points to — no conversion takes place.
- *Why B is correct:* Type casting is the programmer's explicit act of calling `int()`, `float()`, `str()`, `bool()`, etc. to convert a value to the desired type before use.
- *Why C is incorrect:* Python is an interpreted, dynamically typed language with no ahead-of-time compiler. Type information is tracked at runtime, not replaced with static inferences.
- *Why D is incorrect:* Checking identifier rules is part of Python's parser — it happens during lexical analysis, not during type conversion. These are separate concepts.

---

### Question 3

Which of the following is a **valid** Python variable name?

- A) `2nd_place`
- B) `user-score`
- C) `class`
- D) `_total_count`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `2nd_place` starts with a digit. Python identifiers must begin with a letter or underscore — never a digit. This raises `SyntaxError`.
- *Why B is incorrect:* `user-score` contains a hyphen, which is not allowed in identifiers. Python would interpret the `-` as a subtraction operator, making `user-score` a subtraction expression, not a valid name.
- *Why C is incorrect:* `class` is a Python reserved keyword used to define classes. Keywords cannot be used as variable names — this raises `SyntaxError`.
- *Why D is correct:* `_total_count` is perfectly valid. It starts with an underscore, contains only letters, digits, and underscores, and is not a reserved keyword. The leading underscore is a Python convention for "internal/private" variables.

---

### Question 4

What error is raised when this code runs and the user enters `25`?

```python
age = input('Enter your age: ')
print(age + 10)
```

- A) `SyntaxError` — the `+` operator cannot be used with `input()`
- B) `ValueError` — `input()` cannot process integer strings
- C) `TypeError` — cannot add `str` and `int`
- D) No error — Python automatically converts the string `'25'` to `25`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* There is no `SyntaxError` — the code is syntactically valid. The error only occurs at runtime when Python tries to execute `age + 10`.
- *Why B is incorrect:* `ValueError` is raised when a value has the wrong content for a function (like `int('hello')`). Here the issue is a type mismatch, not a bad value — so `TypeError` is the correct error.
- *Why C is correct:* `input()` returns `str`. `age` holds the string `'25'`. When Python tries to execute `'25' + 10`, it encounters a `str` and an `int` — incompatible types for `+`. Python raises `TypeError: can only concatenate str (not "int") to str`.
- *Why D is incorrect:* Python does NOT automatically convert string input to numeric types. This is the core behavior to memorize: `input()` always returns `str`, always requires explicit conversion.

---

### Question 5

What does the following code output?

```python
age = input('Enter your age: ')
print(age * 2)
```

If the user enters `5`:

- A) `10`
- B) `55`
- C) `TypeError: unsupported operand type`
- D) `ValueError: cannot multiply str`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `age` is a `str`, not an `int`. `str * int` does not multiply — it repeats the string. `'5' * 2` produces `'55'`, not `10`.
- *Why B is correct:* `input()` returns `'5'` (a string). `str * int` in Python is valid — it repeats the string. `'5' * 2` = `'55'`. This is a silent logical error that produces wrong output without raising an exception — one of the most dangerous kinds of bugs.
- *Why C is incorrect:* `str * int` is valid Python syntax and does not raise `TypeError`. That error would occur with `str + int`, not `str * int`.
- *Why D is incorrect:* `ValueError` is not raised here. `str * int` is a supported operation in Python — it repeats the string `int` times.

---

### Question 6

What does `print('hello', 'world', sep='-')` output?

- A) `hello world`
- B) `hello-world`
- C) `hello - world`
- D) `helloworld`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `hello world` would be the output with the default `sep=' '` (a single space). The `sep='-'` argument overrides that default.
- *Why B is correct:* The `sep` parameter specifies what goes between each argument passed to `print()`. With `sep='-'`, the separator is a hyphen. The result is `hello-world` — no spaces around the hyphen.
- *Why C is incorrect:* `hello - world` would require `sep=' - '` (space-hyphen-space). `sep='-'` uses only the hyphen with no surrounding spaces.
- *Why D is incorrect:* `helloworld` with no separator would require `sep=''` (empty string). `'-'` is a non-empty separator.

---

### Question 7

Which of the following f-strings correctly embeds the variable `price` rounded to two decimal places?

- A) `f'Price: {price}'`
- B) `f'Price: {price:.2f}'`
- C) `f'Price: {price, 2f}'`
- D) `f'Price: %(price).2f'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `f'Price: {price}'` embeds `price` but uses no format spec — the full float precision is displayed (e.g., `19.989999999`). You need `:.2f` for two decimal places.
- *Why B is correct:* Inside an f-string `{}`, a colon `:` separates the expression from the format spec. `.2f` means two decimal places, fixed-point notation. `f'Price: {price:.2f}'` is the correct syntax.
- *Why C is incorrect:* `{price, 2f}` is not valid f-string syntax. The colon `:` is required before the format spec — a comma is not used here.
- *Why D is incorrect:* `%(price).2f` is the old `%` string formatting style from Python 2. It is not f-string syntax, and it would not work inside an f-string.

---

### Question 8

What is the output of this code?

```python
x = 10
x += 5
x *= 2
x -= 3
print(x)
```

- A) `10`
- B) `27`
- C) `30`
- D) `22`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The augmented assignment operators modify `x` in place. Starting at `10` and applying three operations produces a result different from the starting value.
- *Why B is correct:* Trace it step by step: `x = 10` → `x += 5` makes `x = 15` → `x *= 2` makes `x = 30` → `x -= 3` makes `x = 27`. Result: `27`.
- *Why C is incorrect:* `30` is the result after `x *= 2` but before `x -= 3`. The final subtraction step is skipped in this reasoning.
- *Why D is incorrect:* `22` does not result from any correct tracing of the operations. Check the order: add first, then multiply, then subtract.

---

### Question 9

Which variable name best follows Python's PEP 8 naming conventions for a variable that stores a student's grade point average?

- A) `GPA`
- B) `gradePointAverage`
- C) `grade_point_average`
- D) `g`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `GPA` (all uppercase) follows the convention for **constants** in PEP 8, not variables. A variable that changes over time should use `snake_case`.
- *Why B is incorrect:* `gradePointAverage` uses `camelCase`, which is the convention in Java and JavaScript but NOT in Python. PEP 8 specifies `snake_case` for Python variable names.
- *Why C is correct:* `grade_point_average` is `snake_case` — all lowercase letters with words separated by underscores. This is the PEP 8 standard for Python variable and function names.
- *Why D is incorrect:* Single-letter variable names like `g` are acceptable only for simple loop counters or coordinates. A name storing something as meaningful as a GPA deserves a descriptive name.

---

### Question 10

What error does `int('3.14')` raise, and how do you fix it?

- A) `TypeError` — fix by using `float('3.14')` instead
- B) `ValueError` — fix by using `int(float('3.14'))`
- C) `SyntaxError` — fix by removing the quotes: `int(3.14)`
- D) No error — `int()` accepts decimal strings and truncates them automatically

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The error is `ValueError`, not `TypeError`. `int()` receives a `str` argument (correct type), but the string `'3.14'` contains a decimal point, which `int()` cannot parse. The fix using `float('3.14')` produces a float, not an int — you still need `int()` wrapped around it.
- *Why B is correct:* `int('3.14')` raises `ValueError: invalid literal for int() with base 10: '3.14'`. The fix is to chain the conversions: `float('3.14')` converts the string to the float `3.14`, then `int(3.14)` truncates it to `3`.
- *Why C is incorrect:* `int('3.14')` has no `SyntaxError` — it is valid Python syntax. The error occurs at runtime when `int()` tries to parse the string. Removing the quotes gives `int(3.14)`, which works but loses the `str` input scenario.
- *Why D is incorrect:* `int()` does NOT accept strings containing decimal points. It only accepts strings of whole-number digits (with optional leading sign). A decimal point in the string always raises `ValueError`.
