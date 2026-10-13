# Video Script: CIS-1310 — Introduction to Python

## Module 02 — Literals, Operators, and Expressions

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
> - Use screen-share for all [DEMO] sections — run everything live in the Python REPL inside Ubuntu.
> - [PAUSE] markers = hold 2 seconds before continuing.
> - Show the exact output after each REPL entry — students will pause and type along.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 02 | Literals, Operators, and Expressions | CIS-1310"]**

"Welcome back, everyone. I'm Professor Nash. If you're here, that means you have Python running in Ubuntu inside VirtualBox, you understand the difference between the REPL and script mode, and you've written your first real Python scripts. That's solid work.

This module is where we get into the actual building blocks of every Python program you will ever write: **literals** — the raw fixed values written directly in code — **data types** — what kind of value each literal represents — and **operators** — the symbols that let you compute new values from existing ones. The PCAP exam hits all of this hard. Let's go."

---

## [00:45 – 02:30] What Is a Literal?

**[SHOW SLIDE: "Literals — Fixed Values Written Directly in Code"]**

"Every program works with data. Some data comes from users, files, or databases. But the simplest kind of data is a **literal** — a value you write directly into your source code.

When you type `42` in a Python program, that is an **integer literal** — the actual number forty-two is right there in the code. `3.14` is a **float literal**. `'Hello'` is a **string literal**. `True` is a **boolean literal**.

Python reads those values exactly as written. They are *literally* right there.

**[DEMO — switch to REPL]**

```python
>>> 42
42
>>> 3.14
3.14
>>> 'Hello'
'Hello'
>>> True
True
```

Now let's check their types using the `type()` function:

```python
>>> type(42)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type('Hello')
<class 'str'>
>>> type(True)
<class 'bool'>
```

The `type()` function is one of your best debugging tools. It tells you exactly what Python is working with. Use it constantly — especially when an operation isn't behaving the way you expect.

Let's go through each type in detail."

---

## [02:30 – 06:00] Python's Core Data Types

**[SHOW SLIDE: "The Four Core Data Types: int, float, str, bool"]**

### int — Integer Numbers

"An `int` is any whole number — positive, negative, or zero. No decimal point.

```python
>>> 42
42
>>> -100
-100
>>> 0
0
```

Python's `int` is **arbitrarily large** — no fixed maximum. You can compute `2 ** 1000` and Python handles it without overflow or error. This is a major difference from C and Java, where integers have strict size limits.

Integer literals can be written in different bases — and the PCAP exam tests all three:

```python
>>> 0b1010
10
>>> 0o17
15
>>> 0xFF
255
```

- `0b` prefix = binary (base 2)
- `0o` prefix = octal (base 8)
- `0x` prefix = hexadecimal (base 16)

All three are just regular Python `int` values — different notation, same type.

**[PAUSE]**

### float — Floating-Point Numbers

A `float` is a number with a decimal point. Python uses **IEEE 754 double-precision** — 64-bit binary floating-point.

```python
>>> 3.14
3.14
>>> -0.5
-0.5
>>> 1e6
1000000.0
>>> 2.5e-3
0.0025
```

Scientific notation: `1e6` means 1 times 10 to the power of 6. `2.5e-3` means 2.5 times 10 to the negative 3.

Now — here is the most important PCAP trap in this entire module. Watch this:

```python
>>> 0.1 + 0.2
0.30000000000000004
```

That is **not** a Python bug. That is how IEEE 754 binary floating-point works in every programming language that uses it — C, Java, JavaScript, Python, all of them. `0.1` cannot be represented exactly in binary. Neither can `0.2`. When you add two approximations, the tiny errors accumulate, and you get a result that is slightly more than `0.3`.

The PCAP exam tests this. The lesson: never use `==` to compare two floats for exact equality. Instead, check if they are close enough using `abs(a - b) < 0.0001` or the `math.isclose()` function.

**[PAUSE]**

### str — Strings

A `str` is an immutable sequence of Unicode characters. You can create string literals three ways:

```python
>>> 'single quotes'
'single quotes'
>>> \"double quotes\"
'double quotes'
>>> \"\"\"triple quotes
... span multiple lines\"\"\"
'triple quotes\nspan multiple lines'
```

Single and double quotes work identically. Triple quotes are for multi-line strings.

**Escape sequences** are special characters that start with a backslash:

```python
>>> print('Line 1\nLine 2')
Line 1
Line 2
>>> print('Column1\tColumn2')
Column1	Column2
>>> print('It\\'s easy')
It's easy
```

