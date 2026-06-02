# Reading Guide: Module 04 — Control Flow: Conditional Statements

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 04 — Control Flow: Conditional Statements**. This module is the turning point where programs stop being linear sequences and start responding to data. Every meaningful program — from login forms to grade calculators to fraud detection engines — uses conditional logic to make decisions.

The PCAP exam tests conditional statements heavily: syntax rules for `if`/`elif`/`else`, behavior of `and`/`or`/`not`, short-circuit evaluation, truthiness rules, chained comparisons, and ternary expressions. Every concept in this guide has appeared on the exam. Work through every example and prediction exercise before starting the lab.

---

## 1. High-Yield Glossary

### Boolean Expression

An expression that evaluates to either `True` or `False`. The `if` statement requires a Boolean expression as its condition. Examples: `x > 5`, `name == 'Alice'`, `x > 0 and x < 100`.

### Relational Operator (Comparison Operator)

An operator that compares two values and returns `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 3` | `True` |
| `<` | less than | `3 < 5` | `True` |
| `>` | greater than | `5 > 3` | `True` |
| `<=` | less than or equal to | `5 <= 5` | `True` |
| `>=` | greater than or equal to | `5 >= 6` | `False` |

**Critical distinction:** `=` is the assignment operator. `==` is the equality comparison operator. These are entirely different. `x = 5` stores the value `5` in `x`. `x == 5` tests whether `x` is currently equal to `5` and returns `True` or `False`.

### Logical Operator

An operator that combines or modifies Boolean expressions.

| Operator | Behavior | Short-circuits? |
|---|---|---|
| `and` | `True` only if both sides are `True` | Yes — stops at first `False` |
| `or` | `True` if at least one side is `True` | Yes — stops at first `True` |
| `not` | Flips `True` to `False` and vice versa | No |

### Short-Circuit Evaluation

Python evaluates `and` and `or` expressions left to right and stops as soon as the result is determined — it does not evaluate the remaining side of the expression.

```python
# and short-circuits: if left is False, right is never evaluated
x = 0
x != 0 and 10 / x > 1    # False — 10/x is never computed
```

```python
# or short-circuits: if left is True, right is never evaluated
x = 5
x > 0 or 10 / x > 1      # True — 10/x is never computed
```

Short-circuit evaluation is not just an optimization — it is a correctness technique for guarding against operations that would raise exceptions.

### if Statement

Executes a block of code only when a condition is `True`.

```python
if condition:
    body_statement_1
    body_statement_2
```

Rules:

- The condition is followed by a colon `:`
- The body is indented (4 spaces by PEP 8 convention)
- The body can contain any number of statements
- If the condition is `False`, the body is skipped entirely

### if-else Statement

Provides two mutually exclusive branches.

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

Exactly one branch always runs. `else` has no condition — it is the fallback for everything the `if` did not catch.

### elif (else if)

Adds additional conditions between `if` and `else`. Python checks each condition in order and executes the **first** matching branch only.

```python
if condition_1:
    branch_1
elif condition_2:
    branch_2
elif condition_3:
    branch_3
else:
    default_branch
```

Key behavior: once Python finds the first `True` condition, it executes that branch and **skips all remaining** `elif` and `else` blocks. Order matters — conditions checked earlier take priority.

### Chained Comparison

Python allows comparison operators to be chained, matching standard mathematical notation.

```python
0 <= score <= 100    # equivalent to: score >= 0 and score <= 100
1 < x < 10           # equivalent to: x > 1 and x < 10
```

The chain is evaluated left to right. Each intermediate value is compared to the next. This is unique to Python — most languages require explicit `and`.

### Truthiness and Falsiness

Any Python value can be evaluated in a Boolean context (inside an `if` condition, with `not`, with `and`/`or`). Values are classified as **truthy** or **falsy**.

**Falsy values — evaluate to False:**

| Value | Type |
|---|---|
| `False` | bool |
| `None` | NoneType |
| `0` | int |
| `0.0` | float |
| `''` | str (empty) |
| `[]` | list (empty) |
| `{}` | dict (empty) |
| `()` | tuple (empty) |

