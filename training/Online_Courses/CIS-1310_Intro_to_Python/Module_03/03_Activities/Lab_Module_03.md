# Lab 3: Operators and Expressions

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Points:** 50 points
**Submission:** Upload your `.ipynb` or `.py` file to the Canvas Lab 3 assignment
**Due:** See Canvas for the deadline

---

## Objectives

By completing this lab, you will:

1. Apply all seven arithmetic operators including floor division and modulo
2. Predict and verify expression results based on operator precedence rules
3. Construct logical expressions using `and`, `or`, and `not`
4. Observe short-circuit evaluation in practice
5. Use membership and identity operators correctly
6. Apply bitwise operators on binary values
7. Build a practical program that combines multiple operator types

---

## Before You Begin

```python
# Student: [Your Full Name]
# Course: CIS-1310 Introduction to Python Programming
# Date: [Today's Date]
# Lab: Module 3 — Operators and Expressions
```

---

## Part 1: Arithmetic Operators (15 points)

### Step 1.1 — Basic Arithmetic Table

Assign `a = 17` and `b = 5`. Compute and print each of the following, labeling each result clearly:

```python
a = 17
b = 5

print("a + b =", a + b)       # Addition
print("a - b =", a - b)       # Subtraction
print("a * b =", a * b)       # Multiplication
print("a / b =", a / b)       # True division — what type is the result?
print("a // b =", a // b)     # Floor division
print("a % b =", a % b)       # Modulo (remainder)
print("a ** b =", a ** b)     # Exponentiation
```

After printing, add `print(type(a / b))` and `print(type(a // b))` to show their different return types. Add comments explaining why they differ.

### Step 1.2 — Negative Floor Division (PCAP Trap)

This is a known PCAP exam trap. Predict the output **before running** each line, write your prediction as a comment, then run and verify:

```python
# Write your prediction as a comment before each line, then run:
print(-7 // 2)     # My prediction: ___
print(7 // -2)     # My prediction: ___
print(-7 // -2)    # My prediction: ___
print(-7 % 2)      # My prediction: ___
print(7 % -2)      # My prediction: ___
```

Below your predictions, write a comment explaining **in your own words** why `-7 // 2` equals `-4` and not `-3`. Reference the concept of "floor" meaning "round toward negative infinity" in your explanation.

### Step 1.3 — Exponentiation Tricks

Write code to compute each of the following using only the `**` operator:

- The square of 15
- The cube root of 27 (hint: what is 1/3 as a float exponent?)
- 2 to the power of 32
- Both `(-2) ** 2` AND `-2 ** 2` — compute both and explain why they differ in a comment

Print each result with a clear label.

---

## Part 2: Operator Precedence (10 points)

### Step 2.1 — Predict Before You Run

For each expression below, write your predicted value as a comment **before running**. After running, if your prediction was wrong, write a follow-up comment explaining why.

```python
# Predict each result before running:
print(2 + 3 * 4)           # Prediction: ___
print((2 + 3) * 4)         # Prediction: ___
print(2 ** 3 ** 2)         # Prediction: ___
print((2 ** 3) ** 2)       # Prediction: ___
print(10 - 3 - 2)          # Prediction: ___
print(not True or False)   # Prediction: ___
print(not (True or False))  # Prediction: ___
print(10 % 3 + 2 * 4)     # Prediction: ___
```

### Step 2.2 — Fix the Precedence Bug

A student tries to calculate the average of three test scores but gets the wrong answer. Find the bug, fix it, and explain:

```python
# This code is WRONG — find and fix the bug:
score1 = 85
score2 = 90
score3 = 78
average = score1 + score2 + score3 / 3    # BUG IS HERE
print("Average:", average)                 # Should output 84.333...
```

Write the corrected version and add a comment explaining which operator precedence rule caused the error.

---

## Part 3: Logical and Comparison Operators (10 points)

### Step 3.1 — Scholarship Eligibility Checker

Write code that checks whether a student meets ALL of the following criteria:
- GPA must be 3.5 or higher
- Age must be between 18 and 25 inclusive
- Must be currently enrolled

