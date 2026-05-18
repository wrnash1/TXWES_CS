# Quiz: Module 5 — Conditional Statements

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Total:** 15 Questions | 2 points each = **30 points**
**Suggested Time:** 20 minutes
**PCAP Alignment:** Section 3 — Control Flow, Conditional Blocks

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

What is the output of the following code?

```python
x = 15
if x > 20:
    print("A")
elif x > 10:
    print("B")
elif x > 5:
    print("C")
else:
    print("D")
```

- A) `A`
- B) **`B`** ← CORRECT
- C) `B` and `C`
- D) `C`

**Correct Answer: B**
**Explanation:** Python checks conditions top-to-bottom. `x > 20` is False (skip). `x > 10` is True (15 > 10) — execute `print("B")` and skip all remaining `elif` and `else` blocks. Only the first matching condition executes.

---

### Question 2

What is the critical syntactic difference between the following two code blocks?

```python
# Block A:
score = 80
if score >= 60: print("Pass")
if score >= 70: print("Good")
if score >= 80: print("Excellent")

# Block B:
if score >= 60:
    print("Pass")
elif score >= 70:
    print("Good")
elif score >= 80:
    print("Excellent")
```

- A) Block A raises a SyntaxError; Block B does not
- B) Both blocks produce identical output
- C) Block B prints all three lines; Block A prints only one
- D) **Block A prints all three lines; Block B prints only "Pass"** ← CORRECT

**Correct Answer: D**
**Explanation:** Block A uses three separate `if` statements — each is checked independently. Since `score = 80` satisfies all three, all three lines print. Block B uses `elif` — once `score >= 60` matches and prints "Pass", the `elif score >= 70` and `elif score >= 80` blocks are skipped entirely. `elif` creates mutually exclusive branches.

---

### Question 3

What is the output of this code?

```python
name = ""
if name:
    print("Hello,", name)
else:
    print("No name provided")
```

- A) `Hello, `
- B) `True`
- C) `SyntaxError`
- D) **`No name provided`** ← CORRECT

**Correct Answer: D**
**Explanation:** An empty string `""` is **falsy** in Python. The `if name:` condition evaluates `""` as `False`, so the `else` block executes. This pattern is idiomatic Python for checking whether a string has content. Any non-empty string is truthy.

---

### Question 4

What is the output of this ternary expression?

```python
x = 7
result = "odd" if x % 2 != 0 else "even"
print(result)
```

- A) `even`
- B) `True`
- C) **`odd`** ← CORRECT
- D) `SyntaxError`

**Correct Answer: C**
**Explanation:** `x % 2 != 0` evaluates `7 % 2 = 1`, and `1 != 0` is `True`. Because the condition is `True`, the expression returns `"odd"` (the value before `if`). The ternary form `value_if_true if condition else value_if_false` returns the left value when the condition is True.

---

### Question 5

What error does the following code raise?

```python
age = 20
if age >= 18
    print("Adult")
```

- A) `IndentationError`
- B) `NameError`
- C) `TypeError`
- D) **`SyntaxError`** ← CORRECT

**Correct Answer: D**
**Explanation:** The colon `:` at the end of the `if` condition is required syntax. `if age >= 18` without the colon causes Python to raise `SyntaxError: expected ':'`. This is one of the most common beginner mistakes. Every `if`, `elif`, `else`, `for`, `while`, `def`, and `class` statement must end with a colon.

---

### Question 6

How many times will `print()` execute in this code?

```python
x = 10
if x > 5:
    print("A")
    print("B")
print("C")
```

- A) 0
- B) 1
- C) 2
- D) **3** ← CORRECT

**Correct Answer: D**
**Explanation:** `x = 10 > 5` is True. Both `print("A")` and `print("B")` are inside the `if` block (indented) and execute. `print("C")` is NOT indented — it is outside the `if` block and always executes regardless of the condition. Total: 3 `print()` calls.

---

### Question 7

What is the output of the following code?

```python
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)
```

- A) `B`
- B) `F`
- C) `B` and `C`
- D) **`C`** ← CORRECT

**Correct Answer: D**
**Explanation:** Check top to bottom: `75 >= 90` False, `75 >= 80` False, `75 >= 70` True — assign `"C"` and stop. The `else` is not reached. Output: `C`.

---

### Question 8

Which of the following is a VALID `else` clause?

- A) `else x > 0:`
- B) `else (x > 0):`
- C) `else if x > 0:`
- D) **`else:`** ← CORRECT

**Correct Answer: D**
**Explanation:** `else` takes **no condition**. It is a catch-all for when all preceding `if`/`elif` conditions are False. `else x > 0:` and `else (x > 0):` raise `SyntaxError`. `else if` is not valid Python syntax — Python uses `elif` (not `else if` like in many other languages).

---

### Question 9

What is the output of this nested conditional?

