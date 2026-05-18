# Unit Test 1: Modules 1–4 — Python Fundamentals

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Coverage:** Module 1 (Intro), Module 2 (Variables/Types), Module 3 (Operators), Module 4 (Conversion/Input)
**Total:** 30 Questions | 3 points each = **90 points** + 10-point bonus question = **100 points possible**
**Suggested Time:** 60 minutes
**PCAP Alignment:** Sections 1 and 2

---

## Canvas Entry Instructions

- **Question Type:** Multiple Choice (unless marked **[SA]** — Short Answer entry in Canvas text field)
- **Points per question:** 3 (bonus question: 10)
- **Shuffle Questions:** No (present in order)
- **Shuffle Answers:** Yes
- **Time Limit:** 60 minutes recommended
- Correct answers marked with **← CORRECT**

> **Instructor Note:** This test is intentionally harder than the module quizzes. Questions require applying knowledge across topics and predicting non-obvious Python behavior. The synthesis and edge-case questions are PCAP exam level.

---

## Questions

---

### Question 1

What is the output of the following code?

```python
print("TX", "WES", sep="", end="!\n")
print("Go", "Rams", sep="-")
```

- A) `TXWES!\nGo-Rams`
- B) **`TXWES!` / `Go-Rams`** ← CORRECT
- C) `TX WES!` / `Go Rams`
- D) `TXWES` / `Go Rams!`

**Correct Answer: B**
**Explanation:** First `print()`: `sep=""` removes spaces between `"TX"` and `"WES"`, producing `TXWES`. `end="!\n"` appends `!` followed by a newline, so the line reads `TXWES!`. Second `print()`: default `end="\n"`, `sep="-"` between `"Go"` and `"Rams"` produces `Go-Rams`.

---

### Question 2

A developer runs the following code. What is the output?

```python
result = print("Hello")
print(result is None)
```

- A) `Hello` / `False`
- B) `None` / `True`
- C) **`Hello` / `True`** ← CORRECT
- D) `Hello` / `<class 'NoneType'>`

**Correct Answer: C**
**Explanation:** `print("Hello")` displays `Hello` (as a side effect) and returns `None`. So `result = None`. `None is None` is `True`. The second `print()` then displays `True`. Note: `result is None` is the idiomatic way to check for `None`.

---

### Question 3

Which of the following violates PEP 8 style guidelines?

- A) `MAX_CONNECTIONS = 100`
- B) `class DatabaseManager:`
- C) **`def CalculateAverage(scores):`** ← CORRECT
- D) `user_email = "admin@txwes.edu"`

**Correct Answer: C**
**Explanation:** PEP 8 specifies that function names should use `snake_case`, not `PascalCase`. `CalculateAverage` uses PascalCase, which is reserved for class names. The correct name would be `calculate_average`. Constants use `UPPER_SNAKE_CASE` (option A is correct), classes use PascalCase (option B is correct), and variables use snake_case (option D is correct).

---

### Question 4

What type of error does the following code raise, and at which line?

```python
x = 10
y = 0
z = x + y
print("Result: " + z)
```

- A) `ZeroDivisionError` at line 2
- B) `SyntaxError` at line 4
- C) **`TypeError` at line 4** ← CORRECT
- D) `NameError` at line 3

**Correct Answer: C**
**Explanation:** Lines 1–3 execute successfully: `x = 10`, `y = 0`, `z = 10`. The error occurs at line 4 where Python attempts to concatenate a string (`"Result: "`) with an integer (`z = 10`). This raises `TypeError: can only concatenate str (not "int") to str`. The fix: `print("Result: " + str(z))` or `print(f"Result: {z}")`.

---

### Question 5

What is the output of this code?

```python
x = 5
y = x
x = 10
print(y)
```

- A) `10` — `y` follows `x`
- B) **`5`** ← CORRECT
- C) `None`
- D) `NameError`

**Correct Answer: B**
**Explanation:** `y = x` makes `y` point to the integer object `5`. Then `x = 10` reassigns `x` to a new integer object `10`. Integers are **immutable** — reassigning `x` does not change the object that `y` still references. `y` remains `5`. (This would behave differently with mutable objects like lists.)

