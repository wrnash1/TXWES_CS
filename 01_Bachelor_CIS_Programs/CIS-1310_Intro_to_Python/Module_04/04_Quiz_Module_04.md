# Quiz: Module 04 — Control Flow: Conditional Statements

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 04 topics.

---

### Question 1

What keyword does Python use to add additional conditions after an initial `if`?

- A) `else if`
- B) `elseif`
- C) `elif`
- D) `otherwise`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `else if` (two words) is the syntax used in C, Java, and JavaScript — not Python. Writing `else if` in Python is a `SyntaxError`.
- *Why B is incorrect:* `elseif` (one word, no space) is used in PHP and some other languages. Python does not recognize it.
- *Why C is correct:* `elif` is Python's dedicated keyword for adding additional conditions to an `if` block. It combines the concepts of "else" and "if" into a single keyword.
- *Why D is incorrect:* `otherwise` is not a Python keyword. It does not exist in Python's syntax.

---

### Question 2

In the following code, what is the output when `score = 95`?

```python
if score >= 60:
    grade = 'D'
elif score >= 70:
    grade = 'C'
elif score >= 80:
    grade = 'B'
elif score >= 90:
    grade = 'A'
else:
    grade = 'F'
print(grade)
```

- A) `A`
- B) `B`
- C) `D`
- D) `SyntaxError` — `elif` cannot follow `if` without `else`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The `grade = 'A'` branch requires `score >= 90`, which `95` satisfies — but Python never reaches that `elif` because it already matched the first condition.
- *Why B is incorrect:* Same issue — `grade = 'B'` is in a later `elif` that Python skips after the first match.
- *Why C is correct:* Python checks conditions top to bottom and executes the **first** matching branch. `95 >= 60` is `True`, so Python executes `grade = 'D'` and skips all remaining `elif` and `else` blocks. This is a silent logic error caused by ordering conditions smallest-first.
- *Why D is incorrect:* The code is syntactically valid. `elif` does not require a preceding `else`. The error here is logical, not syntactic.

---

### Question 3

What does the following expression evaluate to?

```python
x = 0
x != 0 and 10 / x > 1
```

- A) `True`
- B) `False`
- C) `ZeroDivisionError` — Python always evaluates both sides of `and`
- D) `TypeError` — `and` cannot be used with comparison expressions

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `x != 0` is `False` (since `x` is `0`), so the `and` expression is `False`. Short-circuit evaluation prevents the right side from running.
- *Why B is correct:* Python uses **short-circuit evaluation** for `and`. If the left side is `False`, the entire expression is `False` and Python never evaluates the right side. `10 / x` is never computed, so no `ZeroDivisionError` is raised.
- *Why C is incorrect:* This would be true only if Python always evaluated both sides. It does not — `and` stops at the first `False`.
- *Why D is incorrect:* `and` works perfectly with Boolean expressions (including comparisons). There is no `TypeError` here.

---

### Question 4

Which of the following values is **falsy** in Python?

- A) `'False'`
- B) `0.001`
- C) `[0]`
- D) `0`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `'False'` is a non-empty string. All non-empty strings are truthy — including a string that happens to spell the word "False".
- *Why B is incorrect:* `0.001` is a non-zero float. All non-zero numbers are truthy.
- *Why C is incorrect:* `[0]` is a list containing one element. It is not empty, so it is truthy — even though that element is `0`.
- *Why D is correct:* The integer `0` is falsy. Python's falsy values include `False`, `None`, `0` (int), `0.0` (float), `''` (empty string), `[]` (empty list), `{}` (empty dict), and `()` (empty tuple).

---

### Question 5

What does `0 <= x <= 100` mean in Python?

- A) It is a syntax error — Python does not support chained comparisons
- B) It tests whether `x` is between 0 and 100 exclusive (not including 0 or 100)
- C) It is equivalent to `0 <= x and x <= 100`
- D) It is equivalent to `0 <= x or x <= 100`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Python explicitly supports chained comparisons. `0 <= x <= 100` is valid Python syntax.
- *Why B is incorrect:* `<=` means "less than or equal to," so both 0 and 100 are included in the valid range.
- *Why C is correct:* Python evaluates `0 <= x <= 100` as `0 <= x and x <= 100`. The chain tests each adjacent pair left to right, and each intermediate value is used in both comparisons. This is equivalent to the explicit `and` form.
- *Why D is incorrect:* `or` would mean any `x` satisfying either condition — which would be nearly all numbers. The `and` relationship is what gives the chained comparison its range-checking behavior.

