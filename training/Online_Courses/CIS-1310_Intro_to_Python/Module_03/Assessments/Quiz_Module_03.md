# Quiz: Module 3 — Operators

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Total:** 15 Questions | 2 points each = **30 points**
**Suggested Time:** 25 minutes
**PCAP Alignment:** Section 2 — Operators, Expressions, Evaluation

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

What is the result of `17 // 5` in Python?

- A) `3.4`
- B) `3.0`
- C) **`3`** ← CORRECT
- D) `4`

**Correct Answer: C**
**Explanation:** `//` is the floor division operator. `17 / 5 = 3.4`, and the floor of `3.4` is `3`. When both operands are `int`, the result is `int`. `3.0` would appear only if at least one operand were a `float` (e.g., `17.0 // 5`).

---

### Question 2

What is the output of `print(-7 // 2)`?

- A) `-3`
- B) `3`
- C) `-3.5`
- D) **`-4`** ← CORRECT

**Correct Answer: D**
**Explanation:** Floor division always rounds toward **negative infinity**. `-7 / 2 = -3.5`, and the floor of `-3.5` is `-4`. Many students incorrectly answer `-3` because they expect rounding toward zero. Python's floor division always rounds toward negative infinity, not toward zero.

---

### Question 3

What is the output of `2 ** 3 ** 2`?

- A) `64`
- B) `36`
- C) `6`
- D) **`512`** ← CORRECT

**Correct Answer: D**
**Explanation:** The `**` operator is **right-associative** — evaluated right to left. So `2 ** 3 ** 2` = `2 ** (3 ** 2)` = `2 ** 9` = `512`. If evaluated left to right it would be `(2**3)**2` = `8**2` = `64`, but that is not how Python evaluates it. Use explicit parentheses when you need a specific order.

---

### Question 4

What is the output of `-2 ** 2`?

- A) `4`
- B) **`-4`** ← CORRECT
- C) `-8`
- D) `SyntaxError`

**Correct Answer: B**
**Explanation:** Unary minus (`-`) has **lower precedence** than exponentiation (`**`). So `-2 ** 2` is evaluated as `-(2 ** 2)` = `-(4)` = `-4`. To compute "negative two squared" and get `4`, you must write `(-2) ** 2`. This is a PCAP exam favorite.

---

### Question 5

What does `print(10 % 3)` output?

- A) `3`
- B) `0`
- C) `3.33`
- D) **`1`** ← CORRECT

**Correct Answer: D**
**Explanation:** `%` is the modulo operator — it returns the remainder after floor division. `10 = 3 × 3 + 1`, so the remainder is `1`. Common uses include checking even/odd (`n % 2 == 0`), checking divisibility, and implementing circular/wrap-around counters.

---

### Question 6

What is the output of `print(5 and 10)`?

- A) `True`
- B) `5`
- C) **`10`** ← CORRECT
- D) `False`

**Correct Answer: C**
**Explanation:** Python's `and` operator returns the **first falsy value** found, or the **last value** if all are truthy. Since `5` is truthy, Python continues to evaluate `10`. `10` is the last value and is truthy, so it is returned. `and` does NOT simply return `True` — it returns the actual operand value.

---

### Question 7

What is the output of `print(0 or "default")`?

- A) `False`
- B) `0`
- C) `True`
- D) **`"default"`** ← CORRECT

**Correct Answer: D**
**Explanation:** `or` returns the **first truthy value**, or the **last value** if all are falsy. `0` is falsy, so Python evaluates the right operand. `"default"` is truthy (non-empty string), so it is returned. The pattern `x or "fallback"` is idiomatic Python for providing default values.

---

### Question 8

Which expression correctly checks if `age` is between 18 and 65 inclusive using Pythonic style?

- A) `18 <= age and age <= 65`
- B) **`18 <= age <= 65`** ← CORRECT
- C) `age >= 18 and <= 65`
- D) `age.between(18, 65)`

**Correct Answer: B**
**Explanation:** Python uniquely supports chained comparisons like `18 <= age <= 65`. Both A and B produce the same result, but B is the more Pythonic form. Option C is a `SyntaxError` — you cannot chain `<= 65` without repeating the variable. Option D does not exist for plain integers.

---

### Question 9

What is the result of `not True or False`?

- A) `True`
- B) **`False`** ← CORRECT
- C) `None`
- D) `SyntaxError`