```python
x = 5
if x > 0:
    if x > 10:
        print("Large positive")
    else:
        print("Small positive")
else:
    print("Non-positive")
```

- A) `Large positive`
- B) `Non-positive`
- C) `Large positive` and `Small positive`
- D) **`Small positive`** ← CORRECT

**Correct Answer: D**
**Explanation:** Outer `if x > 0`: `5 > 0` is True — enter the outer block. Inner `if x > 10`: `5 > 10` is False — skip. Inner `else`: print `"Small positive"`. The outer `else` is never reached because the outer condition was True.

---

### Question 10

What does this ternary expression evaluate to?

```python
print("Pass" if 75 >= 60 and 75 <= 100 else "Invalid")
```

- A) `Invalid`
- B) `False`
- C) `True`
- D) **`Pass`** ← CORRECT

**Correct Answer: D**
**Explanation:** The condition `75 >= 60 and 75 <= 100` evaluates `True and True` = `True`. The ternary returns `"Pass"` when the condition is `True`. This is equivalent to checking if 75 is in the range [60, 100].

---

### Question 11

A student writes this ternary expression. What error occurs?

```python
x = 5
result = "positive" if x > 0
print(result)
```

- A) `NameError`
- B) `ValueError`
- C) **`SyntaxError`** ← CORRECT
- D) No error — `result` is `"positive"`

**Correct Answer: C**
**Explanation:** A ternary expression **requires** both `if` and `else` parts. `"positive" if x > 0` is incomplete — the `else` clause is missing. Python raises `SyntaxError`. The correct form: `result = "positive" if x > 0 else "non-positive"`.

---

### Question 12

What is the output of `print("10" > "9")`?

- A) `True`
- B) **`False`** ← CORRECT
- C) `TypeError`
- D) `1`

**Correct Answer: B**
**Explanation:** String comparison is **lexicographic** (character by character using ASCII values). `"10"` vs `"9"`: compare first characters — `"1"` (ASCII 49) vs `"9"` (ASCII 57). Since 49 < 57, `"10" < "9"`, so `"10" > "9"` is `False`. Never compare numeric strings with `>` or `<` — convert to `int` first.

---

### Question 13

What is the output of the following?

```python
a = None
b = None
if a is None and b is None:
    print("Both are None")
elif a is None:
    print("Only a is None")
else:
    print("Neither is None")
```

- A) `Only a is None`
- B) `Neither is None`
- C) `None`
- D) **`Both are None`** ← CORRECT

**Correct Answer: D**
**Explanation:** `a is None` is `True` and `b is None` is `True`. `True and True` = `True`, so the first `if` block executes. Note: using `is None` is the correct idiom for checking None — preferred over `== None`.

---

### Question 14

What is the output of the following code?

```python
x = 0
if x:
    print("Truthy")
elif not x:
    print("Falsy")
else:
    print("Unknown")
```

- A) `Truthy`
- B) **`Falsy`** ← CORRECT
- C) `Unknown`
- D) No output

**Correct Answer: B**
**Explanation:** `if x:` evaluates `if 0:` — `0` is falsy, so skip. `elif not x:` evaluates `elif not 0:` = `elif True:` — execute `print("Falsy")`. The `else` is skipped.

---

### Question 15

Which of the following correctly implements a three-way categorization (positive, negative, zero) in the most Pythonic style?

- A)
```python
if n > 0: print("positive")
if n < 0: print("negative")
if n == 0: print("zero")
```
- B)
```python
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")
```
- C)
```python
print("positive") if n > 0 else print("negative") if n < 0 else print("zero")
```
- D) **B is the most Pythonic** ← CORRECT

**Correct Answer: D**
**Explanation:** Option A uses three separate `if` statements — all are checked independently, which is both less efficient and logically incorrect (it checks `n == 0` even after already printing "positive"). Option B is correct and Pythonic — uses `if/elif/else` for mutually exclusive conditions. Option C uses chained ternaries on `print()` calls — valid but hard to read and not recommended for logic this simple.

---

## Answer Key (for Instructor Reference)

| Q | Answer | Topic |
|---|---|---|
| 1 | B | `elif` first-match behavior |
| 2 | D | `if` vs `elif` multiple checks |
| 3 | D | Empty string is falsy |
| 4 | C | Ternary expression evaluation |
| 5 | D | Missing colon SyntaxError |
| 6 | D | Indentation determines block membership |
| 7 | D | `if/elif/else` grade evaluation |
| 8 | D | `else` takes no condition |
| 9 | D | Nested conditional tracing |
| 10 | D | Ternary with compound condition |
| 11 | C | Ternary requires `else` |
| 12 | B | Lexicographic string comparison |
| 13 | D | `is None` idiom |
| 14 | B | Falsy zero in condition |
| 15 | D | Pythonic if/elif/else |

---

*These questions are included in Unit Test 2 (Modules 5–8).*