---

### Question 6

What does the following code output when `age = 17`?

```python
label = 'adult' if age >= 18 else 'minor'
print(label)
```

- A) `adult`
- B) `minor`
- C) `SyntaxError` — ternary expressions are not valid in Python
- D) `None`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `17 >= 18` is `False`, so Python uses the value after `else`, which is `'minor'`.
- *Why B is correct:* The ternary expression syntax is `value_if_true if condition else value_if_false`. With `age = 17`, the condition `age >= 18` is `False`, so `label` is assigned `'minor'`.
- *Why C is incorrect:* Python fully supports ternary (conditional) expressions. They have been valid since Python 2.5.
- *Why D is incorrect:* `None` would only result if the ternary expression were missing the `else` clause or if both branches returned `None`. Both branches here return string literals.

---

### Question 7

A program uses a guardian pattern: `if score < 0 or score > 100:` followed by a print error statement. What is the purpose of this guard?

- A) To raise a `ValueError` automatically when the score is out of range
- B) To prevent the grade calculation logic from running on invalid data
- C) To force the user to re-enter a score until it is valid
- D) To convert non-numeric input to a default score of 0

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python does not automatically raise exceptions based on value ranges. The code only prints an error message — no exception is raised unless you explicitly write `raise`.
- *Why B is correct:* The guardian pattern validates input before the main logic runs. The `else` branch (containing the grade calculation) only executes if the guard condition is `False` — meaning the score is valid. This prevents invalid data from reaching the calculation.
- *Why C is incorrect:* A basic `if` guard does not loop. To force re-entry, you would need a `while` loop (covered in Module 05).
- *Why D is incorrect:* The guardian only checks the range — it does not convert anything. If the user entered a non-numeric value, `float(input(...))` would raise `ValueError` before the guard even runs.

---

### Question 8

What is the output of this code?

```python
x = 10
y = 20
if x > 5:
    if y > 15:
        print('A')
    else:
        print('B')
else:
    print('C')
```

- A) `A`
- B) `B`
- C) `C`
- D) Both `A` and `C`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Trace the execution: `x > 5` is `True` (10 > 5), so the outer `else` (`C`) is skipped. Inside the outer `if`, `y > 15` is `True` (20 > 15), so `'A'` is printed and the inner `else` (`B`) is skipped. Only `A` prints.
- *Why B is incorrect:* `B` only prints when the outer `if` is True but the inner `if` is False — `y > 15` is True here, so `B` is skipped.
- *Why C is incorrect:* `C` only prints when the outer `if` condition is False — `x > 5` is True, so `C` is skipped.
- *Why D is incorrect:* In an `if-else`, only one branch executes. Both `A` and `C` cannot print from a single execution.

---

### Question 9

What does `not (5 > 3)` evaluate to?

- A) `True`
- B) `False`
- C) `0`
- D) `SyntaxError` — `not` requires a variable, not an expression

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `5 > 3` is `True`. `not True` is `False`, not `True`.
- *Why B is correct:* `5 > 3` evaluates to `True`. The `not` operator flips it to `False`.
- *Why C is incorrect:* `not` applied to a Boolean returns a Boolean (`True` or `False`), not an integer. Although `False == 0` is `True` (since `bool` inherits from `int`), the direct result of `not True` is the Boolean `False`.
- *Why D is incorrect:* `not` can be applied to any expression that evaluates to a Boolean. `not (5 > 3)` is perfectly valid — the parentheses ensure the comparison is evaluated first.

---

### Question 10

Which of the following correctly validates that a month number is in the range 1 through 12 (inclusive) using Python's chained comparison syntax?

- A) `if month > 1 and month < 12:`
- B) `if 1 < month < 12:`
- C) `if 1 <= month <= 12:`
- D) `if month >= 1 or month <= 12:`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `month > 1 and month < 12` excludes both 1 and 12. `>` means strictly greater than, so month = 1 fails the first condition; `<` means strictly less than, so month = 12 fails the second. This is an off-by-one error.
- *Why B is incorrect:* `1 < month < 12` uses strict less-than on both sides, excluding 1 and 12 from the valid range.
- *Why C is correct:* `1 <= month <= 12` uses `<=` (less than or equal to) on both sides, including both 1 and 12. This is the correct chained comparison for an inclusive range.
- *Why D is incorrect:* `month >= 1 or month <= 12` is logically equivalent to "any number" — every possible integer satisfies at least one of these conditions. `or` is the wrong operator here; `and` (or chained comparison) is needed.