- `\n` — newline
- `\t` — tab
- `\\` — literal backslash
- `\'` — literal single quote (inside single-quoted strings)
- `\"` — literal double quote (inside double-quoted strings)

**[PAUSE]**

### bool — Booleans

A `bool` has exactly two possible values: `True` and `False`. Capital T, capital F — Python is case-sensitive. `true` and `false` with lowercase letters are NOT keywords — they would be treated as variable names and raise a `NameError`.

Here is the critical fact: **`bool` is a subclass of `int` in Python**. `True` equals `1`. `False` equals `0`.

```python
>>> True == 1
True
>>> False == 0
True
>>> True + True
2
>>> True * 10
10
>>> int(True)
1
>>> int(False)
0
```

`True + True` equals `2`. That is a guaranteed PCAP question. Because `bool` inherits from `int`, arithmetic on booleans is completely valid Python.

### None

`None` is its own special type — `NoneType`. It represents the intentional absence of a value.

```python
>>> type(None)
<class 'NoneType'>
>>> None == 0
False
>>> None == False
False
```

`None` is not zero. `None` is not `False`. `None` is strictly `None`. We use it as a placeholder and as the default return value of functions that don't return anything explicitly."

---

## [06:00 – 08:30] Arithmetic Operators

**[SHOW SLIDE: "Python's Seven Arithmetic Operators"]**

"Python has seven arithmetic operators. All seven appear on the PCAP exam.

```python
>>> 5 + 3
8
>>> 5 - 3
2
>>> 5 * 3
15
>>> 10 / 4
2.5
>>> 10 // 4
2
>>> 10 % 3
1
>>> 2 ** 8
256
```

The first three are straightforward. Let me focus on the four that cause confusion.

### True Division vs. Floor Division

`/` is **true division**. In Python 3, it always returns a `float` — always, no exceptions.

```python
>>> 10 / 2
5.0
>>> 4 / 2
2.0
```

Even `4 / 2` — two numbers that divide evenly — returns `2.0`, not `2`. This changed from Python 2, and it trips up people who learned Python 2.

`//` is **floor division**. It divides and rounds **toward negative infinity** — the 'floor.'

```python
>>> 10 // 3
3
>>> 7 // 2
3
```

The word 'floor' is key. With positive numbers, flooring looks like truncation — you drop the decimal. But with negative numbers, they're different:

```python
>>> -7 // 2
-4
```

Truncation toward zero would give you `-3`. Floor division gives you `-4` — the next integer below. The PCAP exam tests negative floor division specifically.

### Modulo

Modulo returns the **remainder** after floor division:

```python
>>> 10 % 3
1
>>> 7 % 2
1
>>> 100 % 10
0
```

Real-world use: `n % 2` tells you even or odd — `0` means even, `1` means odd. With negatives:

```python
>>> -7 % 2
1
```

Python's modulo follows the sign of the **divisor** (the second number). This is mathematical modulo behavior — different from C and Java which follow the dividend sign.

### Exponentiation

```python
>>> 2 ** 10
1024
>>> 4 ** 0.5
2.0
>>> 27 ** (1/3)
3.0
```

`**` works with floats — `4 ** 0.5` is the square root of 4. `27 ** (1/3)` is the cube root of 27."

---

## [08:30 – 10:30] Operator Precedence — The Rules and the Traps

**[SHOW SLIDE: "Operator Precedence — Highest to Lowest"]**

"When an expression has multiple operators, Python uses **precedence rules** to decide the order of evaluation. Higher precedence operations go first.

For arithmetic, highest to lowest:

```text
1.  **          exponentiation  (RIGHT-to-left associativity)
2.  Unary -     negation (e.g., -x)
3.  *, /, //, %
4.  +, -
```

Let's trace through examples:

```python
>>> 2 + 3 * 4
14
```

`*` beats `+` — so `3 * 4 = 12` first, then `2 + 12 = 14`.

```python
>>> 10 - 2 ** 3
2
```

`**` is highest — `2 ** 3 = 8` first, then `10 - 8 = 2`.

**The #1 PCAP trap — negation and exponentiation:**

```python
>>> -2 ** 2
-4
```

Most students expect `4`. The logic seems to be: negative 2, squared, equals 4. But Python evaluates `**` before unary minus. So it reads as `-(2 ** 2)` = `-(4)` = `-4`.

To get `4`, you need parentheses:

