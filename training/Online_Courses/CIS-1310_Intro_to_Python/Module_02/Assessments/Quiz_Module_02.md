# Quiz: Module 2 — Variables, Literals, and Data Types

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Total:** 15 Questions | 2 points each = **30 points**
**Suggested Time:** 20 minutes
**PCAP Alignment:** Section 2 — Data Types, Evaluation, Basic I/O

---

## Canvas Entry Instructions

- **Question Type:** Multiple Choice (unless noted otherwise)
- **Points per question:** 2
- **Shuffle Answers:** Yes
- **Allowed Attempts:** 1 (or per course policy)
- Correct answers are marked with **← CORRECT**

---

## Questions

---

### Question 1

Which of the following is a VALID Python variable name?

- A) `2fast`
- B) `my-name`
- C) `class`
- D) **`student_gpa`** ← CORRECT

**Correct Answer: D**
**Explanation:** `student_gpa` follows PEP 8 snake_case conventions and contains only letters and underscores. `2fast` starts with a digit (SyntaxError). `my-name` contains a hyphen (SyntaxError). `class` is a reserved Python keyword (SyntaxError).

---

### Question 2

What is the output of the following code?

```python
x = 10
x = "Python"
x = 3.14
print(type(x))
```

- A) `<class 'int'>`
- B) `<class 'str'>`
- C) **`<class 'float'>`** ← CORRECT
- D) `TypeError — cannot reassign a variable`

**Correct Answer: C**
**Explanation:** Python is dynamically typed — a variable can be reassigned to a value of any type. After the three assignments, `x` holds `3.14` (a `float`). The last assigned value determines the current type.

---

### Question 3

What is the output of `print(0xFF)`?

- A) `0xFF`
- B) `FF`
- C) `15`
- D) **`255`** ← CORRECT

**Correct Answer: D**
**Explanation:** `0xFF` is a hexadecimal literal. `F` in hex equals 15, so `FF` = (15 × 16) + 15 = 240 + 15 = 255. Python stores and displays all integer literals as decimal values regardless of the format used to write them.

---

### Question 4

What is the output of the following code?

```python
print(type(True))
```

- A) `<class 'bool'>`  ← Wait — is this correct or not?
- A) `<class 'NoneType'>`
- B) `<class 'int'>`
- C) **`<class 'bool'>`** ← CORRECT
- D) `<class 'Boolean'>`

**Correct Answer: C**
**Explanation:** `True` is a boolean literal. `type(True)` returns `<class 'bool'>`. Although `bool` is technically a subclass of `int` (meaning `isinstance(True, int)` returns `True`), the direct type is `bool`. `Boolean` is not a Python type name.

---

### Question 5

What is the output of `print(True + True + False)`?

- A) `TrueTrueFalse`
- B) `True`
- C) `3`
- D) **`2`** ← CORRECT

**Correct Answer: D**
**Explanation:** In Python, `bool` is a subclass of `int`. `True` has the integer value `1` and `False` has the value `0`. So `True + True + False` = `1 + 1 + 0` = `2`. This arithmetic is valid because Python treats booleans as integers in numeric operations.

---

### Question 6

Which of the following values evaluates to `False` in a boolean context?

- A) `"False"` (a string containing the word False)
- B) `-1`
- C) `0.001`
- D) **`0.0`** ← CORRECT

**Correct Answer: D**
**Explanation:** In Python, `0.0` (zero as a float) is **falsy** — it evaluates to `False`. Any non-zero numeric value (including `-1` and `0.001`) is truthy. The string `"False"` is truthy because it is a non-empty string — its content does not matter. Only empty strings are falsy.

---

### Question 7

What does the following code output?

```python
a, b, c = 10, 20, 30
a, c = c, a
print(a, b, c)
```

- A) `10 20 30`
- B) `30 20 10`
- C) **`30 20 10`** ← CORRECT
- D) `10 20 10`

**Correct Answer: C**
**Explanation:** `a, c = c, a` uses tuple unpacking to swap `a` and `c` simultaneously. Python evaluates the right side (`c, a` = `30, 10`) before assigning. After the swap: `a = 30`, `b` is unchanged at `20`, `c = 10`. Output: `30 20 10`.

---

### Question 8

After running the following code, what is the value of `score`?

```python
score = 10
score *= 3
score -= 5
score //= 5
```

- A) `3`
- B) `4`
- C) **`5`** ← CORRECT
- D) `6`

**Correct Answer: C**
**Explanation:** Step by step: `score = 10` → `score *= 3` makes it `30` → `score -= 5` makes it `25` → `score //= 5` (floor division) makes it `5`. Floor division (`//`) divides and discards the remainder.

---

### Question 9

What is `type(None)` in Python?