---

### Question 11

What is the output of the following code?

```python
x = 5
result = 'big' if x > 10 else 'medium' if x > 3 else 'small'
print(result)
```

- A) `big`
- B) `medium`
- C) `small`
- D) `SyntaxError: nested ternary is not allowed`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `x > 10` is `False` (5 is not greater than 10), so the first ternary's `if` branch is skipped.
- *Why B is correct:* The expression evaluates left to right. `x > 10` is `False`, so Python evaluates the else branch: `'medium' if x > 3 else 'small'`. `x > 3` is `True` (5 > 3), so the result is `'medium'`.
- *Why C is incorrect:* `'small'` would only be selected if both `x > 10` and `x > 3` were `False`. Since `5 > 3` is `True`, `'medium'` is selected.
- *Why D is incorrect:* Python fully supports nested (chained) ternary expressions. They are valid syntax, though PEP 8 recommends using them sparingly for readability.

---

### Question 12

Which of the following demonstrates the correct way to test if `x` is between 10 and 20, exclusive?

- A) `if 10 < x and x < 20:`
- B) `if 10 < x < 20:`
- C) `if x > 10 and < 20:`
- D) Both A and B are correct

**Correct Answer:** D

**Distractor Analysis:**

- *Why A alone is not the full answer:* `10 < x and x < 20` is valid and correct, but Python also supports the chained form.
- *Why B alone is not the full answer:* `10 < x < 20` is Python's chained comparison — also valid and correct.
- *Why C is incorrect:* `x > 10 and < 20` is a `SyntaxError`. The `<` operator requires both a left and right operand. You cannot write `and < 20` without specifying what is being compared.
- *Why D is correct:* Both `10 < x and x < 20` and `10 < x < 20` are correct and equivalent in Python. The chained form (`10 < x < 20`) is more Pythonic and preferred by PEP 8.

---

### Question 13

What does `or` return when both operands are truthy?

```python
result = 'hello' or 'world'
```

- A) `True`
- B) `'hello'`
- C) `'world'`
- D) `'helloworld'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python's `or` operator does not return a `bool` — it returns the actual value of one of its operands. This is called short-circuit value return.
- *Why B is correct:* `or` returns the **first truthy value** it finds, short-circuiting the rest. `'hello'` is truthy, so Python returns it immediately without evaluating `'world'`. This behavior underpins the common pattern `value = user_input or 'default'`.
- *Why C is incorrect:* `'world'` would be returned if the first operand were falsy. Since `'hello'` is truthy, the second operand is never evaluated.
- *Why D is incorrect:* `or` on strings does not concatenate them. It returns one of the operands based on truthiness, not the combination of both.

---

### Question 14

What is the output of this code?

```python
x = None
y = x or 'default'
print(y)
```

- A) `None`
- B) `'default'`
- C) `True`
- D) `TypeError: unsupported operand type`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `None` is falsy. When `x` is falsy, `x or 'default'` returns the right operand: `'default'`.
- *Why B is correct:* `None or 'default'` — `None` is falsy, so `or` moves to the right side and returns `'default'`. This is a very common Python idiom for providing fallback values.
- *Why C is incorrect:* `or` returns an operand value, not a boolean. The result here is the string `'default'`, not `True`.
- *Why D is incorrect:* `or` works on any Python objects. There is no TypeError for using `or` with `None` and a string.

---

### Question 15

How many branches of the following if-elif-else chain can execute for a single value of `temperature`?

```python
if temperature < 0:
    print('freezing')
elif temperature < 10:
    print('cold')
elif temperature < 20:
    print('cool')
elif temperature < 30:
    print('warm')
else:
    print('hot')
```

- A) All branches that have `True` conditions execute
- B) Exactly one branch executes
- C) Zero branches execute if no condition is `True`
- D) The `else` branch always executes in addition to whichever `elif` matches

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python's `if-elif-else` chain executes only the first matching branch. Even if multiple conditions are `True`, only the first `True` branch runs.
- *Why B is correct:* In an `if-elif-else` chain, exactly one branch executes per run — the first one whose condition is `True`. If no condition is `True`, the `else` branch executes. The `else` guarantees at least one branch always runs.
- *Why C is incorrect:* The `else` clause has no condition — it is a catch-all that runs when all prior conditions are `False`. So at least one branch always executes.
- *Why D is incorrect:* The `else` branch only runs when ALL prior conditions are `False`. It never runs alongside an `elif` branch.

---

### Question 16

What will be printed by the following code?

```python
a = 0
b = 5
c = 10

