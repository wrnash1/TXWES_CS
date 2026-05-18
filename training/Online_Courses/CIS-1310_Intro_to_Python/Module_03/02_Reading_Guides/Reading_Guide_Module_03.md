# Reading Guide: Module 3 — Operators

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Certification Alignment:** PCAP — Certified Associate in Python Programming
**PCAP Exam Section:** Section 2 — Data Types, Evaluation, Basic I/O, Operators
**Estimated Reading Time:** 50–65 minutes
**OER Resources:** [edube.org PE1 Module 2](https://edube.org/) | [Python Expressions](https://docs.python.org/3/reference/expressions.html)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Apply all Python arithmetic operators, including floor division and modulo
2. Explain and apply Python's operator precedence rules correctly
3. Construct boolean expressions using comparison and logical operators
4. Predict the outcome of complex expressions involving `and`, `or`, and `not`
5. Use identity (`is`, `is not`) and membership (`in`, `not in`) operators correctly
6. Perform basic bitwise operations and explain their use cases
7. Distinguish between `=` (assignment), `==` (equality), and `is` (identity)

---

## Section 1: Arithmetic Operators

Arithmetic operators perform mathematical calculations. Python supports seven arithmetic operators.

### The Seven Arithmetic Operators

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `3 * 7` | `21` |
| `/` | True Division | `10 / 3` | `3.3333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulo (Remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 8` | `256` |

### True Division vs. Floor Division

This distinction is critical for the PCAP exam.

**True division (`/`)** always returns a `float`, even when dividing integers evenly:

```python
print(10 / 2)    # 5.0 — float, not 5
print(7 / 2)     # 3.5
print(10 / 3)    # 3.3333333333333335
```

**Floor division (`//`)** returns the largest integer less than or equal to the result (floors toward negative infinity):

```python
print(10 // 3)    # 3  (3.333... → floor → 3)
print(7 // 2)     # 3  (3.5 → floor → 3)
print(-7 // 2)    # -4 (−3.5 → floor → −4, NOT −3)
```

> **PCAP Exam Tip:** Floor division with negative numbers surprises most students. `-7 // 2` is `-4`, not `-3`. "Floor" always rounds toward **negative infinity**, not toward zero.

### Modulo Operator (`%`)

The modulo operator returns the **remainder** after floor division:

```python
print(10 % 3)     # 1  (10 = 3×3 + 1)
print(17 % 5)     # 2  (17 = 5×3 + 2)
print(-7 % 3)     # 2  (Python modulo is non-negative when divisor is positive)
```

**Common use cases:**
- Check if a number is even: `n % 2 == 0`
- Check divisibility: `n % divisor == 0`
- Wrap around (clock arithmetic): `hour % 12`

### Exponentiation (`**`)

```python
print(2 ** 10)    # 1024
print(3 ** 3)     # 27
print(16 ** 0.5)  # 4.0 — square root using fractional exponent
print(2 ** -1)    # 0.5 — negative exponent inverts
```

### Type Rules for Arithmetic

| Operation | Result Type |
|---|---|
| `int` op `int` (except `/`) | `int` |
| `int` / `int` | always `float` |
| `int` op `float` | `float` |
| `float` op `float` | `float` |

```python
print(type(5 + 3))      # <class 'int'>
print(type(5 + 3.0))    # <class 'float'>
print(type(10 / 2))     # <class 'float'>  — always float
print(type(10 // 2))    # <class 'int'>
```

---

## Section 2: Operator Precedence

When an expression contains multiple operators, Python evaluates them in a specific order — **operator precedence**. This is Python's equivalent of mathematical order of operations.

### Python Operator Precedence (Highest to Lowest)

| Priority | Operator(s) | Description |
|---|---|---|
| 1 (highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Multiplication, division, modulo |
| 5 | `+`, `-` | Addition, subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `in` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 (lowest) | `or` | Logical OR |

### Precedence Examples

```python
print(2 + 3 * 4)        # 14 — multiplication before addition
print((2 + 3) * 4)      # 20 — parentheses override precedence
print(2 ** 3 ** 2)      # 512 — ** is right-associative: 2**(3**2) = 2**9 = 512
print((2 ** 3) ** 2)    # 64  — parentheses change it: (8)**2 = 64
print(-2 ** 2)          # -4  — unary minus applies AFTER exponentiation: -(2**2)
print((-2) ** 2)        # 4   — parentheses make the base negative: (-2)^2 = 4
```

> **PCAP Exam Tip:** The right-associativity of `**` and the behavior of unary minus with exponentiation are classic exam traps. `-2**2 == -4` because `**` has higher precedence than unary `-`.

### Left Associativity (Default for Most Operators)

Most operators of equal precedence are evaluated **left to right**:

```python
print(10 - 3 - 2)    # 5 — evaluated as (10-3)-2
print(16 / 4 / 2)    # 2.0 — evaluated as (16/4)/2
```

Exponentiation is **right-associative** (right to left):

```python
print(2 ** 3 ** 2)    # 512 — evaluated as 2**(3**2)
```

---

## Section 3: Comparison Operators

Comparison operators compare two values and always return a `bool` (`True` or `False`).

| Operator | Name | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `6 >= 7` | `False` |

**Chained comparisons** — Python's unique and readable syntax:

```python
age = 20
print(18 <= age <= 65)    # True — reads like mathematics
print(0 < 5 < 10 < 20)   # True — chains can be longer
```

---

## Section 4: Logical Operators

Logical operators combine boolean expressions. Python's three logical operators are `and`, `or`, and `not`.

### Truth Tables

| A | B | A and B | A or B | not A |
|---|---|---|---|---|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

### Short-Circuit Evaluation

Python stops evaluating as soon as the result is determined:

- `and`: If the left is falsy, returns it without evaluating the right
- `or`: If the left is truthy, returns it without evaluating the right

```python
x = 0
result = x and (10 / x)    # Safe: x is 0 (falsy), division never executes
print(result)               # 0

y = 5
result = y or (10 / 0)     # Safe: y is truthy, division never executes
print(result)               # 5
```

### `and`/`or` Return the Operand, Not Just True/False

```python
print(5 and 10)     # 10  — left is truthy, returns right
print(0 and 10)     # 0   — left is falsy, returns left
print(0 or 10)      # 10  — left is falsy, returns right
print(5 or 10)      # 5   — left is truthy, returns left
print("" or "Hi")  # "Hi" — useful default value pattern
```

> **PCAP Exam Tip:** The fact that `and`/`or` return the actual operand (not just `True`/`False`) is a frequently tested concept. Know the rule: `and` returns the first falsy value or the last value; `or` returns the first truthy value or the last value.

---

## Section 5: Identity and Membership Operators

### Identity Operators — `is` and `is not`

Tests whether two variables refer to the **same object in memory**:

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)    # True  — same values
print(x is y)    # False — different objects in memory
print(x is z)    # True  — z points to the same object as x
```

Always check for `None` using `is`:

```python
result = None
print(result is None)      # True  — correct idiom
print(result is not None)  # False
```

### Membership Operators — `in` and `not in`

```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)       # True
print("mango" not in fruits)   # True

