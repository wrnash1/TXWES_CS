# Video Script: CIS-1310 — Introduction to Python

## Module 04 — Control Flow: Conditional Statements

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - For the grade calculator demo, type the code live so students see the build-up.
> - Show the elif ordering consequence before showing the fix.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 04 | Control Flow: Conditional Statements | CIS-1310"]**

"Welcome back. We are in Module 04, and this is the module where Python stops being a calculator and starts making decisions.

Every program you have written so far runs the same way every time — top to bottom, no detours. But real software has to respond to different situations. A login form should behave differently for a correct password versus an incorrect one. A shipping calculator should apply different rates for different weights. A grade book needs to assign a letter grade based on a score.

All of that requires **control flow** — the ability to choose which lines of code run based on conditions. The primary tool for that in Python is the `if` statement. This module covers everything from basic `if` to `elif` to `else`, nested conditions, chained comparisons, truthiness, short-circuit evaluation, and a production-tested technique called the guardian pattern. Let's go."

---

## [00:45 – 02:30] Boolean Expressions and Relational Operators

**[SHOW SLIDE: "Boolean Expressions — True or False"]**

"Before we can write an `if` statement, we need to understand what it tests. An `if` statement evaluates a **Boolean expression** — any expression that produces the value `True` or `False`.

The most common Boolean expressions use **relational operators** — also called comparison operators:

```text
==   equal to
!=   not equal to
<    less than
>    greater than
<=   less than or equal to
>=   greater than or equal to
```

**[DEMO — REPL]**

```python
>>> 10 > 5
True
>>> 10 < 5
False
>>> 10 == 10
True
>>> 10 == '10'
False
>>> 10 != 5
True
```

Pay close attention to `==` versus `=`. The single `=` is the assignment operator — it stores a value. The double `==` is the equality comparison operator — it tests whether two values are equal. This is one of the most common beginner mistakes in Python.

**[DEMO]**

```python
>>> x = 10
>>> x == 10
True
>>> x == 20
False
```

Notice `10 == '10'` is `False`. The integer `10` and the string `'10'` are different types — Python does not automatically convert one to the other for comparison."

---

## [02:30 – 04:15] Logical Operators — and, or, not

**[SHOW SLIDE: "Logical Operators — Combining Conditions"]**

"A single comparison is often not enough. You might need both conditions to be true, or either one to be true, or you might want to reverse a True to False. That is what the three **logical operators** handle:

- `and` — both sides must be `True` for the result to be `True`
- `or` — at least one side must be `True` for the result to be `True`
- `not` — flips `True` to `False` and `False` to `True`

**[DEMO]**

```python
>>> age = 20
>>> age >= 18 and age < 65
True
>>> age < 18 or age >= 65
False
>>> not (age >= 18)
False
```

### Short-Circuit Evaluation

**[PAUSE]**

This is an important optimization concept that also appears on the PCAP exam. Python evaluates logical expressions left to right and **stops as soon as the result is determined**.

For `and`: if the left side is `False`, the whole expression is `False` — Python never evaluates the right side.

For `or`: if the left side is `True`, the whole expression is `True` — Python never evaluates the right side.

**[DEMO]**

```python
>>> x = 0
>>> x != 0 and 10 / x > 1
False
```

If Python evaluated the right side, `10 / 0` would raise a `ZeroDivisionError`. But because `x != 0` is `False`, Python short-circuits and never reaches `10 / x`. This is not just an exam fact — it is a practical technique for writing safe conditions."

---

## [04:15 – 06:30] The if Statement

**[SHOW SLIDE: "if — The Decision Maker"]**

"Now we can put conditions to work. The `if` statement runs a block of code only when a condition is `True`.

```python
if condition:
    # this block runs only if condition is True
    statement_1
    statement_2
```

The colon after the condition is required. The indented block that follows is the **body** of the `if` — Python uses consistent 4-space indentation to define what belongs to the `if`.

**[DEMO]**

```python
>>> score = 85
>>> if score >= 60:
...     print('You passed.')
...
You passed.
```

```python
>>> score = 45
>>> if score >= 60:
...     print('You passed.')
...
>>>
```

When `score` is `45`, the condition is `False` and the body does not execute — the program continues past the `if` block with no output.