---

### Question 6

What is the output of the following code?

```python
a = 0b1111
b = 0xFF
c = 0o17
print(a == b, b == c, a == c)
```

- A) `True False False`
- B) `False True False`
- C) `False False True`
- D) **`False False True`** ← CORRECT

**Correct Answer: D**
**Explanation:** `0b1111` (binary) = 15. `0xFF` (hex) = 255. `0o17` (octal) = 15. So `a = 15`, `b = 255`, `c = 15`. `a == b` → `15 == 255` → `False`. `b == c` → `255 == 15` → `False`. `a == c` → `15 == 15` → `True`.

---

### Question 7

What does `isinstance(True, int)` return and why?

- A) `False` — `True` is of type `bool`, not `int`
- B) `TypeError` — cannot compare class types this way
- C) **`True` — `bool` is a subclass of `int`** ← CORRECT
- D) `None` — the relationship is undefined in Python

**Correct Answer: C**
**Explanation:** In Python's type hierarchy, `bool` is a **subclass** of `int`. `True` and `False` are instances of both `bool` and `int`. `isinstance()` checks the full inheritance hierarchy, so `isinstance(True, int)` returns `True`. This is why `True + True == 2` and `True == 1` evaluate as `True`.

---

### Question 8

What is the output of the following code?

```python
x = None
y = None
print(x == y, x is y)
```

- A) `True False`
- B) `False True`
- C) `False False`
- D) **`True True`** ← CORRECT

**Correct Answer: D**
**Explanation:** `None` is a **singleton** in Python — there is exactly one `None` object in the entire program. Every variable assigned `None` points to the same object. Therefore `x is y` is `True` (same object) AND `x == y` is `True` (same value). This is why the idiom `if x is None:` is safe and preferred.

---

### Question 9

What is the output of this complex augmented assignment sequence?

```python
x = 100
x //= 3
x **= 2
x %= 7
print(x)
```

- A) `5`
- B) `4`
- C) `2`
- D) **`6`** ← CORRECT

**Correct Answer: D**
**Explanation:** Step by step: `x = 100` → `x //= 3` gives `x = 33` (100 // 3 = 33) → `x **= 2` gives `x = 1089` (33² = 1089) → `x %= 7` gives `x = 6` (1089 = 155×7 + 4... wait, 155×7 = 1085, 1089-1085=4. Hmm, let me recalculate. 1089/7 = 155.57, floor = 155, 155×7=1085, 1089-1085=4. So x=4, not 6. Let me re-check. 100//3 = 33. 33**2 = 1089. 1089 % 7: 7×155 = 1085, 1089-1085 = 4. Answer should be 4.

**CORRECTION — Correct Answer: B (4)**
**Explanation:** Step by step: `x = 100` → `x //= 3` → `x = 33` (floor(100/3) = 33) → `x **= 2` → `x = 1089` (33² = 1089) → `x %= 7` → `x = 4` (1089 = 7×155 + 4). Final value: `4`.

---

### Question 10

What is the output of the following expression?

```python
print(not not not True)
```

- A) `True`
- B) **`False`** ← CORRECT
- C) `None`
- D) `SyntaxError`

**Correct Answer: B**
**Explanation:** Apply `not` three times from right to left: `not True` = `False`, `not False` = `True`, `not True` = `False`. An odd number of `not` operations on `True` produces `False`. An even number returns the original `True`. This tests understanding of unary `not` chaining.

---

### Question 11

What is the output of the following?

```python
print(-10 % 3)
```

- A) `-1`
- B) `-2`
- C) `1`
- D) **`2`** ← CORRECT

**Correct Answer: D**
**Explanation:** Python's modulo follows floor division. `-10 // 3 = -4` (floor toward negative infinity: -3.333 → -4). Then: `-10 = 3 × (-4) + r` → `-10 = -12 + r` → `r = 2`. So `-10 % 3 = 2`. The result is always non-negative when the divisor is positive. This is different from C or Java's behavior where `%` can return negative values.

---

### Question 12

What is the result of this expression?

```python
print(10 / 5 // 1)
```

- A) `2`
- B) `1.0`
- C) **`2.0`** ← CORRECT
- D) `10`