```python
>>> (-2) ** 2
4
```

**[PAUSE]**

**`**` is right-associative — this matters:**

```python
>>> 2 ** 3 ** 2
512
```

Most operators evaluate left to right. `**` evaluates right to left. So this is `2 ** (3 ** 2)` = `2 ** 9` = `512`. Not `(2 ** 3) ** 2` = `8 ** 2` = `64`.

**Parentheses override everything:**

```python
>>> (2 + 3) * 4
20
>>> 2 + (3 * 4)
14
```

When in doubt, add parentheses. They make your intent explicit and your code readable."

---

## [10:30 – 11:45] Comparison and Logical Operators

**[SHOW SLIDE: "Comparison and Logical Operators"]**

"Two more sets of operators you need for Module 04 (Control Flow) and the PCAP exam.

**Comparison operators** — they produce `True` or `False`:

```python
>>> 5 == 5
True
>>> 5 != 3
True
>>> 10 > 7
True
>>> 3 >= 3
True
>>> 2 < 1
False
```

Critical distinction: `==` is comparison. `=` is assignment. Writing `if x = 5` is a `SyntaxError` in Python.

**Logical operators** — `and`, `or`, `not`:

```python
>>> True and True
True
>>> True and False
False
>>> False or True
True
>>> not True
False
>>> not False
True
```

`and` — both must be `True`. `or` — at least one must be `True`. `not` — flips the value.

We'll use these constantly starting in Module 04."

---

## [11:45 – 13:15] Type Conversion Functions

**[SHOW SLIDE: "Type Conversion: int(), float(), str(), bool()"]**

"Python gives you four built-in functions to convert values between types:

```python
>>> int(3.9)
3
```

`int()` **truncates** floats — it drops the decimal, it does NOT round. `3.9` becomes `3`, not `4`.

```python
>>> int('42')
42
>>> float('3.14')
3.14
>>> str(42)
'42'
>>> str(3.14)
'3.14'
```

`int()` and `float()` can convert strings that look like numbers. But:

```python
>>> int('3.14')
ValueError
```

`int()` can't directly convert a float-looking string. You'd need `int(float('3.14'))`.

**Truthiness with `bool()`:**

```python
>>> bool(0)
False
>>> bool(1)
True
>>> bool(-5)
True
>>> bool('')
False
>>> bool('hello')
True
>>> bool(None)
False
```

**Falsy** values — things that convert to `False`: `0`, `0.0`, `''` (empty string), `[]` (empty list), `{}` (empty dict), `None`.

Everything else is **truthy** — converts to `True`. This concept is essential for control flow in Module 04."

---

## [13:15 – 15:00] Lab Preview & PCAP Exam Summary

**[SHOW SLIDE: "Module 02 — Key Exam Points & Lab Preview"]**

"Let me wrap up with the exam essentials you need to lock in from this module:

**1.** `0.1 + 0.2` does NOT equal `0.3` exactly — floating-point precision issue.

**2.** `/` always returns `float`. `4 / 2` = `2.0`, not `2`.

**3.** `//` floors toward negative infinity. `-7 // 2` = `-4`, not `-3`.

**4.** `-2 ** 2` = `-4`. Exponentiation before unary minus.

**5.** `2 ** 3 ** 2` = `512` because `**` is right-associative.

**6.** `True + True` = `2` because `bool` is a subclass of `int`.

**7.** `int(3.9)` = `3` — truncation, not rounding.

**8.** `bool(0)`, `bool('')`, `bool(None)` all return `False` — they are falsy.

For your **Module 02 lab**, you will:

- Explore all data type literals in the REPL, including binary, octal, and hex integers
- Demonstrate the `0.1 + 0.2` float precision issue
- Write a circle area and circumference calculator using `math.pi`
- Write a Fahrenheit-to-Celsius temperature converter
- Practice operator precedence with and without parentheses
- Explore floor division and modulo with negative numbers

Full step-by-step instructions are in your lab document. Complete the lab, post to the discussion board by Wednesday, reply to two classmates by Sunday.

Module 03 covers variables — how to store and name values in Python — plus user input with `input()` and formatted output with f-strings. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 02 — Literals, Operators, and Expressions]**

---

## Additional Resources

- [Python for Everybody — Chapter 2](https://www.py4e.com/book) — Variables, Expressions, and Statements
- [Official Python Docs — Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Official Python Docs — Operator Precedence Table](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Episodes 3–4 cover data types and expressions