```python
gpa = 3.7
age = 22
is_enrolled = True

# Write a single boolean expression using 'and' and comparison operators:
eligible = ___
print("Scholarship eligible:", eligible)
```

Test your expression with at least 3 different value sets — one eligible, two not. Show each test case with its own variables and `print()`.

### Step 3.2 — Short-Circuit Safety

Rewrite the following dangerous code using short-circuit evaluation so that it never crashes:

```python
# This crashes when divisor = 0 — rewrite using short-circuit evaluation:
divisor = 0
result = 10 / divisor     # ZeroDivisionError!
print(result)
```

The fixed version should: if `divisor` is 0, set `result` to `0`; otherwise, compute `10 / divisor`. Write this as a **single assignment statement** using `and`.

### Step 3.3 — `and`/`or` Return Values (Not Just True/False)

Predict each result, then run and verify:

```python
print(5 and 10)       # Prediction: ___
print(0 and 10)       # Prediction: ___
print(0 or 10)        # Prediction: ___
print(5 or 10)        # Prediction: ___
print("" or "Hello")  # Prediction: ___
print("Hi" or "Bye")  # Prediction: ___
```

Write a comment explaining the rule: when does `and` return the left operand vs. the right? When does `or` return the left vs. the right?

---

## Part 4: Membership and Identity Operators (10 points)

### Step 4.1 — Membership Check

Create a list of approved programming languages for a job posting. Check at least 5 languages:

```python
approved_languages = ["Python", "JavaScript", "Java", "Go", "Rust"]

# Check membership:
print("Python" in approved_languages)
print("COBOL" in approved_languages)
print("Ruby" not in approved_languages)
# Add 2 more checks of your choice
```

Also test membership on a string:

```python
university = "Texas Wesleyan University"
print("Wesleyan" in university)    # What is the result?
print("texas" in university)       # What is the result? Explain in a comment why.
```

### Step 4.2 — Identity vs. Equality

Demonstrate the difference between `==` (value equality) and `is` (object identity):

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("list_a == list_b:", list_a == list_b)
print("list_a is list_b:", list_a is list_b)
print("list_a == list_c:", list_a == list_c)
print("list_a is list_c:", list_a is list_c)
```

Write a comment explaining each result. Then write one paragraph answering: when would you use `is` vs. `==` in real code? Give a specific example of each.

---

## Part 5: Practical Grade Calculator (5 points)

Build a mini grade calculator using the operators from this module:

```python
exam1 = 88
exam2 = 72
exam3 = 95

# Calculate average with correct parentheses:
average = ___

# Determine pass/fail (True if average >= 70):
passed = ___

# Determine if each grade range applies using chained comparison:
is_a_grade = ___    # 90 <= average <= 100
is_b_grade = ___    # 80 <= average < 90
is_c_grade = ___    # 70 <= average < 80

print("Average:", round(average, 2))
print("Passed:", passed)
print("Grade A:", is_a_grade)
print("Grade B:", is_b_grade)
print("Grade C:", is_c_grade)
```

Test with at least two different score sets (one A/B range, one C/D range).

---

## Submission Checklist

- [ ] Student header at the top
- [ ] All 5 parts completed and run without errors
- [ ] Predictions written BEFORE running code in Parts 1.2, 2.1, and 3.3
- [ ] Comment explaining floor division rounding direction (Part 1.2)
- [ ] Precedence bug explanation in Part 2.2
- [ ] Short-circuit safety rewrite in Part 3.2
- [ ] `and`/`or` return value rule explained (Part 3.3)
- [ ] `is` vs. `==` explanation (Part 4.2)
- [ ] File saved as `lab03_yourLastName.ipynb` or `.py`

**Submit** to the **Lab 3** assignment in Canvas.

---

## Grading Rubric

| Part | Task | Points |
|---|---|---|
| Part 1 | Arithmetic operators, floor division predictions, exponentiation | 15 |
| Part 2 | Precedence predictions and bug fix | 10 |
| Part 3 | Logical expressions, short-circuit, return value explanation | 10 |
| Part 4 | Membership checks, identity vs. equality analysis | 10 |
| Part 5 | Grade calculator | 5 |
| **Total** | | **50** |

---

*Next: Module 4 Lab — Type Conversion and User Input*