**Correct Answer: C**
**Explanation:** Evaluate left to right (same precedence level): `10 / 5` = `2.0` (true division always produces float). Then `2.0 // 1` = `2.0` (floor division with a float operand returns a float). The result is `2.0`, not `2`. Floor division only returns `int` when BOTH operands are `int`.

---

### Question 13

What does the following code output?

```python
x = 5
print(x > 3 and x < 10 or x == 5)
```

- A) `5`
- B) `False`
- C) `10`
- D) **`True`** ← CORRECT

**Correct Answer: D**
**Explanation:** Evaluate by precedence (`and` before `or`): `(x > 3 and x < 10) or (x == 5)`. Inner: `(True and True)` = `True`. Then: `True or True` = `True`. The `and` expression short-circuits — once `True and True` produces `True`, the `or` sees a truthy left operand and returns it. Result: `True`.

---

### Question 14

What is the output of the following code?

```python
a = [1, 2, 3]
b = a
b += [4]
print(a, b)
print(a is b)
```

- A) `[1, 2, 3]` / `[1, 2, 3, 4]` / `False`
- B) **`[1, 2, 3, 4]` / `[1, 2, 3, 4]` / `True`** ← CORRECT
- C) `[1, 2, 3]` / `[1, 2, 3, 4]` / `True`
- D) `[1, 2, 3, 4]` / `[1, 2, 3, 4]` / `False`

**Correct Answer: B**
**Explanation:** `b = a` makes `b` point to the **same list object** as `a`. `b += [4]` is `b.__iadd__([4])` — it **mutates** the existing list object in place (does not create a new list). Since `a` and `b` reference the same object, both show `[1, 2, 3, 4]`. `a is b` is `True` — they still reference the same object. This contrasts with `b = b + [4]`, which would create a new list and break the shared reference.

---

### Question 15

Which statement about Python's `//` floor division is TRUE for negative results?

- A) `-7 // 2` equals `-3` because Python rounds toward zero
- B) **`-7 // 2` equals `-4` because Python always floors toward negative infinity** ← CORRECT
- C) `-7 // 2` raises a `ValueError` for negative operands
- D) `-7 // 2` equals `-3.5` because floor division returns a float

**Correct Answer: B**
**Explanation:** Python's floor division (`//`) rounds toward **negative infinity**, not toward zero. `-7 / 2 = -3.5`, and the floor (largest integer ≤ -3.5) is `-4`. Compare to `int()` conversion: `int(-3.5)` = `-3` (truncates toward zero). The distinction between floor and truncation toward zero for negative numbers is a classic PCAP exam concept.

---

### Question 16

What does the following output?

```python
x = "Python"
print("Python" in x, "python" in x, "Py" in x)
```

- A) `True True True`
- B) `True False False`
- C) `False True True`
- D) **`True False True`** ← CORRECT

**Correct Answer: D**
**Explanation:** `in` for strings is **case-sensitive**. `"Python"` is found in `"Python"` → `True`. `"python"` (all lowercase) is NOT in `"Python"` (capital P) → `False`. `"Py"` (capital P, lowercase y) IS in `"Python"` (capital P, lowercase ython) → `True`. String membership checks every substring position.

---

### Question 17

What is the output of this code?

```python
def f(): return 42   # Do not worry about def syntax yet — just know f() returns 42
x = 0
y = x or f()
print(y, type(y))
```

- A) `0 <class 'int'>`
- B) `True <class 'bool'>`
- C) **`42 <class 'int'>`** ← CORRECT
- D) `False <class 'bool'>`

**Correct Answer: C**
**Explanation:** `x = 0` is falsy. `or` evaluates its right operand when the left is falsy, so `f()` is called and returns `42`. `or` returns `42`. The type is `int` because `or` returns the actual operand value, not a converted boolean. This pattern (`value or default`) is commonly used to provide fallback values.

---

### Question 18

What is the output of `print(int(float("3.99")))`?

- A) `4`
- B) `3.99`
- C) **`3`** ← CORRECT
- D) `ValueError`