### if-else

To handle both cases explicitly, add an `else`:

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

**[DEMO]**

```python
>>> score = 45
>>> if score >= 60:
...     print('You passed.')
... else:
...     print('You did not pass.')
...
You did not pass.
```

`else` has no condition of its own — it is the default fallback. It runs when none of the preceding conditions are `True`."

---

## [06:30 – 08:30] elif — Multiple Branches

**[SHOW SLIDE: "elif — More Than Two Outcomes"]**

"A grade calculator cannot just say pass or fail — it needs to assign A, B, C, D, or F. That requires more than two branches. Python provides `elif` — short for 'else if' — to add additional conditions.

```python
if condition_1:
    # runs if condition_1 is True
elif condition_2:
    # runs if condition_1 is False AND condition_2 is True
elif condition_3:
    # runs if condition_1 and condition_2 are False AND condition_3 is True
else:
    # runs if all conditions above are False
```

**[DEMO — type this live]**

```python
score = 88

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'Grade: {grade}')
```

Output:

```text
Grade: B
```

**Critical rule:** Python checks conditions top to bottom and stops at the **first** `True` condition. For `score = 88`, it checks `88 >= 90` (False), then `88 >= 80` (True) — it assigns `'B'` and skips all remaining `elif` and `else` blocks entirely.

This ordering matters. If you wrote the conditions from smallest to largest — `if score >= 60`, then `elif score >= 70`, etc. — every score above 60 would hit the first branch and get 'D'. The order of `elif` conditions is a logic decision, not just a style choice.

You can have any number of `elif` branches. `else` is optional — if you omit it and no condition matches, no branch runs."

---

## [08:30 – 09:45] Chained Comparisons

**[SHOW SLIDE: "Chained Comparisons — Python's Clean Syntax"]**

"Python allows you to chain comparisons in a way that is not available in most other languages:

```python
0 <= score <= 100
```

This means 'score is greater than or equal to 0 AND less than or equal to 100.' In Java or C you would have to write `score >= 0 && score <= 100`. Python's chaining reads like a math inequality.

**[DEMO]**

```python
>>> score = 85
>>> 0 <= score <= 100
True
>>> score = -5
>>> 0 <= score <= 100
False
>>> score = 150
>>> 0 <= score <= 100
False
```

You can chain more than two comparisons:

```python
>>> x = 5
>>> 1 < x < 10 < 20
True
```

**PCAP exam alert:** Chained comparisons evaluate left to right. `0 <= score <= 100` is exactly equivalent to `0 <= score and score <= 100`. Know this equivalence — the exam will test it."

---

## [09:45 – 11:00] Truthiness — What Python Considers True and False

**[SHOW SLIDE: "Truthiness and Falsiness"]**

"An `if` condition does not have to be a comparison expression. Any Python value can be used as a condition directly — Python evaluates it as either **truthy** (treated as True) or **falsy** (treated as False).

**Falsy values — these ALL evaluate to False in a condition:**

```text
False
None
0        (integer zero)
0.0      (float zero)
''       (empty string)
[]       (empty list)
{}       (empty dict)
()       (empty tuple)
```

Everything else is truthy.

**[DEMO]**

```python
>>> if 0:
...     print('zero is truthy')
... else:
...     print('zero is falsy')
...
zero is falsy

>>> if 'hello':
...     print('non-empty string is truthy')
...
non-empty string is truthy

>>> name = ''
>>> if name:
...     print(f'Hello, {name}')
... else:
...     print('No name provided.')
...
No name provided.
```

The pattern `if name:` — testing whether a string is non-empty — is used everywhere in professional Python code. Instead of `if name != ''`, you just write `if name`. Clean, readable, and tested on the PCAP exam."

---

## [11:00 – 12:30] The Guardian Pattern and Nested Conditionals

**[SHOW SLIDE: "Guardian Pattern — Validate Before You Calculate"]**

"In production software, you cannot trust user input. Users type letters where you expect numbers, leave required fields blank, or enter values outside valid ranges. The **guardian pattern** is the practice of checking preconditions at the top of a block — failing fast before doing the real work.

**[DEMO]**

