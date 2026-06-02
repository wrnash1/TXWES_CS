# Quiz: Module 02 — Literals, Operators, and Expressions

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. Trace all expressions by hand before selecting an answer.

---

### Question 1

What is the result of `print(11 // 3)` in Python?

- A) `3.6666666666666665`
- B) `3`
- C) `4`
- D) `2`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That is the result of `11 / 3` using true division, which always returns a `float`. The `//` operator is floor division, not true division.
- *Why B is correct:* `//` performs floor division — it divides and rounds down to the nearest integer. `11 / 3 = 3.666...`, and the floor of `3.666` is `3`.
- *Why C is incorrect:* `4` would be the result of rounding `3.666` to the nearest integer. Floor division does not round — it always goes toward negative infinity.
- *Why D is incorrect:* `2` is not the floor of `3.666`. `2` would be the result of `11 % 3` (the remainder), not floor division.

---

### Question 2

Which of the following best describes Python's `int` data type?

- A) A whole-number type that can represent arbitrarily large integers without overflow, unlike fixed-size integers in languages like C
- B) A numeric type that stores values using IEEE 754 double-precision floating-point, introducing small rounding errors for some decimals
- C) An immutable sequence of digit characters that must be converted before arithmetic can be performed on it
- D) A numeric type limited to values between -2,147,483,648 and 2,147,483,647 on all Python platforms

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Python `int` is arbitrary-precision — it grows as needed and never overflows. You can compute `2 ** 1000` without error. This is a key difference from C/Java 32-bit integers.
- *Why B is incorrect:* That describes the `float` type. Floats use IEEE 754 double-precision format and have rounding issues. `int` is always exact.
- *Why C is incorrect:* That describes the `str` type. A string `"42"` is a sequence of characters, not a number. You must use `int("42")` to convert it.
- *Why D is incorrect:* Python `int` has no fixed-size limit. The range `-2,147,483,648` to `2,147,483,647` describes a 32-bit signed integer in languages like Java and C — not Python.

---

### Question 3

What is the output of the following code?

```python
print(0.1 + 0.2 == 0.3)
```

- A) `True`
- B) `False`
- C) `0.30000000000000004`
- D) `TypeError: cannot compare float to float`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `0.1 + 0.2` does not equal exactly `0.3` in Python. Both `0.1` and `0.2` have binary representation errors in IEEE 754 floating-point format. When added, those errors accumulate and the result is `0.30000000000000004`, which is not equal to `0.3`.
- *Why B is correct:* The expression `0.1 + 0.2` evaluates to `0.30000000000000004` due to binary floating-point imprecision. This is not equal to `0.3`, so the comparison returns `False`.
- *Why C is incorrect:* `0.30000000000000004` would be the output of `print(0.1 + 0.2)` — not the output of the equality comparison. The comparison `==` returns a boolean, not the float value.
- *Why D is incorrect:* There is nothing wrong with comparing two floats using `==` in Python — it is perfectly valid syntax. It just returns `False` here because of floating-point imprecision.

---

### Question 4

What is the result of `True + True + False`?

- A) `TrueTrueFalse`
- B) `True`
- C) `2`
- D) `TypeError: unsupported operand type`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The `+` operator on `bool` values performs integer addition, not string concatenation. Concatenation with `+` only works when both operands are `str` type.
- *Why B is incorrect:* `True` would imply the result is a boolean, but here `+` with bool operands produces an `int`. `True + True` = `1 + 1` = `2`. Adding `False` (which equals `0`) leaves `2`.
- *Why C is correct:* `bool` is a subclass of `int` in Python. `True` equals `1`, `False` equals `0`. So `True + True + False` = `1 + 1 + 0` = `2`. The result type is `int`.
- *Why D is incorrect:* Because `bool` is a subclass of `int`, arithmetic operations on booleans are perfectly valid in Python — no `TypeError` is raised.

---

### Question 5

What does `-2 ** 2` evaluate to in Python?

- A) `4`
- B) `-4`
- C) `SyntaxError`
- D) `0`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This is the most common wrong answer. The reasoning "negative two squared equals four" applies only if the negation is part of the base. In Python, `**` has higher precedence than unary minus, so `-2 ** 2` is evaluated as `-(2 ** 2)`, not `(-2) ** 2`.
- *Why B is correct:* Unary minus has lower precedence than `**`. Python evaluates `2 ** 2 = 4` first, then applies the unary minus: `-(4) = -4`. To get `4`, you must write `(-2) ** 2`.
- *Why C is incorrect:* `-2 ** 2` is valid Python syntax — no error is raised. Python evaluates it as `-(2 ** 2)`.
- *Why D is incorrect:* `0` has no mathematical basis here. This is a pure precedence question: `-(2 ** 2) = -4`.

