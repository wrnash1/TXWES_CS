# Quiz: Module 4 — Type Conversion and User Input

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Total:** 15 Questions | 2 points each = **30 points**
**Suggested Time:** 20 minutes
**PCAP Alignment:** Section 2 — Data Types, Evaluation, Basic I/O

---

## Canvas Entry Instructions

- **Question Type:** Multiple Choice
- **Points per question:** 2
- **Shuffle Answers:** Yes
- Correct answers marked with **← CORRECT**

---

## Questions

---

### Question 1

What is the output of `print(int(3.9))`?

- A) `4`
- B) **`3`** ← CORRECT
- C) `3.9`
- D) `ValueError`

**Correct Answer: B**
**Explanation:** `int()` **truncates** toward zero — it discards the decimal portion entirely without rounding. `int(3.9)` = `3`, not `4`. Note: this differs from floor division. `int(-3.9)` = `-3` (truncates toward zero), while `(-3.9) // 1` = `-4` (floors toward negative infinity).

---

### Question 2

Which of the following `int()` calls raises a `ValueError`?

- A) `int(3.0)`
- B) `int(True)`
- C) **`int("3.14")`** ← CORRECT
- D) `int("42")`

**Correct Answer: C**
**Explanation:** `int()` can convert float literals (truncating) and boolean values, and it can parse clean integer strings like `"42"`. However, `"3.14"` contains a decimal point — `int()` cannot parse a decimal string directly. You must first convert it to a float: `int(float("3.14"))` = `3`. This raises a `ValueError: invalid literal for int() with base 10: '3.14'`.

---

### Question 3

What does the following code output?

```python
x = input("Enter a number: ")
print(type(x))
```

Assume the user types `42` and presses Enter.

- A) `<class 'int'>`
- B) `<class 'float'>`
- C) `<class 'NoneType'>`
- D) **`<class 'str'>`** ← CORRECT

**Correct Answer: D**
**Explanation:** `input()` **always** returns a string (`str`), regardless of what the user types. If the user types `42`, `x` holds the string `"42"`, not the integer `42`. You must explicitly convert: `x = int(input("Enter a number: "))` to get an integer.

---

### Question 4

What is the output of `print(round(2.5))`?

- A) `3`
- B) `2.5`
- C) `3.0`
- D) **`2`** ← CORRECT

**Correct Answer: D**
**Explanation:** Python 3 uses **banker's rounding** (round half to even). When the value is exactly 0.5 away from two integers, Python rounds to the nearest **even** number. `2.5` is equidistant between `2` and `3`. Since `2` is even, Python rounds to `2`. Similarly, `round(3.5)` = `4` (4 is even), and `round(1.5)` = `2` (2 is even).

---

### Question 5

What is the result of the following code?

```python
print("Score: " + 95)
```

- A) `Score: 95`
- B) `Score:95`
- C) `ValueError`
- D) **`TypeError`** ← CORRECT

**Correct Answer: D**
**Explanation:** Python does NOT implicitly convert `int` to `str` when using the `+` concatenation operator. Attempting to concatenate a string with an integer raises a `TypeError: can only concatenate str (not "int") to str`. The fix is explicit conversion: `"Score: " + str(95)` or use an f-string: `f"Score: {95}"`.

---

### Question 6

What is the output of `print(bool("False"))`?

- A) `False`
- B) `None`
- C) **`True`** ← CORRECT
- D) `TypeError`

**Correct Answer: C**
**Explanation:** `bool()` evaluates **truthiness**, not the logical meaning of a string's content. Any non-empty string is truthy, including `"False"`, `"0"`, `"None"`, etc. Only the empty string `""` is falsy. The string `"False"` contains characters, making it non-empty and therefore truthy. This is a classic PCAP exam trap.

---

### Question 7

What will the following f-string output?

```python
pi = 3.14159
print(f"{pi:.2f}")
```

- A) `3.14159`
- B) `3.1`
- C) **`3.14`** ← CORRECT
- D) `3`

**Correct Answer: C**
**Explanation:** The `:.2f` format specifier in an f-string formats a float to exactly 2 decimal places, rounding the result. `3.14159` rounded to 2 decimal places is `3.14`. The `f` in `.2f` specifies fixed-point notation. Without the specifier, `f"{pi}"` would output the full `3.14159`.

---

### Question 8

Which conversion will raise a `TypeError` (not a `ValueError`)?

- A) `int("hello")`
- B) `float("abc")`
- C) **`int(None)`** ← CORRECT
- D) `int("FF")`

**Correct Answer: C**
**Explanation:** `TypeError` occurs when the type itself is incompatible. `None` is `NoneType` — it is fundamentally not a numeric type and cannot be converted to `int`. `ValueError` occurs when the type is correct but the value is invalid: `int("hello")` and `float("abc")` receive strings (the right type) but with non-numeric content. `int("FF")` raises `ValueError` only without a base; `int("FF", 16)` = 255.

---

### Question 9

What is the output of the following code?

```python
x = float("inf")
print(x > 1000000)
print(type(x))
```