name = "Texas Wesleyan"
print("Texas" in name)         # True — works on strings
print("texas" in name)         # False — case-sensitive!
```

---

## Section 6: Bitwise Operators

Bitwise operators work on the binary representation of integers.

| Operator | Name | Example | Result |
|---|---|---|---|
| `&` | AND | `5 & 3` | `1` |
| `\|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT | `~5` | `-6` |
| `<<` | Left shift | `5 << 1` | `10` |
| `>>` | Right shift | `5 >> 1` | `2` |

```python
# 5 = 0b101, 3 = 0b011
print(bin(5 & 3))    # 0b001 = 1
print(bin(5 | 3))    # 0b111 = 7
print(bin(5 ^ 3))    # 0b110 = 6

print(4 << 2)        # 16 — left shift 2 positions = multiply by 4
print(16 >> 2)       # 4  — right shift 2 positions = divide by 4
```

> **Key fact:** `~n` equals `-(n+1)`. So `~5 == -6`. Left shift by 1 = multiply by 2. Right shift by 1 = floor divide by 2.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| **True division (`/`)** | Division that always returns a float |
| **Floor division (`//`)** | Integer division rounding toward negative infinity |
| **Modulo (`%`)** | The remainder after floor division |
| **Operator precedence** | Rules determining evaluation order in an expression |
| **Short-circuit evaluation** | Stopping logical evaluation as soon as result is known |
| **Identity operator** | `is` / `is not` — tests if two names reference the same object |
| **Membership operator** | `in` / `not in` — tests if a value exists in a collection |

---

## External Resources

| Resource | Link | What to Study |
|---|---|---|
| Python Operator Precedence | [docs.python.org/3/reference/expressions.html#operator-precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence) | Full precedence table |
| edube.org PE1 Module 2 | [edube.org](https://edube.org/) | Operators section |
| Python Bitwise Operations | [docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types) | Bitwise reference |

---

## Self-Check Review Questions

1. What is the result of `-7 // 2` and why is it not `-3`?
2. Why does `2 ** 3 ** 2` equal `512` and not `64`?
3. What does `-2 ** 2` evaluate to, and how is it different from `(-2) ** 2`?
4. Describe short-circuit evaluation and give an example preventing a `ZeroDivisionError`.
5. What is the difference between `==` and `is`? When should you use each?
6. What does `5 and 0 or 10` evaluate to? Walk through each step.

---

*Next Module → Module 4: Type Conversion and User Input*