**Correct Answer: B**
**Explanation:** Operator precedence: `not` has higher precedence than `or`. Evaluate as: `(not True) or False` = `False or False` = `False`. If the expression were `not (True or False)`, it would be `not True` = `False` — same result but a different evaluation path. For more complex expressions, precedence order becomes critical.

---

### Question 10

What does `print(x is y, x is z)` output given this code?

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x
```

- A) `True True`
- B) `False False`
- C) `True False`
- D) **`False True`** ← CORRECT

**Correct Answer: D**
**Explanation:** `x is y` is `False` — `x` and `y` are two separate list objects in memory (even though they have identical values). `x is z` is `True` — `z = x` makes `z` point to the **same object** as `x`. `is` tests object identity (same memory address), not value equality. Use `==` for value comparison.

---

### Question 11

What is `5 & 3` in Python?

- A) `7`
- B) `6`
- C) **`1`** ← CORRECT
- D) `8`

**Correct Answer: C**
**Explanation:** `&` is the bitwise AND operator. `5 = 0b101`, `3 = 0b011`. Bitwise AND: each bit position is `1` only when BOTH corresponding bits are `1`. `101 & 011`: bit2 (1&0=0), bit1 (0&1=0), bit0 (1&1=1) → `001` = `1`.

---

### Question 12

What is the output of `10 / 5` in Python 3?

- A) `2`
- B) **`2.0`** ← CORRECT
- C) `2.5`
- D) `TypeError`

**Correct Answer: B**
**Explanation:** In Python 3, the `/` operator (true division) **always returns a float**, even when the result is a whole number. `10 / 5 = 2.0`. To get an integer result, use floor division: `10 // 5 = 2`. This is a key difference from Python 2, where `/` between two integers returned an integer.

---

### Question 13

Which expression uses short-circuit evaluation to safely prevent a `ZeroDivisionError` when `divisor = 0`?

- A) `try: 100 / divisor`
- B) `result = 100 / divisor if divisor else 0`
- C) **`result = divisor != 0 and 100 / divisor`** ← CORRECT
- D) `result = 100 / divisor or 0`

**Correct Answer: C**
**Explanation:** When `divisor = 0`: `divisor != 0` is `False`. Because `and` short-circuits on falsy left operands, Python never evaluates `100 / divisor`. `result` becomes `False` (the falsy left operand). Option D would attempt the division before evaluating `or`. Option B is also a valid safe approach (ternary conditional) but does not demonstrate `and` short-circuiting.

---

### Question 14

What is the output of `print("Py" in "Python", "py" in "Python")`?

- A) `True True`
- B) `False True`
- C) `False False`
- D) **`True False`** ← CORRECT

**Correct Answer: D**
**Explanation:** The `in` operator for strings is **case-sensitive**. `"Py"` (capital P) is found at the start of `"Python"` → `True`. `"py"` (lowercase p) is NOT in `"Python"` — the `p` in `"Python"` is capital — so → `False`. Case-sensitive membership checking is a common source of bugs and PCAP exam questions.

---

### Question 15

What does `5 and 0 or 10` evaluate to?

- A) `5`
- B) `0`
- C) `True`
- D) **`10`** ← CORRECT

**Correct Answer: D**
**Explanation:** `and` has higher precedence than `or`, so evaluate as `(5 and 0) or 10`. Step 1: `5 and 0` — `5` is truthy, so evaluate `0`; `0` is falsy, so `and` returns `0`. Step 2: `0 or 10` — `0` is falsy, so evaluate `10`; `10` is truthy, so `or` returns `10`. Final answer: `10`.

---

## Answer Key (for Instructor Reference)

| Q | Answer | Topic |
|---|---|---|
| 1 | C | Floor division |
| 2 | D | Negative floor division |
| 3 | D | `**` right-associativity |
| 4 | B | Unary minus vs. exponentiation precedence |
| 5 | D | Modulo operator |
| 6 | C | `and` return value |
| 7 | D | `or` default value pattern |
| 8 | B | Chained comparison |
| 9 | B | `not` precedence |
| 10 | D | `is` identity operator |
| 11 | C | Bitwise AND |
| 12 | B | True division always returns float |
| 13 | C | Short-circuit safety |
| 14 | D | `in` case-sensitivity |
| 15 | D | `and`/`or` complex evaluation |

---

*These questions are included in Unit Test 1 (Modules 1–4).*
