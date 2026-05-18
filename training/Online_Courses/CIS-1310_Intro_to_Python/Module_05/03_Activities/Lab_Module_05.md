# Lab 5: Conditional Statements

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Points:** 50 points
**Submission:** Upload your `.ipynb` or `.py` file to the Canvas Lab 5 assignment
**Due:** See Canvas for the deadline

---

## Objectives

1. Write correct `if`, `elif`, and `else` blocks with proper indentation
2. Trace through conditional logic to predict output before running
3. Build programs that make decisions based on user input
4. Apply the ternary conditional expression
5. Detect and fix common `if` statement errors

---

## Before You Begin

```python
# Student: [Your Full Name]
# Course: CIS-1310 Introduction to Python Programming
# Date: [Today's Date]
# Lab: Module 5 — Conditional Statements
```

---

## Part 1: Basic `if`/`elif`/`else` (15 points)

### Step 1.1 — Letter Grade Calculator

Write a program using `if/elif/else` that assigns a letter grade based on a numeric score:
- A: 90–100
- B: 80–89
- C: 70–79
- D: 60–69
- F: below 60

```python
score = float(input("Enter your score (0-100): "))

# Write your if/elif/else block here:
if ___:
    grade = "A"
elif ___:
    grade = "B"
# ... complete the remaining grades

print(f"Score: {score:.1f} | Grade: {grade}")
```

Test with at least 5 different scores covering all five grade ranges plus the boundaries (exactly 90, 80, 70, 60).

### Step 1.2 — Trace Before Running

For each code block below, write your predicted output as a comment **before** running. Then run and verify.

**Block A:**
```python
x = 15
if x > 20:
    print("Greater than 20")
elif x > 10:
    print("Greater than 10")    # Prediction: runs or skips?
elif x > 5:
    print("Greater than 5")     # Prediction: runs or skips?
else:
    print("5 or less")
```

**Block B:**
```python
score = 80
if score >= 60:
    print("Passed")
if score >= 70:
    print("Good")
if score >= 80:
    print("Excellent")
# How many lines print? How would this differ if you used elif?
```

**Block C:**
```python
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("No name entered")
# Why does an empty string trigger the else?
```

---

## Part 2: Nested Conditionals and Logic (10 points)

### Step 2.1 — Access Control System

Build an access control system with two factors: age and membership status:

```python
age = int(input("Enter age: "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

# Logic:
# - Age >= 21 AND member: "Welcome! Full access granted."
# - Age >= 21 AND NOT member: "Welcome! Please purchase a membership for full access."
# - Age < 21: "Access denied. Must be 21 or older."

# Write your conditional logic here (you may use nested ifs OR logical operators):
```

Test all three scenarios. Show your test output.

### Step 2.2 — Season Identifier

Write code that uses `if/elif/else` to determine the season based on a month number (1–12):
- Winter: December (12), January (1), February (2)
- Spring: March–May (3–5)
- Summer: June–August (6–8)
- Fall: September–November (9–11)

Hint: Use `or` to combine months within a season, or use chained comparisons.

```python
month = int(input("Enter month number (1-12): "))
# Write your season identifier here
```

---

## Part 3: Ternary (Conditional) Expression (10 points)

### Step 3.1 — Basic Ternary Practice

Rewrite each `if/else` block as a single ternary expression:

**Block 1 — rewrite as ternary:**
```python
x = 7
if x % 2 == 0:
    parity = "even"
else:
    parity = "odd"
# Your ternary version:
parity = ___
```

**Block 2 — rewrite as ternary:**
```python
temperature = 28
if temperature > 25:
    description = "hot"
else:
    description = "comfortable"
# Your ternary version:
description = ___
```

**Block 3 — use ternary in f-string:**
```python
balance = -50
# Print: "Status: Overdraft" if balance < 0, else "Status: OK"
print(f"Status: {___ if balance < 0 else ___}")
```

### Step 3.2 — Ternary Chain (Advanced)

Write a single-line ternary expression that assigns `"A"`, `"B"`, `"C"`, or `"F"` based on a score. You can chain ternary expressions:

```python
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade)
```

Explain in a comment why chained ternaries, while possible, are generally discouraged for more than 2–3 levels (readability).

---

## Part 4: Input-Driven Programs (10 points)

### Step 4.1 — Body Mass Index (BMI) Classifier

```python
print("=== BMI Calculator ===")
weight_kg = float(input("Weight in kilograms: "))
height_m  = float(input("Height in meters: "))

bmi = weight_kg / (height_m ** 2)

# BMI Categories (WHO):
# < 18.5: Underweight
# 18.5–24.9: Normal weight
# 25–29.9: Overweight
# >= 30: Obese

# Write if/elif/else to determine category:

print(f"\nBMI: {bmi:.1f}")
print(f"Category: {category}")
```

Test with at least 3 different inputs covering different categories.

### Step 4.2 — Simple Authentication

Simulate a login check:

```python
CORRECT_USERNAME = "student"
CORRECT_PASSWORD = "txwes2024"

username = input("Username: ")
password = input("Password: ")

# Check credentials and print appropriate message:
# - Both correct: "Login successful! Welcome, [username]."
# - Username wrong: "Username not found."
# - Username right but password wrong: "Incorrect password."
```

Implement using nested `if` statements (not just `and`). Show test cases for all three outcomes.

---

## Part 5: Error Detection and Correction (5 points)

Each of the following code blocks contains a bug. Identify the bug type (SyntaxError, LogicError, or IndentationError), explain it in a comment, and write the corrected version.

**Buggy Block 1:**
```python
score = 75
if score >= 60
    print("Pass")
```

**Buggy Block 2:**
```python
x = 10
if x > 5:
print("Greater than 5")
```

**Buggy Block 3:**
```python
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else grade >= 60:
    print("D")
```

**Buggy Block 4 (Logic error — no syntax error, but wrong behavior):**
```python
score = 95
if score >= 60:
    print("D")
elif score >= 70:
    print("C")
elif score >= 80:
    print("B")
elif score >= 90:
    print("A")
```
Explain what this code does wrong and why order matters.

---

## Submission Checklist

- [ ] Student header at the top
- [ ] All 5 parts completed
- [ ] Trace predictions written before running (Part 1.2)
- [ ] All three access control scenarios tested (Part 2.1)
- [ ] Ternary expressions written for all 3 blocks (Part 3.1)
- [ ] BMI calculator tested with 3+ inputs (Part 4.1)
- [ ] Authentication tested for all 3 outcomes (Part 4.2)
- [ ] All 4 bugs identified, explained, and corrected (Part 5)
- [ ] File saved as `lab05_yourLastName.ipynb` or `.py`

**Submit** to the **Lab 5** assignment in Canvas.

---

## Grading Rubric

| Part | Task | Points |
|---|---|---|
| Part 1 | Letter grade calculator + trace predictions | 15 |
| Part 2 | Nested conditionals: access control + seasons | 10 |
| Part 3 | Ternary expression rewrites + chain | 10 |
| Part 4 | BMI calculator + authentication system | 10 |
| Part 5 | Bug detection and correction | 5 |
| **Total** | | **50** |

---

*Next: Module 6 Lab — While Loops*
