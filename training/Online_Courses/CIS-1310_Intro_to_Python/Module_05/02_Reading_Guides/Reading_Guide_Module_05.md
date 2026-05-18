# Reading Guide: Module 5 — Conditional Statements

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Certification Alignment:** PCAP — Certified Associate in Python Programming
**PCAP Exam Section:** Section 3 — Control Flow — Conditional Blocks and Loops
**Estimated Reading Time:** 45–55 minutes
**OER Resources:** [edube.org PE1 Module 3](https://edube.org/) | [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Write `if`, `elif`, and `else` blocks with correct syntax and indentation
2. Trace through nested conditional logic to predict output
3. Apply comparison and logical operators in conditional expressions
4. Use the ternary (conditional) expression for concise one-line conditionals
5. Understand how Python evaluates any expression as truthy or falsy in an `if` condition
6. Recognize common `if` statement errors (missing colon, wrong indentation, incorrect `elif` usage)

---

## Section 1: The `if` Statement

The `if` statement is the fundamental decision-making construct in Python. It executes a block of code only when a condition is `True`.

### Syntax

```python
if condition:
    # indented block — runs only if condition is True
    statement1
    statement2
```

**Rules:**
- The condition is any expression that evaluates to a truthy or falsy value
- The colon `:` is **required** after the condition — missing it causes a `SyntaxError`
- The body must be indented (4 spaces by PEP 8 convention)
- The block ends when indentation returns to the `if` level

### Basic Examples

```python
age = 20
if age >= 18:
    print("You are an adult.")
    print("You may vote.")

temperature = 35
if temperature > 30:
    print("It's hot today!")
```

### What Happens When the Condition is False

If the condition is `False`, the body is skipped entirely — Python moves to the next unindented statement:

```python
score = 55
if score >= 60:
    print("Passing")   # Skipped — condition is False
print("Check complete")  # Always runs — not in the if block
```

---

## Section 2: The `else` Clause

`else` provides a block that runs when the `if` condition is `False`. It is optional.

```python
if condition:
    # runs if condition is True
else:
    # runs if condition is False
```

```python
score = 55
if score >= 60:
    print("Pass")
else:
    print("Fail")
# Output: Fail
```

**Only one branch executes** — either the `if` block OR the `else` block, never both.

---

## Section 3: The `elif` Clause

`elif` (short for "else if") handles multiple mutually exclusive conditions. Python checks each condition in order, top to bottom, and executes only the **first** block whose condition is `True`.

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False AND condition2 is True
elif condition3:
    # runs if both above are False AND condition3 is True
else:
    # runs if ALL conditions above are False
```

### Grade Example

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")   # Grade: B
```

> **PCAP Exam Tip:** `elif` conditions are checked in order. Once one is `True`, all subsequent `elif` and `else` blocks are skipped. You can have any number of `elif` clauses but only one `else`. Python does not have a `switch`/`case` statement (Python 3.10+ has `match`, but that is not in PCAP scope).

### Critical: `elif` vs. Separate `if` Statements

```python
# Using elif — only one branch executes:
x = 10
if x > 5:
    print("Greater than 5")
elif x > 3:
    print("Greater than 3")   # Skipped! First condition matched.

# Using separate ifs — both branches can execute:
x = 10
if x > 5:
    print("Greater than 5")   # Executes
if x > 3:
    print("Greater than 3")   # Also executes — separate check
```

---

## Section 4: Nested Conditional Statements

`if` statements can be nested inside other `if` blocks. Each nested block adds one indentation level (4 more spaces).

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("Must be 18 or older")
```

### Equivalent Using Logical Operators (Preferred for Simple Cases)

```python
if age >= 18 and has_id:
    print("Access granted")
elif age >= 18 and not has_id:
    print("ID required")
else:
    print("Must be 18 or older")
```

> **Best Practice:** Avoid deep nesting. If you find yourself 3+ levels deep, consider using logical operators or reorganizing your logic.

---

## Section 5: Truthy and Falsy in `if` Conditions

Any Python value can be used as an `if` condition. Python evaluates it as truthy or falsy:

```python
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("No name provided")   # Output: No name provided (empty string is falsy)

items = [1, 2, 3]
if items:
    print(f"List has {len(items)} items")   # Executes — non-empty list is truthy

count = 0
if count:
    print("Has items")   # Skipped — 0 is falsy
```

This pattern is very common in Python for checking if a value has been set:

```python
result = None
if result is None:       # Explicit check for None
    print("No result yet")

user_input = input("Enter something: ")
if not user_input:       # Equivalent to if user_input == ""
    print("You entered nothing")
```

---

## Section 6: The Conditional (Ternary) Expression

Python's conditional expression provides a one-line `if/else`:

```python
value_if_true if condition else value_if_false
```

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult

# Equivalent long form:
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

```python
x = 10
print("positive" if x > 0 else "non-positive")   # positive

# In f-strings:
score = 85
print(f"Result: {'Pass' if score >= 60 else 'Fail'}")
```

> **PCAP Exam Tip:** The ternary expression always requires both the `if` and `else` parts. `x = 5 if condition` without an `else` is a `SyntaxError`.

---

## Section 7: Common `if` Statement Errors

| Error | Example | Cause | Fix |
|---|---|---|---|
| Missing colon | `if x > 5` | No `:` at end | `if x > 5:` |
| Wrong indentation | Statement not indented | Body must indent 4 spaces | Indent the body |
| `=` instead of `==` | `if x = 5:` | Assignment in condition | `if x == 5:` |
| `elif` without `if` | `elif x > 3:` alone | `elif` must follow `if` | Add `if` first |
| `else` with condition | `else x > 0:` | `else` takes no condition | Remove condition from `else` |

```python
# Common mistake: assignment in condition
x = 10
if x = 5:    # SyntaxError — use == not =
    print("five")
```

---

## Section 8: Comparing Strings

Strings compare **lexicographically** (character by character using Unicode/ASCII values):

```python
print("apple" < "banana")    # True — 'a' < 'b'
print("Apple" < "apple")     # True — uppercase letters have lower ASCII values
print("abc" == "abc")        # True — same characters
print("10" > "9")            # False — "1" < "9" in lexicographic order!
```

> **PCAP Exam Tip:** When comparing strings, Python uses character codes, not numeric values. `"10" > "9"` is `False` because `"1"` (ASCII 49) < `"9"` (ASCII 57). Always convert to `int` before numeric comparison.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| **`if` statement** | Executes a block of code only when a condition is `True` |
| **`elif`** | "Else if" — provides additional mutually exclusive conditions |
| **`else`** | Executes when all preceding `if`/`elif` conditions are `False` |
| **Conditional expression** | Ternary form: `value_if_true if condition else value_if_false` |
| **Nested conditional** | An `if` statement inside another `if` block |
| **Lexicographic comparison** | String comparison based on character code values |

---

## External Resources

| Resource | Link | What to Study |
|---|---|---|
| Python Control Flow | [docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html) | Section 4.1: `if` Statements |
| edube.org PE1 Module 3 | [edube.org](https://edube.org/) | Conditional statements section |
| Python `if` Reference | [docs.python.org/3/reference/compound_stmts.html#the-if-statement](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) | Full `if` syntax |

---

## Self-Check Review Questions

1. What is the difference between using `elif` and using a second `if` statement?
2. What happens if the `if` condition is `False` and there is no `else`?
3. Write a ternary expression that assigns `"even"` or `"odd"` based on whether `n % 2 == 0`.
4. Why does `"10" > "9"` evaluate to `False` in Python?
5. How many `elif` clauses can a single `if` statement have?

---

*Next Module → Module 6: While Loops*