---

### Question 6

What is the result of `4 / 2` in Python 3?

- A) `2`
- B) `2.0`
- C) `int`
- D) `ZeroDivisionError`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* In Python 3, the `/` operator always returns a `float`, even when both operands are integers and the result divides evenly. `4 / 2` returns `2.0`, not `2`. This is different from Python 2 and from many other languages.
- *Why B is correct:* In Python 3, `/` is true division and always returns a `float`. `4 / 2 = 2.0`. To get an integer result, you must use floor division: `4 // 2 = 2`.
- *Why C is incorrect:* `int` is a type name, not a value. The question asks for the result of evaluating the expression.
- *Why D is incorrect:* `ZeroDivisionError` only occurs when dividing by zero. `4 / 2` divides by `2`, which is perfectly valid.

---

### Question 7

What does `2 ** 3 ** 2` evaluate to?

- A) `64` — because `(2 ** 3) ** 2 = 8 ** 2 = 64`
- B) `512` — because `2 ** (3 ** 2) = 2 ** 9 = 512`
- C) `36` — because `2 + 3 ** 2 = 2 + 9 = 11`... wait, that doesn't make sense
- D) `SyntaxError` — two consecutive `**` operators are not permitted

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This would be the result if `**` were left-associative. But `**` is uniquely right-associative in Python — the rightmost operation evaluates first. `(2 ** 3) ** 2 = 64` is what left-to-right evaluation gives, but that is NOT how Python handles `**`.
- *Why B is correct:* `**` is right-associative in Python, meaning consecutive `**` operators evaluate right-to-left. `2 ** 3 ** 2` = `2 ** (3 ** 2)` = `2 ** 9` = `512`. This is a direct PCAP exam topic.
- *Why C is incorrect:* The expression `2 ** 3 ** 2` contains only `**` operators, no `+`. This answer is nonsensical and is a trap for students who are not reading carefully.
- *Why D is incorrect:* `2 ** 3 ** 2` is completely valid Python syntax. Multiple `**` operators in one expression are allowed and evaluated right-to-left.

---

### Question 8

What is the result of `-7 // 2` in Python?

- A) `-3`
- B) `-4`
- C) `3`
- D) `-3.5`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `-3` would be the result of **truncation toward zero** — which is how C and Java handle integer division with negative numbers. Python uses floor division, which rounds toward **negative infinity**, not toward zero.
- *Why B is correct:* `-7 / 2 = -3.5`. The floor of `-3.5` is `-4` (the next integer below `-3.5` on the number line). Python's `//` always floors toward negative infinity.
- *Why C is incorrect:* `3` is the result of `7 // 2` with positive numbers. The negative sign on `-7` changes the result.
- *Why D is incorrect:* `//` is floor division — it always returns an `int` when both operands are `int`. `-3.5` would be the result of `-7 / 2` using true division.

---

### Question 9

What is the result of `bool('')`?

- A) `True`
- B) `False`
- C) `None`
- D) `TypeError: cannot convert str to bool`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* An empty string is **falsy** in Python. It represents "nothing" — no characters. `bool('')` returns `False`. Any non-empty string, including a string containing only a space like `' '`, would return `True`.
- *Why B is correct:* The empty string `''` is one of Python's **falsy** values. Falsy values: `0`, `0.0`, `''`, `[]`, `{}`, `set()`, `None`. All others are truthy.
- *Why C is incorrect:* `None` is a value representing absence — it is not what `bool()` returns. `bool()` always returns `True` or `False`.
- *Why D is incorrect:* `bool()` can accept any Python object — it is not type-restricted. Converting a `str` to `bool` is perfectly valid Python.

---

### Question 10

A developer writes `int(7.99)` expecting to get `8`. What does Python actually return, and why?

- A) `8` — Python rounds to the nearest integer
- B) `7` — `int()` truncates toward zero, discarding the decimal portion
- C) `8.0` — `int()` still returns a float when the input is a float
- D) `ValueError` — `int()` cannot convert floats that are not whole numbers

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `int()` does **not** round. It truncates — it drops the decimal component entirely, regardless of how close the value is to the next integer. `int(7.99)` returns `7`, not `8`. To round to the nearest integer, use the `round()` function: `round(7.99)` returns `8`.
- *Why B is correct:* `int()` converts a float to integer by truncating — dropping everything after the decimal point, moving toward zero. `int(7.99) = 7`. `int(-7.99) = -7` (not `-8`).
- *Why C is incorrect:* `int()` always returns an `int` type, never a `float`. The name makes this clear — you are converting TO int.
- *Why D is incorrect:* `int()` can convert any float to an integer by truncation. There is no restriction on values with non-zero decimal parts. `ValueError` from `int()` only occurs when passing a non-numeric string like `int('hello')`.