**Correct Answer: C**
**Explanation:** This is a two-step conversion. `float("3.99")` = `3.99` (valid string-to-float). Then `int(3.99)` = `3` (truncates toward zero — does NOT round). The result is `3`, not `4`. This is a common mistake: students expect `int()` to round, but it always truncates. Use `round()` for rounding: `round(float("3.99"))` = `4`.

---

### Question 19

What is the output of `print(round(2.5), round(3.5), round(4.5))`?

- A) `3 4 5`
- B) `2 3 4`
- C) `3 3 5`
- D) **`2 4 4`** ← CORRECT

**Correct Answer: D**
**Explanation:** Python 3 uses banker's rounding (round half to even). `round(2.5)` → nearest even between 2 and 3 → `2`. `round(3.5)` → nearest even between 3 and 4 → `4`. `round(4.5)` → nearest even between 4 and 5 → `4`. Always rounds 0.5 to the nearest EVEN integer, which alternates the direction of rounding.

---

### Question 20

What error does the following code raise?

```python
age = input("Age: ")   # User types "twenty"
years_until_100 = 100 - age
print(years_until_100)
```

- A) `ValueError` — "twenty" is not a number
- B) **`TypeError` — cannot subtract str from int** ← CORRECT
- C) `NameError` — `age` is not defined
- D) `SyntaxError` — `input()` requires explicit type

**Correct Answer: B**
**Explanation:** `input()` returns the string `"twenty"`. The subtraction `100 - "twenty"` attempts to subtract a `str` from an `int`, which Python refuses with a `TypeError: unsupported operand type(s) for -: 'int' and 'str'`. A `ValueError` would occur if you tried `int("twenty")`. The fix: convert immediately with `age = int(input("Age: "))` — though that would then raise `ValueError` for non-numeric input.

---

### Question 21

What is the output of the following?

```python
x = True
y = False
print(x + y, x * 10, x - y, y ** x)
```

- A) `True 10 True 0`
- B) `1 10 1 0`
- C) **`1 10 1 0`** ← CORRECT
- D) `True True True False`

**Correct Answer: C**
**Explanation:** Booleans are integers: `True = 1`, `False = 0`. `x + y = 1 + 0 = 1`. `x * 10 = 1 * 10 = 10`. `x - y = 1 - 0 = 1`. `y ** x = 0 ** 1 = 0`. Results are integers (not booleans) because arithmetic with booleans produces `int` results (except when comparing booleans). Output: `1 10 1 0`.

---

### Question 22

What is the output of this complex precedence expression?

```python
print(2 + 3 ** 2 * 4 - 10 // 3)
```

- A) `43`
- B) **`33`** ← CORRECT
- C) `37`
- D) `100 - 3`

**Correct Answer: B**
**Explanation:** Apply precedence: (1) `3 ** 2 = 9`, (2) `9 * 4 = 36`, (3) `10 // 3 = 3`, (4) `2 + 36 - 3 = 35`. Wait — let me recalculate: `2 + 36 - 3 = 35`. Hmm, that gives 35. Let me re-verify: `2 + (3**2 * 4) - (10//3)` = `2 + (9*4) - 3` = `2 + 36 - 3` = `35`. The answer should be 35, not 33.

**CORRECTION — Correct Answer: `35`**

- A) `43`
- B) `33`
- C) `37`
- D) **`35`** ← CORRECT

**Explanation:** Operator precedence: `**` first, then `*` and `//` left-to-right, then `+` and `-` left-to-right. `3**2 = 9`, `9*4 = 36`, `10//3 = 3`. Then: `2 + 36 - 3 = 35`.

---

### Question 23

Which f-string produces exactly `Student ID: 001042`?

- A) `f"Student ID: {1042}"`
- B) `f"Student ID: {1042:d}"`
- C) `f"Student ID: {1042:6d}"`
- D) **`f"Student ID: {1042:06d}"`** ← CORRECT

**Correct Answer: D**
**Explanation:** The format spec `06d` means: integer (`d`), total field width of `6`, padded with `0`s on the left. `1042` is 4 digits, needing 2 leading zeros to reach width 6: `001042`. Option C (`6d`) pads with spaces: `  1042`. Option A and B produce `1042` without padding.

---

### Question 24