Everything else is **truthy** — any non-zero number, any non-empty string, any non-empty collection.

**Practical use:**

```python
name = input('Enter name: ')
if name:              # truthy check — name is non-empty
    print(f'Hello, {name}')
else:
    print('No name entered.')
```

### Nested Conditional

An `if` statement placed inside the body of another `if`, `elif`, or `else`. Nesting creates more specific conditions.

```python
if outer_condition:
    if inner_condition:
        # runs only when BOTH conditions are True
    else:
        # runs when outer is True but inner is False
```

Keep nesting shallow — no more than two or three levels. Deep nesting is a code quality problem.

### Guardian Pattern

A defensive programming technique that validates preconditions before doing the main work. Place validation checks at the top; if they fail, exit early (print an error, return, or raise an exception). This prevents invalid data from propagating into calculations.

```python
score = int(input('Score: '))
if score < 0 or score > 100:
    print('Invalid score.')
else:
    # only reach here with a valid score
    ...
```

### Ternary Expression (Conditional Expression)

A compact one-line form of if-else that produces a value.

**Syntax:**

```python
value_if_true if condition else value_if_false
```

**Examples:**

```python
result = 'pass' if score >= 60 else 'fail'
label = 'even' if n % 2 == 0 else 'odd'
```

The ternary is appropriate for simple, single-value decisions. Do not use it for nested conditions or multiple statements.

---

## 2. Operator Precedence for Conditions

Python evaluates conditions according to operator precedence. From highest to lowest priority among the operators relevant to this module:

| Priority | Operator(s) | Notes |
|---|---|---|
| 1 (highest) | `**` | Exponentiation |
| 2 | Unary `-`, `+` | Negation, positive |
| 3 | `*`, `/`, `//`, `%` | Multiplication, division |
| 4 | `+`, `-` | Addition, subtraction |
| 5 | `<`, `>`, `<=`, `>=`, `==`, `!=` | Comparisons |
| 6 | `not` | Logical NOT |
| 7 | `and` | Logical AND |
| 8 (lowest) | `or` | Logical OR |

**Practical meaning:** In the expression `x + 1 > 5 and y - 2 < 10`, Python computes `x + 1` and `y - 2` first (arithmetic), then performs the comparisons, then evaluates the `and`. Use parentheses to make complex conditions explicit and readable.

---

## 3. if-elif-else Execution Flow

Trace through this diagram mentally for every conditional code question on the exam:

```text
Evaluate condition_1
      |
   True? ──── YES ──── Run branch_1, skip all remaining branches
      |
     NO
      |
Evaluate condition_2
      |
   True? ──── YES ──── Run branch_2, skip all remaining branches
      |
     NO
      |
  (more elif?)
      |
Evaluate else_condition (implicit — always True)
      |
      └── Run else branch
```

Exactly **one** branch runs per execution. If there is no `else` and no condition matches, **no branch runs**.

---

## 4. Common Error Patterns to Memorize

**Pattern 1 — Assignment in a condition (`SyntaxError`):**

```python
if x = 5:     # SyntaxError — should be ==
    print(x)
```

**Pattern 2 — Wrong keyword (`SyntaxError`):**

```python
if x > 0:
    print('positive')
else if x < 0:    # SyntaxError — Python keyword is elif, not else if
    print('negative')
```

**Pattern 3 — Wrong elif order (silent logic error):**

```python
# BUG — score 95 gets 'D' because 60 is checked first
if score >= 60:
    grade = 'D'
elif score >= 70:
    grade = 'C'
elif score >= 80:
    grade = 'B'
elif score >= 90:
    grade = 'A'
```

**Pattern 4 — Relying on truthiness when type matters:**

```python
x = 0
if x:
    print('x has a value')    # Does NOT print — 0 is falsy
```

If `0` is a meaningful value (not just "nothing"), test explicitly: `if x is not None:`.

---

## 5. Certification Exam Tips

**Tip 1 — Know the `elif` spelling.**
The PCAP exam will offer `else if`, `elseif`, `elif`, and `else:if` as options. Only `elif` is valid Python.

**Tip 2 — Only the first matching branch runs.**
On exam questions showing an if-elif-else chain, trace from top to bottom and mark the first `True` condition. All subsequent branches are skipped regardless of their truth value.

