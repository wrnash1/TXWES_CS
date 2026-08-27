# Reading Guide: Module 02 — Literals, Operators, and Expressions

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 02 — Literals, Operators, and Expressions**. This module gives you the raw building blocks every Python program is made of: the literal values written directly in code, the data types Python assigns to them, and the operators that transform them into new values. There is no module in this course that is more directly tested on the PCAP exam than this one — operator precedence, data type behaviors, and expression evaluation appear on almost every practice exam.

Complete this reading guide before starting the lab. Work through every glossary entry, trace through every example in the Exam Tips section by hand, and verify your answers in the REPL before moving on.

---

## 1. High-Yield Glossary

### Literal

A fixed value written directly in source code. When you type `42`, `3.14`, `'Hello'`, or `True` in a Python program, those are literals. Python reads them as their exact value with no further evaluation needed.

### int

Python's integer type. Represents any whole number — positive, negative, or zero — with no decimal component. Python `int` is **arbitrarily large** — it has no fixed maximum value and never overflows, unlike 32-bit integers in C or Java. Integer literals can be written in decimal (`42`), binary (`0b1010`), octal (`0o17`), or hexadecimal (`0xFF`) notation.

### float

Python's floating-point type. Represents real numbers with a decimal point, stored as **IEEE 754 double-precision** (64-bit binary format). Because of binary representation, some decimal values cannot be stored exactly — `0.1` is a classic example. This leads to results like `0.1 + 0.2 = 0.30000000000000004`. This is not a Python bug — it is a universal property of binary floating-point arithmetic. Always use tolerance comparisons (`abs(a - b) < epsilon`) rather than `==` when comparing floats.

### str