- A) `False` / `<class 'float'>`
- B) `True` / `<class 'int'>`
- C) `ValueError` / N/A
- D) **`True` / `<class 'float'>`** ← CORRECT

**Correct Answer: D**
**Explanation:** `float("inf")` creates Python's positive infinity, which is a valid `float` value. Infinity is greater than any finite number, so `inf > 1000000` is `True`. Infinity is still of type `float`. Python also supports `float("-inf")` (negative infinity) and `float("nan")` (not a number).

---

### Question 10

A student writes this code to add two numbers from user input. What is wrong?

```python
a = input("First number: ")
b = input("Second number: ")
print("Sum:", a + b)
```

If the user enters `5` and `3`:

- A) The output is `Sum: 8`
- B) The output is `Sum: 5.0 3.0`
- C) **The output is `Sum: 53`** ← CORRECT
- D) `TypeError` is raised

**Correct Answer: C**
**Explanation:** `input()` returns strings. `a = "5"` and `b = "3"`. The `+` operator on two strings performs **concatenation**, not addition. So `"5" + "3"` = `"53"`. The fix: convert inputs to numbers first: `a = int(input(...))` or `a = float(input(...))`.

---

### Question 11

What is the output of `int("FF", 16)`?

- A) `ValueError`
- B) `16`
- C) `15`
- D) **`255`** ← CORRECT

**Correct Answer: D**
**Explanation:** `int(string, base)` converts a string from the specified base to a decimal integer. `"FF"` in hexadecimal (base 16): `F = 15`, so `FF = (15 × 16) + 15 = 240 + 15 = 255`. This syntax also works for binary (`int("1010", 2)` = 10) and octal (`int("17", 8)` = 15).

---

### Question 12

What is the output of `print(str(True), str(None))`?

- A) `1 None`
- B) `True null`
- C) **`True None`** ← CORRECT
- D) `true None`

**Correct Answer: C**
**Explanation:** `str(True)` returns the string `"True"` (capital T — the Python boolean keyword). `str(None)` returns the string `"None"` (capital N — the Python None keyword). Python converts booleans and None to their canonical string representations. Note: `str(1)` returns `"1"` (the number), not `"True"`.

---

### Question 13

What does the following output?

```python
x = 5
y = 2
result = str(x) + str(y)
print(result, type(result))
```

- A) `7 <class 'int'>`
- B) `7 <class 'str'>`
- C) `52 <class 'int'>`
- D) **`52 <class 'str'>`** ← CORRECT

**Correct Answer: D**
**Explanation:** `str(5)` = `"5"` and `str(2)` = `"2"`. String concatenation: `"5" + "2"` = `"52"`. The result is the string `"52"`, not the integer `7`. When you convert numbers to strings before using `+`, you get string concatenation. This is a common source of bugs when students accidentally convert numbers to strings.

---

### Question 14

Which f-string correctly formats `12345.6789` as `$12,345.68`?

- A) `f"${12345.6789:.2}"`
- B) `f"${12345.6789:,.2}"`
- C) **`f"${12345.6789:,.2f}"`** ← CORRECT
- D) `f"$12345.6789{:2f}"`

**Correct Answer: C**
**Explanation:** The format spec `,.2f` combines: `,` (add thousands separators) and `.2f` (fixed-point with 2 decimal places). The `f` after `.2` is required — without it, `.2` is interpreted as total significant digits, not decimal places. Result: `$12,345.68`.

---

### Question 15

A student needs to convert the string `"3.14"` to an integer. Which approach is correct?

- A) `int("3.14")` — converts directly
- B) `int.parse("3.14")` — Python's parse method
- C) **`int(float("3.14"))` — convert to float first, then truncate to int** ← CORRECT
- D) `(int)"3.14"` — C-style cast

**Correct Answer: C**
**Explanation:** `int("3.14")` raises a `ValueError` because `int()` cannot parse a string containing a decimal point. The correct approach is a two-step conversion: `float("3.14")` first produces `3.14` as a float, and then `int(3.14)` truncates it to `3`. Python has no `.parse()` method or C-style casts — it uses the built-in conversion functions.

---

## Answer Key (for Instructor Reference)

| Q | Answer | Topic |
|---|---|---|
| 1 | B | `int()` truncates (not rounds) |
| 2 | C | `ValueError` on decimal string |
| 3 | D | `input()` always returns str |
| 4 | D | Banker's rounding |
| 5 | D | `TypeError`: str + int |
| 6 | C | `bool("False")` is True |
| 7 | C | f-string `:.2f` specifier |
| 8 | C | `TypeError` vs `ValueError` |
| 9 | D | `float("inf")` |
| 10 | C | input string concatenation trap |
| 11 | D | `int("FF", 16)` hex conversion |
| 12 | C | `str(True)` and `str(None)` |
| 13 | D | str + str = concatenation |
| 14 | C | f-string `,.2f` format |
| 15 | C | Two-step string-to-int via float |

---

*These questions are included in Unit Test 1 (Modules 1–4) — see `Unit_Test_1.md` in this folder.*