**Tip 3 — Chained comparisons are valid.**
`0 <= x <= 100` is valid Python syntax and is equivalent to `0 <= x and x <= 100`. The exam may show one form and ask what the other form is.

**Tip 4 — Short-circuit evaluation stops evaluation.**
In `A and B`, if `A` is `False`, `B` is never evaluated. In `A or B`, if `A` is `True`, `B` is never evaluated. This can prevent exceptions and is tested directly.

**Tip 5 — Memorize the falsy values.**
The full list: `False`, `None`, `0`, `0.0`, `''`, `[]`, `{}`, `()`. Any empty container and any numeric zero. Everything else is truthy.

**Tip 6 — Ternary expression order.**
The syntax is `value_if_true if condition else value_if_false`. The condition is in the middle, not at the start. Many students write it backwards. Practice: `'yes' if x > 0 else 'no'`.

**Tip 7 — Indentation defines the body.**
The body of an `if` ends at the first line that is de-indented back to the `if` level. Python does not use `{}` braces for blocks — indentation is the structure.

---

## 6. Beyond the Exam — Real-World Context

**Why does Python use `elif` instead of `else if`?**
In C and Java, `else if` is actually a nested `if` inside an `else` block — the language just allows omitting the braces for single-statement bodies. Python made `elif` an explicit keyword to make the flat chain structure clear and avoid deep nesting in grade-calculator-style code.

**Short-circuit evaluation in production code.**
Python's short-circuit evaluation is relied upon in security code. A common pattern:

```python
if user is not None and user.is_authenticated():
    # safe — is_authenticated() only called if user exists
```

If `user` is `None`, calling `user.is_authenticated()` would raise `AttributeError`. Short-circuiting prevents this without requiring a nested `if`.

**The guardian pattern in web APIs.**
In real web application code, functions that receive user-submitted data always start with validation:

```python
def process_payment(amount, card_number):
    if amount <= 0:
        return {'error': 'Amount must be positive'}
    if len(card_number) != 16:
        return {'error': 'Invalid card number'}
    # actual payment logic only runs here
    ...
```

This is the guardian pattern at production scale. Every major web framework (Django, Flask, FastAPI) relies on this kind of early-return validation structure.

---

## 7. Required Readings and Videos

**Required Reading — Chapter 3:**
Read Chapter 3 of [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book). The chapter covers conditional execution with `if`, `elif`, and `else`, and introduces the key patterns used in this module.

**Required Reading — Official Python Docs:**
Read [Compound Statements: if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) and [Boolean Operations](https://docs.python.org/3/reference/expressions.html#boolean-operations) in the official Python 3 documentation.

**Required Video:**
Watch Episode 7 of the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp). Dr. Severance walks through conditional execution with live examples.

---

## 8. Lab and Command Preview

| Task | What You Will Do |
|---|---|
| Relational operator REPL | Test all 6 operators, predict results before running |
| Logical operator REPL | Practice `and`, `or`, `not` with compound conditions |
| Short-circuit demo | Observe that `10/0` is never reached with `and` short-circuit |
| `grade_calculator.py` | Full if-elif-else grade calculator with guardian pattern |
| `login_validator.py` | Guardian pattern validating username and password length |
| `season_checker.py` | Chained comparisons determining season from month number |
| Truthiness exploration | Test all falsy values in REPL, observe behavior |
| Ternary practice | Rewrite two-line if-else blocks as ternary expressions |

---

## 9. Study Checklist

- [ ] Watch the Module 04 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary — especially the elif execution flow and truthiness table.
- [ ] Work through the Common Error Patterns in Section 4 — predict each outcome before reading.
- [ ] Read Chapter 3 of *Python for Everybody* at py4e.com.
- [ ] Read the if statement and Boolean operations pages in the Official Python 3 Docs.
- [ ] Watch Episode 7 of the Python for Everybody playlist.
- [ ] Review all 7 Certification Exam Tips in Section 5.
- [ ] Preview the lab tasks in Section 8.
- [ ] Proceed to the Module 04 Lab Activity.