What is the output of `print(bool(""), bool(" "), bool("0"))`?

- A) `False False False`
- B) `False True False`
- C) **`False True True`** ← CORRECT
- D) `True True True`

**Correct Answer: C**
**Explanation:** `bool("")` = `False` — the empty string is the only falsy string. `bool(" ")` = `True` — a space is a non-empty string (it has one character). `bool("0")` = `True` — the string containing the digit zero is non-empty. Only empty string `""` is falsy; `"0"` is truthy because it has content. `0` (integer) is falsy, but `"0"` (string) is truthy.

---

### Question 25

What error does the following code raise and why?

```python
x = 5
y = 2
result = x and y and (10 / (x - 5))
print(result)
```

- A) No error — short-circuit prevents division: result is `2`
- B) No error — result is `True`
- C) **`ZeroDivisionError` — short-circuit does NOT protect here** ← CORRECT
- D) `TypeError` — `and` cannot chain three operands

**Correct Answer: C**
**Explanation:** `x = 5`, so `x - 5 = 0`. Evaluate left to right: `x and y` → `5 and 2` → both truthy, `and` continues and returns `2`. Then `2 and (10 / (5 - 5))` → `2` is truthy, so Python MUST evaluate the right side. `10 / 0` raises `ZeroDivisionError`. Short-circuit only protects when the LEFT operand is falsy. Since `x and y` returns the truthy `2`, the division IS evaluated.

---

### Question 26

A student writes this code. What is the output if the user enters `100`?

```python
x = input("Enter: ")
y = x * 3
print(y)
```

- A) `300`
- B) `100100100`  ← Hmm — is this the correct interpretation?
- C) **`100100100`** ← CORRECT
- D) `TypeError`

**Correct Answer: C (if formatted as single option)**
**Explanation:** `input()` returns the string `"100"`. Multiplying a string by an integer (`str * int`) performs **string repetition** in Python: `"100" * 3` = `"100100100"`. This does not raise an error — it is valid Python string multiplication. To get `300`, the student must first convert: `x = int(input("Enter: "))`.

- A) `300`
- B) `300.0`
- C) `TypeError`
- D) **`100100100`** ← CORRECT

---

### Question 27

What is the output of this code?

```python
a, b = 5, 10
a, b = b, a + b
print(a, b)
```

- A) `5 10`
- B) `10 15`
- C) **`10 15`** ← CORRECT
- D) `10 10`

**Correct Answer: C**
**Explanation:** Python evaluates the right side completely before assigning. Right side: `b, a + b` = `10, 5 + 10` = `10, 15`. Then assign: `a = 10`, `b = 15`. This is a key feature of tuple unpacking — the right side is evaluated all at once using the original values of `a` and `b` before any assignment takes place.

---

### Question 28

Which of the following expressions evaluates to `True`?

- A) `0.1 + 0.2 == 0.3`
- B) `int(3.9) == 4`
- C) `round(2.5) == 3`
- D) **`isinstance(False, int)`** ← CORRECT

**Correct Answer: D**
**Explanation:** `isinstance(False, int)` is `True` because `bool` is a subclass of `int`. The others: `0.1 + 0.2 == 0.3` is `False` (float imprecision). `int(3.9) == 4` is `False` (int truncates to 3). `round(2.5) == 3` is `False` (banker's rounding returns 2). These are the four most common Python "gotchas" on the PCAP exam.

---

### Question 29

What is the output of the following code?

```python
x = 15
print(f"{x:b}", f"{x:o}", f"{x:x}")
```

- A) `0b1111 0o17 0xf`
- B) `15 15 15`
- C) **`1111 17 f`** ← CORRECT
- D) `0b1111 17 f`

**Correct Answer: C**
**Explanation:** f-string format specifiers: `:b` formats as binary (no `0b` prefix), `:o` formats as octal (no `0o` prefix), `:x` formats as lowercase hex (no `0x` prefix). To include the prefix, use `:#b`, `:#o`, `:#x`. So `f"{15:b}"` = `"1111"`, `f"{15:o}"` = `"17"`, `f"{15:x}"` = `"f"`.

---

### Question 30

What is the complete output of the following program?