- A) `<class 'None'>`
- B) **`<class 'NoneType'>`** ← CORRECT
- C) `<class 'null'>`
- D) `<class 'undefined'>`

**Correct Answer: B**
**Explanation:** `None` is the sole instance of the `NoneType` class. Its type is `NoneType`. Python has no `null` type (that is from other languages). `None` itself is not a class name — `NoneType` is. To check if something is `None`, use `value is None` (not `value == None`).

---

### Question 10

Which of the following creates a float literal in Python?

- A) `x = 100`
- B) `x = 0b1010`
- C) `x = True`
- D) **`x = 1e2`** ← CORRECT

**Correct Answer: D**
**Explanation:** `1e2` is scientific notation meaning 1 × 10² = 100.0, which is a `float`. `100` is an `int`. `0b1010` is a binary integer literal (value 10). `True` is a `bool`. Scientific notation always produces a `float` in Python.

---

### Question 11

What is the output of the following code?

```python
x = y = z = 5
z = 10
print(x, y, z)
```

- A) `10 10 10`
- B) **`5 5 10`** ← CORRECT
- C) `5 10 10`
- D) `5 5 5`

**Correct Answer: B**
**Explanation:** `x = y = z = 5` sets all three variables to `5`. Then `z = 10` only reassigns `z` — `x` and `y` still point to the integer object `5`. Integers are immutable, so this behaves predictably. Output: `5 5 10`.

---

### Question 12

Which statement about Python's dynamic typing is TRUE?

- A) Variables must be declared with a type before use
- B) A variable's type is fixed once assigned and cannot change
- C) Python checks all variable types before running the program
- D) **A variable's type is determined by the value it currently holds** ← CORRECT

**Correct Answer: D**
**Explanation:** Python is dynamically typed — the type is an attribute of the *value* (object), not the variable name. A variable can be reassigned to hold any type. Python does NOT require type declarations. Type checking occurs at runtime, not before execution.

---

### Question 13

What is the result of `isinstance(True, int)` in Python?

- A) `False` — `True` is of type `bool`, not `int`
- B) **`True` — `bool` is a subclass of `int`** ← CORRECT
- C) `TypeError` — cannot compare `bool` to `int`
- D) `None` — the relationship is undefined

**Correct Answer: B**
**Explanation:** In Python, `bool` is a subclass of `int`. This means `True` and `False` are also integers (`1` and `0`). `isinstance(True, int)` returns `True` because of this inheritance relationship. `isinstance()` checks the entire inheritance hierarchy, unlike `type() == int` which would return `False`.

---

### Question 14

What does the following code output, and why?

```python
print(0.1 + 0.2 == 0.3)
```

- A) `True` — Python's arithmetic is always exact
- B) `True` — Python rounds floats automatically
- C) **`False` — floating-point binary representation causes imprecision** ← CORRECT
- D) `SyntaxError` — cannot compare float expressions

**Correct Answer: C**
**Explanation:** Due to the way computers represent decimal numbers in binary (IEEE 754 floating-point), `0.1 + 0.2` evaluates to `0.30000000000000004`, not exactly `0.3`. This comparison returns `False`. This is not a Python bug — it affects all languages using IEEE 754 floats. Use `math.isclose()` for reliable float comparison.

---

### Question 15

A student writes the following code. What error will Python raise?

```python
for = 10
print(for)
```

- A) `IndentationError` — the code block is not indented
- B) `NameError` — `for` is not defined
- C) `ValueError` — `10` cannot be assigned to a keyword
- D) **`SyntaxError` — `for` is a reserved keyword** ← CORRECT

**Correct Answer: D**
**Explanation:** `for` is a Python keyword used for iteration. Keywords are reserved and cannot be used as variable names. Python raises a `SyntaxError` immediately when it encounters `for = 10` because the parser expects a `for` loop structure, not an assignment. Check the full keyword list using `import keyword; print(keyword.kwlist)`.

---

## Answer Key (for Instructor Reference)

| Q | Answer | Topic |
|---|---|---|
| 1 | D | Valid variable names |
| 2 | C | Dynamic typing |
| 3 | D | Hex literal |
| 4 | C | `type(True)` |
| 5 | D | Boolean arithmetic |
| 6 | D | Falsy values |
| 7 | C | Tuple unpacking / swap |
| 8 | C | Augmented assignment chaining |
| 9 | B | `type(None)` |
| 10 | D | Float literals / scientific notation |
| 11 | B | Multiple assignment |
| 12 | D | Dynamic typing definition |
| 13 | B | `isinstance()` and inheritance |
| 14 | C | Float precision |
| 15 | D | Keywords as variable names |

---

*These questions are included in Unit Test 1 (Modules 1–4).*
