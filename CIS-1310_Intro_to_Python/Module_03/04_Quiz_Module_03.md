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

---

### Question 11

What is the output of the following code?

```python
a, b, c = 1, 2, 3
a, b = b, a
print(a, b, c)
```

- A) `1 2 3`
- B) `2 1 3`
- C) `3 2 1`
- D) `SyntaxError: cannot unpack`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The line `a, b = b, a` swaps the values of `a` and `b`. After the swap `a = 2` and `b = 1`. Printing `a b c` gives `2 1 3`, not `1 2 3`.
- *Why B is correct:* Python evaluates the right side `b, a` as the tuple `(2, 1)` before any assignment occurs. Then `a` receives `2` and `b` receives `1`. `c` is unchanged at `3`. Output: `2 1 3`.
- *Why C is incorrect:* `c` retains its original value `3`. Only `a` and `b` are swapped.
- *Why D is incorrect:* `a, b = b, a` is valid Python tuple unpacking — a standard swap idiom. No `SyntaxError` is raised.

---

### Question 12

Which of the following is NOT a valid Python identifier?

- A) `_hidden`
- B) `__dunder__`
- C) `myVariable123`
- D) `return`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect (i.e., it IS valid):* `_hidden` is a valid identifier. A leading underscore is permitted and conventionally indicates a "private" or internal name.
- *Why B is incorrect (it IS valid):* `__dunder__` (double underscore on both sides) is valid and follows Python's dunder/magic method naming convention. It is widely used in the standard library.
- *Why C is incorrect (it IS valid):* `myVariable123` is valid — it starts with a letter, contains only letters, digits, and no special characters.
- *Why D is correct (it is INVALID):* `return` is a Python reserved keyword. Keywords cannot be used as identifiers. The PCAP exam requires knowing all Python keywords.

---

### Question 13

What does `print('A', 'B', 'C', sep='', end='!\n')` output?

- A) `A B C!`
- B) `ABC!`
- C) `A B C!` followed by a newline
- D) `A\nB\nC!`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `A B C!` would result from the default `sep=' '`. Since `sep=''` (empty string), no space is inserted between arguments.
- *Why B is correct:* `sep=''` means no separator between arguments, producing `ABC`. `end='!\n'` replaces the default newline with `!` followed by a newline. Final output: `ABC!` followed by a newline.
- *Why C is incorrect:* Spaces between letters would require `sep=' '`. `sep=''` is an empty string.
- *Why D is incorrect:* `\n` between each letter would require `sep='\n'`. The `end` parameter only affects what follows the final argument, not separators between arguments.

---

### Question 14

A student wants to display a number with exactly 8 characters total width, right-aligned, with 2 decimal places. Which f-string format spec achieves this?

- A) `f'{value:.2f}'`
- B) `f'{value:8.2f}'`
- C) `f'{value:2.8f}'`
- D) `f'{value:>8}'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `:.2f` specifies 2 decimal places but no total width. The output width equals however many characters the number needs.
- *Why B is correct:* `8.2f` means total field width of 8, 2 decimal places, fixed-point format. The number is right-aligned by default within the 8-character field. For example, `f'{3.14:8.2f}'` produces `    3.14` (4 leading spaces + 4 characters for `3.14`).
- *Why C is incorrect:* `2.8f` reverses the numbers — 2 total width and 8 decimal places, which would produce a wide number, not a narrow one. The format spec order is `width.precisiontype`.
- *Why D is incorrect:* `>8` right-aligns within 8 characters but applies no decimal rounding. For a float this would give more decimal places than desired.

---

### Question 15

What is the output of this code?

```python
x = 7
x //= 2
x **= 2
print(x)
```

- A) `12.25`
- B) `9`
- C) `6.25`
- D) `7`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `12.25` would come from `(7 / 2) ** 2 = 3.5 ** 2 = 12.25` using true division. But `//=` is floor division: `7 // 2 = 3`.
- *Why B is correct:* `x //= 2` → `x = 7 // 2 = 3`. Then `x **= 2` → `x = 3 ** 2 = 9`. Result: `9`.
- *Why C is incorrect:* `6.25` = `2.5 ** 2`, which would only arise if `x` became `2.5` — impossible from floor division of integers.
- *Why D is incorrect:* `7` is the starting value, before any augmented assignments are applied.

---

### Question 16

Which of the following correctly reads an integer from the user and stores it?