```python
x = 10
y = 3
z = x / y
w = x // y
v = x % y
print(f"{z:.3f}", w, v, int(z) == w)
```

- A) `3.333 3 1 False`
- B) `3.333 3 1 True`
- C) `3.33 3 1 True`
- D) **`3.333 3 1 True`** ← CORRECT

**Correct Answer: D**
**Explanation:** `z = 10 / 3 = 3.3333...` (float). `w = 10 // 3 = 3` (int). `v = 10 % 3 = 1` (int). `f"{z:.3f}"` = `"3.333"` (3 decimal places). Then: `int(z)` = `int(3.333...)` = `3` (truncates). `3 == w` = `3 == 3` = `True`. Full output: `3.333 3 1 True`.

---

## Bonus Question (10 points)

### Question 31 — [SA] Short Answer

```python
a = 2
b = 3
c = a
a, b = b ** c, a ** b
c += a
print(a, b, c)
```

What is the output? Show your work step by step. Points awarded for correct reasoning even with a computational error.

**Correct Answer:** `8 8 10`

**Step-by-step:**
1. Initial values: `a = 2`, `b = 3`, `c = a = 2`
2. Right side evaluated first (using original a=2, b=3): `b ** c = 3**2 = 8`... wait, right side is `b ** c` and `a ** b`:
   - `b ** c = 3 ** 2`... but wait, `c = a = 2`, so `b ** c = 3 ** 2 = 9`? No, `c = a = 2`, so `b ** c = 3 ** 2 = 9`. But the code says `b ** c` where `c = 2` and `b = 3`.
   
Let me re-read: `a, b = b ** c, a ** b`. Right side: `b ** c = 3 ** 2 = 9` and `a ** b = 2 ** 3 = 8`.

So after assignment: `a = 9`, `b = 8`.

Then `c += a` → `c = 2 + 9 = 11`.

Output: `9 8 11`

**Corrected Answer: `9 8 11`**

**Explanation:** Right side evaluated using original values (a=2, b=3, c=2): `b**c = 3**2 = 9`, `a**b = 2**3 = 8`. After assignment: `a=9, b=8`. `c += a` → `c = 2 + 9 = 11`. Output: `9 8 11`.

---

## Answer Key (for Instructor Reference)

| Q | Answer | Module | Topic |
|---|---|---|---|
| 1 | B | M1 | `print()` sep and end |
| 2 | C | M1 | `print()` return value |
| 3 | C | M1 | PEP 8 function naming |
| 4 | C | M1 | TypeError: str + int |
| 5 | B | M2 | Integer immutability |
| 6 | D | M2 | Number base literals |
| 7 | C | M2 | `isinstance()` and bool/int |
| 8 | D | M2 | None singleton |
| 9 | B | M2 | Augmented assignment chain |
| 10 | B | M3 | Triple `not` |
| 11 | D | M3 | Negative modulo |
| 12 | C | M3 | Division with float result |
| 13 | D | M3 | Logical operator chain |
| 14 | B | M2/M3 | Mutable list reference + `+=` |
| 15 | B | M3 | Floor division direction |
| 16 | D | M3 | `in` case-sensitivity |
| 17 | C | M3 | `or` return value |
| 18 | C | M4 | `int(float())` truncation |
| 19 | D | M4 | Banker's rounding |
| 20 | B | M4 | `input()` + arithmetic TypeError |
| 21 | C | M2/M3 | Boolean arithmetic |
| 22 | D | M3 | Complex precedence |
| 23 | D | M4 | f-string zero-padding |
| 24 | C | M4 | `bool()` string edge cases |
| 25 | C | M3 | Short-circuit limitation |
| 26 | D | M4 | `input()` string × int repetition |
| 27 | C | M2 | Tuple unpacking evaluation order |
| 28 | D | M2/M3/M4 | Synthesis: four common gotchas |
| 29 | C | M4 | f-string `:b`, `:o`, `:x` |
| 30 | D | M3/M4 | Synthesis: division + f-string |
| 31 | — | M2/M3 | Bonus: right-side evaluation order |

---

*Unit Test 2 will cover Modules 5–8 (Control Flow and Loops)*