```python
score = int(input('Enter score (0-100): '))

if score < 0 or score > 100:
    print('Invalid score. Must be between 0 and 100.')
else:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f'Grade: {grade}')
```

The outer `if` is the guard — it catches invalid input early and stops the program from proceeding with bad data. The grade logic only runs if the score is valid.

**Nested conditionals** — an `if` inside another `if` — are the mechanism here. Nesting is powerful but should be kept shallow. More than two or three levels of nesting is a signal that the code needs restructuring. Deeply nested code is hard to read and harder to debug.

A common alternative to the nested pattern is an **early return** using the guardian at the top — we will cover that in the functions module."

---

## [12:30 – 13:30] Ternary Expressions

**[SHOW SLIDE: "Ternary Expression — One-Line if-else"]**

"Python has a compact form for a simple if-else that produces a value — the **ternary expression**, also called a **conditional expression**:

```python
value_if_true if condition else value_if_false
```

**[DEMO]**

```python
>>> score = 75
>>> result = 'pass' if score >= 60 else 'fail'
>>> result
'pass'

>>> age = 17
>>> status = 'adult' if age >= 18 else 'minor'
>>> print(f'Status: {status}')
Status: minor
```

The ternary is useful for concise assignment — anywhere you would write a two-line if-else just to set a variable. Do not use it for complex logic — a full if-else is more readable in those cases.

PCAP exam questions will show ternary expressions and ask what value is produced. Trace them left to right: evaluate the condition first, then pick `value_if_true` or `value_if_false`."

---

## [13:30 – 14:30] Putting It Together — Grade Calculator

**[DEMO — type the complete script live]**

"Let me build the complete grade calculator from the lab. This uses everything from this module:

```python
# grade_calculator.py
# Module 04 Lab — CIS-1310

print('=== Grade Calculator ===')
print()

score = float(input('Enter your numeric score (0-100): '))

if score < 0 or score > 100:
    print(f'Error: {score} is not a valid score.')
    print('Please enter a number between 0 and 100.')
else:
    if score >= 90:
        grade = 'A'
        message = 'Excellent!'
    elif score >= 80:
        grade = 'B'
        message = 'Good work.'
    elif score >= 70:
        grade = 'C'
        message = 'Satisfactory.'
    elif score >= 60:
        grade = 'D'
        message = 'Needs improvement.'
    else:
        grade = 'F'
        message = 'Please see your instructor.'

    passed = 'Yes' if score >= 60 else 'No'

    print(f'Score:   {score:.1f}')
    print(f'Grade:   {grade}')
    print(f'Passed:  {passed}')
    print(f'Note:    {message}')
```

This is a complete, production-quality program in about 30 lines. It validates input with a guardian, uses an if-elif-else chain with correct ordering, uses a ternary for a simple binary decision, and formats the output with f-strings."

---

## [14:30 – 15:15] PCAP Exam Tips and Wrap-Up

**[SHOW SLIDE: "Module 04 — PCAP Alignment"]**

"Key exam take-aways:

**1.** `=` assigns. `==` compares. Using `=` in an `if` condition raises `SyntaxError`.

**2.** `elif` is the Python keyword — not `else if` (two words). Two-word syntax is C and Java, not Python.

**3.** Only the **first** matching branch in an `if-elif-else` chain runs — even if later conditions would also be True.

**4.** Chained comparisons: `0 <= x <= 100` is valid Python, equivalent to `0 <= x and x <= 100`.

**5.** Falsy values: `0`, `0.0`, `''`, `None`, `False`, `[]`, `{}`, `()`. Everything else is truthy.

**6.** Short-circuit evaluation: `and` stops at the first `False`; `or` stops at the first `True`.

**7.** Ternary syntax: `value_if_true if condition else value_if_false`.

Module 05 covers loops — `while` and `for` — where conditions become even more important because they control how many times code repeats. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 04 — Control Flow: Conditional Statements]**

---

## Additional Resources

- [Python for Everybody — Chapter 3](https://www.py4e.com/book) — Conditional Execution
- [Official Python Docs — Compound Statements: if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)
- [Official Python Docs — Boolean Operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)
- [PEP 8 — Programming Recommendations](https://peps.python.org/pep-0008/#programming-recommendations)
- [Python for Everybody Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Episode 7 (Conditionals)