Python's string type. An **immutable** sequence of Unicode characters. "Immutable" means once created, a string cannot be changed — operations that appear to modify strings actually create new ones. String literals are enclosed in single quotes (`'hello'`), double quotes (`"hello"`), or triple quotes (`'''hello'''` or `"""hello"""`). Triple-quoted strings span multiple lines.

### Escape Sequences

Special character combinations starting with `\` that represent characters you cannot type directly:

| Sequence | Meaning |
|---|---|
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Literal backslash |
| `\'` | Literal single quote |
| `\"` | Literal double quote |

### bool

Python's boolean type. Has exactly two values: `True` and `False` (both capitalized — Python is case-sensitive). Critical fact: **`bool` is a subclass of `int`**. `True` equals `1`, `False` equals `0`. This means `True + True` evaluates to `2`, and `True * 5` evaluates to `5` — valid Python that the PCAP exam tests repeatedly.

### None

The `NoneType` singleton. Represents intentional absence of a value. `None` is not `0`, not `False`, not an empty string — it is strictly `None`. Functions that do not explicitly return a value return `None` by default.

### Arithmetic Operators

Python's seven arithmetic operators:

| Operator | Name | Notes |
|---|---|---|
| `+` | Addition | |
| `-` | Subtraction | |
| `*` | Multiplication | |
| `/` | True division | Always returns `float` in Python 3 |
| `//` | Floor division | Rounds toward negative infinity |
| `%` | Modulo | Returns remainder; follows divisor sign |
| `**` | Exponentiation | Right-associative |

### True Division vs. Floor Division

`/` (true division) always returns a `float`, even when both operands are integers: `4 / 2` = `2.0`.

`//` (floor division) rounds the result **down toward negative infinity**. With positive numbers this looks like truncation. With negative numbers it differs: `-7 // 2` = `-4`, not `-3`. (Truncation gives `-3`; floor gives `-4` because `-4` is the next integer below `-3.5`.)

### Modulo

The `%` operator returns the remainder after floor division. In Python, the result's sign follows the **divisor** (second operand), not the dividend. So `-7 % 2` = `1` (positive, following the divisor `2`). This differs from C and Java, where modulo follows the sign of the dividend.

### Operator Precedence

The rules governing which operator is evaluated first in a multi-operator expression. Python's arithmetic precedence (highest to lowest):

```text
1. **           (exponentiation — RIGHT-to-left)
2. Unary -      (negation, e.g., -x)
3. *, /, //, %
4. +, -         (lowest)
```

### Operator Associativity

When operators have the same precedence, associativity determines left-to-right or right-to-left evaluation. Most Python operators are **left-associative** (`8 - 3 - 2` = `(8 - 3) - 2` = `3`). The **`**` operator is right-associative**: `2 ** 3 ** 2` = `2 ** (3 ** 2)` = `2 ** 9` = `512`.

### Type Conversion Functions

Built-in functions that convert values between types:

| Function | Converts to | Notes |
|---|---|---|
| `int(x)` | `int` | Truncates floats (does NOT round); fails on float-like strings |
| `float(x)` | `float` | Works on int and numeric strings |
| `str(x)` | `str` | Works on any type |
| `bool(x)` | `bool` | Evaluates truthiness |

### Truthiness and Falsiness

Every Python value has a boolean truth value. **Falsy** values (evaluate to `False`): `0`, `0.0`, `''` (empty string), `[]` (empty list), `{}` (empty dict), `set()`, `None`. **Everything else is truthy** (evaluates to `True`). This concept underpins all control flow in Python.

### Comparison Operators

Operators that compare two values and return `True` or `False`:

`==`, `!=`, `<`, `>`, `<=`, `>=`

Critical distinction: `==` tests equality. `=` is assignment. Using `=` in a comparison expression is a `SyntaxError`.

### Logical Operators

`and` — returns `True` only if both operands are truthy.
`or` — returns `True` if at least one operand is truthy.
`not` — returns the inverse boolean of its operand.

---

## 2. Operator Precedence — Full Python Reference

Below is the complete Python operator precedence table from highest (top) to lowest (bottom). You only need to memorize the arithmetic portion for Module 02; the rest becomes relevant in later modules.

```text
Precedence  Operator(s)          Description
----------  -------------------  ---------------------------
Highest     ()                   Parentheses — override all
            **                   Exponentiation (right-to-left)
            +x, -x, ~x           Unary plus, minus, bitwise NOT
            *, @, /, //, %       Multiplication, matrix mult, division
            +, -                 Addition, subtraction
            <<, >>               Bitwise shifts
            &                    Bitwise AND
            ^                    Bitwise XOR
            |                    Bitwise OR
            ==, !=, <, >, <=, >= Comparisons
            not                  Logical NOT
            and                  Logical AND
Lowest      or                   Logical OR
```

---

## 3. Expression Tracing Practice

Work through each expression by hand **before** checking in the REPL. Tracing expressions manually is the skill the PCAP exam directly tests.

**Expression 1:** `2 + 3 * 4`

Step 1: `*` has higher precedence than `+`, so `3 * 4 = 12` first.
Step 2: `2 + 12 = 14`
Answer: `14`

**Expression 2:** `10 - 2 ** 3`

Step 1: `**` is highest, so `2 ** 3 = 8` first.
Step 2: `10 - 8 = 2`
Answer: `2`

**Expression 3:** `-2 ** 2`

Step 1: `**` has higher precedence than unary `-`, so `2 ** 2 = 4` first.
Step 2: Apply unary minus: `-(4) = -4`
Answer: `-4` (NOT `4`)

**Expression 4:** `2 ** 3 ** 2`

Step 1: `**` is right-associative, so evaluate right-to-left: `3 ** 2 = 9` first.
Step 2: `2 ** 9 = 512`
Answer: `512` (NOT `64`)

**Expression 5:** `10 % 3 ** 2`

Step 1: `**` beats `%`, so `3 ** 2 = 9` first.
Step 2: `10 % 9 = 1`
Answer: `1`

**Expression 6:** `-7 // 2`

Floor division floors toward negative infinity. `-7 / 2 = -3.5`. Floor of `-3.5` = `-4`.
Answer: `-4`

---

## 4. Certification Exam Tips

**Tip 1 — `-2 ** 2` = `-4`, not `4`.**
Unary minus has lower precedence than `**`. The expression reads as `-(2 ** 2)`. This is possibly the most common precedence trap on the PCAP exam.

**Tip 2 — `4 / 2` = `2.0`, not `2`.**
In Python 3, `/` always returns `float`. Students from Python 2 or other languages expect integer division when both operands are integers. Python 3 changed this. Know it.

**Tip 3 — `0.1 + 0.2` is not `0.3`.**
The result is `0.30000000000000004`. Never use `==` to compare floats. This appears on PCAP in questions about float equality comparisons.

**Tip 4 — `True + True` = `2`.**
`bool` is a subclass of `int`. `True` equals `1`. `False` equals `0`. Arithmetic on booleans is valid Python and PCAP tests it.

**Tip 5 — `int(3.9)` = `3`, not `4`.**
`int()` truncates — it drops the decimal toward zero. It does NOT round.

**Tip 6 — `**` is right-associative.**
`2 ** 3 ** 2` = `2 ** (3 ** 2)` = `2 ** 9` = `512`. The rightmost `**` evaluates first.

**Tip 7 — Binary, octal, and hex literals.**
Know the prefixes: `0b` (binary), `0o` (octal), `0x` (hex). The PCAP may ask what value `0b1010` represents — the answer is `10`.

---

## 5. Beyond the Exam — Real-World Context

**Why does float imprecision matter in real software?**
In financial applications, using `float` for currency calculations is a bug, not just an inconvenience. If you're calculating a total bill and `0.1 + 0.2 = 0.30000000000000004`, your invoices will be off by fractions of a cent — and those errors accumulate over millions of transactions. The solution is Python's `decimal` module, which provides exact decimal arithmetic. The PCAP doesn't test `decimal`, but every professional Python developer working in finance knows it.

**Why does Python use floor division instead of truncation?**
Mathematical modulo is defined such that `a == (a // b) * b + (a % b)`. If Python used truncation for `//`, this equation would still hold, but the sign behavior would differ from mathematical convention. Python chose mathematical consistency — floor division and modulo match how mathematicians define these operations. C chose truncation for performance. This is a conscious design decision, not an oversight.

**Why is `bool` a subclass of `int`?**
Historically, Python didn't have a `bool` type at all — `True` and `False` were just `1` and `0`. When `bool` was added in Python 2.3, making it a subclass of `int` preserved backward compatibility with all existing code that used `1` and `0` as truth values. It's an example of the engineering tradeoffs that go into language design.

---

## 6. Required Readings & Videos

**Required Reading — Chapter 2:**
Read Chapter 2 "Variables, Expressions, and Statements" in [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). Focus especially on the sections about values, types, operators, and order of operations. Work through every example.

**Required Reading — Official Python Docs, Expressions:**
Read the [Operator Precedence table](https://docs.python.org/3/reference/expressions.html#operator-precedence) in the official Python documentation. Bookmark this page — you will reference it throughout the course.

**Required Video — Python for Everybody Playlist, Episodes 3–4:**
Watch episodes 3 and 4 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). These cover data types and expressions with live REPL demonstrations.

---

## 7. Lab & Command Preview

| Task | What You Will Do |
|---|---|
| REPL data type exploration | Test `type()` on `int`, `float`, `str`, `bool`, `None` literals |
| Binary/octal/hex integers | Enter `0b1010`, `0o17`, `0xFF` and observe results |
| Float precision | Type `0.1 + 0.2` and observe the result |
| All 7 arithmetic operators | Test each with positive and negative operands |
| Precedence tracing | Predict output before running; verify in REPL |
| `circle.py` script | Compute area and circumference using `math.pi` |
| `temp_converter.py` | Convert Fahrenheit to Celsius: `C = (F - 32) * 5 / 9` |
| Type conversion exercises | Use `int()`, `float()`, `str()`, `bool()` on various inputs |

---

## 9. Supplemental Resources

**1. Official Python 3 Docs — Built-in Types**
[https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)
The authoritative reference for all built-in types including `int`, `float`, `bool`, `str`, and `NoneType`. Sections on numeric types cover truthiness, arithmetic operations, and type hierarchy. Essential bookmarked reading for the PCAP exam.

**2. Python for Everybody — Chapter 2: Variables, Expressions and Statements**
[https://www.py4e.com/html3/02-variables](https://www.py4e.com/html3/02-variables)
Dr. Severance's free textbook chapter directly aligned to Module 02 topics. Covers literals, operators, order of operations, and type conversions with clear examples and practice exercises.

**3. Real Python — Operators and Expressions in Python**
[https://realpython.com/python-operators-expressions/](https://realpython.com/python-operators-expressions/)
A comprehensive free article covering all Python operators, precedence rules, and associativity with worked examples. The section on augmented assignment operators previews content from Module 03.

**4. Python Docs — Floating Point Arithmetic: Issues and Limitations**
[https://docs.python.org/3/tutorial/floatingpoint.html](https://docs.python.org/3/tutorial/floatingpoint.html)
The official explanation of why `0.1 + 0.2 != 0.3`. Essential reading for understanding IEEE 754 binary floating-point and why you should never use `==` to compare floats. This page is directly referenced in PCAP study materials.

**5. Wikipedia — IEEE 754 Floating-Point Standard (Simplified Overview)**
[https://en.wikipedia.org/wiki/IEEE_754](https://en.wikipedia.org/wiki/IEEE_754)
Background reading on the binary floating-point standard that governs Python's `float` type. The "Basic and interchange formats" section explains double-precision (64-bit) format used by Python. Understanding this removes all mystery from float imprecision issues.

---

## 8. Study Checklist

Work through in order:

- [ ] Watch the Module 02 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary above — verify each definition in the REPL.
- [ ] Work through the Expression Tracing Practice in Section 3 by hand before checking in REPL.
- [ ] Read Chapter 2 of *Python for Everybody* at py4e.com.
- [ ] Read the Operator Precedence table in the Official Python 3 documentation.
- [ ] Watch Episodes 3–4 of the Python for Everybody video playlist.
- [ ] Review the Certification Exam Tips in Section 4.
- [ ] Preview the lab tasks in Section 7.
- [ ] Proceed to the Module 02 Lab Activity.
