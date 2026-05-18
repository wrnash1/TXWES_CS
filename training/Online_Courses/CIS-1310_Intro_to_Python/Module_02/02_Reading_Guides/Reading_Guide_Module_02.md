# Reading Guide: Module 2 — Variables, Literals, and Data Types

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Certification Alignment:** PCAP — Certified Associate in Python Programming
**PCAP Exam Section:** Section 2 — Data Types, Evaluation, Basic I/O, Operators
**Estimated Reading Time:** 45–60 minutes
**OER Resources:** [edube.org PE1 Module 2](https://edube.org/) | [Python 3 Built-in Types](https://docs.python.org/3/library/stdtypes.html)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define what a variable is and explain how Python manages variable assignment
2. Apply Python's variable naming rules to create valid identifiers
3. Identify and differentiate the five primitive data types: `int`, `float`, `str`, `bool`, and `NoneType`
4. Recognize and write numeric literals in decimal, binary, octal, and hexadecimal formats
5. Use the `type()` function to inspect the data type of any value
6. Perform multiple assignment and augmented assignment operations
7. Explain Python's dynamic typing model and how it differs from static typing

---

## Section 1: Variables in Python

A **variable** is a named storage location in memory that holds a value. In Python, you create a variable the moment you assign a value to it — there is no separate declaration step.

### Assignment Syntax

```python
variable_name = value
```

The `=` symbol is the **assignment operator** — it is NOT the mathematical equality sign. It means "store the value on the right into the variable on the left."

```python
age = 21
name = "Alex"
gpa = 3.85
enrolled = True
```

After these lines run, Python has four variables in memory, each holding a different type of value.

### Python's Dynamic Typing

Python is **dynamically typed**, meaning:
- You do not declare the type of a variable
- The type is determined by the value assigned to it
- The type can change when a new value is assigned

```python
x = 10        # x is int
x = "hello"   # x is now str — the previous int value is discarded
x = 3.14      # x is now float
```

This contrasts with **statically typed** languages like Java or C++, where you must declare the type upfront and cannot change it. In Java, attempting `int x = 10; x = "hello";` causes a compile error.

> **PCAP Exam Tip:** "Dynamic typing" means types are associated with values (objects), not with variable names. The variable is just a label pointing to an object in memory.

### Variables Are References

In Python, a variable does not directly contain a value — it holds a **reference** (pointer) to an object in memory.

```python
x = [1, 2, 3]
y = x           # y points to the SAME list object as x
y.append(4)
print(x)        # Output: [1, 2, 3, 4] — x also shows the change
```

Understanding references becomes critical when working with mutable types (lists, dictionaries) in later modules.

---

## Section 2: Variable Naming Rules

Python has strict rules for variable names (identifiers) that you must follow, plus PEP 8 conventions you should follow.

### Legal Naming Rules (Required — Violations Cause Errors)

| Rule | Valid Examples | Invalid Examples |
|---|---|---|
| Letters, digits, and underscores only | `name`, `value_2`, `_x` | `my-name`, `my name` |
| Must begin with a letter or underscore | `name`, `_temp`, `GPA` | `2fast`, `9lives` |
| Case-sensitive | `age`, `Age`, `AGE` are different | — |
| Cannot be a Python keyword | `score`, `total` | `if`, `for`, `class`, `None` |

### Python Keywords (Cannot Be Used as Variable Names)

```
False    await    else     import   pass
None     break    except   in       raise
True     class    finally  is       return
and      continue for      lambda   try
as       def      from     nonlocal while
assert   del      global   not      with
async    elif     if       or       yield
```

Attempting to use a keyword as a variable name raises a `SyntaxError`.

### PEP 8 Naming Conventions

| Identifier Type | Convention | Example |
|---|---|---|
| Variables and functions | `snake_case` | `student_name`, `total_score` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_GRADE = 100`, `PI = 3.14159` |
| Classes | `PascalCase` (CapWords) | `class StudentRecord:` |
| Private identifiers | `_leading_underscore` | `_internal_count` |

---

## Section 3: Literals

A **literal** is a value written directly in source code. Python recognizes five categories of primitive literals.

### Integer Literals (`int`)

Whole numbers — positive, negative, or zero. Python integers have **unlimited precision** (no overflow).

```python
count    = 42          # Decimal (base 10)
negative = -100        # Negative integer
zero     = 0

# Underscore separators improve readability (Python 3.6+)
population = 8_100_000_000     # Easier to read than 8100000000
```

**Non-decimal integer formats:**

```python
binary_val = 0b1010     # Binary (base 2), prefix 0b — value is 10
octal_val  = 0o17       # Octal (base 8), prefix 0o — value is 15
hex_val    = 0xFF       # Hexadecimal (base 16), prefix 0x — value is 255
```

All are stored as `int` — the prefix only tells Python how to interpret the literal:

```python
print(0b1010)    # 10
print(0o17)      # 15
print(0xFF)      # 255
print(type(0b1010))   # <class 'int'>
```

### Float Literals (`float`)

Numbers with a decimal point. Uses 64-bit IEEE 754 double precision.

```python
pi          = 3.14159
temperature = -17.5
whole       = 1.0         # Note: 1 (int) and 1.0 (float) have different types

# Scientific notation
speed_of_light = 3e8       # 3 × 10^8 = 300000000.0
electron_mass  = 9.11e-31  # Very small number
```

> **PCAP Exam Tip:** Float arithmetic can produce surprising results due to binary representation:
> ```python
> print(0.1 + 0.2)    # 0.30000000000000004 — not exactly 0.3
> ```
> This is a known limitation of floating-point arithmetic, not a Python bug.

### String Literals (`str`)

Sequences of characters in quotes. Python accepts single, double, or triple quotes.

```python
first_name = "Alice"
city       = 'Fort Worth'
empty      = ""             # Empty string — valid, length is 0

# Triple quotes allow multi-line strings
message = """Dear Student,
Welcome to CIS-1310.
Good luck this semester!"""
```

Strings are explored in depth in Module 9. For now, understand that any value in quotes is type `str`.

### Boolean Literals (`bool`)

Exactly two values: `True` and `False` (must be capitalized).

```python
is_enrolled = True
has_passed  = False
```

Booleans are a **subclass of int** in Python: `True` evaluates to `1` and `False` evaluates to `0`:

```python
print(True + True)    # 2
print(False + 10)     # 10
print(int(True))      # 1
print(int(False))     # 0
```

**Truthy and Falsy values** — Python treats certain values as `False` in boolean context:

| Evaluates to `False` | Evaluates to `True` |
|---|---|
| `False` | `True` |
| `0`, `0.0` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `None` | Any non-None value |
| `[]`, `{}`, `()` (empty collections) | Any non-empty collection |

```python
print(bool(0))       # False
print(bool(42))      # True
print(bool(""))      # False
print(bool("hi"))    # True
print(bool(None))    # False
```

### None Literal (`NoneType`)

`None` is Python's null value — it represents the **absence of a value**. It is the only instance of `NoneType`.

```python
result = None
print(result)          # None
print(type(result))    # <class 'NoneType'>
print(result is None)  # True — use 'is' not '==' to check for None
```

`None` is commonly used as a function's default return value, as a placeholder for missing data, and to reset a variable.

---

## Section 4: The `type()` Function

`type()` is a built-in function that returns the class (type) of any value or variable.

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>

x = 100
print(type(x))         # <class 'int'>
x = "now a string"
print(type(x))         # <class 'str'>  — dynamic typing in action
```

### Checking Type with `isinstance()`

`isinstance()` is preferred over comparing `type()` results when testing for compatibility:

```python
x = 42
print(isinstance(x, int))           # True
print(isinstance(x, float))         # False
print(isinstance(x, (int, float)))  # True — accepts tuple of types
print(isinstance(True, int))        # True — bool is a subclass of int
```

---

## Section 5: Multiple Assignment and Augmented Assignment

### Assign the Same Value to Multiple Variables

```python
x = y = z = 0
print(x, y, z)    # 0 0 0
```

### Tuple Unpacking — Multiple Values in One Statement

```python
a, b, c = 1, 2, 3
print(a, b, c)    # 1 2 3

# Classic Python swap — no temporary variable needed
x = 10
y = 20
x, y = y, x
print(x, y)       # 20 10
```

### Augmented Assignment Operators

| Operator | Example | Equivalent | Result (x=10) |
|---|---|---|---|
| `+=` | `x += 5` | `x = x + 5` | `15` |
| `-=` | `x -= 3` | `x = x - 3` | `7` |
| `*=` | `x *= 2` | `x = x * 2` | `20` |
| `/=` | `x /= 4` | `x = x / 4` | `2.5` |
| `//=` | `x //= 3` | `x = x // 3` | `3` |
| `%=` | `x %= 3` | `x = x % 3` | `1` |
| `**=` | `x **= 2` | `x = x ** 2` | `100` |

```python
score = 0
score += 10    # Player scores 10 points
score *= 2     # Score doubled (bonus round)
print(score)   # 20
```

---

## Section 6: Data Type Summary

| Type | Keyword | Literal Examples | `type()` Result |
|---|---|---|---|
| Integer | `int` | `42`, `-7`, `0b1010`, `0xFF` | `<class 'int'>` |
| Float | `float` | `3.14`, `-17.5`, `3e8` | `<class 'float'>` |
| String | `str` | `"hello"`, `'world'`, `"""block"""` | `<class 'str'>` |
| Boolean | `bool` | `True`, `False` | `<class 'bool'>` |
| None | `NoneType` | `None` | `<class 'NoneType'>` |

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| **Variable** | A named reference that points to an object in memory |
| **Assignment operator** | `=` — stores a value in a variable (not mathematical equality) |
| **Dynamic typing** | Types are associated with values/objects, not variable names |
| **Literal** | A value written directly in source code (`42`, `"hello"`, `True`) |
| **`int`** | Python's integer type — whole numbers, unlimited precision |
| **`float`** | Python's floating-point type — decimal numbers (64-bit) |
| **`str`** | Python's string type — sequences of characters |
| **`bool`** | Python's boolean type — only `True` or `False`; subclass of `int` |
| **`NoneType`** | The type of `None` — Python's null/no-value object |
| **`type()`** | Built-in function returning the data type of a value |
| **`isinstance()`** | Built-in function checking if a value is of a specified type |
| **Augmented assignment** | Operators like `+=`, `-=` that combine arithmetic and assignment |
| **Tuple unpacking** | Assigning multiple values to multiple variables in one statement |
| **Truthy/Falsy** | Whether a value evaluates to `True` or `False` in a boolean context |

---

## External Resources

| Resource | Link | What to Study |
|---|---|---|
| Python Built-in Types | [docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html) | Numeric Types, Boolean, None |
| Lexical Analysis — Literals | [docs.python.org/3/reference/lexical_analysis.html](https://docs.python.org/3/reference/lexical_analysis.html) | Sections 2.4.4–2.4.8 |
| edube.org PE1 Module 2 | [edube.org](https://edube.org/) | Data types, literals, type conversion |
| Python Keywords Reference | [docs.python.org/3/reference/lexical_analysis.html#keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords) | Full reserved keyword list |

---

## Self-Check Review Questions

1. Why will `2variable = 10` raise a `SyntaxError` while `variable2 = 10` does not?
2. What is the output of `type(True)` and why is it a subclass of `int`?
3. Write the integer `255` as a binary, octal, and hexadecimal literal.
4. What does `bool(0)`, `bool("")`, and `bool(None)` each evaluate to, and why?
5. Write a single Python statement that swaps the values of `x` and `y` without a temporary variable.
6. What is the difference between `x = y = 0` and `x, y = 0, 1`?
7. Why might `0.1 + 0.2 == 0.3` return `False` in Python?

---

*Next Module → Module 3: Operators — Arithmetic, Comparison, and Logical*