if a or b:
    print('first')
if not a and c:
    print('second')
if a and b or c:
    print('third')
```

- A) `first` and `second` only
- B) `first`, `second`, and `third`
- C) `second` only
- D) `first` and `third` only

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The third `if` also evaluates to `True`. `a and b` = `0 and 5` = `0` (falsy). Then `0 or c` = `0 or 10` = `10` (truthy). So the third `if` body executes.
- *Why B is correct:* First `if`: `a or b` = `0 or 5` = `5` (truthy) → prints `first`. Second `if`: `not a` = `not 0` = `True`, and `c` = `10` (truthy) → prints `second`. Third `if`: `a and b` = `False`, so `0 or c` = `10` (truthy) → prints `third`. All three print.
- *Why C is incorrect:* The first `if` is also truthy (`0 or 5` = `5`), so `first` prints too.
- *Why D is incorrect:* The second `if` is also truthy (`not 0` is `True`, and `10` is truthy), so `second` also prints.

---

### Question 17

What is the result of `bool('0')`?

- A) `False` — because `'0'` represents the number zero
- B) `True` — because `'0'` is a non-empty string
- C) `0` — `bool()` of a numeric string returns the integer equivalent
- D) `ValueError` — `bool()` cannot convert numeric strings

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `'0'` is a string, not an integer. `bool()` on a string checks whether it is empty or not — it does not parse numeric content. Any non-empty string is truthy.
- *Why B is correct:* `'0'` contains one character and is therefore a non-empty string. `bool('0')` returns `True`. Only `bool('')` (empty string) returns `False`.
- *Why C is incorrect:* `bool()` always returns `True` or `False`, never an integer. It also does not parse string content for numeric meaning.
- *Why D is incorrect:* `bool()` accepts any Python object without raising `ValueError`. It simply checks truthiness.

---

### Question 18

What is the output of the following code?

```python
x = 10
if x > 5:
    y = 'high'
print(y)
```

- A) `high`
- B) `NameError: name 'y' is not defined`
- C) `None`
- D) `SyntaxError`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `x > 5` is `True`, so the `if` body executes and `y` is assigned `'high'`. After the `if` block, `print(y)` finds `y` in scope and prints `high`.
- *Why B is incorrect:* `NameError` would occur only if the `if` block were skipped (e.g., if `x = 3`). Since `10 > 5` is `True`, `y` is defined before `print(y)` runs.
- *Why C is incorrect:* `y` was explicitly assigned `'high'` — it is not `None`.
- *Why D is incorrect:* The code is syntactically valid. There is no structural error.

---

### Question 19

Which of the following correctly demonstrates the guardian (early exit) pattern?

- A) Checking input validity at the end of a function, after the computation
- B) Checking input validity at the start of a function and returning/printing an error before the main logic
- C) Using `try/except` to catch exceptions when invalid data is processed
- D) Asking the user to re-enter data in a loop until valid input is provided

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Checking at the end of a function means invalid data has already been processed, potentially causing errors or wrong output. The guardian pattern checks first.
- *Why B is correct:* The guardian pattern places input validation at the very beginning of a function or block. If the data is invalid, the function returns (or prints an error) immediately — the main logic never runs on bad data. This is "guard the entry."
- *Why C is incorrect:* `try/except` is exception handling, not the guardian pattern. Exception handling reacts to errors after they occur; the guardian pattern prevents errors by checking preconditions proactively.
- *Why D is incorrect:* Looping until valid input is provided is input validation with a loop (covered in Module 05), not the guardian pattern. The guardian does not loop — it simply rejects invalid input and exits.

---

### Question 20

What does `and` return when both operands are falsy?

```python
result = 0 and ''
```

- A) `False`
- B) `0`
- C) `''`
- D) `None`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Like `or`, `and` returns an actual operand value rather than a boolean. It returns the first falsy value it encounters.
- *Why B is correct:* `and` returns the **first falsy value**. `0` is falsy, so `and` short-circuits immediately and returns `0` without evaluating `''`. This is consistent with Python's short-circuit value-return behavior.
- *Why C is incorrect:* `''` would be returned by `and` only if the first operand were truthy, causing evaluation to continue to the second operand.
- *Why D is incorrect:* `None` is not involved anywhere in this expression. `and` returns one of its operands, not `None`.
