# Reading Guide: Module 4 — Type Conversion and User Input

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Certification Alignment:** PCAP — Certified Associate in Python Programming
**PCAP Exam Section:** Section 2 — Data Types, Evaluation, Basic I/O, Operators
**Estimated Reading Time:** 45–55 minutes
**OER Resources:** [edube.org PE1 Module 2](https://edube.org/) | [Python Built-in Functions](https://docs.python.org/3/library/functions.html)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Differentiate between implicit (automatic) and explicit (manual) type conversion
2. Apply `int()`, `float()`, `str()`, and `bool()` to convert between data types correctly
3. Use the `input()` function to collect user input and handle its string return type
4. Explain why `input()` always returns a string and convert it for numeric calculations
5. Format output using f-strings (f-literals)
6. Use the `round()` function and understand Python 3's banker's rounding behavior
7. Predict which conversion calls will raise `ValueError` or `TypeError`

---

## Section 1: Implicit Type Conversion

**Implicit conversion** (also called type coercion) happens automatically when Python converts one type to a "wider" or more capable type to complete an operation — you do not write any conversion code.

### When Python Converts Automatically

```python
result = 5 + 3.0      # int + float → Python promotes int to float
print(result)          # 8.0 — float
print(type(result))    # <class 'float'>

result2 = True + 5     # bool + int → True is 1
print(result2)         # 6 — int
```

**The promotion hierarchy:** `bool` → `int` → `float`

Python will automatically promote to a more general type but will **never automatically narrow** (e.g., it will not silently truncate a `float` to an `int`).

### When Implicit Conversion Does NOT Happen

```python
print("Score: " + 95)    # TypeError — Python won't auto-convert int to str
print("2" + 2)            # TypeError — str + int not allowed
```

> **PCAP Exam Tip:** Python does NOT implicitly convert numbers to strings. Attempting `"Total: " + 100` raises a `TypeError`. You must explicitly convert: `"Total: " + str(100)`.

---

## Section 2: Explicit Type Conversion (Type Casting)

**Explicit conversion** means you call a function to convert one type to another. Python provides four primary conversion functions.

### `int()` — Convert to Integer

```python
print(int(3.9))       # 3 — truncates (does NOT round) toward zero
print(int(3.1))       # 3
print(int(-3.9))      # -3 — truncates toward zero (not floor!)
print(int("42"))      # 42 — parses a decimal string
print(int(True))      # 1
print(int(False))     # 0
```

**What `int()` will NOT accept:**

```python
int("3.14")      # ValueError — "3.14" has a decimal point
int("hello")     # ValueError — not a number
int([1, 2, 3])   # TypeError — lists cannot convert to int
int(None)        # TypeError — None cannot convert to int
```

**Non-decimal string conversion:**

```python
print(int("FF", 16))      # 255 — parse hex string with base 16
print(int("1010", 2))     # 10  — parse binary string with base 2
print(int("17", 8))       # 15  — parse octal string with base 8
```

> **PCAP Exam Tip:** `int(3.9)` is `3`, not `4`. It **truncates** toward zero, not rounds. `int(-3.9)` is `-3`, not `-4` (floor division `//` would give `-4`). This distinction between truncation and floor is frequently tested.

### `float()` — Convert to Float

```python
print(float(42))          # 42.0
print(float("3.14"))      # 3.14
print(float("3"))         # 3.0 — string "3" converts fine
print(float(True))        # 1.0
print(float(False))       # 0.0
print(float("inf"))       # inf — positive infinity (valid!)
print(float("-inf"))      # -inf — negative infinity
print(float("nan"))       # nan — not a number (valid!)
```

**What `float()` will NOT accept:**

```python
float("hello")    # ValueError
float(None)       # TypeError
```

### `str()` — Convert to String

`str()` converts virtually anything to its string representation:

```python
print(str(42))        # "42"
print(str(3.14))      # "3.14"
print(str(True))      # "True"
print(str(False))     # "False"
print(str(None))      # "None"
print(str([1, 2]))    # "[1, 2]"
```

`str()` is the go-to solution when you need to concatenate a number with a string:

```python
score = 95
message = "Your score: " + str(score)
print(message)    # Your score: 95
```

### `bool()` — Convert to Boolean

Any value can be converted to `bool`. The rules for what is `True` vs. `False`:

| Converts to `False` | Converts to `True` |
|---|---|
| `0`, `0.0`, `0j` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `[]`, `()`, `{}`, `set()` | Any non-empty collection |
| `None` | Any non-None value |
| `False` | `True` |

```python
print(bool(0))        # False
print(bool(42))       # True
print(bool(""))       # False
print(bool("False"))  # True  — non-empty string, even if content is "False"!
print(bool(None))     # False
print(bool([]))       # False
print(bool([0]))      # True  — list has one element (even if that element is 0)
```

> **PCAP Exam Tip:** `bool("False")` is `True`. The string `"False"` is truthy because it is a non-empty string. Only the empty string `""` is falsy. This is a classic trap question.

---

## Section 3: The `input()` Function

The `input()` function pauses the program, displays a prompt to the user, waits for the user to type something and press Enter, and then **returns the input as a `str`**.

### Basic Syntax

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Critical rule:** `input()` ALWAYS returns a `str`, regardless of what the user types.

```python
age = input("Enter your age: ")
print(type(age))    # <class 'str'> — even if user typed "21"
```

### Converting Input for Numeric Operations

Because `input()` returns a string, you must convert it before doing math:

```python
age_str = input("Enter your age: ")
age = int(age_str)                    # Convert to int for arithmetic
print("In 10 years you will be:", age + 10)
```

**Shorthand (common pattern):**

```python
age = int(input("Enter your age: "))
```

### Handling Potential Errors

If the user types non-numeric input and you try to convert it to `int`, Python raises a `ValueError`:

```python
# If user types "twenty" instead of "20":
age = int(input("Enter age: "))    # ValueError: invalid literal for int()
```

Error handling using `try`/`except` (covered in Module 14) is the proper solution. For now, assume users enter valid data unless instructed otherwise.

---

## Section 4: String Formatting

Python provides three ways to format strings. **f-strings** are the modern, preferred approach.

### Method 1: String Concatenation (Manual)

```python
name = "Alice"
score = 95
print("Student: " + name + " | Score: " + str(score))
```

Tedious — requires explicit `str()` conversion for every non-string value.

### Method 2: `.format()` Method

```python
print("Student: {} | Score: {}".format(name, score))
print("Student: {0} | Score: {1}".format(name, score))
print("Student: {name} | Score: {score}".format(name=name, score=score))
```

### Method 3: f-Strings (Recommended — Python 3.6+)

F-strings (formatted string literals) embed expressions directly in strings using `{}`:

```python
name = "Alice"
score = 95
gpa = 3.875

print(f"Student: {name} | Score: {score}")
print(f"GPA: {gpa:.2f}")           # Two decimal places
print(f"Score: {score:05d}")        # Padded to 5 digits with zeros
print(f"Upper: {name.upper()}")     # Expressions allowed inside {}
print(f"Score × 2 = {score * 2}")  # Arithmetic inside {}
```

**Common f-string format specifiers:**

| Specifier | Effect | Example | Result |
|---|---|---|---|
| `.2f` | Float, 2 decimal places | `f"{3.14159:.2f}"` | `3.14` |
| `.0f` | Float, no decimals (rounds) | `f"{3.7:.0f}"` | `4` |
| `d` | Integer (decimal) | `f"{42:d}"` | `42` |
| `05d` | Integer, padded to 5 with zeros | `f"{42:05d}"` | `00042` |
| `>10` | Right-align in field of 10 | `f"{'hi':>10}"` | `        hi` |
| `<10` | Left-align in field of 10 | `f"{'hi':<10}"` | `hi        ` |

---

## Section 5: The `round()` Function

`round()` rounds a number to a specified number of decimal places.

### Basic Usage

```python
print(round(3.14159))      # 3    — rounds to nearest integer
print(round(3.14159, 2))   # 3.14 — rounds to 2 decimal places
print(round(3.14159, 4))   # 3.1416
print(round(2.675, 2))     # 2.67 — float precision issue; not 2.68
```

### Python 3 Banker's Rounding (Round Half to Even)

Python 3 uses **banker's rounding** (round half to even) rather than always rounding 0.5 up:

```python
print(round(0.5))    # 0 — rounds to nearest EVEN number
print(round(1.5))    # 2 — rounds to nearest EVEN number
print(round(2.5))    # 2 — rounds to nearest EVEN number
print(round(3.5))    # 4 — rounds to nearest EVEN number
```

> **PCAP Exam Tip:** `round(2.5)` returns `2`, not `3`. Python 3's banker's rounding rounds 0.5 to the nearest **even** integer. This differs from everyday rounding rules and commonly appears on the exam.

---

## Section 6: Common Type Conversion Errors

### `ValueError` — Right Type, Wrong Value

Raised when the type is correct but the value cannot be converted:

```python
int("hello")      # ValueError — "hello" is a string but not a numeric string
int("3.14")       # ValueError — "3.14" has a decimal; use float() first
float("abc")      # ValueError
```

### `TypeError` — Wrong Type Entirely

Raised when the type is fundamentally incompatible:

```python
int([1, 2, 3])    # TypeError — lists cannot be converted to int
int(None)         # TypeError — None cannot be converted
"Score: " + 95    # TypeError — cannot concatenate str and int
```

---

## Section 7: Complete `input()` Program Example

```python
# Student Grade Calculator
print("=== Student Grade Calculator ===")

student_name = input("Enter student name: ")
exam1 = float(input("Enter exam 1 score (0-100): "))
exam2 = float(input("Enter exam 2 score (0-100): "))
exam3 = float(input("Enter exam 3 score (0-100): "))

average = (exam1 + exam2 + exam3) / 3
passed = average >= 70

print(f"\n--- Report for {student_name} ---")
print(f"Exam 1: {exam1:.1f}")
print(f"Exam 2: {exam2:.1f}")
print(f"Exam 3: {exam3:.1f}")
print(f"Average: {average:.2f}")
print(f"Passed: {passed}")
```

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| **Implicit conversion** | Automatic type promotion by Python (int → float when mixed in arithmetic) |
| **Explicit conversion** | Manual conversion using `int()`, `float()`, `str()`, or `bool()` |
| **`int()`** | Converts to integer; truncates floats toward zero; raises ValueError on non-numeric strings |
| **`float()`** | Converts to float; accepts `"inf"`, `"nan"` as special values |
| **`str()`** | Converts any value to its string representation |
| **`bool()`** | Converts any value to True or False using truthiness rules |
| **`input()`** | Built-in function that reads user input as a string |
| **f-string** | Formatted string literal (f"...{expression}...") — Python 3.6+ |
| **`round()`** | Rounds a number; Python 3 uses banker's rounding (round half to even) |
| **`ValueError`** | Raised when a function receives the right type but an invalid value |
| **`TypeError`** | Raised when an operation is applied to an incompatible type |
| **Banker's rounding** | Rounding 0.5 to the nearest even integer (Python 3 default) |

---

## External Resources

| Resource | Link | What to Study |
|---|---|---|
| Python `input()` | [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input) | Function signature and return type |
| Python f-strings | [docs.python.org/3/reference/lexical_analysis.html#f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) | Full syntax and format specifiers |
| Python `round()` | [docs.python.org/3/library/functions.html#round](https://docs.python.org/3/library/functions.html#round) | Banker's rounding behavior |
| edube.org PE1 Module 2 | [edube.org](https://edube.org/) | Type conversion exercises |

---

## Self-Check Review Questions

1. Why does `int("3.14")` raise a `ValueError` but `int(float("3.14"))` works?
2. What is the difference between `int(3.9)` and `3.9 // 1`? Which truncates toward zero and which floors?
3. What does `bool("False")` return? Why?
4. What is the output of `round(2.5)` and `round(3.5)` in Python 3? What rule governs this?
5. Write a complete program that asks the user for two numbers and prints their sum, difference, and average using f-strings with 2 decimal places.

---

*Next Module → Module 5: Conditional Statements (if/elif/else)*
*Unit Test 1 covers Modules 1–4 — review all module quizzes before attempting.*