- A) `n = input(int('Enter n: '))`
- B) `n = int(input('Enter n: '))`
- C) `n = input('Enter n: ', int)`
- D) `n = (int) input('Enter n: ')`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `int('Enter n: ')` tries to convert the prompt string `'Enter n: '` to an integer, which raises `ValueError` immediately — before any user input is received.
- *Why B is correct:* The correct pattern is to call `input()` first (which returns a `str`), then wrap it with `int()` to convert: `n = int(input('Enter n: '))`. This is the standard Python idiom.
- *Why C is incorrect:* `input()` accepts only one argument — the prompt string. It does not accept a type argument. This raises `TypeError`.
- *Why D is incorrect:* `(int) input(...)` is not valid Python syntax. C-style casting with parenthesized type names is not how Python works.

---

### Question 17

What is the output of the following code?

```python
name = 'Python'
print(f'{"Hello":>10} {name}!')
```

- A) `Hello Python!`
- B) `     Hello Python!`
- C) `Hello      Python!`
- D) `SyntaxError: expressions in f-strings cannot use format specs with string literals`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `>10` right-aligns within a 10-character field. `'Hello'` is 5 characters, so 5 spaces are prepended: `     Hello`. The total output is `     Hello Python!`.
- *Why B is correct:* The f-string expression `{"Hello":>10}` formats the string literal `'Hello'` right-aligned in a 10-character wide field, producing `     Hello` (5 spaces + `Hello`). Then a space and `Python!` follow.
- *Why C is incorrect:* `Hello      Python!` would require left-alignment (`<10`), which pads spaces after the string.
- *Why D is incorrect:* F-strings fully support format specs applied to string literals inside `{}`. Expressions can be any valid Python expression, including string literals.

---

### Question 18

Python variable names are case-sensitive. What does the following code output?

```python
Score = 95
score = 80
SCORE = 70
print(Score + score + SCORE)
```

- A) `NameError` — Python sees three different variables
- B) `245`
- C) `95` — only the first assignment is used
- D) `SyntaxError` — you cannot have three versions of the same name`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Score`, `score`, and `SCORE` are three distinct, valid variable names in Python — all defined without error. No `NameError` occurs since all three are defined before `print()`.
- *Why B is correct:* All three variables are defined and hold integer values. `95 + 80 + 70 = 245`. Python's case sensitivity means these are three independent variables that can all coexist.
- *Why C is incorrect:* Python does not deduplicate variable names by case. Each name is a separate binding in the namespace.
- *Why D is incorrect:* Python has no restriction against having variables with the same spelling in different cases. It is poor style (PEP 8 warns against it), but it is not a syntax error.

---

### Question 19

Which of the following statements about Python's dynamic typing is TRUE?

- A) A variable's type is fixed when it is first assigned and cannot change
- B) Python infers types at compile time the first time a variable is used
- C) A variable can be rebound to a value of a different type at any time
- D) Dynamic typing means Python performs no type checking and all operations always succeed

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* This describes static typing (C, Java). Python variables are not bound to a type — only values have types. The variable is just a name pointing to an object.
- *Why B is incorrect:* Python does not compile to native code with type inference. Types are determined at runtime, not compile time.
- *Why C is correct:* In Python, variables are references to objects. You can do `x = 5` then `x = 'hello'` then `x = [1, 2, 3]` — the variable `x` simply points to a new object each time. The type is a property of the object, not the variable.
- *Why D is incorrect:* Dynamic typing does not mean "no type checking." Python checks types at runtime and raises `TypeError` when an operation is applied to incompatible types (e.g., `'hello' + 5`). The checking happens later (at runtime) rather than earlier (at compile time).

---

### Question 20

What does the following code print?

```python
total = 0
total += 10
total += 20
total -= 5
total *= 3
print(total)
```

- A) `75`
- B) `90`
- C) `25`
- D) `30`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Trace step by step: `total = 0` → `+= 10` → `10` → `+= 20` → `30` → `-= 5` → `25` → `*= 3` → `75`. Final value: `75`.
- *Why B is incorrect:* `90` would result if `*= 3` were applied before `-= 5`: `30 * 3 = 90`. But the operations execute in written order — subtraction before multiplication.
- *Why C is incorrect:* `25` is the intermediate value after the subtraction, before `*= 3` is applied.
- *Why D is incorrect:* `30` is the intermediate value after the second addition, before subtraction and multiplication.
